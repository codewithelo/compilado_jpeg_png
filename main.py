from PIL import Image
import os
import re

def chave_ordenacao_natural(texto):
    """
    Divide a string em partes de texto e números.
    Converte os números para inteiros para que sejam ordenados matematicamente.
    """
    return [int(parte) if parte.isdigit() else parte.lower() for parte in re.split(r'(\d+)', texto)]

def concatenar_imagens_para_pdf():
    diretorio_entrada = "/app/input"
    
    if not os.path.exists(diretorio_entrada):
        print(f"O diretório {diretorio_entrada} não existe.")
        return

    print(f"Procurando imagens em: {diretorio_entrada}")
    
    # Lista todos os arquivos da pasta mapeada
    arquivos_pasta = os.listdir(diretorio_entrada)
    
    # Filtra apenas imagens válidas
    image_files = [f for f in arquivos_pasta if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("Nenhum arquivo de imagem encontrado na pasta 'input'.")
        print("Por favor, coloque suas imagens na pasta local './input' e tente novamente.")
        return

    # Ordena os arquivos usando a ordenação natural
    image_files.sort(key=chave_ordenacao_natural)

    print("\nProcessando os seguintes arquivos na ordem correta:")
    for img_name in image_files:
        print(f"- {img_name}")

    # Abre e converte todas as imagens para o formato RGB
    imagens = []
    for f in image_files:
        caminho_completo = os.path.join(diretorio_entrada, f)
        try:
            imagem = Image.open(caminho_completo)
            if imagem.mode in ('RGBA', 'LA', 'P'):
                imagem = imagem.convert('RGB')
            imagens.append(imagem)
        except Exception as e:
            print(f"Erro ao abrir a imagem {f}: {e}")

    nome_saida = os.path.join(diretorio_entrada, "imagens_concatenadas.pdf")

    # Salva o PDF no diretório mapeado
    if imagens:
        imagens[0].save(
            nome_saida,
            save_all=True,
            append_images=imagens[1:]
        )
        print(f"\nSucesso! Arquivo gerado em: {nome_saida}")

if __name__ == "__main__":
    concatenar_imagens_para_pdf()