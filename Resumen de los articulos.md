Aquí tienes un resumen más detallado con un enfoque en las variables utilizadas y las técnicas aplicadas en cada estudio.

---

## **1. Desafíos Modernos en el Monitoreo y Control de un Proceso de Fermentación a Escala Industrial**

**Autores:** Stephen Goldrick, Carlos A. Duran-Villalobos, Karolis Jankauskas, David Lovett, Suzanne S. Farid, Barry Lennox

**Publicación:** *Computers and Chemical Engineering (2019)*

### **Objetivo del estudio:**

Evaluar y mejorar estrategias de monitoreo y control en procesos de fermentación a escala industrial mediante la simulación  **IndPenSim** , la cual incorpora herramientas avanzadas de análisis de procesos y detección de fallos.

### **Variables estudiadas:**

* **Variables de control:**
  * Temperatura ( *T* ), controlada mediante un algoritmo PID.
  * pH, también regulado con PID.
  * Flujo de sustrato ( *F_s* ), controlado manualmente o por receta.
  * Flujo de ácido fenilacético ( *F_PAA* ), controlado manualmente.
* **Variables de monitoreo:**
  * Concentración de oxígeno disuelto ( *DO₂* ).
  * Concentración de penicilina ( *P* ).
  * Biomasa ( *X* ).
  * Concentración de ácido fenilacético ( *PAA* ).
  * Concentración de nitrógeno ( *N* ).
  * Viscosidad ( *μ* ).
  * Medición de gases ( *CO₂* , *O₂* en off-gas).
  * Mediciones de espectroscopia Raman.

### **Técnicas utilizadas:**

* **Simulación de procesos:**
  * Desarrollo y uso de  **IndPenSim** , basado en un modelo matemático detallado de fermentación de penicilina.
  * Capacidad de operar en modo fijo o controlado por operador.
  * Incorporación de espectroscopia Raman simulada para mejorar la predicción en línea de parámetros clave.
* **Control avanzado:**
  * Implementación de *Quality by Design (QbD)* y *Process Analytical Technology (PAT)* para mejorar la calidad del producto final.
  * Evaluación de estrategias de control para minimizar la variabilidad del proceso.
* **Detección de fallos:**
  * Uso de algoritmos para detectar anomalías en el proceso mediante datos de múltiples lotes de producción.
  * Aplicación de técnicas de *big data* y *machine learning* para análisis predictivo.

### **Resultados clave:**

* **IndPenSim** permitió evaluar estrategias de control y mejorar el rendimiento del proceso de fermentación.
* Se identificaron variables críticas ( *pH* ,  *T* ,  *DO₂* ) que afectan directamente la producción de penicilina.
* Se propuso un modelo de control basado en la optimización de parámetros como el tiempo de cosecha, maximizando la producción anual.
* Se demostró que la espectroscopia Raman integrada a la simulación puede mejorar la predicción en tiempo real de compuestos clave en el proceso.

### **Conclusión:**

Este estudio destaca la importancia de incorporar tecnologías avanzadas en el monitoreo y control de fermentaciones industriales, optimizando tanto la producción como la estabilidad del proceso.

---

## **2. Desarrollo de una Simulación de Fermentación Fed-Batch a Escala Industrial**

**Autores:** Stephen Goldrick, Andrei Ștefan, David Lovett, Gary Montague, Barry Lennox

**Publicación:** *Journal of Biotechnology (2014)*

### **Objetivo del estudio:**

Desarrollar un modelo estructurado para simular un proceso de fermentación *fed-batch* de penicilina a escala industrial, considerando variables críticas y restricciones operacionales reales.

### **Variables estudiadas:**

* **Variables de crecimiento y producción:**
  * Biomasa total ( *X* ), subdividida en:
    * Biomasa en crecimiento ( *A₀* ).
    * Biomasa no creciente ( *A₁* ).
    * Biomasa degenerada ( *A₃* ).
    * Biomasa autolizada ( *A₄* ).
  * Concentración de penicilina ( *P* ).
  * Sustrato consumido ( *S* ).
