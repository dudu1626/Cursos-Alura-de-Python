from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

# instanciando usuário
dudu = Usuario('Eduardo')
fer = Usuario('Fernando')
amor = Usuario('Aline')

# instanciando lance
lance_dudu = Lance(dudu, 100.0)
lance_fer = Lance(fer, 150.0)
lance_amor = Lance(amor, 200.0)

#instanciando leilão
leilao = Leilao('celular')

leilao.propoe(lance_dudu)
leilao.propoe(lance_fer)
leilao.propoe(lance_amor)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de R${lance.valor}.')


print(f'O maior lance do leilão foi de {avaliador.maior_lance} e o menor lance foi de {avaliador.menor_lance}.')


