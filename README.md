# 🧬 Mystale Catalog

Sistema web interno para catalogar criaturas energéticas relevadas en campo.  
Desarrollado como *take-home challenge* para Mystale Labs.

---

## 📋 Requisitos

- Python 3.10+
- pip

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ramirousnayo/mystale-catalog.git
cd mystale-catalog
```

---

### 2. Crear y activar el entorno virtual

**Mac / Linux**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Configurar variables de entorno

```bash
cp .env.example .env
```

Editar `.env`:

```env
SECRET_KEY=tu_clave_secreta_larga_y_aleatoria
```

---

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

---

### 6. Cargar datos iniciales (opcional)

```bash
python manage.py loaddata initial_data
```

---

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir: http://127.0.0.1:8000

---

## 🚀 Funcionalidades

- Catálogo navegable de criaturas (tipo Pokédex)  
- Filtro por categoría elemental  
- Formulario de registro con validaciones  
- Panel de administración en `/admin/`  

---

## 🧠 Decisiones Técnicas

### Dos modelos — dos migraciones

`CombatStats` se separa de `Creature` para mantener el modelo limpio:

- `0001_creature`
- `0002_combat_stats`

---

### Uso de `select_related`

Se evita el problema N+1 usando:

```python
Creature.objects.select_related('combat_stats')
```

---

### Transacción atómica

```python
from django.db import transaction

with transaction.atomic():
    # guardar creature y stats
```

---

### Seguridad

- Uso de `.env` con `python-dotenv`
- `.env` en `.gitignore`
- `.env.example` como referencia

---

## 📁 Estructura del Proyecto

```bash
mystale-catalog/
├── config/
├── catalog/
│   ├── migrations/
│   ├── templates/
│   ├── fixtures/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🌍 Categorías Elementales

🔥 Fuego
💧 Agua
🌱 Tierra
⚡ Rayo
🌑 Sombra
💎 Cristal
🌪️ Viento
❄️ Hielo
