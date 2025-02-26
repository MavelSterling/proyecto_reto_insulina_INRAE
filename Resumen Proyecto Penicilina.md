## **IndPenSim: Un Modelo de Simulación Industrial para la Fermentación de Penicilina y su Potencial en Inteligencia Artificial**

El modelo **IndPenSim** es una simulación de fermentación industrial de **Penicillium chrysogenum**, desarrollada en MATLAB, que permite investigar el **crecimiento celular, producción de penicilina y estrategias de control avanzado**. Su desarrollo ha permitido evaluar **tecnologías analíticas de procesos (PAT)** y algoritmos de detección de fallos mediante datos obtenidos de biorreactores de **100,000 litros**.

Para iniciar una investigación seria sobre **cómo aplicar redes neuronales recurrentes (RNNs) en este tipo de fermentaciones**, es fundamental entender **el diseño del sistema, los métodos de control existentes y los datos que se pueden extraer**. A continuación, se detallan los aspectos más relevantes de IndPenSim y cómo puede aprovecharse para avanzar en investigaciones en inteligencia artificial aplicada a bioprocesos.

---

# **1. IndPenSim: Un modelo de fermentación industrial basado en principios matemáticos**

## **1.1 Propósito del modelo**

IndPenSim fue desarrollado para:

1. **Simular la producción industrial de penicilina** en condiciones realistas, utilizando datos de un biorreactor de **100,000 L**.
2. **Evaluar estrategias de control de procesos avanzadas**, incluyendo el uso de sensores espectroscópicos (*Raman spectroscopy*).
3. **Optimizar la detección de fallos** a lo largo de un año de producción utilizando métodos de análisis de datos e inteligencia artificial.
4. **Servir como plataforma de investigación** para desarrollar e implementar **técnicas de aprendizaje automático** para mejorar el control de fermentaciones.

---

## **1.2 Estructura del modelo**

IndPenSim **integra diferentes modelos matemáticos** para representar la fermentación de penicilina:

- **Modelo de Crecimiento Celular**: Considera el crecimiento, metabolismo y degeneración de la biomasa en el biorreactor.
- **Modelo de Producción de Penicilina**: Relaciona la conversión de sustrato en penicilina bajo condiciones de oxígeno limitado.
- **Modelo de Control de Procesos**: Usa **controladores PID** y tecnologías PAT para ajustar parámetros clave como pH, temperatura y oxígeno disuelto.
- **Modelo de Espectroscopía Raman**: Simula un sensor de espectroscopía Raman que mide en tiempo real la biomasa, el sustrato y la concentración de penicilina.

Cada uno de estos modelos permite simular **diferentes estrategias de control y monitoreo**, lo que hace que IndPenSim sea ideal para aplicar **inteligencia artificial y redes neuronales** en bioprocesos.

---

## **1.3 Fases del proceso de fermentación en IndPenSim**

La simulación sigue un esquema **fed-batch**, donde se controla la adición de sustrato para **maximizar la producción**:

### **1. Inicio del proceso**

- Se inocula el biorreactor con *Penicillium chrysogenum*.
- Se introducen **sustrato, ácido fenilacético (PAA) y fuentes de nitrógeno**.

### **2. Fase de crecimiento exponencial**

- Se optimiza la alimentación de **glucosa y aceite de soja** para maximizar el crecimiento celular.
- Se monitorean variables como **oxígeno disuelto (DO2), temperatura y pH**.

### **3. Fase de producción de penicilina**

- Se reducen los niveles de **sustrato** para inducir la producción de penicilina.
- Se ajusta la alimentación de **PAA**, ya que es el precursor de la penicilina.

### **4. Fase de mantenimiento y cosecha**

- Se mantienen las condiciones para evitar **la degradación del producto**.
- La penicilina se cosecha y el biorreactor se limpia para el siguiente ciclo.

---

# **2. Aplicación de Inteligencia Artificial en IndPenSim**

