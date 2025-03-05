# importa librerias
import pandas as pd # importa pandas y la renombra como pd
import re # importa re para expresiones regulares

# lee el archivo csv y lo guarda en la variable df
# header=0 indica que la primera fila es el encabezado
# index_col='Noticia_id' indica que la columna Noticia_id es el índice
# de la tabla
df = pd.read_csv('dataset.csv', header=0, index_col='Noticia_id')

# elimina las filas que tengan valores nulos en la columna index
# esto es porque el índice de la tabla no puede tener valores nulos
df = df[df.index.notnull()]


if df.isnull().values.any(): # si hay valores nulos en la tabla
    if df['Medio'].isnull().values.any(): # verifica la col 'Medio' es nula
        df[['Medio']] = df[['Medio']].fillna('Desconocido') # si es nula, rellena con 'Desconocido'
    if df['Seccion'].isnull().sum(): # si la col ' seccion' tiene cuenta nulos
        df.Seccion = df.Seccion.fillna('Otra') # rellena con la col 'Seccion' con el valor: 'Otra'


def processText(input_text: str) -> str: # funcion que recibe un string y devuelve un string
    processed_text = re.sub('[^a-zA-Záéíóúñü]+', ' ', input_text) # elimina caracteres especiales
    processed_text = processed_text.lower() # convierte el texto a minúsculas
    return processed_text # retorna el texto procesado


# Aplica la función processText a cada fila del DataFrame, específicamente a la columna Cuerpo.
# con una funcion lambda que recibe una fila y aplica la funcion processText a la columna Cuerpo
# alo largo de la (axis=1) Solo filas
df['Cuerpo_procesado'] = df.apply(lambda row: processText(row['Cuerpo']), axis=1) 


# Guardamos en un archivo CSV en UTF-8 usando separador tab, incluye cabeceras y el indice Noticia_id
df.to_csv('output_df.csv', sep='\t', index=True, encoding='utf-8', header=True)

# Es un scrip muy útil para limpiar y preprocesar datos de texto para su posterior análisis.