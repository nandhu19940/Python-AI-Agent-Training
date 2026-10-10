skills = ['Python', 'Azure', 'AI', 'DevOps', 'Linux']
skills_temp = []
for skills_lower in skills:
   skills_temp.append(skills_lower.lower())
while True:
      skill_remove_userinput = input(("Enter the skill you want to remove "))
      skill_remove = skill_remove_userinput.lower()
      if skill_remove in skills_temp:
         position = skills_temp.index(skill_remove)
         del skills_temp[position]
         del skills[position]
         break
      else:
         print(f'You have entered {skill_remove_userinput} Please enter correct skill to remove')
for skill in skills:
   print('I have skill called', skill)
print ('In total I have', len(skills), 'skills')