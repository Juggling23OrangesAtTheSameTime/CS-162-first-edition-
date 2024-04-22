# Prem=Premium, Stan=Standard, Econ=Economy
input_packets = open("input_queue.txt", "r")
econ_queue = []
stan_queue = []
prem_queue = []
# this for loop organizes the customers into their queues
for line in input_packets:
    line = line.strip("\n")
    customer = line[2:]
    if line[0] == "P":
        prem_queue.append(customer)
    elif line[0] == "S":
        stan_queue.append(customer)
    elif line[0] == "E":
        econ_queue.append(customer)
# these print functions are just so you can later see how the wfq was successful
print("Premium:", prem_queue)
print("Standard:", stan_queue)
print("Economy:", econ_queue)
# the variables a,b,c will make sure that all customers get printed out
a = b = c = True
priority_output = []
# this while loop appends the popped parts of each queue into an organized priority list
while a or b or c:
    if len(prem_queue) < 3:
        for i in range(len(prem_queue)):
            priority_output.append(prem_queue.pop(0))
            a = False
    else:
        for i in range(3):
            priority_output.append(prem_queue.pop(0))

    if len(stan_queue) <= 2:
        for i in range(len(stan_queue)):
            priority_output.append(stan_queue.pop(0))
        b = False
    else:
        for i in range(2):
            priority_output.append(stan_queue.pop(0))

    if len(econ_queue) < 1:
        c = False
    else:
        priority_output.append(econ_queue.pop(0))

print(priority_output)
