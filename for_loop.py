skills = ['Python', 'Azure', 'Linux', 'Database', 'Coding']
for skill in skills:
    print('I have skill of',skill)
print('I have currently',str(len(skills)),'skills')

#Adding new skill called AI

skills.append('AI')
print('I have added new skill called', skills[5])

for skill in skills:
    print('I have skill of',skill)
print('I have currently',len(skills),'skills')

#Removing the new skill AI
if 'AI' in skills:
    skills.remove('Java')
print('I have removed new skill')


for skill_number, skill in enumerate(skills, start=1):
    print(f'{skill_number} {skill}')
print('I have finally',len(skills),'skills')