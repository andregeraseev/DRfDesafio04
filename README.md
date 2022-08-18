![image](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)


##  Api Financeiro

Projeto de gerenciamento financeiro para despesas e rendas, devolvendo listas de ambas com consultas e resumos mensais.
consiste em um  CRUD que pode ser utilizado diretamente pela URL, abaixo temos todas endpoits, tambem pode ser utilizado mandando e recebendo requisições com programas como postman por exemplo, todos modelos para fazer as requisisões estão abaixo.


## Endpoints para utilizar o projeto

https://desafiobackend04.herokuapp.com/doc/

<b>cadastrar_usuario</b>


GET
/cadastrar_usuario/

cadastrar_usuario_list


POST
/cadastrar_usuario/

cadastrar_usuario_create


GET
/cadastrar_usuario/{id}/

cadastrar_usuario_read


PUT
/cadastrar_usuario/{id}/

cadastrar_usuario_update


PATCH
/cadastrar_usuario/{id}/

cadastrar_usuario_partial_update


DELETE
/cadastrar_usuario/{id}/

cadastrar_usuario_delete

<b>despesas</b>


GET
/despesas/

despesas_list


POST
/despesas/

despesas_create


GET
/despesas/{ano}/{mes}/

despesas_read


GET
/despesas/{id}/

despesas_read


PUT
/despesas/{id}/

despesas_update


PATCH
/despesas/{id}/

despesas_partial_update


DELETE
/despesas/{id}/

despesas_delete

<b>receitas</b>


GET
/receitas/

receitas_list


POST
/receitas/

receitas_create


GET
/receitas/{ano}/{mes}/

receitas_read


GET
/receitas/{id}/

receitas_read


PUT
/receitas/{id}/

receitas_update


PATCH
/receitas/{id}/

receitas_partial_update


DELETE
/receitas/{id}/

receitas_delete

<b>resumo</b>

GET
/resumo/{ano}/{mes}/


## Modelos

# Usuario
```
{
username*                      string
                               title: Username
                               maxLength: 40
                               minLength: 1
                               
email*	                       string($email)          
                               title: Email
                               maxLength: 30
                               minLength: 1
                               
password*	                     string($slug)        
                               title: Senha                   
                               pattern: ^[-a-zA-Z0-9_]+$
                               minLength: 1
                               
password_confirm*	             string($slug)
                               title: Confirme a senha        
                               pattern: ^[-a-zA-Z0-9_]+$
                               minLength: 1 
}
```

## Despesas
```
{
descricao*	                    string
                                title: Descricao
                                maxLength: 100
                                minLength: 1
                                
valor*	                        string($decimal)
                                title: Valor     

categoria	                      string
                                title: Categoria
                                Enum:
                                Array [ 8 ]
                                
data*	                          string($date)
                                title: Data 
}
```

## Receita
```
{
descricao*	                    string               
                                title: Descricao
                                maxLength: 100
                                minLength: 1
                                
valor*	                        string($decimal)
                                title: Valor
                                
categoria*	                    string
                                title: Categoria
                                maxLength: 50
                                minLength: 1
                                
data*	                          string($date)
                                title: Data
 
}
```

## 📁 Acesso ao projeto

https://desafiobackend04.herokuapp.com/

crie um usuario novo em: 
https://desafiobackend04.herokuapp.com/cadastrar_usuario/

ou use o nosso usuario teste:

usuario: test

senha: 123456

