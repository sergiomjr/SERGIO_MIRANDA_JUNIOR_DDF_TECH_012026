#criar o script generate_product_catalog.py
code = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
import argparse, csv, json, random, re, sys, uuid
from dataclasses import dataclass
from typing import Dict, List, Optional

CATEGORIES: Dict[str, Dict[str, List[str]]] = {
    "telefonia": {
        "materials": ["PU Leather", "Silicone", "TPU", "Policarbonato", "Couro legítimo", "ABS"],
        "brands": ["Samsung", "Motorola", "Xiaomi", "Apple", "Realme", "LG"],
        "features": ["antichoque", "resistente a riscos", "RFID", "magnetic lock", "kickstand", "proteção de câmera"],
        "compat": ["Galaxy S23", "Galaxy A54", "Moto G84", "Redmi Note 12", "iPhone 14", "iPhone 15"],
    },
    "informatica_acessorios": {
        "materials": ["Alumínio", "ABS", "Acrílico", "Borracha", "Nylon"],
        "brands": ["Logitech", "Dell", "HP", "Lenovo", "Razer", "Corsair"],
        "features": ["retroiluminado", "ergonômico", "plug and play", "alta precisão", "silencioso", "2.4GHz wireless"],
        "compat": ["Windows 10/11", "macOS", "Linux", "USB-C", "USB-A", "Bluetooth 5.0"],
    },
    "casa_cozinha": {
        "materials": ["Aço inox", "Vidro temperado", "Cerâmica", "Plástico BPA Free", "Madeira"],
        "brands": ["Tramontina", "Brastemp", "Philips Walita", "Arno", "Electrolux"],
        "features": ["antiaderente", "fácil limpeza", "alta durabilidade", "economia de energia", "design moderno"],
        "compat": ["110V", "220V", "bivolt", "lava-louças", "micro-ondas"],
    },
    "beleza_saude": {
        "materials": ["Hipoalergênico", "Vegano", "Sem parabenos", "Dermatologicamente testado"],
        "brands": ["Nivea", "L'Oréal", "Vichy", "La Roche-Posay", "Avon", "Natura"],
        "features": ["hidratação intensa", "FPS 50", "controle de oleosidade", "efeito matte", "anti-idade", "sem fragrância"],
        "compat": ["pele oleosa", "pele seca", "pele sensível", "uso diário", "todos os tipos de pele"],
    },
    "esporte_lazer": {
        "materials": ["Poliéster", "Algodão", "Neoprene", "EVA", "Borracha natural"],
        "brands": ["Nike", "Adidas", "Puma", "Under Armour", "Mormaii"],
        "features": ["respirável", "leve", "ajuste confortável", "antiderrapante", "alta resistência"],
        "compat": ["corrida", "treino", "yoga", "ciclismo", "trilha"],
    },
    "moveis_decoracao": {
        "materials": ["MDF", "Madeira maciça", "Metal", "Vidro", "Tecido suede"],
        "brands": ["Mobly", "Tok&Stok", "IKEA", "Madesa", "Politorno"],
        "features": ["fácil montagem", "acabamento premium", "design escandinavo", "estrutura reforçada"],
        "compat": ["sala", "quarto", "escritório", "varanda", "cozinha"],
    },
    "automotivo": {
        "materials": ["Borracha", "Aço", "Polímero", "Couro sintético"],
        "brands": ["Bosch", "3M", "Michelin", "Goodyear", "Pioneer"],
        "features": ["alta aderência", "resistente a calor", "longa vida útil", "fácil instalação"],
        "compat": ["carro", "moto", "SUV", "sedan", "hatch"],
    },
}

COLORS = ["Preto","Branco","Cinza","Azul","Vermelho","Verde","Rosa","Roxo","Dourado","Prata"]
SIZES = ["PP","P","M","G","GG","Único"]
WARRANTY = ["90 dias","6 meses","12 meses","24 meses"]
SHIPPING = ["Envio imediato","Postagem em 24h","Postagem em 48h","Sob encomenda (3-5 dias)"]
ADJECTIVES = ["Premium","Original","Reforçado","Compacto","Leve","Ultra resistente","Profissional","Econômico"]
BENEFITS = [
    "Melhora sua rotina com praticidade.",
    "Ideal para uso diário e alta durabilidade.",
    "Ótima relação custo-benefício.",
    "Design moderno e acabamento superior.",
    "Proteção e eficiência em um só produto.",
]
DISCLAIMER = [
    "Imagens meramente ilustrativas.",
    "As cores podem variar conforme a tela.",
    "Verifique a compatibilidade antes da compra.",
    "Produto novo e lacrado.",
]
PHRASES = [
    "Fabricado com materiais selecionados e padrão de qualidade elevado.",
    "Desenvolvido para oferecer desempenho consistente e uso confortável.",
    "Projetado para encaixe preciso e melhor experiência do usuário.",
    "Excelente escolha para quem busca durabilidade e estética.",
    "Produto com ótimo acabamento, resistente ao uso contínuo.",
    "Compatível com múltiplos cenários de uso e fácil instalação.",
    "Recomendado para consumidores que valorizam segurança e praticidade.",
]

