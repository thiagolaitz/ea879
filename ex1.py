#Thiago Soares Laitz

import ply.lex as lex

#Definição dos possíveis tokens
tokens = (
   'TOKEN_INT',
   'TOKEN_EXP',
   'TOKEN_HEX',
   'TOKEN_FLOAT',
)

#Funções que descrevem as expressões regulares
def t_TOKEN_EXP(t):
   r'(-?[0-9]+\.[0-9]+[eE]-?([0-9])+) | (-?[0-9]+[eE]-?([0-9])+)'
   return t


def t_TOKEN_HEX(t):
   r'0[xX]([0-9]|[a-f]|[A-F])+'
   return t


def t_TOKEN_FLOAT(t):
   r'-?[0-9]+\.[0-9]+'
   return t


def t_TOKEN_INT(t):
   r'-?[0-9]+'
   return t

#Caso em que não reconheça o símbolo digitado
def t_error(t):
   print("Simbolo NAO reconhecido: {}".format(t.value[0]))
   t.lexer.skip(1)

# o analisador lexico
lexer = lex.lex()

if __name__ == "__main__":
   pilha = []
   while True:
      try:
         texto = input("\nDigite um texto: ")
      except EOFError:
         print("\n")
         break
      # analisa o texto
      lexer.input(texto)

      # processa cada token
      while True:
         tok = lexer.token()
         if tok and tok.type == 'TOKEN_EXP': #Caso exp
            print("Expressao reconhecida exp: {}".format(tok.value))
            pilha.append(float(tok.value))
         elif tok and tok.type == 'TOKEN_INT': #Caso int
            print("Expressao reconhecida int: {}".format(tok.value))
            pilha.append(int(tok.value))
         elif tok and tok.type == 'TOKEN_FLOAT': #Caso float
            print("Expressao reconhecida float: {}".format(tok.value))
            pilha.append(float(tok.value))
         elif tok and tok.type == 'TOKEN_HEX': #Caso hex
            print("Expressao reconhecida hex: {}".format(tok.value))
            pilha.append(int(tok.value, 16))

         elif tok == None:
            break

         print("Pilha:", pilha)
