import os
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 
'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 
'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 
'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for text_file in range(1,11):
    ekzamen = open(r'C:\Users\Пользователь\Desktop\Ekzamen\Bilet\bilet %s.txt'%(text_file),'w')
    keys = open(r'C:\Users\Пользователь\Desktop\Ekzamen\Otvet\otvet %s.txt'%(text_file),'w')
    ekzamen.write('name:\n')
    ekzamen.write('date:\n\n')
    ekzamen.write(' '*15+'Ticket%s\n'%(text_file))
    states = list(capitals.keys())
    random.shuffle(states)
    for question_num in range(50):
        correct = capitals[states[question_num]]
        wrong = list(capitals.values())
        del wrong[wrong.index(correct)]
        wrong = random.sample(wrong,3)
        variant = wrong + [correct]
        random.shuffle(variant)

        ekzamen.write('       #%s  What is capital of %s\n'%(question_num+1,states[question_num]))
        for answer_num in range(4):
            ekzamen.write('%s %s \n'%('ABCD'[answer_num],variant[answer_num]))
        ekzamen.write('\n')
        keys.write('%s %s\n'%(question_num+1,'ABCD'[variant.index(correct)]))
    ekzamen.close()
    keys.close()
        
            
        
        
    
