class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

class Table:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_pid(self):
        for i in range(len(self.processes)):
            for j in range(len(self.processes) - i - 1):
                if self.processes[j].p_id > self.processes[j + 1].p_id:
                    self.processes[j], self.processes[j + 1] = self.processes[j + 1], self.processes[j]

    def sort_by_start_time(self):
        for i in range(len(self.processes)):
            for j in range(len(self.processes) - i - 1):
                if self.processes[j].start_time > self.processes[j + 1].start_time:
                    self.processes[j], self.processes[j + 1] = self.processes[j + 1], self.processes[j]

    def sort_by_priority(self):
        priority_order = {"High": 1, "MID": 2, "Low": 3}
        for i in range(len(self.processes)):
            for j in range(len(self.processes) - i - 1):
                if priority_order[self.processes[j].priority] > priority_order[self.processes[j + 1].priority]:
                    self.processes[j], self.processes[j + 1] = self.processes[j + 1], self.processes[j]

    def display(self):
        print("{:<5} {:<10} {:<15} {}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
        print("=" * 40)
        for process in self.processes:
            print("{:<5} {:<10} {:<15} {}".format(process.p_id, process.name, process.start_time, process.priority))

def main():
    table = Table()

    table.add_process(Process("P1", "VSCode", 100, "MID"))
    table.add_process(Process("P23", "Eclipse", 234, "MID"))
    table.add_process(Process("P93", "Chrome", 189, "High"))
    table.add_process(Process("P42", "JDK", 9, "High"))
    table.add_process(Process("P9", "CMD", 7, "High"))
    table.add_process(Process("P87", "NotePad", 23, "Low"))

    while True:
        print("\nSelect sorting parameter:")
        print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            table.sort_by_pid()
        elif choice == "2":
            table.sort_by_start_time()
        elif choice == "3":
            table.sort_by_priority()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

        table.display()

if __name__ == "__main__":
    main()