El modelo **IndPenSim genera una gran cantidad de datos**, lo que permite el uso de técnicas de **aprendizaje automático y redes neuronales** para mejorar la **predicción, detección de fallos y optimización de procesos**.

---

## **2.1 Implementación de redes neuronales recurrentes (RNNs)** en la fermentación industrial

Las **redes neuronales recurrentes (RNNs)** pueden ser usadas en IndPenSim para **mejorar el control y la optimización del proceso de fermentación**. Las áreas clave donde pueden aplicarse incluyen:

### **2.1.1 Predicción en tiempo real de variables críticas**

Las RNNs pueden ser entrenadas con datos históricos de fermentaciones para **predecir valores futuros de variables clave**, como:

- **Concentración de penicilina** en el medio de cultivo.
- **Oxígeno disuelto (DO2)** y su impacto en el metabolismo celular.
- **Crecimiento de biomasa** basado en espectros Raman.

📌 **Caso de uso**: Implementar una **Long Short-Term Memory (LSTM)** para predecir **concentraciones de penicilina** basándose en datos de **temperatura, pH y oxígeno disuelto**.

---

### **2.1.2 Detección temprana de fallos en la fermentación**

Las RNNs pueden identificar patrones anómalos en:

- **Fluctuaciones en la alimentación de sustrato**.
- **Desviaciones en sensores de pH y temperatura**.
- **Datos espectroscópicos Raman inusuales**.

📌 **Caso de uso**: Usar una **Gated Recurrent Unit (GRU)** para predecir fallos en el **sistema de aireación**, permitiendo **acciones correctivas antes de que se vea afectada la producción**.

---

### **2.1.3 Control adaptativo del proceso**

Las RNNs pueden ser usadas en **aprendizaje por refuerzo** para **ajustar automáticamente los parámetros de control**, como:

- **Tasa de alimentación de sustrato** para maximizar la producción.
- **Regulación del pH** basada en la predicción de fluctuaciones futuras.
- **Optimización del tiempo de cosecha** en función del rendimiento del lote.

📌 **Caso de uso**: Un sistema basado en RNN podría aprender a **ajustar dinámicamente la alimentación de ácido fenilacético (PAA)** en función de la producción de penicilina.

---

## **2.2 Comparación entre control tradicional y control basado en RNN**

| **Característica**          | **Control tradicional (PID)** | **Control basado en RNN**   |
| ---------------------------------- | ----------------------------------- | --------------------------------- |
| **Adaptabilidad**            | Baja (requiere ajuste manual)       | Alta (se ajusta dinámicamente)   |
| **Manejo de ruido**          | Sensible a mediciones inexactas     | Puede aprender a filtrar ruido    |
| **Capacidad de predicción** | No predictivo                       | Predice valores futuros           |
| **Eficiencia energética**   | No optimizada                       | Puede reducir consumo energético |

Esto muestra que las **redes neuronales recurrentes (RNNs) pueden mejorar significativamente la eficiencia del proceso**, permitiendo que **IndPenSim evolucione hacia un sistema autónomo de fermentación**.

---

# **3. Conclusión y futuro de la investigación**

IndPenSim es una plataforma de simulación **altamente avanzada**, ideal para probar **estrategias de control inteligente** en fermentaciones industriales. El uso de **redes neuronales recurrentes (RNNs)** puede mejorar la **predicción, detección de fallos y optimización de procesos**, permitiendo:

- **Mayor estabilidad en la producción** de penicilina.
- **Menos consumo energético y de materias primas**.
- **Automatización inteligente del control del proceso**.

🔬 **Línea de investigación recomendada**: Implementar una arquitectura híbrida combinando **modelos físicos de IndPenSim con redes neuronales recurrentes**, creando un **gemelo digital inteligente** para la fermentación industrial.

