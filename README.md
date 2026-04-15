# Calculadora TecMilenio (Aritmética, Binaria y Lógica)

Ejercicio que implementa una calculadora web en **Python (Flask)**,
contenedorizada con **Docker**, desplegada mediante **AWS CodePipeline** y validada en **Cloud Shell** 
con registro de cambios en `backup.log`.

---

## 📂 Estructura del proyecto
├── app.py              # Aplicación Flask
├── templates/
│   └── index.html      # Interfaz web
├── requirements.txt    # Dependencias
├── Dockerfile          # Imagen Docker
├── buildspec.yml       # Configuración AWS CodeBuild
├── backup.log          # Registro de cambios
└── README.md           # Documentación
