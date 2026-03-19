# Mystale Catalog

Sistema web interno para catalogar criaturas energéticas relevadas en campo.
Desarrollado como take-home challenge para Mystale Labs.

---

## Requisitos

- Python 3.10+
- pip

---

## Instalación

### 1. Clonar el repositorio

\```bash
git clone https://github.com/ramirousnayo/mystale-catalog.git
cd mystale-catalog
\```

### 2. Crear y activar el entorno virtual

\```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows
\```

### 3. Instalar dependencias

\```bash
pip install -r requirements.txt
\```

### 4. Configurar variables de entorno

\```bash
cp .env.example .env
\```

Editar `.env` y completar `SECRET_KEY` con cualquier string largo y aleatorio.

### 5. Aplicar migraciones

\```bash
python manage.py migrate
\```

### 6. Cargar datos iniciales (opcional)

\```bash
python manage.py loaddata initial_data
\```

### 7. Correr el servidor

\```bash
python manage.py runserver
\```

Abrir `http://127.0.0.1:8000` en el navegador.

---

## Funcionalidades

- Catálogo navegable de criaturas con diseño tipo Pokédex
- Filtro por categoría elemental
- Formulario de registro con validaciones
- Panel de administración en `/admin/`

---

## Decisiones técnicas

### Dos modelos — dos migraciones
`CombatStats` se separó en su propio modelo en lugar de aplanar las estadísticas en `Creature`. Esto mantiene el modelo principal limpio y permite que el historial de migraciones refleje la evolución natural del esquema: primero la entidad base (`0001_creature`), luego sus estadísticas de combate (`0002_combat_stats`).

### `select_related` en todas las vistas
Todas las consultas que acceden a `combat_stats` usan `select_related` para evitar el problema N+1 — una sola query SQL en lugar de una por criatura.

### Transacción atómica en el formulario de registro
La vista `creature_create` guarda `Creature` y `CombatStats` dentro de un `transaction.atomic()`. Si cualquiera de los dos falla, ninguno se persiste. Esto garantiza consistencia en la base de datos.

### Seguridad de claves
`SECRET_KEY` y `DEBUG` se leen desde un archivo `.env` usando `python-dotenv`. El `.env` está en `.gitignore` y nunca se sube al repositorio. Se incluye `.env.example` como referencia.

---

## Estructura del proyecto

\```
mystale-catalog/
├── config/          # Configuración Django (settings, urls)
├── catalog/         # App principal
│   ├── migrations/  # 0001_creature, 0002_combat_stats
│   ├── templates/   # Templates HTML con diseño tipo Pokédex
│   ├── fixtures/    # Datos iniciales de prueba
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── .env.example
├── requirements.txt
└── README.md
\```

---

## Categorías elementales

`fuego` `agua` `tierra` `rayo` `sombra` `cristal` `viento` `hielo`