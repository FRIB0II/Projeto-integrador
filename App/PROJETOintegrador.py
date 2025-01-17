import mysql.connector

import projetointegrador2
from datetime import datetime,timedelta

def conexao():
    global meuBancoDeDados
    meuBancoDeDados = mysql.connector.connect(
        host="localhost",
        user="root",
        database="bd_projeto"
    )
    meuCursor = meuBancoDeDados.cursor()
    return meuCursor


def entrar(usuario_login, senha_login):
  log = projetointegrador2.login1(usuario_login, senha_login)
  inserir2(log)
  cont =1 
  return cont


def cadastro(email_cad, usuario_cad, senha_cad, cod):
 cad = projetointegrador2.cadastro1(email_cad, usuario_cad, senha_cad, cod)
 inserir(cad)
 cont = 1
 return cont
 

def inserir(cadastro1):
    meuCursor = conexao()
    sql = "INSERT INTO cadastro2 (email, usuario, senha) VALUES (%s, %s, %s)"
    valor = (cadastro1.email, cadastro1.usuario, cadastro1.senha)
    meuCursor.execute(sql, valor)

    meuBancoDeDados.commit()
    print(meuCursor.rowcount, "registro inserido.")
    # livro()


def inserir2(login1):
    meuCursor = conexao()
    sql = "INSERT INTO login3 (usuario, senha) VALUES (%s, %s)"
    valor = (login1.usuario, login1.senha)
    meuCursor.execute(sql, valor)

    meuBancoDeDados.commit()
    consultar()


def consultar():
    meuCursor = conexao()
    sql = "SELECT * FROM cadastro2"
    meuCursor.execute(sql)

    meusResultados = meuCursor.fetchall()
    

    meuCursor2 = conexao()
    sql2 = "SELECT * FROM login3"
    meuCursor2.execute(sql2)

    meusResultados2 = meuCursor2.fetchall()

    aux = 0
    for resultado in meusResultados2:
       aux +=1
    
    listalog= []
    cont = 0
    
    for resultado in meusResultados2:
       loog = projetointegrador2.login1(resultado[0], resultado[1])
       listalog.append(loog)
       cont +=1
       if cont == aux:
          auxlog = loog.usuario
          auxlog2 = loog.senha 


    #listacad = []
    cont2 = 0 
    for resultado in meusResultados:
        caad = projetointegrador2.cadastro1(resultado[0], resultado[1], resultado[2], resultado[3])
        auxcad = caad.usuario
        auxcad2 = caad.senha
        global codcad
        codcad = caad.cod

        #listacad.append(caad)
        
        if auxlog == auxcad and auxlog2 == auxcad2:
           print("Login existente")
           cont2 = 1
           #livro()
    if cont2 != 1:
        print("Login não existe, faça o seu cadastro")    


def emprestimo(titulo, autor):
   print('Socorro')
   livro1 = titulo
   livro2 = autor

   meuCursor = conexao()
   sql = "SELECT * FROM livro"
   meuCursor.execute(sql)

   meusResultados = meuCursor.fetchall()
   
   global cont 
   cont = 0
   print('Sucesso')
   for resultado in meusResultados: 
     print('Sucesso 2')
     liv = projetointegrador2.livro(resultado[0],resultado[1], resultado[2])
     liv1 = liv.titulo
     liv2 = liv.autor
     global liv3
     print('Sucesso 3')
     if liv1 == livro1 and liv2 == livro2:
        print("Livro encontrado")
        cont = 1
        liv3 = liv.cod

   if cont != 1:
        print("Livro nao existe")

   if cont==1:
      dataAtual = datetime.now()
      dt_emprestimo = dataAtual.date()
      
      dt_devolucao = dt_emprestimo + timedelta(weeks=3)


      meuCursor = conexao()
      sql = "INSERT INTO emprestimo (dt_emprestimo, dt_devolucao, codlivro, codcadastro) VALUES (%s, %s, %s, %s)"
      valor = (dt_emprestimo, dt_devolucao, liv3, codcad)
      meuCursor.execute(sql, valor)
 
      meuBancoDeDados.commit()
      print("Emprestimo realizado.")
      print(f"Data da devolução: {dt_devolucao}")
      cont = 1
      return dt_devolucao
