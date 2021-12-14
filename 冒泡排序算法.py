def bubble_sort_plus(alist):
    n = len(alist)
    # j表示每次遍历需要比较的次数，是逐渐减小的
    for j in range(n - 1):
        count = 0  # 用于记录一次比较过程中交换了多少次数据、交换0次、已经排序完成！！！
        # i表示一次比较要比较多少次
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:
            return


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort_plus(li)
    print(li)