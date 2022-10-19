import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calculator(QWidget):
	def __init__(self):
		super().__init__()

		self.vbox = QVBoxLayout(self)

		self.hbox_input = QHBoxLayout()
		self.hbox_first = QHBoxLayout()
		self.hbox_actions = QHBoxLayout()
		self.hbox_result = QHBoxLayout()

		self.vbox.addLayout(self.hbox_input)
		self.vbox.addLayout(self.hbox_first)
		self.vbox.addLayout(self.hbox_actions)
		self.vbox.addLayout(self.hbox_result)

		self.input = QLineEdit(self)
		self.hbox_input.addWidget(self.input)

		self.b_1 = QPushButton("1", self)
		self.hbox_first.addWidget(self.b_1)

		self.b_2 = QPushButton("2", self)
		self.hbox_first.addWidget(self.b_2)

		self.b_3 = QPushButton("3", self)
		self.hbox_first.addWidget(self.b_3)

		for operation in ["+", "-", "*", "/"]:
			action_button = QPushButton(operation, self)
			action_button.clicked.connect(lambda state, x=operation: self._operation(x))
			self.hbox_actions.addWidget(action_button)

		self.b_result = QPushButton("=", self)
		self.hbox_result.addWidget(self.b_result)

		self.b_result.clicked.connect(self._result)

		self.b_1.clicked.connect(lambda: self._button("1"))
		self.b_2.clicked.connect(lambda: self._button("2"))
		self.b_3.clicked.connect(lambda: self._button("3"))

	def _button(self, param):
		line = self.input.text()
		self.input.setText(line + param)

	def _operation(self, op):
		self.num_1 = int(self.input.text())
		self.op = op
		self.input.setText("")
	
	def _result(self):
		self.num_2 = int(self.input.text())
		if self.op == "+":
			self.input.setText(str(self.num_1 + self.num_2))
		elif self.op == "-":
			self.input.setText(str(self.num_1 - self.num_2))
		elif self.op == "*":
			self.input.setText(str(self.num_1 * self.num_2))
		elif self.op == "/":
			self.input.setText(str(self.num_1 / self.num_2))


def main():
	app = QApplication(sys.argv)

	win = Calculator()
	win.show()

	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
