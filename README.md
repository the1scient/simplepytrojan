# Simples Trojan feito com Python

## Como funciona?
O Trojan fará com que a máquina alvo (que estará executando o script) se conecte ao CCHOST (máquina atacante).

O CCHOST deverá estar executando o netcat com o comando `sudo nc -lvp 443`.

Após a conexão, a máquina atacante irá conseguir executar comandos na máquina alvo, como `whoami` e `dir`, conseguirá criar/remover pastas e arquivos, executar scripts, entre outros.

Agradecimentos ao Cryptodata.
