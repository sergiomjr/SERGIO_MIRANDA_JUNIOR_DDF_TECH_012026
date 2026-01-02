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

ADJECTIVES = ["Premium", "Original", "Reforçado", "Compacto", "Lev]()

