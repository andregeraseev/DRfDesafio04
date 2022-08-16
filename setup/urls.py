from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from renda.views import ReceitaViewSet, DespesasViewSet, ListaReceitasMes, ListaDespesasMes, ResumoView
from usuario.views import UsuariosViewSet, ListaUsuarios



router = routers.DefaultRouter()

router.register(r'receitas', ReceitaViewSet, basename='Receitas')
router.register(r'despesas', DespesasViewSet, basename='Despesas')
router.register('cadastrar_usuario', UsuariosViewSet, basename='Cadastrar Usuário')


urlpatterns = [
    path('', include((router.urls))),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('receitas/<int:ano>/<int:mes>/', ListaReceitasMes.as_view()),
    path('despesas/<int:ano>/<int:mes>/', ListaDespesasMes.as_view()),
    path('resumo/<int:ano>/<int:mes>/', ResumoView.as_view()),
    path('cadastrar_usuario/', ListaUsuarios.as_view())

]
