# Dio - Python

## Projetos e desafios do bootcamp "Potência Tech powered by iFood | Ciência de Dados"

### Sistema bancário versão 1 :

O desafio consiste em desenvolver um sistema bancário simples
utilizando a linguagem Python.
Para a primeira versão do sistema devemos implementar apenas 3 
operações: depósito, saque e extrato.
Neste sistema considera-se apenas um usuário.
```
Operação de depósito:
- Todos os depósitos devem ser armazenados em uma variável e
exibidos na operação de extrato.

Operação de saque:
- O sistema deve permitir realizar 3 saques diários com limite
máximo de R$ 500,00 por saque.
- Caso o usuário não tenha saldo em conta, o sistema deve exibir
uma mensagem informando que não será possível sacar o dinheiro
por falta de saldo.
- Todos os saques devem ser armazenados em uma variável e exibidos
na operação de extrato.

Operação de extrato:
- Essa operação deve listar todos os depósitos e saques
realizados na conta.
- No fim da listagem deve ser exibido o saldo atual da conta.
- Se o extrato estiver em branco, exibir a mensagem:
"Não foram realizadas movimentações."
- Os valores devem ser exibidos utilizando o formato R$ xxx.xx
```


### Sistema bancário versão 2 : 

Objetivo Geral
Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: Cadastrar usuário (cliente) e cadastrar conta bancária.

Desafio
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)

1- Pegar o código e separá-lo em funções - Sacar, Depositar e Extrato.
Cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas pode ser definida por você.

```
Saque:
A função de saque deve receber os argumentos apenas por nome ( keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

Depósito:
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

Extrato:
A função extrato deve receber os argumentos por posição e nome ( positional e keyword). Argumentos posicionais: saldo, argumentos nomeados: extrato.
```

2- Criar duas novas funções - Criar usuário e Criar conta corrente e vincular com o usuário.

```
Criar usuário ( Cliente) 
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do cpf. Não podemos cadastrar 2 usuários com o mesmo cpf.

Criar conta corrente
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo “0001”. O usuário pode ter mais de uma conta, mas uma conta pertece somente a um usuário.

Dica
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do cpf informado para cada usuário da lista.
```
