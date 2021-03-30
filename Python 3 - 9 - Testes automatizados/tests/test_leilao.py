from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao

# criado automaticamente com o comando Ctrl+shift+t com o cursor na classe Avaliador


class TestLeilao(TestCase):

    def setUp(self):  # criação de um cenário único para os teste rodarem
        self.dudu = Usuario('Eduardo', 300.0)
        self.fer = Usuario('Fernando', 300.0)
        self.amor = Usuario('Aline', 300.0)

        self.lance_amor = Lance(self.amor, 100.0)
        self.lance_fer = Lance(self.fer, 150.0)
        self.lance_dudu = Lance(self.dudu, 200.0)
        self.leilao = Leilao('celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_amor)
        self.leilao.propoe(self.lance_fer)
        self.leilao.propoe(self.lance_dudu)

        valor_esperado_maior = 200.0
        valor_esperado_menor = 100.0

        self.assertEqual(valor_esperado_menor, self.leilao.menor_lance)
        self.assertEqual(valor_esperado_maior, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_apenas_um_lance(self):
        self.leilao.propoe(self.lance_dudu)

        valor_esperado_maior = 200
        valor_esperado_menor = 200

        self.assertEqual(valor_esperado_menor, self.leilao.menor_lance)
        self.assertEqual(valor_esperado_maior, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_dudu)
            self.leilao.propoe(self.lance_fer)
            self.leilao.propoe(self.lance_amor)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_dudu_250 = Lance(self.dudu, 250.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_dudu)
            self.leilao.propoe(lance_dudu_250)
