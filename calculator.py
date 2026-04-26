# filepath: calculator.py
"""Simple Python Calculator"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")
    
    while True:
        expression = input("Enter expression (e.g., 5 + 3): ").strip()
        
        if expression.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            parts = expression.split()
            if len(parts) != 3:
                print("Invalid format. Use: number operator number")
                continue
            
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
            
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print("Invalid operator. Use: +, -, *, /")
                continue
            
            print(f"Result: {result}")
            
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()