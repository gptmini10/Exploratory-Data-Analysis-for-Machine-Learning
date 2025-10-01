class EmptyStackException(Exception):
    pass

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        """Returns True if the stack is empty, otherwise False."""
        return len(self.stack) == 0

    def clear(self):
        """Clears the stack."""
        self.stack = []

    def push(self, x):
        """Inserts a node with value x at the top of the stack."""
        self.stack.append(x)

    def pop(self):
        """Removes the top element of the stack and returns its value."""
        if self.isEmpty():
            raise EmptyStackException("Stack is empty!")
        return self.stack.pop()

    def top(self):
        """Returns the value of the top node of the stack."""
        if self.isEmpty():
            raise EmptyStackException("Stack is empty!")
        return self.stack[-1]

    def traverse(self):
        """Displays all values in the stack from top to bottom."""
        if self.isEmpty():
            print("Stack is empty!")
        else:
            print("Stack contents (top to bottom):")
            for value in reversed(self.stack):
                print(value)

    def decimal_to_binary(self, n):
        """Converts a decimal number to binary using a stack."""
        while n > 0:
            self.push(str(n % 2))
            n //= 2
        
        binary = ""
        while not self.isEmpty():
            binary += self.pop()
        
        return binary


# Main function to test the stack
def main_stack():
    stack = Stack()

    # Demonstrating stack operations with String values
    print("Is stack empty?", stack.isEmpty())  # Should print True

    # Pushing String values onto the stack
    stack.push("apple")
    stack.push("banana")
    stack.push("cherry")

    # Traversing the stack
    stack.traverse()

    # Top value in the stack
    print("Top value:", stack.top())  # Should print "cherry"

    # Popping the top value
    print("Popped value:", stack.pop())  # Should print "cherry"

    # Traversing the stack again
    stack.traverse()

    # Converting a decimal number to binary using stack
    decimal_number = 29
    binary_number = stack.decimal_to_binary(decimal_number)
    print(f"Binary representation of {decimal_number} is: {binary_number}")

    # Clearing the stack
    stack.clear()
    print("Is stack empty after clearing?", stack.isEmpty())  # Should print True


# Call the main function for stack
main_stack()

Modified Queue Program (String type)

class EmptyQueueException(Exception):
    pass

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        """Returns True if the queue is empty, otherwise False."""
        return len(self.queue) == 0

    def clear(self):
        """Clears the queue."""
        self.queue = []

    def enqueue(self, x):
        """Inserts a node with value x at the end of the queue."""
        self.queue.append(x)

    def dequeue(self):
        """Removes the first element of the queue and returns its value."""
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty!")
        return self.queue.pop(0)

    def first(self):
        """Returns the value of the first node of the queue."""
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty!")
        return self.queue[0]

    def traverse(self):
        """Displays all values in the queue from front to rear."""
        if self.isEmpty():
            print("Queue is empty!")
        else:
            print("Queue contents (front to rear):")
            for value in self.queue:
                print(value)

    def decimal_to_binary(self, n):
        """Converts a real number less than 1 (decimal fraction) to binary."""
        binary = "."
        while n > 0 and len(binary) < 32:  # Limiting to 32 digits after the decimal
            n *= 2
            bit = int(n)
            binary += str(bit)
            n -= bit
        return binary


# Main function to test the queue
def main_queue():
    queue = Queue()

    # Demonstrating queue operations with String values
    print("Is queue empty?", queue.isEmpty())  # Should print True

    # Enqueueing String values into the queue
    queue.enqueue("apple")
    queue.enqueue("banana")
    queue.enqueue("cherry")

    # Traversing the queue
    queue.traverse()

    # First value in the queue
    print("First value:", queue.first())  # Should print "apple"

    # Dequeueing the first value
    print("Dequeued value:", queue.dequeue())  # Should print "apple"

    # Traversing the queue again
    queue.traverse()

    # Converting a decimal number less than 1 to binary using queue
    decimal_number = 0.625
    binary_number = queue.decimal_to_binary(decimal_number)
    print(f"Binary representation of {decimal_number} is: {binary_number}")

    # Clearing the queue
    queue.clear()
    print("Is queue empty after clearing?", queue.isEmpty())  # Should print True


# Call the main function for queue
main_queue()









