

import time



correct = 0
crt_let = []
para = 'sample sam sample sample'

###Main Working
start = time.time()
print(para)
user_input = input('Start Typing here:\n')
for index, val in enumerate(user_input):
    if user_input[index] == para[index]:
        correct+=1
        crt_let.append(val)
end = time.time()
elas = end - start
####ends here


words_dict = user_input.split(' ')

# print('Correct letters',crt_let)
print(words_dict)
print('Time elasped is',elas)
# print('time type',type(elas))
alpha_result = correct/(elas/60)
crtword_result = len(words_dict)/(elas/60)
print(f'Your average typing speed for Correct alphabets is {alpha_result} alphabets per minute')
print(f'Average typing speed is {crtword_result} Words per minute')



