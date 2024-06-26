import os 

arquivo = open("dados.txt", "r")
print(arquivo.readlines())
arquivo.close()

with open("dados.txt", "r") as file:
    print(file.read())

with open("dados.txt", "r") as file:
    linhas = file.readlines()
    for linha in linhas:
        print(f"olha a linha: {linha}")

class Id:      
    def __init__(self, tabela, id=1):
        self.file = "ids.csv"
        self.tabela = tabela
        self.id = id

    def save(self):
        line = f"{self.tabela},{self.id}\n"
        with open(self.file, "a") as file:
            file.write(linha)
            

    def read(self):
        with open(self.file, "r") as file:
            for linha in file:
                tabela, id = linha.strip().split(",")
                if tabela == self.tabela:
                    return int(id)

    def update(self):
        with open(self.file, "a") as file:
            lines = file.readlines()
            for line in file:
                if line.startswith(self.tabela):
                    index = lines.index(line)
                    line = f"{self.tabela},{self.id}\n"
                    lines[index] = line
            file.write("".join(lines))
    def delete(self):
        pass


class Produto:      
    def __init__(self, nome, descricao, preco, imagem, id=0):
        self.file = "produtos.csv"
        self.nome = nome
        self.preco = preco
        self.descricao = descricao 
        self.imagem = imagem
        if id > 0:
            self.id = id
        else:
            id_class = Id("produtos")
            self.id = id_class.read() + 1
        

    def save(self):
        linha = f"{self.id},{self.nome},{self.descricao},{self.preco},{self.imagem}\n"
        with open(self.file, "a") as file:
            file.write(linha)
            
        id_class = Id("produtos", self.id)
        id_class.update()

    
    @staticmethod
    def readAll():
        produtos = []

        with open("produtos.csv", "r") as file:
            for linha in file:
                id, nome, descricao, preco, imagem = linha.strip().split(",")
                
                produto = Produto(nome, descricao, float(preco), imagem, int(id))

                produtos.append(produto)

        return produtos


    def __str__(self):
        return f"Produto=[ nome = {self.nome},\n\tdescricao = {self.descricao},\n\tpreco = {self.preco},\n\timage = {self.imagem} ]"

    def update(self):
        pass

    def delete(self):
        pass


print("\n".join([str(i) for i in Produto.readAll()]))
coca = Produto("Coca-cola", "mata a sede", 5.00, "coca.png")
doritos = Produto("Doritos", "suja a mao", 15.00, "doritos.png")
mouse = Produto("Mouse", "coisnasfasfasf", 15.00, "mouse.png")
teclado = Produto("Teclado", "Muito barulhento", 180.00, "teclado.png")
coca.save()
doritos.save()
mouse.save()
teclado.save()
print()
print("\n".join([str(i) for i in Produto.readAll()]))


    