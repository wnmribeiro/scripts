import re
import sys

#Check do argumento indicando o arquivo
if len(sys.argv) == 2:
    print ("Lendo arquivo "+sys.argv[1])
elif len(sys.argv) != 2:
	print("Use o modelo - python "+sys.argv[0]+" exemplo.txt")
	exit()

# Abrindo o arquivo
text = open(sys.argv[1], mode='r', encoding='utf-8-sig')
# Criando o dicionário vazio
d = dict()

# Loop através de cada linha do arquivo
for line in text:
	# Removendo os espaços iniciais e o caractere de nova linha
	line = line.strip()

	# Convertendo os caracteres para minusculo
	line = line.lower()
	# Dividingo as linhas a cada espaço
	words = line.split(" ")
	# Iterator em cada palavra para remover todos os caracteres não alfanuméricos
	for word in words:
		word = re.sub("[^a-z0-9\n\r ]+", "", str(word))
		# Checando se a palavra já existe no dicionario
		if word in d:
			# Incrementando +1 caso já exista
			d[word] = d[word] + 1
		else:
			# Adicionando a palavra no dicionario caso não exista
			d[word] = 1

		
#Abrindo um arquivo de saida e gravando a saída
saida = open('saida.txt', 'w')
for w in sorted(d, key=d.get, reverse=True):
    print(w,d[w], file = saida)
saida.close()