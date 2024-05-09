# Python-TowerUniteImageRec
Este é um script Python que utiliza várias bibliotecas para realizar a leitura de texto em imagens e automatizar a digitação do texto lido.

## Dependências
O script utiliza as seguintes bibliotecas:

cv2: Para processamento de imagens.
pytesseract: Para realizar OCR (Optical Character Recognition) nas imagens.
pyautogui: Para capturar screenshots e automatizar a digitação.
keyboard: Para detectar quando uma tecla específica é pressionada.
pynput: Para obter as coordenadas do mouse.
## Como funciona
O script funciona da seguinte maneira:

Primeiro, ele define o caminho para o executável do Tesseract-OCR.
Em seguida, define uma função get_text_from_img(img) que recebe uma imagem, aplica um threshold e usa o Tesseract para extrair o texto da imagem.
O script então entra em um loop onde captura screenshots de uma região específica da tela, extrai o texto da imagem capturada e digita o texto extraído.
Além disso, o script também contém um listener de mouse que imprime as coordenadas do mouse quando um botão do mouse é pressionado. Isso pode ser útil para determinar as coordenadas para a captura de screenshot.
Por fim, o script contém um loop onde pressiona a tecla de espaço várias vezes com um delay decrescente entre cada pressionamento.
Uso
Para usar o script, você precisa ter todas as bibliotecas necessárias instaladas e o Tesseract-OCR instalado no caminho especificado no script. Em seguida, você pode simplesmente executar o script e ele começará a funcionar.

Por favor, note que você pode precisar ajustar as coordenadas para a captura de screenshot e os valores de delay para a digitação automática para se adequar ao seu caso de uso específico.
