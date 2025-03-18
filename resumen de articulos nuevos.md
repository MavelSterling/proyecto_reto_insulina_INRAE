### **Análisis de la Metodología, Variables y Modelos Utilizados en los Artículos**

Se han analizado tres artículos relacionados con la optimización y control de fermentaciones por lotes y alimentación por lotes. A continuación, se presenta el análisis de la metodología utilizada en cada uno, las variables involucradas y los modelos empleados.

---

## **1. Optimization and Control of Fed-Batch Fermentation Processes**

### **Metodología**

* Se enfoca en la optimización y control de procesos de fermentación por lotes alimentados (fed-batch).
* Analiza estrategias de control como la alimentación exponencial, el control basado en modelos y el uso de algoritmos avanzados.
* Se incluyen modelos matemáticos para representar la cinética de crecimiento de microorganismos en el proceso de fermentación.

### **Variables Involucradas**

* **Concentración de sustrato** (ejemplo: glucosa).
* **Concentración de biomasa** .
* **Producción de metabolitos** (ejemplo: etanol).
* **Tasa de crecimiento específica** .
* **Tasa de consumo de oxígeno y producción de CO₂** .
* **Estrategias de alimentación** (flujo de nutrientes).

### **Modelo Utilizado**

* **Modelos cinéticos** basados en ecuaciones diferenciales que describen el crecimiento celular y la conversión de sustrato en productos.
* **Algoritmos de optimización** para maximizar la eficiencia del proceso.
* **Técnicas de control predictivo** para ajustar la alimentación del sustrato.

---

## **2. A Hybrid Neural Network Approach for Batch Fermentation Simulation**

### **Metodología**

* Desarrolla un **modelo híbrido de red neuronal** combinado con ecuaciones diferenciales para simular la fermentación por lotes.
* Se emplearon datos experimentales para entrenar y validar la red neuronal.
* Se utilizó un **perceptrón multicapa (MLP)** con una capa oculta.
* Se aplicó el **algoritmo de Levenberg-Marquardt** para la optimización de pesos y sesgos de la red neuronal.

### **Variables Involucradas**

* **pH** .
* **Biomasa** (densidad celular).
* **Sustrato consumido** (glucosa).
* **Ethanol producido** .
* **Tiempo de fermentación** .

### **Modelo Utilizado**

* **Red Neuronal Artificial (ANN)** : Se usó un **MLP con una capa oculta** y una función de activación sigmoide en la capa oculta y lineal en la capa de salida.
* **Modelo híbrido ANN + ecuaciones diferenciales** : Se combinaron redes neuronales con ecuaciones diferenciales que modelan la cinética de fermentación.
* **Interpolación spline** : Se usó para construir perfiles de los datos experimentales.

---

## **3. Control of Fed-Batch Fermentations**

### **Metodología**

* Revisión de métodos de control para fermentaciones por lotes alimentados.
* Se examinan enfoques tradicionales y avanzados, como:
  * **Alimentación exponencial** .
  * **Control difuso (fuzzy control)** .
  * **Redes neuronales** .
  * **Técnicas inferenciales** para estimar variables clave.

### **Variables Involucradas**

* **Tasa de crecimiento celular** .
* **Concentración de oxígeno disuelto (DO)** .
* **Dióxido de carbono emitido (CER)** .
* **Tasa de consumo de oxígeno (OUR)** .
* **Concentración de sustrato en el medio** .
* **Flujo de alimentación de nutrientes** .

### **Modelo Utilizado**

* **Estrategias de control predictivo** para optimizar la alimentación de nutrientes.
* **Modelos inferenciales** para estimar la concentración de sustrato y ajustar el flujo de alimentación.
* **Redes neuronales** utilizadas para modelar la tasa de crecimiento celular y mejorar la precisión del control del proceso.

---

### **Conclusión**

Los tres artículos abordan el control y optimización de fermentaciones desde diferentes enfoques:

1. **Optimización basada en modelos cinéticos y algoritmos de control** .
2. **Uso de redes neuronales híbridas para mejorar la simulación de la fermentación** .
3. **Aplicación de técnicas avanzadas de control, incluyendo control difuso y redes neuronales** .

Cada enfoque tiene ventajas según el tipo de proceso y la disponibilidad de datos experimentales.
