Algoritmo: Desarrollo de Soft Sensors para Producción de Penicilina

Entrada:

- Dataset IndPenSim con 100 lotes (cada lote con 113,935 instancias)
- Variables medidas en línea: Fs, Agitación, T, pH, DO, V, CO2,og, O2,og
- Variable a predecir: P (concentración de penicilina)
- Estrategias de control (por receta, por operadores, con APC, con fallas)

Salida:

- Modelos interpretables entrenados (CART, M5, CUBIST, RF) listos para predecir P

Pasos:

1. Preparación de Datos:
   a. Cargar el dataset IndPenSim.
   b. Seleccionar las variables relevantes: {Fs, Agitación, T, pH, DO, V, CO2,og, O2,og, P}.
   c. Segmentar los lotes según estrategia de control:
   	- Receta: Lotes 1–30
   	- Operadores: Lotes 31–60
   	- APC (Raman): Lotes 61–90
   	- Fallas: Lotes 91–100
   d. Dividir cada segmento en conjuntos:
   	- Entrenamiento: 80% de los lotes asignados a cada estrategia.
   	- Prueba: 20% restante.
2. Exploración de Datos:
   a. Para cada estrategia de control:
   	- Visualizar y analizar la distribución y rangos de las variables.
   b. Seleccionar el lote 2 como caso de estudio:
   	- Extraer 3 instancias en tiempos específicos (68.4 h, 120 h, 200 h).
   	- Registrar los valores de las variables y la concentración real de P.
   c. Evaluar la importancia de cada variable (por ejemplo, identificando que V, DO, O2,og y Fs son críticas).
3. Configuración y Ajuste de Modelos:
   Para cada modelo en {CART, M5, CUBIST, RF}:
   	a. Definir hiperparámetros iniciales:
   		- CART: profundidad máxima (por ejemplo, probar de 1 a 10 y elegir 7).
   		- M5: mínimo número de instancias por hoja (se probó entre 1000 y 15,000; se eligió 12,000).
   		- CUBIST: número de comités y vecinos (se optimizó para favorecer interpretabilidad, e.g., 1 comité y 3 vecinos).
   		- RF: número de árboles (se ajustó a 5 para mantener la interpretabilidad).
   	b. Realizar validación cruzada:
   		- Aplicar 10-fold cross-validation con 3 repeticiones.
   		- Ajustar hiperparámetros según las métricas (R², MSE, RMSE, MAE).
4. Entrenamiento y Evaluación:
   a. Entrenar cada modelo con el conjunto de entrenamiento.
   b. Evaluar el desempeño usando el conjunto de prueba, calculando:
   	- Coeficiente de determinación (R²)
   	- Error cuadrático medio (MSE)
   	- Raíz del error cuadrático medio (RMSE)
   	- Error absoluto medio (MAE)
   c. Documentar los resultados obtenidos para cada estrategia de control.
5. Comparación e Interpretación:
   a. Comparar las métricas de desempeño entre los modelos.
   b. Analizar la estructura de los modelos:
   	- Revisar reglas y ramas en CART y CUBIST.
   	- Evaluar las regresiones lineales en M5.
   	- Estudiar la consistencia de las reglas en RF.
   c. Identificar el balance entre precisión e interpretabilidad.
   	- Se observa que CUBIST y RF ofrecen mejores resultados, aunque CART y M5 son más simples.
6. Conclusión y Futuras Líneas de Trabajo:
   a. Seleccionar el modelo o modelos que mejor se adapten al monitoreo en tiempo real.
   b. Utilizar la interpretación de las reglas para identificar variables críticas y posibles fallas en el proceso.
   c. Proponer mejoras futuras, como la integración de técnicas post-hoc o modelos híbridos que combinen principios físicos con datos.

Fin del Algoritmo
