import pandas as pd 
import numpy as np 

data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
grades = np.array(data)

study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5, 12.0]

student_data = np.array([study_hours, grades])


df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

# Use the isnull method to identify which individual values are null
print(df_students.isnull())

#Para cuando tengamos muchisimos datos, es mejor checar la suma de los nulos 
# para ver cuantos tenemos, de la siguiente manera
print(df_students.isnull().sum())

#Para que me devuelva los valores nulos
print(df_students[df_students.isnull().any(axis=1)])

# Para trabajar con estos valores nulos, podemos hacer dos cosas. Una seria
# usar fillna para, por ejemplo, reemplasar los valores nulos por el 
# tiempo promedio de estudio. En estos ejercicios, estamos asumiendo que 
# tengo valores nulos xd 

df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())
print("Usando fillna: \n" + str(df_students))

# En cambio, para simplemente remover los valores nulos, usamos dropna 
df_students = df_students.dropna(axis=0, how='any')

#------------------------------------------------------------------
# A estos procedimientos se les llama clean up data, o sea estamos 
# limpiando nuestros datos de valores nulos y cosas no necesarias+
#------------------------------------------------------------------