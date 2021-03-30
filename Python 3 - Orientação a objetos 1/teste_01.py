# ambiente de testes da classe conta:

from conta import Conta  # chama a classe "Conta" na aba "conta"


conta1 = Conta(123, "Nico", 255.5, 1000.0)
# criação de um objeto e indexando a uma variável que fica apontando para o endereço de memória do objeto
# vai imprimir uma resposta pq assim diz na classe

conta2 = Conta(321, "Marco", 500.0, 1000.0)
# criação de um novo objeto com uma nova variável para poder apontar para esse novo objeto

print("")
print("Impressão do saldo da conta 1:")
print(conta1.saldo) # chamada do método do objeto

print("")
print("Impressão do saldo da conta 2:")
print(conta2.saldo)

print("")
print("Impressão do saldo da conta 1 depois de um depósito de R$ 100:")
conta1.depositar(100)
print(conta1.saldo)

print("")
print("Impressão de uma transferência de R$ 10.00 saindo da conta 1 e indo para a conta 2:")
conta1.transferir(10, conta2)
print("Saldo conta 2: R$ {}".format(conta2.saldo))
print("Saldo conta 1: R$ {}".format(conta1.saldo))

print("")
print("Impressão do teste de alteração direta pelo método @limite.setter")
conta1.limite = 2000
print("Limite da conta 1: {}".format(conta1.limite))
print("Conta 1, número {} tem como titular o Sr. {} é o saldo e {} é o limite de {}".format(conta1.numero, conta1.titular, conta1.saldo, conta1.limite))

print("")
print("Impressão do teste da tentativa de saque de 5000:")
conta1.sacar(5000)

print("")
print("O código do banco é: {}".format(Conta.codigo_bco()))#detalhe que estou pedindo informação diretamente da classe, não do objeto

print("A Conta 1, do banco {4} número {0} tem como titular o Sr. {1} é o saldo e {2} é o limite de {3}".format(conta1.numero, conta1.titular, conta1.saldo, conta1.limite, conta1.codigo_bco()))

