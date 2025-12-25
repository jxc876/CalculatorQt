DIGITS = "1234567890"
OPERATORS = "+-x/"
EQUAL = "="
CLEAR_ENTRY = "C"
ALL_CLEAR = "AC"
BACKSPACE = "<"
SIGN = "+/-"

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
        elif str == EQUAL:
            self.handle_equals()
        elif str == SIGN:
            self.handle_sign()
        else:
            self.handle_other(str)

    def handle_digits(self, str):
        str = str.upper()
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

    def handle_sign(self):
        if self.display_str[0] == "-":
            self.display_str = self.display_str[1:] # remove negative
        elif self.display_str != "0":
            self.display_str = f"-{self.display_str}" # add negative if no sign

    def handle_other(self, str):
        if str == CLEAR_ENTRY:
            self.display_str = "0" # (Clear Entry) erases the current number
        elif str == ALL_CLEAR:
            self.display_str = "0" # (All Clear) reset everything
            self.operand_1 = ""
            self.operation = ""
        elif str == BACKSPACE:
            # backspace
            if len(self.display_str) == 1:
                self.display_str = "0"
            else:
                self.display_str = self.display_str[:-1]
