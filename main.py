
import time

# Phase One ----> simple terminal Based

correct = 0
# crt_let = []
para = ("Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them. \n"
        "So when they were old enough, she sent them out into the world to seek their fortunes.The first little \n"
        "pig was very lazy. He didn't want to work at all and he built his house out of straw. The second little \n"
        "pig worked a little bit harder but he was somewhat lazy too and he built his house out of sticks. Then, \n"
        "they sang and danced and played together the rest of the day.The third little pig worked hard all day and \n"
        "built his house with bricks. It was a sturdy house complete with a fine fireplace and chimney. It looked \n"
        "like it could withstand the strongest winds.The next day, a wolf happened to pass by the lane where the \n"
        "three little pigs lived; and he saw the straw house, and he smelled the pig inside. He thought the pig \n"
        "would make a mighty fine meal and his mouth began to water.")

###Main Working
start = time.time()
print(para)
user_input = input('Start Typing here:\n')

if len(user_input) <= len(para):
    for index, val in enumerate(user_input):
        if user_input[index] == para[index]:
            correct+=1
            # crt_let.append(val)

    end = time.time()
    elas = end - start
    user_words_dict = user_input.split(' ')
    para_words_dict = para.split(' ')
    correct_words = 0
    for idx,word in enumerate(user_words_dict):
        if para_words_dict[idx] == user_words_dict[idx]:
            correct_words+=1

    print('Correct Words',correct_words)
    print('Time elasped is',elas)
    # print('time type',type(elas))
    alpha_result = correct/(elas/60)
    crtword_result = correct_words/(elas/60)
    print(f'Your Current Average typing speed for Correct alphabets is {alpha_result} alphabets per minute')
    print(f'Average typing speed is {crtword_result} Words per minute')


else:
    print('Please Type correctly, You have typed more that original paragraph')
