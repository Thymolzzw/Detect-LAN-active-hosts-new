


if __name__ == '__main__':
    with open("ans.txt", "r") as f:
        num = 0
        ok_num = 0
        for line in f:
            print(line, end="")
            if line.count("连接成功"):
                ok_num += 1
            num += 1
        print("总数：", num)
        print("成功连接数：", ok_num)

