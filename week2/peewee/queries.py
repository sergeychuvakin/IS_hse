from ex import * 

school = School.get(School.school_name == 'Union Square Academy for Health Sciences')
print(school.dbn)

school = School.get(School.borough == 'Brooklyn')
print(school.school_name)

print('=================================')

schools = School.select().where(School.borough == 'Brooklyn')
print(type(schools))

print('=================================')

print(schools.count())
for school in schools:
  print (school.school_name)

print('=================================')

schools = School.select().where(School.borough == 'Manhattan').limit(5).order_by(School.total_students.asc())
for school in schools:
  print(school.school_name, school.total_students)

print('=================================')

schools = School.select().where(School.borough == 'Bronx').limit(5).order_by(School.total_students.desc())
for school in schools:
  print(school.school_name, school.total_students)