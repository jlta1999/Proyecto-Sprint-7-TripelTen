Proyecto-Sprint-7-TripelTen

* Enlace a mi pagina cargada en Render:  https://proyecto-sprint-7-tripelten.onrender.com

* Este repositorio, es para cursar y realizar el proyecto del sprint 7 en mi bootcamp. 

* En aras de la simplicidad, se anadiran las 3 librerias con las que se trabajan, sin especificar las versiones.

* Aplicación web en **Streamlit** para explorar un conjunto de datos de anuncios de venta de vehículos en EE. UU. Permite generar visualizaciones interactivas con un clic (histograma y dispersión) para entender la distribución del odómetro y la relación entre odómetro y precio.

Funcionalidad principal:
- **Histograma (odometer):** Visualiza la distribución del kilometraje declarado.
- **Gráfico de dispersión (odometer vs price):** Explora la relación entre precio y uso del vehículo.
- Interfaz simple con **botones** (`st.button`) y gráficos interactivos con **Plotly Express** (`st.plotly_chart`).

Requisitos:
- Archivo `requirements.txt` con librerias a utilizar:
pandas
plotly_express
streamlit