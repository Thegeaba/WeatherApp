# Am creat fisierul "urls.py" pentru a crea diferite rute (routes), pentru ca mai apoi sa le conectam cu "views.py".

from django.urls import path
from . import views # importez views.py folderul curent

# In "urlpatterns" specific caile care conecteaza un URL pattern de o cale sau un view specific
urlpatterns = [
    # defaulte route = ""
    
    # Cand ma duc la calea "", chemam functia home() din views.py care la randul ei o sa returneze un raspuns http ce ne va permite 
    # sa il vizualizam.

    path("", views.home, name = "home")
]

# (1)
# !!! URL-ul este configurat pentru aplicatia "Soccer", dar trebuie configurat si pentru "WebData".
# Vezi WebData -> urls.py