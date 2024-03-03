class Nums:

    def __init__(self, list):
       self.numbers = list
       self.predictedNumber = None
       self.child = None

    def process_nums(self):
        new_nums = []
        for indx, v in enumerate(self.numbers):
            if indx < len(self.numbers)-1:
                new_nums.append(int(self.numbers[indx+1])-int(v))

        if sum(new_nums) != 0:
            self.child = Nums(new_nums)
            self.child.process_nums()
    def print_nums(self):
        print(self.numbers, self.predictedNumber)
        if self.child != None:
            self.child.print_nums()

    def predict_prev_num(self):
        stack = [self]
        child = self.child
        while child != None:
            stack.append(child)
            child = child.child

        while len(stack) != 0:
            nums = stack.pop()
            if nums.child == None:
                nums.predictedNumber = int(nums.numbers[0])
            else:
                nums.predictedNumber = int(nums.numbers[0])-int(nums.child.predictedNumber)
    def predict_next_num(self):
            stack = [self]
            child = self.child
            while child != None:
                stack.append(child)
                child = child.child

            while len(stack) != 0:
                nums = stack.pop()
                if nums.child == None:
                    nums.predictedNumber = int(nums.numbers[0])
                else:
                    nums.predictedNumber = int(nums.numbers[len(nums.numbers)-1])+int(nums.child.predictedNumber)






#part1
f = open("input.txt", "r")
total = 0
for line in f:
  n1 = Nums(line.split())
  n1.process_nums()
  n1.predict_next_num()
  total += n1.predictedNumber
f.close()

#answer 1647269739
print("part 1 day 9", total)

# part2
f1 = open("input.txt", "r")
total = 0
for line in f1:
    n1 = Nums(line.split())
    n1.process_nums()
    n1.predict_prev_num()
    total += n1.predictedNumber
f1.close()

#answer 1647269739
print("part 2 day 9", total)

