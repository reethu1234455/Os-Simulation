import operator

# Define a data structure to hold process information
processes = []
class Process:
    def _init_(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.waiting_time = 0
        self.priority = 0

# Get the number of processes to be scheduled
n = int(input("Enter the number of processes: "))

# Prompt the user to enter burst time for each process
for i in range(n):
    burst_time = int(input("Enter burst time for process {}: ".format(i+1)))
    processes.append(Process(i+1, burst_time))

# Initialize waiting time and priority for each process to 0
for process in processes:
    process.waiting_time = 0
    process.priority = 1 + process.waiting_time / process.burst_time

# Sort the processes based on priority
processes.sort(key=operator.attrgetter('priority'))

# Start the scheduling process
total_waiting_time = 0
print("Gantt Chart:")
for i in range(n):
    process = processes[i]
    print("P{} [{}]".format(process.pid, process.burst_time), end=' ')
    for j in range(process.burst_time):
        # Update waiting time and priority for all processes
        for p in processes:
            if p != process:
                p.waiting_time += 1
                p.priority = 1 + p.waiting_time / p.burst_time
        # Re-sort the processes based on the updated priority
        processes.sort(key=operator.attrgetter('priority'))
    # Calculate individual waiting time for each process
    process.waiting_time = sum([p.burst_time for p in processes[:i]]) 
    total_waiting_time += process.waiting_time

# Calculate average waiting time
avg_waiting_time = total_waiting_time / n

# Print individual and average waiting time
print("\nIndividual waiting time:")
for process in processes:
    print("P{}: {}".format(process.pid, process.waiting_time))
print("Average waiting time: {:.2f}".format(avg_waiting_time))
