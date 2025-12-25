DIGITS = "1234567890"
OPERATORS = "+-x/"

class Calculator:

    display_str = ""
    operand_1 = ""
    operation = ""

    def __init__(self):
        self.display_str = "0"

    def put(self, str: str):
        if str in DIGITS:
            self.handle_digits(str)
        elif str in OPERATORS:
            self.handle_operators(str)
        elif str == "=":
            self.handle_equals()

    def handle_digits(self, str):
        if self.display_str == "0" and str == "0":
            return # no leading double zeros

        elif self.display_str == "0":
            self.display_str = str

        else:
            self.display_str += str

    def handle_operators(self, str):
        self.operation = str # store operation
        self.operand_1 = self.display_str # store operand 1
        self.display_str = "0"

    def handle_equals(self):
        try:
            # parse operand 1 and operand 2
            operand_1 = float(self.operand_1)
            operand_2 = float(self.display_str)
            operation = self.operation

            if operation == "+":
                self.display_str = str(operand_1 + operand_2)
            elif operation == "-":
                self.display_str = str(operand_1 - operand_2)
            elif operation == "x":
                self.display_str = str(operand_1 * operand_2)

            # reset
            self.operand_1 = ""
            self.operation = ""
        except:
            print("calculator - error parsing numbers")
            self.display_str = "Err"