* **Variables ambientales:**
  * Temperatura del caldo ( *T_b* ).
  * pH.
  * Oxígeno disuelto ( *DO₂* ).
  * Dióxido de carbono disuelto ( *CO₂* ).
* **Variables de control y alimentación:**
  * Flujo de azúcar ( *F_s* ).
  * Flujo de ácido fenilacético ( *F_PAA* ).
  * Flujo de aceite de soja ( *F_oil* ).
  * Tasa de aireación ( *F_g* ).
  * Potencia del agitador ( *P_ag* ).

### **Técnicas utilizadas:**

* **Modelado matemático:**
  * Se utilizó un modelo estructurado basado en ecuaciones diferenciales para describir el crecimiento de *Penicillium chrysogenum* y la producción de penicilina.
  * Se incluyeron efectos de transferencia de masa y consumo de oxígeno.
  * Se modelaron reacciones de hidrólisis que afectan la estabilidad de la penicilina.
* **Validación con datos industriales:**
  * Se compararon las predicciones del modelo con registros de 10 fermentaciones de 100,000 litros.
  * Se evaluaron variaciones de crecimiento y producción entre lotes.
* **Optimización del proceso:**
  * Se analizaron estrategias para mantener la concentración de oxígeno y mejorar la transferencia de masa.
  * Se evaluó el impacto de fluctuaciones en nutrientes como nitrógeno y fenilacético en la producción de penicilina.

### **Resultados clave:**

* El modelo logró predecir con precisión la variabilidad del proceso, incluyendo retrasos en la medición de parámetros clave.
* Se identificó que la viscosidad del caldo afecta la transferencia de oxígeno y, por lo tanto, la producción de penicilina.
* Se propuso un enfoque para optimizar estrategias de alimentación, asegurando un suministro adecuado de nutrientes y evitando inhibición por acumulación de productos metabólicos.

### **Conclusión:**

El simulador desarrollado permite analizar y mejorar estrategias de control en fermentaciones industriales, proporcionando una herramienta útil para optimizar la producción de penicilina y reducir variabilidad en la calidad del producto final.

---


## **3. Multivariate Statistical Process Control of an Industrial-Scale Fed-Batch Simulator**

**Autores:** Carlos A. Duran-Villalobos, Stephen Goldrick, Barry Lennox

**Publicación:** *Computers and Chemical Engineering 132 (2019) 106620*

---

### **Objetivo del estudio**

Este artículo presenta una estrategia de control estadístico multivariado de procesos (*Multivariate Statistical Process Control* - MSPC) aplicada a un simulador industrial de fermentación  *fed-batch* . Se desarrollaron métodos de control predictivo y optimización de lotes para mejorar la calidad del producto final y reducir la variabilidad entre lotes.

---

### **Variables estudiadas**

* **Variables de entrada (control y alimentación):**
  * Tasa de alimentación de glucosa ( *F_glucosa* ).
  * Concentración de oxígeno disuelto ( *DO₂* ).
  * Flujo de aire ( *F_aire* ).
  * pH del medio de cultivo.
  * Temperatura del reactor.
  * Concentración de fenilacético ( *PAA* ).
* **Variables de monitoreo y salida:**
  * Concentración de penicilina ( *P* ).
  * Crecimiento de biomasa ( *X* ).
  * Producción de CO₂ en el gas de salida ( *CO₂_off-gas* ).
  * Transferencia de oxígeno ( *k_La* ).
  * Volumen del medio de fermentación.

---

### **Técnicas utilizadas**

#### **1. Optimización de lotes mediante Batch-to-Batch (B2B)**

* Ajusta los parámetros de control en cada lote con base en el rendimiento previo.
* Minimiza la variabilidad causada por fluctuaciones en las materias primas y perturbaciones en el proceso.
* Implementa un modelo adaptativo basado en **Partial Least Squares (PLS)** para predecir el comportamiento del sistema.
* Se utiliza **Bootstrap Resampling** para calcular intervalos de confianza sin asumir distribución normal.

