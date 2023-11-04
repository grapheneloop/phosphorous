def run(left, right, lind=0, rind=0):
    if lind < len(left) and rind < len(right):
        if left[lind] == right[rind]:
            print(left[lind])
            lind += 1
            rind += 1
        elif left[lind] < right[rind]:
            lind += 1
        else:
            rind += 1
        run(left, right, lind, rind)


if __name__ == "__main__":
    run([13, 27, 35, 40, 49, 55, 59], [17, 35, 39, 40, 55, 58, 60])
