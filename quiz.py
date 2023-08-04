import os
def rungame():
    print("Welcome to the OOP Quiz!\n")

    playing = input("Are you ready to take the quiz? (Yes/No): ")

    if playing != "Yes" and playing != "yes":
        quit()

    print("\nThen let us begin!\nPress ENTER for the next question.\nPress Q to quit.\n\n")
    input()

    score = 0;

    char = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    with open('questions.txt') as q:
        with open('answers.txt') as a:
            with open('explanations.txt') as e:
                with open('options.txt') as o:
                    opt = o.readline()
                    for i in range(0,100):
                        os.system('cls')
                        que = q.readline()
                        print(que)
                        for j in range(0,100):
                            opt = o.readline()
                            if(len(opt)<4):
                                break
                            print(char[j], "-", opt)
                        uans = input("Answer: ")
                        ans = a.readline()
                        ex = e.readline()
                        if(uans == ans[0]):
                            print("CORRECT\n")
                            score = score+10
                        else:
                            print("WRONG")
                            score = score-5
                            print("\nSolution:")
                            print(ans)
                        print("Explanation:")
                        print(ex)
                        uans = input("")
                        if(uans=='Q' or uans=='q'):
                            os.system('cls')
                            print("YOUR FINAL SCORE IS: ", score)
                            print("\n\nTHANK YOU FOR PLAYING!!!")
                            input()
                            quit()


