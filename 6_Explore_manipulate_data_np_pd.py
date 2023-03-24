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

# Get the mean study hours using to column name as an index
mean_study = df_students['StudyHours'].mean()

# Get the mean grade using the column name as a property (just to make the point!)
mean_grade = df_students.Grade.mean()

# Print the mean study hours and mean grade
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))

# Get students who studied for the mean or more hours
print(df_students[df_students.StudyHours > mean_study])

# What was their mean grade?
print(df_students[df_students.StudyHours > mean_study].Grade.mean())

#Add a new column to the DataFrame that indicates whether or not each student passed.
# Para ello usamos pandas Series, el cual contiene el indicador pass/fail (True/False)
# para despues concatenar esa serie como una nueva columna (axis 1).
# Un objeto "Series" es un vector con datos indexados. Axis 1 es para columnas
# y 0 es para filas.
passes  = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

print(df_students)


# Usar groupby para agrupar a los que si pasaron y los que no, y contarlos

print(df_students.groupby(df_students.Pass).Name.count())

#Para calcular el promedio de tiempo de estudio y calificaciones de los anteriores:
print(df_students.groupby(df_students.Pass)['StudyHours', 'Grade'].mean())


# Create a DataFrame with the data sorted by Grade (descending)
df_students = df_students.sort_values('Grade', ascending=False)

# Show the DataFrame
df_students

