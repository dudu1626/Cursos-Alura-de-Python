
class Usuario:
    def __init__(self, nome, valor_carteira):
        self.__nome = nome
        self.__carteira = valor_carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor_lance):
        if valor_lance > self.__carteira:
            raise ValueError('Não pode propor um lance maior que o valor de carteira')

        lance = Lance(self, valor_lance)
        leilao.propoe(lance)

        self.__carteira -= valor_lance


class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.menor_lance = 0
        self.maior_lance = 0

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if not self.__lances:
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor  # o ultimo lance será sempre o maior

            self.__lances.append(lance)
        else:
            raise ValueError('Erro ao propor lance')

    @property
    def lances(self):
        return self.__lances[:]  #devolve uma cópia da lista. Não é a original

    def _usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def _lance_maior_que_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_eh_valido(self, lance):
        return not self.__lances or self._usuarios_diferentes(lance) and self._lance_maior_que_anterior(lance)