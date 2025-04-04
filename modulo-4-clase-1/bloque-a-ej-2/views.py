# views.py
from templates import render_template

class View:
    """
    Clase base para las vistas que manejan las respuestas HTTP.
    Proporciona métodos para renderizar templates HTML.
    """
    
    def get_response(self):
        """
        Maneja la vista de la página principal.
        
        Returns:
            str: Nombre del archivo de template HTML para la página principal ('home.html')
        """
        return render_template("home.html")