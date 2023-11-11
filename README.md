## Projeto de Controle Financeiro e Conversor de Moedas

Este é um simples projeto de controle financeiro e conversor de moedas desenvolvido em Python usando a biblioteca Tkinter. Ele consiste em duas funcionalidades principais:

1. **Controle Financeiro (Meta Financeira):**
   - Permite ao usuário definir uma meta de poupança e o valor mensal que pretende economizar.
   - Calcula automaticamente o número de meses necessários para atingir a meta.
   - Interface gráfica amigável.

2. **Conversor de Moedas:**
   - Obtém dados de uma API de câmbio para listar as moedas disponíveis.
   - Permite ao usuário escolher uma moeda e converter um valor para essa moeda.
   - Fornece uma interface simples com um campo de entrada, lista suspensa e botão de conversão.
### Teste Online

- Você pode testar a aplicação online [aqui](https://replit.com/@GilbertoSa/App-Financeiro).

### Vídeo de Demonstração

- Assista a um vídeo de demonstração [aqui](https://drive.google.com/file/d/1PZNI-1gUONKQlGZjgNPIPr7bHIQeCiUz/view?usp=drive_link).

### Estrutura do Código

- `main.py`: Script principal que inicia a interface gráfica e contém a lógica principal.
- `financeiro.py`: Módulo com as funções relacionadas ao controle financeiro.
- `conversor.py`: Módulo com as funções relacionadas ao conversor de moedas.

### Bibliotecas Utilizadas

- `tkinter`: Usada para criar a interface gráfica.
- `requests`: Utilizada para realizar requisições HTTP para a API de câmbio.
- `xmltodict`: Usada para desserializar os dados XML obtidos da API.