#### **2. Control Predictivo Basado en Modelo (MPC)**

* Ajusta la alimentación de glucosa durante el lote para mantener la producción en su punto óptimo.
* Se basa en el control  **Model Predictive Control (MPC)** , optimizando el proceso en tiempo real.
* Utiliza **Quadratic Programming (QP)** para minimizar la diferencia entre el rendimiento real y el esperado.
* Aplica restricciones de validez basadas en las estadísticas **T² de Hotelling** y **Q-statistic** para garantizar que las decisiones de control sean confiables.

#### **3. Métodos de estimación de datos faltantes**

* **Projection to the Model Plane (PMP):** proyecta las mediciones disponibles en el espacio latente del modelo.
* **Trimmed Score Regression (TSR):** usa regresión para reconstruir valores faltantes de manera más robusta.

---

### **Resultados clave**

* La optimización **B2B** redujo la variabilidad en la producción de penicilina, logrando una convergencia en 10 lotes.
* El control predictivo **MPC** redujo la variabilidad dentro del lote y mantuvo la concentración de penicilina cerca de los 30 g/L.
* La combinación de **B2B + MPC** mejoró la estabilidad del proceso, reduciendo la dispersión del rendimiento final.
* Se demostró que las restricciones de validez con *bootstrap resampling* fueron más efectivas que los enfoques basados en distribución normal.

---

### **Conclusión**

El estudio muestra que la combinación de **optimización B2B y control MPC** es altamente efectiva para reducir la variabilidad en fermentaciones industriales. El uso de **PLS adaptativo, restricciones de validez y estimación de datos faltantes** permitió mejorar la estabilidad del proceso. Estos resultados sugieren que la implementación de estas estrategias en la industria biofarmacéutica podría mejorar significativamente la producción y calidad de productos fermentativos.

---

## **Comparación de los Artículos sobre Fermentación a Escala Industrial**

