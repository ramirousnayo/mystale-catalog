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
# Mystale Catalog

Sistema web para registrar y consultar criaturas energéticas. Proyecto preparado como take-home challenge.

## Contenido

- Catálogo con filtro por elemento
- Formulario para registrar criaturas y sus estadísticas de combate
- Integración con el panel de administración de Django

---

## Requisitos

- Python 3.10+
- pip

---

## Instalación rápida

1. Clona el repositorio:

```bash
git clone https://github.com/ramirousnayo/mystale-catalog.git
cd mystale-catalog
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate  # Windows
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Copia el ejemplo de variables de entorno y edítalo:

```bash
cp .env.example .env
```

# Mystale Catalog

Sistema web para registrar y consultar criaturas energéticas. Proyecto preparado como take-home challenge.

## Contenido

- Catálogo con filtro por elemento
- Formulario para registrar criaturas y sus estadísticas de combate
- Integración con el panel de administración de Django

---

## Requisitos

- Python 3.10+
- pip

---

## Instalación rápida

1. Clona el repositorio:

```bash
git clone https://github.com/ramirousnayo/mystale-catalog.git
cd mystale-catalog
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate  # Windows
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Copia el ejemplo de variables de entorno y edítalo:

```bash
cp .env.example .env
```

Rellena `SECRET_KEY` en `.env` con una cadena larga y segura.

5. Aplica migraciones:

```bash
python manage.py migrate
```

6. (Opcional) Carga datos iniciales:

```bash
python manage.py loaddata initial_data
```

7. Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre http://127.0.0.1:8000 en tu navegador.

---

## Funcionalidades principales

- Navegación por catálogo con tarjetas temáticas por elemento
- Filtro por elemento
- Registro de criaturas con estadísticas de combate (HP, Ataque, Defensa, Velocidad)
- Panel de administración en `/admin/`

---

## Decisiones técnicas (resumen)

- `CombatStats` es un modelo separado relacionado one-to-one con `Creature` para mantener el modelo principal sencillo y explícito en migraciones.
- Se usa `select_related('combat_stats')` en vistas para evitar consultas N+1.
- El registro de criatura y sus estadísticas se guarda dentro de `transaction.atomic()` para garantizar consistencia.
- `SECRET_KEY` y `DEBUG` se leen de `.env` usando `python-dotenv`. El `.env` no debe subirse al repositorio.

---

## Estructura del proyecto

```text
mystale-catalog/
├── config/          # Configuración Django (settings, urls)
├── catalog/         # App principal
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

## Categorías elementales

fuego · agua · tierra · rayo · sombra · cristal · viento · hielo

---
