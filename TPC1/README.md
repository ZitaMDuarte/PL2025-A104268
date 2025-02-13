# 📌 Somador On/Off

## 📅 Data
13/02/2025

## 👤 Autor
- **Nome:** Zita Magalhães Duarte
- **Número de Aluno:** A104268

![Zita Duarte](../zitaduarte.jpeg)

## 📖 Resumo
Este projeto consiste num programa em Python que processa um texto e soma todas as sequências de dígitos encontradas, com um comportamento que pode ser ativado e desativado com palavras-chave.

### 🔹 Funcionamento:
1. O programa soma todos os números encontrados no texto.
2. Sempre que encontra a string "Off" (insensível a maiúsculas e minúsculas), o comportamento de soma é desativado.
3. Sempre que encontra a string "On" (também insensível a maiúsculas e minúsculas), o comportamento de soma é reativado.
4. Sempre que encontra o caráter "=", o resultado da soma é apresentado na saída.
5. O programa pode receber um ficheiro como entrada ou aceitar texto digitado pelo utilizador.

## 📂 Estrutura do Código

### 🔹 `process_text(text)`
```python
import sys

def process_text(text):
    total = 0
    current_number = ''
    summing = True
    index = 0
    
    while index < len(text):
        char = text[index]
        
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                if summing:
                    total += int(current_number)
                current_number = ''
            
            if char == '=':
                print(total)
            elif char.lower() == 'o':  # Pode ser início de "On" ou "Off"
                if text[index:index+2].lower() == 'on':
                    summing = True
                    index += 1  # Pular o próximo caractere "n"
                elif text[index:index+3].lower() == 'off':
                    summing = False
                    index += 2  # Pular os próximos caracteres "ff"
        index += 1
    
    if current_number and summing:
        total += int(current_number)
```

### 🔹 `main()`
```python
def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            content = file.read()
    else:
        content = input("Digite o texto: ")
    
    process_text(content)

if __name__ == "__main__":
    main()
```

## 🛠️ Execução do Programa
O programa pode ser executado de duas formas:
1. Com um ficheiro de entrada:
   ```bash
   python tpc1.py input.txt
   ```
2. Diretamente no terminal:
   ```bash
   python tpc1.py
   Digite o texto: 12On34Off56On78=
   124
   ```

---

