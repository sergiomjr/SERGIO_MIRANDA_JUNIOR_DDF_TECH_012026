#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador de Catálogo de Produtos Sintético (E-commerce) – 100k+ registros
Saída principal: NDJSON (.jsonl) para facilitar ingestão e volumes grandes.

Uso (exemplos):
  python synthetic_data/generate_product_catalog.py \
    --n 120000 \
    --out synthetic_data/product_catalog_120k.jsonl

  # com CSV também
  python synthetic_data/generate_product_catalog.py \
    --n 100000 \
    --out synthetic_data/product_catalog_100k.jsonl \
    --csv synthetic_data/product_catalog_100k.csv

Observações:
- "product_id" segue o padrão UUID4 (string).
- Textos longos variam por categoria e incluem atributos técnicos e claims.
- Seed garante reprodutibilidade.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
import uuid
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


# -----------------------------
# Configuração de categorias e dicionários
# -----------------------------

# Categorias inspiradas no domínio do Olist (PT-BR) + algumas variações realistas
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

COLORS = [
    "Preto", "Branco", "Cinza", "Azul", "Vermelho", "Verde", "Rosa", "Roxo", "Dourado", "Prata",
]
SIZES = ["PP", "P", "M", "G", "GG", "Único"]
WARRANTY = ["90 dias", "6 meses", "12 meses", "24 meses"]
SHIPPING = ["Envio imediato", "Postagem em 24h", "Postagem em 48h", "Sob encomenda (3-5 dias)"]

ADJECTIVES = ["Premium", "Original", "Reforçado", "Compacto", "Leve", "Ultra resistente", "Profissional", "Econômico"]
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

# Palavras para formar descrições longas com variação
PHRASES = [
    "Fabricado com materiais selecionados e padrão de qualidade elevado.",
    "Desenvolvido para oferecer desempenho consistente e uso confortável.",
    "Projetado para encaixe preciso e melhor experiência do usuário.",
    "Excelente escolha para quem busca durabilidade e estética.",
    "Produto com ótimo acabamento, resistente ao uso contínuo.",
    "Compatível com múltiplos cenários de uso e fácil instalação.",
    "Recomendado para consumidores que valorizam segurança e praticidade.",
]


# -----------------------------
# Utilidades
# -----------------------------

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\s+", "_", text)
    text = re.sub(r"[^a-z0-9_]+", "", text)
    return text[:60] if len(text) > 60 else text


def pick_weighted(rng: random.Random, items: List[str]) -> str:
    return rng.choice(items)


def make_product_id() -> str:
    return str(uuid.uuid4())


@dataclass
class ProductRecord:
    product_id: str
    category: str
    title: str
    description: str

    def to_json(self) -> Dict[str, str]:
        return {
            "product_id": self.product_id,
            "category": self.category,
            "title": self.title,
            "description": self.description,
        }


def build_title(rng: random.Random, category: str, meta: Dict[str, List[str]]) -> str:
    brand = pick_weighted(rng, meta["brands"])
    material = pick_weighted(rng, meta["materials"])
    feat = pick_weighted(rng, meta["features"])
    compat = pick_weighted(rng, meta["compat"])
    color = pick_weighted(rng, COLORS)

    adj = pick_weighted(rng, ADJECTIVES)

    # Títulos variam por categoria
    templates = [
        f"{adj} {brand} {category.replace('_', ' ').title()} em {material} – {feat} – {color} – Compatível com {compat}",
        f"{brand} {category.replace('_', ' ').title()} {adj} ({material}) com {feat} | Cor {color} | {compat}",
        f"{adj} {category.replace('_', ' ').title()} {brand} {material} – {feat} – Para {compat} – {color}",
    ]
    return pick_weighted(rng, templates)


def build_description(rng: random.Random, category: str, meta: Dict[str, List[str]]) -> str:
    material = pick_weighted(rng, meta["materials"])
    brand = pick_weighted(rng, meta["brands"])
    compat = pick_weighted(rng, meta["compat"])
    color = pick_weighted(rng, COLORS)
    size = pick_weighted(rng, SIZES)
    warranty = pick_weighted(rng, WARRANTY)
    shipping = pick_weighted(rng, SHIPPING)

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

    # Texto longo com parágrafos + bullets + disclaimers
    paragraph_1 = " ".join(rng.sample(PHRASES, k=3))
    paragraph_2 = " ".join(rng.sample(PHRASES, k=3))
    paragraph_3 = pick_weighted(rng, BENEFITS)

    disclaimer = " ".join(rng.sample(DISCLAIMER, k=2))

    # Inserir algo semiestruturado típico de e-commerce
    desc = (
        f"{paragraph_1}\n\n"
        f"{paragraph_2}\n\n"
        f"{paragraph_3}\n\n"
        f"Especificações:\n" + "\n".join(bullets) + "\n\n"
        f"Observações: {disclaimer}"
    )
    return desc


def generate_records(n: int, seed: int) -> List[ProductRecord]:
    rng = random.Random(seed)
    cats = list(CATEGORIES.keys())

    records: List[ProductRecord] = []
    for _ in range(n):
        category = pick_weighted(rng, cats)
        meta = CATEGORIES[category]

        pid = make_product_id()
        title = build_title(rng, category, meta)
        description = build_description(rng, category, meta)

        records.append(ProductRecord(
            product_id=pid,
            category=category,
            title=title,
            description=description
        ))

    return records


def write_jsonl(records: List[ProductRecord], out_path: str) -> None:
    with open(out_path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r.to_json(), ensure_ascii=False) + "\n")


def write_csv(records: List[ProductRecord], out_path: str) -> None:
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["product_id", "category", "title", "description"])
        writer.writeheader()
        for r in records:
            writer.writerow(r.to_json())


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Gerar catálogo sintético de produtos (JSONL/CSV)")
    p.add_argument("--n", type=int, default=100_000, help="Número de registros a gerar (default: 100000)")
    p.add_argument("--seed", type=int, default=42, help="Seed para reprodutibilidade (default: 42)")
    p.add_argument("--out", type=str, required=True, help="Caminho do arquivo de saída .jsonl (NDJSON)")
    p.add_argument("--csv", type=str, default="", help="(Opcional) Caminho de saída .csv")
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)

    if args.n < 100_000:
        print("[ERRO] O case exige >= 100.000 registros. Use --n 100000 ou mais.", file=sys.stderr)
        return 2

    if not args.out.endswith(".jsonl"):
        print("[DICA] Recomendo usar extensão .jsonl para NDJSON. Ex: product_catalog_100k.jsonl", file=sys.stderr)

    print(f"[INFO] Gerando {args.n} registros com seed={args.seed} ...")
    records = generate_records(args.n, args.seed)

    print(f"[INFO] Salvando JSONL em: {args.out}")
    write_jsonl(records, args.out)

    if args.csv:
        print(f"[INFO] Salvando CSV em: {args.csv}")
        write_csv(records, args.csv)

    print("[OK] Geração concluída.")
    print("[OK] Próximo passo: fazer upload do JSONL na Dadosfera e catalogar o dataset.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
