from play import play


def main():
    x_win = 0
    o_win = 0
    draws = 0
    for _ in range(10):
        result = play()
        if result == 1:
            x_win += 1
        elif result == -1 :
            o_win += 1
        else:
            draws += 1
    print("X won " + str(x_win) + " times")
    print("O won " + str(o_win) + " times")
    print("Draws: " + str(draws))


if __name__ == "__main__":
    main()