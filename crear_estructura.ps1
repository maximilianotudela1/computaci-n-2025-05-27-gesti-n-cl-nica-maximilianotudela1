# Crear carpetas
mkdir modelos -ErrorAction SilentlyContinue
mkdir excepciones -ErrorAction SilentlyContinue
mkdir cli -ErrorAction SilentlyContinue
mkdir tests -ErrorAction SilentlyContinue

# Crear archivos en modelos
New-Item -Path "modelos\__init__.py" -ItemType File -Force
New-Item -Path "modelos\paciente.py" -ItemType File -Force
New-Item -Path "modelos\medico.py" -ItemType File -Force
New-Item -Path "modelos\especialidad.py" -ItemType File -Force
New-Item -Path "modelos\turno.py" -ItemType File -Force
New-Item -Path "modelos\receta.py" -ItemType File -Force
New-Item -Path "modelos\historia_clinica.py" -ItemType File -Force
New-Item -Path "modelos\clinica.py" -ItemType File -Force

# Crear archivos en excepciones
New-Item -Path "excepciones\__init__.py" -ItemType File -Force
New-Item -Path "excepciones\excepciones_clinica.py" -ItemType File -Force

# Crear archivos en cli
New-Item -Path "cli\__init__.py" -ItemType File -Force
New-Item -Path "cli\interfaz_consola.py" -ItemType File -Force

# Crear archivos en tests
New-Item -Path "tests\__init__.py" -ItemType File -Force
New-Item -Path "tests\test_paciente.py" -ItemType File -Force
New-Item -Path "tests\test_medico.py" -ItemType File -Force
New-Item -Path "tests\test_especialidad.py" -ItemType File -Force
New-Item -Path "tests\test_turno.py" -ItemType File -Force
New-Item -Path "tests\test_receta.py" -ItemType File -Force
New-Item -Path "tests\test_historia_clinica.py" -ItemType File -Force
New-Item -Path "tests\test_clinica.py" -ItemType File -Force

# Crear archivos en la raíz
New-Item -Path "main.py" -ItemType File -Force
New-Item -Path "README.md" -ItemType File -Force

Write-Host "Estructura del proyecto creada exitosamente" -ForegroundColor Green