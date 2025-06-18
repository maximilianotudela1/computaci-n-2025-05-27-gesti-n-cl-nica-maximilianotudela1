#!/usr/bin/env python3
"""
Sistema de Gestión para Clínica Médica
Punto de entrada principal del programa
"""

import sys
import os

# Asegurar que el directorio actual esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli.interfaz_consola import CLI

def main():
    """Función principal que ejecuta el sistema"""
    print("=== Sistema de Gestión de Clínica Médica ===")
    print("Bienvenido al sistema de gestión")
    
    # Crear y ejecutar la interfaz de consola
    interfaz = CLI()
    interfaz.ejecutar()

if __name__ == "__main__":
    main()