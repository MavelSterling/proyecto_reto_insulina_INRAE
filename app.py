import streamlit as st
import pandas as pd

st.set_page_config(page_title="Presentación Sensores Blandos", layout="wide")

st.markdown("<h1 style='text-align: center; color: #003366;'>Presentación Proyecto: Implementación de sensores blandos (soft-sensors) en la industria de producción de penicilina </h1>", unsafe_allow_html=True)

st.image("logo.png", width=150)

st.markdown("""
<style>
    .block-container {
        padding: 2rem 4rem 2rem;
    }
    h2 {
        text-align: center;
        color: #004488;
    }
    .stRadio > div {
        flex-direction: row !important;
        justify-content: center;
    }
    /* Estilos para las tablas */
    .stTable {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .stTable table {
        border-collapse: collapse;
        width: 100%;
    }
    .stTable th {
        background-color: #003366;
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: bold;
    }
    .stTable td {
        padding: 8px 12px;
        border-bottom: 1px solid #dee2e6;
    }
    .stTable tr:nth-child(even) {
        background-color: #f1f3f4;
    }
    .stTable tr:hover {
        background-color: #e3f2fd;
    }
    /* Estilos para títulos de sección */
    h4 {
        color: #004488;
        border-bottom: 2px solid #004488;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

seccion = st.radio(
    "Navegar por las secciones:",
    ["Título y Autores", "Motivación", "Objetivos", "Árbol del Problema","Marco Teórico",
        "Estado del Arte", "Metodología", "Resultados", "Hallazgos y Conclusiones", "Referencias", "Cronograma"],
    index=0,
    horizontal=True
)

if seccion == "Título y Autores":
    st.subheader("Autores:")
    st.markdown("**Felipe Guerra y Mavelyn Sterling**")
    st.markdown("Universidad Icesi – Maestría en Inteligencia Artificial Aplicada")
   
elif seccion == "Motivación":
    st.subheader("Motivación")
    st.markdown("""
- La producción industrial de penicilina es un proceso no lineal y altamente sensible a las condiciones operativas.
- Aún se usan controles manuales que dificultan una predicción precisa en tiempo real.
- Este proyecto propone sensores blandos basados en IA para optimizar el control del proceso.
    """)

elif seccion == "Objetivos":
    st.subheader("Objetivos")
    st.markdown("""
**General:** Desarrollar modelos predictivos tipo sensores blandos usando MLP para estimar la concentración de penicilina.

**Específicos:**
- Analizar un dataset simulado de fermentación industrial (IndPenSim)
- Aplicar técnicas de selección de variables (Lasso, PLS)
- Entrenar redes MLP por tipo de operación
- Evaluar su desempeño predictivo
    """)

elif seccion == "Árbol del Problema":
    st.subheader("Árbol de Problemas")

    st.markdown("<h4 style='text-align: center;'>PROBLEMA CENTRAL</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Falta de herramientas inteligentes para la predicción precisa de variables clave<br>en procesos biofarmacéuticos como la producción de penicilina</p>", unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown("### 🧩 Causas Principales")
        st.markdown("- Uso de estrategias de control tradicionales (recetas u operadores)\n- Ausencia de sensores blandos con modelos IA\n- Complejidad multivariable del proceso y falta de modelos predictivos adecuados")

    with col2:
        st.markdown("### ⚠️ Efectos Directos")
        st.markdown("- Predicciones inexactas de variables críticas\n- Dificultad en la detección temprana de fallos\n- Baja capacidad de respuesta del sistema de control")

    with col3:
        st.markdown("### 🚨 Consecuencias")
        st.markdown("- Pérdidas económicas por ineficiencia en producción\n- Variabilidad en la calidad del producto final\n- Limitada capacidad de optimización del proceso")

elif seccion == "Marco Teórico":
    st.subheader("Marco Teórico – Sensores Blandos e IA en Bioprocesos")
    st.markdown("""
1. **Fermentación industrial de penicilina**  
   Proceso biofarmacéutico complejo, altamente no lineal, multivariable y dependiente del tiempo, con alta variabilidad entre lotes.

2. **Sensores blandos (soft-sensors)**  
   - Modelos computacionales que permiten estimar variables no medibles directamente.  
   - Combinan mediciones en tiempo real con modelos de aprendizaje automático.  
   - Mejoran el control del proceso sin necesidad de sensores físicos adicionales.

3. **Redes neuronales MLP (Multilayer Perceptron)**  
   - Arquitectura seleccionada por su capacidad de modelar relaciones no lineales.  
   - Entrenadas con variables relevantes del proceso para predecir la concentración de penicilina (P: g/L).

4. **Técnicas de selección de variables**  
   - **Lasso**: penalización L1 para eliminar variables irrelevantes.  
   - **PLS**: captura relaciones latentes, útil en entornos operativos estables.

5. **Segmentación del sistema**  
   Agrupación por estrategia de control (Receta, Operador, APC Raman, Fallas) mejora la capacidad predictiva.

6. **Simulación con IndPenSim**  
   Gemelo digital de una planta de fermentación (100.000 L), incluye fallos simulados y control avanzado basado en espectroscopía Raman.
""")
elif seccion == "Estado del Arte":
    st.subheader("Estado del Arte – Puntos Clave")

    st.markdown("##### [1] Goldrick et al. (2019) – Sensores blandos con PLS y Raman")
    st.markdown("""
- Simulación industrial con espectroscopía Raman.  
- Aplicación de PLS para predecir concentración de penicilina (RMSE ≈ 0.10 g/L).  
- Detección de fallos con SPE-PCA (100 % éxito).  
- **Limitación**: no incluye algoritmos de IA avanzados ni técnicas automáticas de selección de variables.
""")

    st.markdown("##### [2] Goldrick et al. (2015) – Modelo mecanicista estructurado")
    st.markdown("""
- Modelo detallado de fermentación fed-batch con 10 lotes reales.  
- Incluye balances dinámicos, control PID y correlaciones para kLa.  
- Validación con R² > 0.90 para penicilina y DO.  
- **Limitación**: sin datos Raman, ni IA, ni fallos simulados.
""")

    st.markdown("##### [3] Acosta-Pavas et al. (2024) – Modelos interpretables (CART, RF, Cubist)")
    st.markdown("""
- Modelos predictivos sobre los 100 lotes de IndPenSim.  
- Cubist: mejor rendimiento (R² = 0.908, MAE = 1.92).  
- **Limitación**: sin uso de memoria temporal ni comparación entre métodos de selección de variables.  
- Proponen usar RNN (LSTM, GRU) con Lasso o PLS en trabajos futuros.
""")

    st.markdown("##### [4] Assidjo et al. (2009) – Modelo híbrido MLP + balances")
    st.markdown("""
- Modelado de fermentación glucosa-etanol en batch.  
- MLP acoplada con balances dinámicos (3-7-3).  
- R² ≈ 0.999 (biomasa), MAE < 5 %.  
- **Limitación**: no incluye selección automática de variables ni memoria para procesos largos o fed-batch.
""")


elif seccion == "Metodología":
    st.subheader("Metodología")

    st.markdown("### 1. Inicio del Proyecto")

    st.markdown("### 2. Análisis Exploratorio de Datos")
    st.markdown("""
2.1 Evaluación de calidad de datos  
2.2 Filtrado y selección de variables relevantes  
2.3 Análisis de correlación con la concentración de penicilina  
2.4 Segmentación por tipo de control:
   - Receta  
   - Operadores  
   - APC Raman  
   - Fallas
    """)

    st.markdown("### 3. Selección de Variables")
    st.markdown("""
3.1 Técnica 1: Regresión Lasso  
3.2 Técnica 2: Regresión PLS
    """)

    st.markdown("### 4. Entrenamiento de Modelos MLP por Grupo")

    st.markdown("### 5. Optimización de Hiperparámetros")
    st.markdown("""
5.1 Búsqueda Aleatoria (`RandomizedSearchCV`)  
5.2 Validación Cruzada (3-Fold)
    """)

    st.markdown("### 6. Evaluación de Desempeño")
    st.markdown("""
6.1 Comparación entre grupos operativos  
6.2 Comparación entre técnicas (Expertos, Lasso, PLS)
    """)


elif seccion == "Resultados":
    st.subheader("Resultados Detallados")
    
    
    # Calidad de la exploración
    st.markdown("#### Calidad de la exploración")
    
    calidad_data = {
        'Variable': ['Tiempo', 'Tasa de aireación (Fg)', 'RPM del agitador', 'Tasa de alimentación de azúcar (Fs)',
                    'Flujo de ácido (Fa)', 'Flujo de base (Fb)', 'Agua calefacción/enfriamiento (Fc)', 'pH',
                    'Temperatura (T)', 'Penicilina (P)', 'Oxígeno disuelto (DO2)', 'Substrato (S)',
                    'Consumo oxígeno (OUR)', '% CO₂ en gas residual', 'Viscosidad (offline)', 'Volumen del reactor (V)',
                    'Biomasa (offline)', 'Tasa de evolución de carbono (CER)'],
        'Unidad': ['h', 'L/h', 'RPM', 'L/h', 'L/h', 'L/h', 'L/h', 'pH', 'K', 'g/L', 'mg/L', 'g/L', 'g/min', '%', 'cP', 'L', 'g/L', 'g/h'],
        'Media (± DE)': ['114.8 ± 67.0', '65.2 ± 11.7', '100.0 ± 0.0', '76.7 ± 25.7', '0.07 ± 0.55', '61.3 ± 45.0',
                        '74.3 ± 108.0', '6.50 ± 0.07', '298.0 ± 0.2', '14.3 ± 9.9', '12.6 ± 1.5', '4.08 ± 13.3',
                        '0.191 ± 0.0047', '1.44 ± 0.50', '51.5 ± 24.1', '73313 ± 8599', '18.8 ± 7.0', '14.4 ± 10.3'],
        'Mediana': [114, 65, 100, 80, 0, 55.4, 34.4, 6.5, 297.99, 14.38, 12.64, 0.0016, 0.191, 1.6, 53.15, 75770, 21.45, 14.57],
        'Mín – Máx': ['0.2 – 290.0', '20.0 – 75.0', '100.0 – 100.0', '2.0 – 150.0', '0.0 – 13.0', '0.0 – 225.0',
                     '0.0001 – 1500.0', '5.40 – 6.77', '296.84 – 302.18', '~0 – 36.18', '1.00 – 16.51', '0.000006 – 115.27',
                     '0.129 – 0.228', '0.075 – 7.12', '4.08 – 117.9', '56549 – 95716', '0.39 – 27.9', '~0 – 36.18'],
        'Interpretación': ['Tiempo medio de fermentación, con alta variabilidad.', 'Suministro constante de oxígeno.',
                          'Velocidad fija, completamente automatizada.', 'Controlada por demanda metabólica.',
                          'Ajustes puntuales del pH.', 'Principal método de control de pH.',
                          'Cambios térmicos intensos en ciertos momentos.', 'Controlado eficientemente.',
                          'Estable, ideal para crecimiento microbiano.', 'Producción variable, pero eficiente.',
                          'Buen nivel de oxigenación.', 'Alta variabilidad por alimentación discontinua.',
                          'Indicador metabólico estable.', 'Representa respiración microbiana.',
                          'Mayor viscosidad implica mayor biomasa o espuma.', 'Volumen ajustado durante el proceso.',
                          'Buena acumulación celular.', 'Alta actividad metabólica respiratoria.']
    }
    
    df_calidad = pd.DataFrame(calidad_data)
    st.table(df_calidad)
    
    # Centrar la imagen
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("src/assets/correlacion.png", caption="Matriz de correlación", width=900)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Selección de Variables
    st.markdown("#### Selección de Variables")
    
    seleccion_data = {
        'Segmento': ['Receta', 'Operadores', 'APC_Raman', 'Fallas'],
        'Variables seleccionadas por Lasso': [
            'Oil flow, CER, Vessel Weight, Aeration rate, Vessel Volume, CO₂ outgas, Cooling/Heating water, Sugar feed, PAA flow, DO₂, Temp, OUR, Water injection, Heating water, Dumped broth, Air head pressure',
            'Oil flow, Vessel Weight, Aeration rate, CO₂ outgas, Sugar feed, PAA flow, DO₂, Temp, OUR, Water injection, Heating water, Air head pressure',
            'Oil flow, CER, Vessel Weight, Aeration rate, Vessel Volume, CO₂ outgas, Cooling/Heating water, Sugar feed, PAA flow, DO₂, Temp, OUR, Water injection, Heating water, Dumped broth, Air head pressure',
            'Oil flow, CER, Aeration rate, Vessel Volume, CO₂ outgas, Cooling/Heating water, Sugar feed, PAA flow, DO₂, Temp, OUR, Water injection, Heating water, Dumped broth, Air head pressure'
        ],
        'Variables más importantes según PLS (Top 10)': [
            'Vessel Volume, CER, OUR, Cooling/Heating water, Vessel Weight, Air head pressure, Heating water, Aeration rate, DO₂, Oil flow',
            'Vessel Volume, Cooling/Heating water, CER, Vessel Weight, OUR, Heating water, Air head pressure, Aeration rate, DO₂, Oil flow',
            'Vessel Volume, CER, OUR, Cooling/Heating water, Vessel Weight, Air head pressure, Aeration rate, Heating water, DO₂, Oil flow',
            'Heating water, OUR, Temp, CO₂ outgas, Cooling/Heating water, Aeration rate, Vessel Volume, CER, Vessel Weight, Oil flow'
        ]
    }
    
    df_seleccion = pd.DataFrame(seleccion_data)
    st.table(df_seleccion)
    
    # Hiperparámetros probados en MLP
    st.markdown("#### Hiperparámetros probados en MLP")
    
    hiperparametros_data = {
        'Hiper parámetro': ['units', 'layers', 'activation', 'learning-rate', 'batch-size', 'epochs'],
        'Valores probados': ['32,64,128,256', '1,2,3', 'relu,tanh,swish', '0.0001, 0.001,0.005,0.01', '16,32,64', '30, 50,100,150'],
        'Cardinalidad': [4, 3, 3, 4, 3, 4]
    }
    
    df_hiperparametros = pd.DataFrame(hiperparametros_data)
    st.table(df_hiperparametros)
    
    # Modelo con las variables seleccionadas en los expertos en estudios anteriores
    st.markdown("#### Modelo con las variables seleccionadas en los expertos en estudios anteriores")
    
    variables_expertos_data = {
        'Variable': ['Fs', 'Agitación', 'T', 'pH', 'DO', 'V', 'CO₂_og', 'O₂_og', 'P', 'Lote'],
        'Descripción': ['Flujo de sustrato (feed rate)', 'Velocidad de agitación (rpm)', 'Temperatura (°C)', 
                       'Potencial de hidrógeno', 'Oxígeno disuelto (%)', 'Volumen de cultivo (L)', 
                       'CO₂ en salida de gas (%)', 'O₂ en salida de gas (%)', 'Presión (bar)', 'Identificador del lote']
    }
    
    df_variables_expertos = pd.DataFrame(variables_expertos_data)
    st.table(df_variables_expertos)
    
    # Resultados del modelo con variables de expertos
    st.markdown("#### Resultados del modelo con variables seleccionadas por expertos")
    
    resultados_expertos_data = {
        'Grupo': ['Receta', 'Operadores', 'APC_Raman', 'Fallas', 'Todos los grupos'],
        'Units': [64, 64, 32, 32, 256],
        'Learning Rate': [0.001, 0.001, 0.005, 0.005, 0.0001],
        'Layers': [3, 3, 3, 3, 2],
        'Epochs': [50, 50, 150, 150, 30],
        'Batch Size': [16, 16, 64, 64, 16],
        'Activation': ['tanh', 'tanh', 'tanh', 'tanh', 'tanh'],
        'MSE': [8.448, 11.208, 4.643, 47.997, 10.944],
        'RMSE': [2.907, 3.348, 2.155, 6.928, 3.308],
        'R²': [0.922, 0.89, 0.957, -3.538, 0.897],
        'MAE': [1.916, 2.212, 1.435, 4.221, 2.079]
    }
    
    df_resultados_expertos = pd.DataFrame(resultados_expertos_data)
    
    # Formatear números para mejor presentación
    df_resultados_expertos['MSE'] = df_resultados_expertos['MSE'].round(3)
    df_resultados_expertos['RMSE'] = df_resultados_expertos['RMSE'].round(3)
    df_resultados_expertos['R²'] = df_resultados_expertos['R²'].round(3)
    df_resultados_expertos['MAE'] = df_resultados_expertos['MAE'].round(3)
    
    st.table(df_resultados_expertos)
    
    # Resultados del modelo con Lasso
    st.markdown("#### Resultados del modelo con selección de variables por Lasso")
    
    resultados_lasso_data = {
        'Grupo': ['Receta', 'Operadores', 'APC_Raman', 'Fallas', 'Todos los grupos'],
        'Units': [32, 64, 32, 32, 128],
        'Learning Rate': [0.005, 0.001, 0.005, 0.005, 0.0001],
        'Layers': [3, 3, 3, 3, 2],
        'Epochs': [150, 50, 150, 150, 100],
        'Batch Size': [64, 16, 64, 64, 32],
        'Activation': ['tanh', 'tanh', 'tanh', 'tanh', 'swish'],
        'MSE': [11.055, 6.333, 2.849, 20.179, 8.528],
        'RMSE': [3.325, 2.517, 1.688, 4.492, 2.92],
        'R²': [0.898, 0.938, 0.974, -0.908, 0.919],
        'MAE': [2.082, 1.638, 1.156, 2.824, 1.691]
    }
    
    df_resultados_lasso = pd.DataFrame(resultados_lasso_data)
    
    # Formatear números para mejor presentación
    df_resultados_lasso['MSE'] = df_resultados_lasso['MSE'].round(3)
    df_resultados_lasso['RMSE'] = df_resultados_lasso['RMSE'].round(3)
    df_resultados_lasso['R²'] = df_resultados_lasso['R²'].round(3)
    df_resultados_lasso['MAE'] = df_resultados_lasso['MAE'].round(3)
    
    st.table(df_resultados_lasso)
    
    # Resultados del modelo con PLS
    st.markdown("#### Resultados del modelo con selección de variables por PLS")
    
    resultados_pls_data = {
        'Grupo': ['Receta', 'Operadores', 'APC_Raman', 'Fallas', 'Todos los grupos'],
        'Units': [64, 32, 64, 32, 128],
        'Learning Rate': [0.001, 0.005, 0.001, 0.005, 0.001],
        'Layers': [3, 3, 3, 3, 1],
        'Epochs': [50, 150, 50, 150, 50],
        'Batch Size': [16, 64, 16, 64, 64],
        'Activation': ['tanh', 'tanh', 'tanh', 'tanh', 'relu'],
        'MSE': [6.321, 11.422, 3.121, 26.009, 6.496],
        'RMSE': [2.514, 3.38, 1.767, 5.1, 2.549],
        'R²': [0.942, 0.888, 0.971, -1.459, 0.939],
        'MAE': [1.611, 2.155, 1.236, 3.167, 1.631]
    }
    
    df_resultados_pls = pd.DataFrame(resultados_pls_data)
    
    # Formatear números para mejor presentación
    df_resultados_pls['MSE'] = df_resultados_pls['MSE'].round(3)
    df_resultados_pls['RMSE'] = df_resultados_pls['RMSE'].round(3)
    df_resultados_pls['R²'] = df_resultados_pls['R²'].round(3)
    df_resultados_pls['MAE'] = df_resultados_pls['MAE'].round(3)
    
    st.table(df_resultados_pls)
    

    
    

elif seccion == "Hallazgos y Conclusiones":
    st.subheader("Aspectos Relevantes y Conclusiones")
    st.markdown("""
### 🌟 Aspectos Relevantes del Proyecto

- Se modeló la producción de penicilina en un entorno simulado de fermentación industrial.
- Se utilizaron técnicas de selección de variables como Lasso y PLS para entrenar redes neuronales MLP.
- Se segmentaron los datos según el tipo de control operativo (Receta, Operador, APC-Raman, Fallas).
- El grupo APC-Raman mostró el mejor rendimiento predictivo (R² > 0.95).
- Las redes MLP con variables seleccionadas automáticamente superaron a las definidas por expertos.
- Las estrategias de control automatizado permitieron capturar relaciones no lineales del proceso.

### 🌟 Conclusiones

- Las MLP integradas con PLS/Lasso son efectivas como sensores blandos.
- El rendimiento mejora significativamente al segmentar por tipo de operación.
- La inclusión de datos Raman permitió alcanzar las mejores métricas predictivas.
- Se evidenció la necesidad de construir modelos específicos para condiciones anómalas (fallas).
""")
    
elif seccion == "Referencias":
    st.subheader("Referencias")
    st.markdown("""   
[1] S. Goldrick et al., "Modern day monitoring and control challenges outlined on an industrial-scale benchmark fermentation process," Computers & Chemical Engineering, vol. 130, pp. 106471, 2019. 

[2] S. Goldrick et al., "The development of an industrial-scale fed-batch fermentation simulation," Journal of Biotechnology, vol. 193, pp. 70–82, 2015. 

[3] J. C. Acosta-Pavas et al., "Soft sensors based on interpretable learners for industrial-scale fed-batch fermentation: Learning from simulations," Computers & Chemical Engineering, vol. 187, pp. 108736, 2024. 

[4]  Assidjo, N. E., Akaki, D., Yao, B. K., & Eboi, T. Y. (2009). A hybrid neural network approach for batch fermentation simulation. Australian Journal of Basic and Applied Sciences, 3(4), 3930-3936. 

 """)  

elif seccion == "Cronograma":
    st.subheader("Cronograma")
    st.markdown("""
    #### Cronograma del Proyecto
    """)
    
    cronograma_data = {
        'Posición': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        'Fecha de inicio': ['17/03/2025', '18/03/2025', '18/03/2025', '26/03/2025', '26/03/2025', 
                           '26/03/2025', '26/03/2025', '07/04/2025', '09/04/2025', '09/04/2025',
                           '29/04/2025', '29/04/2025', '29/04/2025', '23/05/2025', '17/05/2025', '21/06/2025'],
        'Fecha de finalización': ['18/03/2025', '26/03/2025', '26/03/2025', '09/04/2025', '09/04/2025',
                                 '09/04/2025', '09/04/2025', '29/04/2025', '29/04/2025', '29/04/2025',
                                 '17/05/2025', '23/05/2025', '31/05/2025', '08/06/2025', '23/06/2025', '09/07/2025'],
        'Hito o actividad': ['Inicio', 'Revisión bibliografica', 'Análisis exploratorio', 'Encontrar los lotes en la BD',
                            'Selección de variables con PLS', 'Selección de variables con Lasso', 'Realizar ACP',
                            'Revisión de artículos nuevos', 'Separar los lotes por los grupos', 'Selección de variables por cada grupo',
                            'Implementar Red neuronal con las variables seleccionadas con PLS', 'Implementar Red neuronal con las variables seleccionadas con Lasso',
                            'Implementar Red neuronal con las variables seleccionadas en estudios anteriores', 'Comparación de resultados y Ajustes de modelos',
                            'Validación de resultados con los expertos de INRAE', 'Conclusiones']
    }
    
    df_cronograma = pd.DataFrame(cronograma_data)
    st.table(df_cronograma)




 