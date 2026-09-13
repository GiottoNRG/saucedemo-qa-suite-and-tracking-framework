# SauceDemo QA Automation Suite & Quality Control Framework

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.10+-green.svg)
![PyTest](https://img.shields.io/badge/PyTest-7.4+-yellow.svg)

## 1. INFORMACIÓN GENERAL
- **Nombre del proyecto:** SauceDemo QA Automation Suite & Tracking Framework
- **Especialidad:** QA (Quality Assurance) / Automation Engineering
- **Fuente del proyecto:** Plataforma e-commerce de práctica libre (SauceDemo / Swag Labs)
- **Link a la fuente original:** [SauceDemo](https://www.saucedemo.com/)
- **Link al proyecto publicado:** [GitHub Repository URL](https://github.com/GiottoNRG/saucedemo-qa-suite-and-tracking-framework.git)

---

## 2. OBJETIVO
Este proyecto valida el flujo crítico de compra (autenticación, gestión de carrito y checkout) en una plataforma e-commerce mediante pruebas funcionales automatizadas con Python y Selenium. Implementa una matriz de trazabilidad y reporte de defectos accesible en formato hoja de cálculo, previniendo errores críticos en la pasarela de pago antes del despliegue a producción.

---

## 3. PLAN DE TRABAJO
1. **Exploración inicial:** Análisis de requisitos funcionales y mapeo de historias de usuario sobre la aplicación SauceDemo.
2. **Preparación:** Diseño de la matriz de casos de prueba (`docs/test_cases_matrix.csv`) y configuración del entorno de desarrollo en Python.
3. **Construcción:** Desarrollo de scripts de automatización con Selenium WebDriver y `pytest` para la ejecución del flujo de compra extremo a extremo (*End-to-End*).
4. **Evaluación:** Ejecución de suites de prueba, cálculo de porcentaje de cobertura de código/requisitos y documentación de defectos.
5. **Conclusiones y próximos pasos:** Elaboración del reporte de cierre de pruebas y estructuración de la plantilla de control comercializable (`templates/QA_Test_Case_and_Bug_Tracker_Template.xlsx`).

---

## 4. PREGUNTAS CLAVE
* ¿Qué impacto financiero tendría en el negocio si falla la validación de campos obligatorios en el formulario de pago durante eventos de alto tráfico?
* ¿Los clasificadores XPATH/CSS Selector utilizados en Selenium son lo suficientemente robustos contra cambios menores en el DOM?
* ¿La matriz de pruebas cubre escenarios de borde (*edge cases*) como intentos de inyección de scripts en los inputs de autenticación?

---

## 5. QUÉ SE HIZO Y CÓMO
* **Tipos de pruebas:** Pruebas funcionales, pruebas de humo (*Smoke Testing*), pruebas de regresión y validación de límites de entrada (*Boundary Value Analysis*).
* **Stack y Herramientas:** Python 3, Selenium WebDriver, PyTest, Pandas (para parsing de datos) y Microsoft Excel (para generación de matrices de prueba).
* **Criterios de Aceptación:** 100% de ejecución exitosa en casos de prueba de severidad Crítica/Alta y cero bloqueos activos en el flujo de checkout.

---

## 6. RESULTADOS
* **Métricas de cobertura:** 100% de cobertura alcanzada en la ruta crítica de compra (*Login -> Add to Cart -> Checkout -> Confirmation*).
* **Resultados de ejecución:** 5/5 casos de prueba ejecutados sin fallos (*Status: Passed*).
* **Tiempos de ejecución:** Suite automatizada completa ejecutada en menos de 15 segundos en modo headless.

---

## 7. CONCLUSIONES
* **Aprendizajes:** Integración eficiente de patrones de automatización (*Page Object Model*) y sincronización de resultados de ejecuciones automatizadas con matrices de reporte ejecutivas.
* **Mejoras futuras:** Integración de ejecuciones continuas mediante GitHub Actions (CI/CD) y reporte de resultados en HTML usando `pytest-html`.
* **Enfoque profesional:** Demuestra la capacidad de estructurar marcos de calidad rigurosos que conectan la ejecución técnica automatizada con reportes de alto nivel entendibles para el negocio.

---

## 8. INSTRUCCIONES DE EJECUCIÓN

```bash
# 1. Clonar el repositorio
git clone [https://github.com/tu-usuario/saucedemo-qa-suite-and-tracking-framework.git](https://github.com/tu-usuario/saucedemo-qa-suite-and-tracking-framework.git)
cd saucedemo-qa-suite-and-tracking-framework

# 2. Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate  # En Windows use: venv\Scripts\activate
pip install -r requirements.txt

# 3. Ejecutar la suite de pruebas
pytest -v tests/