🚀 **Impacto esperado**: Desarrollo de **biorreactores autónomos** con **control basado en IA**, optimizando la **industria farmacéutica y biotecnológica**.


---


# **📌 Fases del Proyecto: "Uso de RNN y Sensores Blandos en la Producción de Penicilina"**

**Institución:** Instituto Nacional de Investigación sobre Agricultura, Alimentación y Medio Ambiente de Francia ( *INRAE* )

**Duración:** Marzo - Junio

| **Fase**                                                                | **Duración**                    | **Actividades principales**                                                                                                                                                                                                                                                                                                          | **Resultados esperados**                                                                                                                                                    |
| ----------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fase 1: Planificación y revisión bibliográfica**                   | **Semana 1 - 3 (Marzo)**         | - Definir objetivos específicos y alcances.<br />  - Revisión de literatura sobre sensores blandos en fermentaciones industriales.<br />  - Estudio del simulador**IndPenSim**y recopilación de datos.<br />  - Identificación de variables clave para el modelado con **RNN** .                                           | ✅ Informe de estado del arte. <br /> ✅ Conjunto de datos inicial (Industrial Penicillin Simulation). <br /> ✅ Definición de variables y arquitectura preliminar de la RNN.    |
| **Fase 2: Preparación de datos y preprocesamiento**                    | **Semana 4 - 6 (Marzo - Abril)** | - Limpieza y análisis exploratorio de datos. <br /> - Ingeniería de características (selección y normalización de variables). <br /> - Generación de datos sintéticos para entrenamiento si es necesario. <br /> - Separación de datos en entrenamiento, validación y prueba.                                                     | ✅ DataFrame con datos procesados. <br /> ✅ Estrategia definida para datos faltantes y escalamiento. <br /> ✅ Dataset final para entrenar el modelo de RNN.                     |
| **Fase 3: Desarrollo del modelo de Redes Neuronales Recurrentes (RNN)** | **Semana 7 - 10 (Abril - Mayo)** | - Implementación de RNN y**LSTM (Long Short-Term Memory)**para predicción del proceso. <br /> - Ajuste de hiperparámetros (capa de neuronas, tasa de aprendizaje, regularización).<br />  - Comparación con otros modelos (*ARIMA, Random Forest* ). <br /> - Validación cruzada y métricas de desempeño ( *RMSE, MAE, R²* ). | ✅ Modelo de RNN funcional con datos simulados. <br /> ✅ Reporte de comparaciones con modelos tradicionales. <br /> ✅ Selección del mejor modelo basado en métricas de error. |
| **Fase 4: Evaluación del modelo en el contexto industrial**            | **Semana 11 - 13 (Mayo)**        | - Pruebas de predicción en escenarios de fermentación simulados. <br /> - Ajustes y optimización del modelo en tiempo real. <br /> - Evaluación del impacto en la reducción de variabilidad y detección de anomalías.                                                                                                               | ✅ Modelo optimizado listo para pruebas finales.<br />  ✅ Análisis del impacto del modelo en la optimización del proceso de fermentación.                                     |
| **Fase 5: Documentación y presentación de resultados**                | **Semana 14 - 16 (Junio)**       | - Elaboración del informe final del proyecto.  <br />- Creación de una presentación con hallazgos clave.<br />  - Entrega de código y dataset procesado para futuras investigaciones.<br />  - Presentación del trabajo al INRAE.                                                                                                     | ✅ Informe final con metodología, resultados y conclusiones. <br /> ✅ Código documentado para futuras aplicaciones. <br /> ✅ Presentación y defensa del proyecto.            |

---

## **🔍 Explicación Detallada de Cada Fase**

### **Fase 1: Planificación y Revisión Bibliográfica (Marzo)**

🔹 **Objetivo:** Definir el alcance del proyecto y recopilar información sobre sensores blandos y redes neuronales recurrentes.

🔹 **Actividades:**