def pick(rng: random.Random, items: List[str]) -> str:
    return rng.choice(items)

def make_product_id() -> str:
    return str(uuid.uuid4())

@dataclass
class ProductRecord:
    product_id: str
    category: str
    title: str
    description: str
    def to_json(self):
        return {"product_id": self.product_id, "category": self.category, "title": self.title, "description": self.description}

def build_title(rng: random.Random, category: str, meta: Dict[str, List[str]]) -> str:
    brand = pick(rng, meta["brands"])
    material = pick(rng, meta["materials"])
    feat = pick(rng, meta["features"])
    compat = pick(rng, meta["compat"])
    color = pick(rng, COLORS)
    adj = pick(rng, ADJECTIVES)
    templates = [
        f"{adj} {brand} {category.replace('_',' ').title()} em {material} – {feat} – {color} – Compatível com {compat}",
        f"{brand} {category.replace('_',' ').title()} {adj} ({material}) com {feat} | Cor {color} | {compat}",
        f"{adj} {category.replace('_',' ').title()} {brand} {material} – {feat} – Para {compat} – {color}",
    ]
    return pick(rng, templates)

def build_description(rng: random.Random, category: str, meta: Dict[str, List[str]]) -> str:
    material = pick(rng, meta["materials"])
    brand = pick(rng, meta["brands"])
    compat = pick(rng, meta["compat"])
    color = pick(rng, COLORS)
    size = pick(rng, SIZES)
    warranty = pick(rng, WARRANTY)
    shipping = pick(rng, SHIPPING)
    feats = rng.sample(meta["features"], k=min(3, len(meta["features"])))
    bullets = [
        f"- Marca: {brand}",
        f"- Material: {material}",
        f"- Cor: {color}",
        f"- Tamanho: {size}",
        f"- Compatibilidade: {compat}",
        f"- Garantia: {warranty}",
        f"- Logística: {shipping}",
        f"- Destaques: {', '.join(feats)}",
    ]
    paragraph_1 = " ".join(rng.sample(PHRASES, k=3))
    paragraph_2 = " ".join(rng.sample(PHRASES, k=3))
    paragraph_3 = pick(rng, BENEFITS)
    disclaimer = " ".join(rng.sample(DISCLAIMER, k=2))
    return (
        f"{paragraph_1}\n\n{paragraph_2}\n\n{paragraph_3}\n\n"
        f"Especificações:\n" + "\n".join(bullets) + f"\n\nObservações: {disclaimer}"
    )

def generate(n: int, seed: int):
    if n < 100_000:
        raise ValueError("O case exige >= 100.000 registros. Use n=100000 ou mais.")
    rng = random.Random(seed)
    cats = list(CATEGORIES.keys())
    for _ in range(n):
        category = pick(rng, cats)
        meta = CATEGORIES[category]
        yield ProductRecord(
            product_id=make_product_id(),
            category=category,
            title=build_title(rng, category, meta),
            description=build_description(rng, category, meta),
        )

def write_jsonl(n: int, seed: int, out_path: str):
    with open(out_path, "w", encoding="utf-8") as f:
        for rec in generate(n, seed):
            f.write(json.dumps(rec.to_json(), ensure_ascii=False) + "\n")

def write_csv(n: int, seed: int, out_path: str):
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["product_id","category","title","description"])
        writer.writeheader()
        for rec in generate(n, seed):
            writer.writerow(rec.to_json())
'''
with open("synthetic_data/generate_product_catalog.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Script criado ✅  -> synthetic_data/generate_product_catalog.py")

<img width="911" height="77" alt="image" src="https://github.com/user-attachments/assets/b5ea970d-7e2f-4126-8e61-d49f7a6975c2" />

#gerar 200k em JSONL
from synthetic_data.generate_product_catalog import write_jsonl

OUT = "outputs/product_catalog_200k.jsonl"
write_jsonl(n=200_000, seed=42, out_path=OUT)
print("Gerado:", OUT)

<img width="702" height="61" alt="image" src="https://github.com/user-attachments/assets/8440319b-c2bd-4f7b-a3f5-460a7474f3b1" />
