import re

class Verifica:
    def cpf_soma(self, data, soma, indice):
        
        soma += int(data[indice]) * self.contador
        
        self.contador -= 1
        if (self.contador >= 2):
            return self.cpf_soma(data, soma, indice+1)
        return soma

    def cpf_divisao(self, data, soma):
        resto = soma * 10 % 11 if soma * 10 % 11 != 10 else 0
        return True if data == resto else False

    def cpf(self, data):
        # padroniza a string
        data = ''.join(re.findall(r"[\w']+", data))

        # verifica se é um cpf de numeros repetidos
        if data in [s * 11 for s in [str(n) for n in range(10)]]:
            return False

        # faz a primeira verificacao
        self.contador = 10
        soma = self.cpf_soma(data, 0, 0) 
        if (self.cpf_divisao(int(data[9]), soma)):
            # faz a segunda verificacao
            self.contador = 11
            soma = self.cpf_soma(data, 0, 0)
            if (self.cpf_divisao(int(data[10]), soma)):
                return True
        return False

    def cnpj(self, data):
        # padroniza a string
        data = ''.join(re.findall(r"[\w']+", data))

        # verifica se é um cnpj de numeros repetidos
        if data in [s * 11 for s in [str(n) for n in range(10)]]:
            return False
        
        inteiros = list(map(int, data))
        novo = inteiros[:12]

        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        while len(novo) < 14:
            r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
            if r > 1:
                f = 11 - r
            else:
                f = 0
            novo.append(f)
            prod.insert(0, 6)

        # Se o número gerado coincidir com o número original, é válido
        if novo == inteiros:
            return True
        return False