* Investigar  **sensores blandos en la industria biofarmacéutica** .
* Analizar los datos disponibles en  **Industrial Penicillin Simulation (IndPenSim)** .
* Definir las **variables de entrada y salida** del modelo (pH, oxígeno disuelto, flujo de aire, temperatura, biomasa, producción de penicilina).
* Revisar artículos científicos y estudios previos sobre **modelado de fermentaciones** con redes neuronales.

### **Fase 2: Preparación de Datos y Preprocesamiento (Marzo - Abril)**

🔹 **Objetivo:** Limpiar y procesar los datos de fermentación antes de entrenar el modelo.

🔹 **Actividades:**

* Cargar los datos de **IndPenSim** y verificar calidad.
* Manejar datos faltantes usando  **imputación estadística o interpolación** .
* Normalizar y escalar los datos para mejorar el desempeño del modelo.
* Dividir el dataset en  **entrenamiento (70%), validación (15%) y prueba (15%)** .

### **Fase 3: Desarrollo del Modelo de RNN (Abril - Mayo)**

🔹 **Objetivo:** Implementar y entrenar una RNN para predecir el comportamiento del proceso de fermentación.

🔹 **Actividades:**

* Construcción de la red neuronal recurrente (**RNN con LSTM** en  **TensorFlow/PyTorch** ).
* Comparación con otros modelos ( **ARIMA, Random Forest, XGBoost** ).
* Ajuste de hiperparámetros mediante  **optimización bayesiana** .
* Evaluación del desempeño con métricas como  **RMSE, MAE y R²** .

### **Fase 4: Evaluación del Modelo en el Contexto Industrial (Mayo)**

🔹 **Objetivo:** Validar la RNN en escenarios de fermentación simulados y evaluar su utilidad en la optimización del proceso.

🔹 **Actividades:**

* Aplicar la RNN a  **lotes de fermentación simulados en IndPenSim** .
* Evaluar su capacidad para detectar  **anomalías y optimizar parámetros del proceso** .
* Comparar la precisión de predicciones con métodos tradicionales.
* Ajustar el modelo para mejorar estabilidad y precisión en predicciones.

### **Fase 5: Documentación y Presentación de Resultados (Junio)**

🔹 **Objetivo:** Comunicar los hallazgos y asegurar que los resultados sean replicables en futuros estudios.

🔹 **Actividades:**

* Elaborar un **informe final** con metodología, resultados y discusión.
* Preparar una **presentación** para el INRAE con gráficos y análisis de desempeño del modelo.
* Entregar el **código y dataset procesado** para futuras investigaciones.

---

## **📊 Herramientas y Tecnologías**

🔹 **Software y Librerías:**

* **Python** con **TensorFlow/PyTorch** (para el modelo de RNN).
* **Pandas y NumPy** (para manipulación de datos).
* **Matplotlib y Seaborn** (para visualización de datos).
* **Scikit-learn** (para comparar con otros modelos).

🔹 **Fuentes de Datos:**

* **Industrial Penicillin Simulation (IndPenSim)**
* **Datos sintéticos generados para pruebas**

🔹 **Infraestructura:**

* **Google Colab / Jupyter Notebook** para desarrollo y pruebas.
* **GitHub o Google Drive** para almacenamiento y versionado de código.

---

## **📅 Cronograma General del Proyecto**

📍 **Marzo:** Revisión bibliográfica y recopilación de datos.

📍 **Abril:** Procesamiento de datos y desarrollo de RNN.

📍 **Mayo:** Evaluación y optimización del modelo.

📍 **Junio:** Documentación y presentación final.

🚀 **Entrega Final:** Junio

---

## **🔚 Conclusión**

Este plan permite desarrollar un **modelo basado en redes neuronales recurrentes (RNN) para optimizar la producción de penicilina** mediante sensores blandos. Se combina investigación teórica, desarrollo de modelos y validación en un entorno simulado, garantizando un enfoque sólido para la aplicación industrial.
