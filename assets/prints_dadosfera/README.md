

<img width="911" height="77" alt="image" src="https://github.com/user-attachments/assets/b5ea970d-7e2f-4126-8e61-d49f7a6975c2" />

#gerar 200k em JSONL
from synthetic_data.generate_product_catalog import write_jsonl

OUT = "outputs/product_catalog_200k.jsonl"
write_jsonl(n=200_000, seed=42, out_path=OUT)
print("Gerado:", OUT)

<img width="702" height="61" alt="image" src="https://github.com/user-attachments/assets/8440319b-c2bd-4f7b-a3f5-460a7474f3b1" />

## Confirmando o  tamanho e contagem de linhas
<img width="533" height="424" alt="image" src="https://github.com/user-attachments/assets/2be26308-ac72-4128-9fa0-afa456ef2ff9" />

