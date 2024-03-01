import re
import math
f = open("input.txt", "r")

count = 0
instructions=""
map = {}


def add_to_map(line):
    three = re.findall(r'\b\w{3}\b', line)
    map[three[0]]=three[1:3]

for line in f:
    if count == 0:
       instructions = line
    elif count == 1:
        pass
    else:
        add_to_map(line)
    count+=1



f.close()

instructions = instructions.replace("\n","")

def get_next(ins, key):
    if ins == "L":
        return (map[key][0])
    else:
        return(map[key][1])

steps = 0
steps_part2=1
def search_for_zzz(key):
    global steps
    for x in instructions:
         key = get_next(x, key)
         steps+=1
        # print (key)
         if key == "ZZZ":
             break
    if key != "ZZZ":
        search_for_zzz(key)

#search_for_zzz("AAA")
#print("part1 steps took to find key ZZZ: " + str(steps))

# answer is: 17141
def search_for_ending_with_z(k):
    count = 0
    stack = [instructions]
    while len(stack)!=0:
        ins = stack.pop()
        for x in ins:
            k=get_next(x,k)
            count+=1
            if k[2:3]=="Z":
               return count
            else:
               stack.append(ins)


keys_ending_with_a = []
for k in map.keys():
    if "A" == k[2:3]:
            keys_ending_with_a.append(k)

total_steps = []
for k1 in keys_ending_with_a:
    total_steps.append(search_for_ending_with_z(k1))

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b) if a and b else 0


def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result


#10818234074807
print("part 2, totals ",  lcm_of_list(total_steps))


