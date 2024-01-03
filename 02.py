class Stack:
    def __init__(self):
        # Use a list to represent the stack
        self.stack = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def push(self, element):
        """Push an element onto the stack."""
        self.stack.append(element)
        print(f"Element {element} pushed onto the stack.")

    def pop(self):
        """Pop the top element from the stack."""
        if not self.is_empty():
            popped_element = self.stack.pop()
            print(f"Element {popped_element} popped from the stack.")
            return popped_element
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        """Return the top element of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek.")

# Example usage:
stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Peek at the top element
top_element = stack.peek()
print(f"Top element of the stack: {top_element}")

# Pop elements from the stack
popped_element1 = stack.pop()
popped_element2 = stack.pop()

# Check if the stack is empty
print(f"Is the stack empty? {stack.is_empty()}")

# Try popping from an empty stack
stack.pop()
