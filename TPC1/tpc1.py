import sys

def process_text(text):
    total = 0
    current_number = ''
    summing = True
    
    for char in text:
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
                index = text.index(char)
                if text[index:index+2].lower() == 'on':
                    summing = True
                elif text[index:index+3].lower() == 'off':
                    summing = False
    
    if current_number and summing:
        total += int(current_number)


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            content = file.read()
    else:
        content = input("Digite o texto: ")
    
    process_text(content)

if __name__ == "__main__":
    main()
 
