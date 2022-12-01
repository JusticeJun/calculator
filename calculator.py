import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_buttons = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 숫자나 연산자 등을 입력받을 위젯을 만들어 둠
        self.equation = QLineEdit("")
        self.operation = QLineEdit("")

        ### 첫 수를 입력받았으면 두 번째 수와 더하기 위해 저장할 변수를 만들어 둠 
        self.num = 0

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(self.equation)

        ### 버튼 추가 ###
        ### 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 새로 추가된 계산 버튼 생성
        button_modulo = QPushButton("%")   
        button_inverse = QPushButton("1/x")
        button_square = QPushButton("x\u00b2")  # x^2
        button_root = QPushButton("\u221ax")    # square root x

        ### =, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_backspace = QPushButton("Backspace")

        ### 새로 추가된 C, CE 버튼 생성
        button_clear = QPushButton("C")
        button_clear_entry = QPushButton("CE")

        ### 위젯 추가 ###
        ### 사칙연산 버튼을 layout_buttons 레이아웃에 추가
        layout_buttons.addWidget(button_plus, 4, 3)
        layout_buttons.addWidget(button_minus, 3, 3)
        layout_buttons.addWidget(button_product, 2, 3)
        layout_buttons.addWidget(button_division, 1, 3)

        ### 새로 추가된 계산 버튼을 layout_buttons 레이아웃에 추가
        layout_buttons.addWidget(button_modulo, 0, 0)
        layout_buttons.addWidget(button_inverse, 1, 0)
        layout_buttons.addWidget(button_square, 1, 1)
        layout_buttons.addWidget(button_root, 1, 2)

        ### =, backspace 버튼을 layout_buttons 레이아웃에 추가
        layout_buttons.addWidget(button_backspace, 0, 3)
        layout_buttons.addWidget(button_equal, 5, 3)

        ### C, CE 버튼을 layout_buttons 레이아웃에 추가
        layout_buttons.addWidget(button_clear, 0, 2)
        layout_buttons.addWidget(button_clear_entry, 0, 1)

        ### 시그널 설정 ###
        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        
        ### 숫자 버튼 생성하고, layout_buttons 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_buttons.addWidget(number_button_dict[number], x + 2, y)
            elif number==0:
                layout_buttons.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_buttons.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_buttons.addWidget(button_double_zero, 5, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        self.num = int(self.equation.text())
        self.operation = operation
        self.equation.setText("")

    def button_equal_clicked(self):
        first = str(self.num)
        equation = first + self.operation + self.equation.text()
        self.equation.setText(str(eval(equation)))
        
    def button_clear_clicked(self):
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())