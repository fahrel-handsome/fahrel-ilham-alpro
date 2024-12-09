#with open ('fileku.txt', 'w') as file:
#    file.write('Hello, Word!\n')
#    file.writelines(['Line 1\n', 'Line 2\n'])

#with open('events (1).txt', 'a') as file:
#   file.write('\nschool Exam,2/12/24')
    
import pandas as pd

df = pd.read_csv('students (1).csv')
print(df)

print("\nBaris pertama:")
print(df.head())
df.info()
print(df.describe())

df['status'] = ['lulus' if nilai >= 80 else 'tidak lulus' for nilai in df['Grade']]
print(df)

df.to_csv('students_processed.csv', index=False)

rata_rata_nilai_grade = df['Grade'].mean()
print("Rata-rata nilai grade student:", rata_rata_nilai_grade)
kelompok = df.groupby('status').size()
print(kelompok)