| **Criterio**                                   | **Artículo 1**(Modern Monitoring and Control Challenges)                                                                                                                                                                                                                            | **Artículo 2**(Development of an Industrial-Scale Fed-Batch Fermentation)                                                                                                                                                                                                                                                           | **Artículo 3**(Multivariate Statistical Process Control)                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Objetivo**                                   | Mejorar el monitoreo y control en fermentaciones industriales usando**IndPenSim** .                                                                                                                                                                                                  | Modelar y simular una fermentación*fed-batch*de penicilina para optimizar el proceso.                                                                                                                                                                                                                                                   | Aplicar**control estadístico multivariado de procesos (MSPC)**y**control predictivo basado en modelo (MPC)**en un proceso industrial de fermentación *fed-batch* .                                                                                                                                                                                                                                                                                                 |
| **Variables utilizadas**                       | - pH, temperatura, DO₂, CO₂, fenilacético, biomasa, viscosidad, espectroscopia Raman.                                                                                                                                                                                                   | - Biomasa (*X* ), penicilina ( *P* ), sustratos ( *S* ), oxígeno disuelto, pH, temperatura, flujo de aire, tasa de crecimiento microbiano.                                                                                                                                                                                          | - Concentración de penicilina, biomasa, DO₂, CO₂, volumen, temperatura, tasa de alimentación de glucosa, flujo de aire, pH.                                                                                                                                                                                                                                                                                                                                              |
| **Cantidad de datos y fuente**                 | -**100 lotes de fermentación**generados con el simulador **IndPenSim** . - Datos simulados basados en un proceso real de producción de penicilina. - No se usaron datos de fermentaciones industriales reales, pero el modelo está calibrado con procesos industriales.     | -**10 lotes industriales de fermentación**de **100,000 L cada uno** , provenientes de una planta biofarmacéutica real. - Se compararon los resultados con un simulador basado en ecuaciones mecanísticas. - Los datos fueron recopilados de registros históricos de producción de penicilina en la industria.             | -**80 lotes de fermentación**del simulador **IndPenSim** . - Mediciones tomadas cada 10 horas dentro de cada lote para el control predictivo ( **MPC** ). - Datos utilizados en la optimización Batch-to-Batch ( **B2B** ) provienen de iteraciones dentro de la simulación.                                                                                                                                                                      |
| **Técnicas estadísticas / Machine Learning** | -**Simulación de procesos**con **IndPenSim** .  -**Process Analytical Technology (PAT)**y **Quality by Design (QbD)** . - Algoritmos de detección de fallos usando *big data* .                                                                                      | -**Modelado mecanístico**basado en ecuaciones diferenciales. - **Ajuste de modelos mediante validación con datos industriales** . - **Ecuaciones de balance de masa y energía** .                                                                                                                                     | -**Partial Least Squares (PLS)**y**Multi-way PLS (MPLS)** . -**Bootstrap Resampling**para intervalos de confianza. -**Quadratic Programming (QP)**para optimización. -**Model Predictive Control (MPC)**para ajustar parámetros en tiempo real. -**Batch-to-Batch Optimization (B2B)**para mejorar el rendimiento de un lote al siguiente. -**Multivariate Statistical Process Control (MSPC)**usando**T² de Hotelling**y **Q-statistic** . |
| **Resultados**                                 | -**Mejor control de la fermentación**con algoritmos avanzados. -**Reducción de la variabilidad**en la producción de penicilina. -**Espectroscopia Raman**mejoró la predicción en línea de compuestos clave.                                                        | -**Simulación precisa de fermentaciones industriales** . -**Mejor entendimiento del proceso**mediante modelado mecanístico. -**Control de oxígeno y nutrientes clave**mejoró la estabilidad del proceso.                                                                                                             | -**B2B redujo la variabilidad entre lotes**y optimizó la producción en 10 lotes. -**MPC redujo la variabilidad dentro del lote**y mantuvo la concentración en **30 g/L** . - **Uso de PLS y restricciones de validez mejoró la robustez del modelo** . - **Bootstrap Resampling superó métodos basados en distribución normal** .                                                                                                       |
| **Conclusión**                                | - Integrar**PAT y QbD**en fermentaciones mejora la estabilidad del proceso. -**IndPenSim**es una herramienta útil para optimizar estrategias de control. - Tecnologías de monitoreo avanzado como**espectroscopia Raman**pueden mejorar la predicción en tiempo real. | -**El modelado mecanístico es esencial**para optimizar fermentaciones industriales. - La simulación proporciona una herramienta poderosa para **probar estrategias de control antes de aplicarlas en la industria** . -**Factores críticos**como oxígeno disuelto y viscosidad afectan la producción de penicilina. | -**Combinar B2B y MPC mejora la eficiencia del proceso** . - **PLS y Bootstrap Resampling mejoran la confiabilidad de los modelos predictivos** . -**Control predictivo reduce la variabilidad en la producción**de penicilina en **fermentaciones industriales** .                                                                                                                                                                                 |

---

### **Explicación de las Fuentes de Datos**

1. **Artículo 1:** Los datos provienen  **de simulaciones realizadas con IndPenSim** , una herramienta que imita un proceso de fermentación industrial de penicilina.
2. **Artículo 2:** Se usaron **datos reales de 10 lotes industriales** de fermentación de  **100,000 litros cada uno** , provenientes de registros históricos de producción en una planta industrial de biofarmacéuticos.
3. **Artículo 3:** Se trabajó con  **datos simulados de 80 lotes en IndPenSim** , con mediciones dentro de cada lote para el control predictivo.

---

### **Conclusión General**

Los tres estudios tienen objetivos diferentes pero complementarios:

* **Artículo 1:** Se enfoca en **el monitoreo avanzado** y en mejorar la predicción mediante técnicas como espectroscopia Raman.
* **Artículo 2:** Se basa en **datos reales de producción** y usa modelos mecanísticos para optimizar la fermentación industrial.
* **Artículo 3:** Usa **control estadístico y técnicas de machine learning** para reducir la variabilidad y optimizar la producción de penicilina.
