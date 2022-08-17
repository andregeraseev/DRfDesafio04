## Readme Projeto Api Financeiro

Api que guarda despesas e rendas, devolvendo listas de ambas com consultas e resumos mensais  


## Endpoints para utilizar o projeto

https://desafiobackend04.herokuapp.com/doc/

##cadastrar_usuario


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

##despesas


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

##receitas


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

##resumo

GET
/resumo/{ano}/{mes}/



## 📁 Acesso ao projeto

https://desafiobackend04.herokuapp.com/

crie um usuario novo em: 
https://desafiobackend04.herokuapp.com/cadastrar_usuario/

ou use o nosso usuario teste:
usuario: test
senha: 123456

