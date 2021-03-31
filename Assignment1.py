player1 = 'Gullit'
player2 = 'Van Basten'

goal_1 = '32'
goal_2 = '54'

scorers = player1 +' ' +str(goal_1) +',' +' ' + player2 +' ' + str(goal_2)
print (scorers)

report = (player1 +' ' +'scored in the' +' ' +goal_1 +'nd minute') +'\n'  +(player2 +' ' +'scored in the' +' ' +goal_2 +'th minute')
print (report)

name = 'Ronald Koeman'
first_name = slice(0,6)
print (name[first_name])

last_name_len = len(name[7:13])
print(last_name_len)

name_short = 'R. Koeman'
print (name_short)

crowd = 'Go'
chant = (crowd+ ' ' +name[first_name]+'!'+' ')*6
print (chant.rstrip())

test_chant = (chant)
good_chant = test_chant != chant
print (good_chant)
