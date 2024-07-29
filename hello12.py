if __name__ == '__main__':
    my_dict = {}
    score_arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_arr.append(score)
        if score in my_dict:
            # list_name = list(my_dict.get(score))
            # list_name.append(name)
            # my_dict[score] = tuple(list_name)
            list_name = my_dict.get(score)
            list_name.append(name)
            my_dict[score] = list_name
        else:
            #my_dict[score] = (name,)
            my_dict[score] = [name]
    lowest_score = None
    for score in sorted(score_arr):
        if lowest_score is None:
            lowest_score = score
        if score != lowest_score:
            second_lowest = my_dict.get(score)
            for name in sorted(second_lowest):
                print(name)
            break
