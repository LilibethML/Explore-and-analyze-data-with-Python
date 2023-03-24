import pandas as pd 
import numpy as np 

data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
grades = np.array(data)

study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

student_data = np.array([study_hours, grades])


df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

#print(df_students)

#Podeos usar el loc method para obtener datos de un index especifico:
print("Con loc: \n" + str(df_students.loc[5]))

#Para un rango de valores:
print("Con loc rango de valores: \n" + str(df_students.loc[0:5]))

#Con iloc pasa algo similar, pero iloc está basado en la posicion ordinal 
# y no en la de los indices

print("Con iloc: \n" + str(df_students.iloc[0:5])) #llega hasta el 4

print("Tambien se puede hacer: \n" + str(df_students.iloc[0,[1,2]]))

#Con loc podemos filtrar datos por el nombre de las columnas:
print('Con nombre de columna con loc: \n' + str(df_students.loc[0,'Grade']))

# Tambien se puede como: 
print('Con nombre de columna con loc: \n' + str(df_students.loc[df_students['Name']=='Aisha']))

# Lo anterior es lo mismo que stas dos siguientes:
# df_students[df_students['Name']=='Aisha']
# df_students.query('Name=="Aisha"')


