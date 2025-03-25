class Parser:
    def __init__(self, input_str):
        self.tokens = self.tokenizar(input_str)
        self.pos = 0

    def tokenizar(self, input_str):
        tokens = []
        i = 0
        while i < len(input_str):
            if input_str[i].isspace():
                i += 1
            elif input_str[i] in '+-*/()':
                tokens.append(input_str[i])
                i += 1
            elif input_str[i].isdigit():
                num = ''
                while i < len(input_str) and input_str[i].isdigit():
                    num += input_str[i]
                    i += 1
                tokens.append(num)
            else:
                raise ValueError(f"Carácter inválido: {input_str[i]}")
        tokens.append('$')  # fim da entrada
        return tokens

    def current_token(self):
        return self.tokens[self.pos]

    def eat(self, token):
        if self.current_token() == token:
            self.pos += 1
        else:
            raise ValueError(f"Esperado '{token}', mas obtido '{self.current_token()}'")

    def parse(self):
        resultado = self.expr()
        if self.current_token() != '$':
            raise ValueError("Expressão mal formada.")
        return resultado

    def expr(self):
        resultado = self.term()
        while self.current_token() in ('+', '-'):
            op = self.current_token()
            self.eat(op)
            if op == '+':
                resultado += self.term()
            else:
                resultado -= self.term()
        return resultado

    def term(self):
        resultado = self.factor()
        while self.current_token() in ('*', '/'):
            op = self.current_token()
            self.eat(op)
            if op == '*':
                resultado *= self.factor()
            else:
                resultado /= self.factor()
        return resultado

    def factor(self):
        if self.current_token() == '(':
            self.eat('(')
            resultado = self.expr()
            self.eat(')')
            return resultado
        else:
            valor = int(self.current_token())
            self.eat(self.current_token())
            return valor


# Exemplo de uso:
if __name__ == "__main__":
    expr = input("Introduz a expressão: ")
    parser = Parser(expr)
    try:
        resultado = parser.parse()
        print("Resultado:", resultado)
    except ValueError as e:
        print("Erro:", e)
