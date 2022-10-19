import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calculator(QWidget):
	def __init__(self):
		super().__init__()

		self.lhs, self.rhs, self.op = None, None, None
		self.save_rhs = False
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
		self.input.setReadOnly(True)
		self.hbox_input.addWidget(self.input)

		for character in ["1", "2", "3", "."]:
			character_button = QPushButton(character, self)
			character_button.clicked.connect(lambda state, x=character: self._button(x))
			self.hbox_first.addWidget(character_button)

		for operation in ["+", "-", "*", "/"]:
			action_button = QPushButton(operation, self)
			action_button.clicked.connect(lambda state, x=operation: self._operation(x))
			self.hbox_actions.addWidget(action_button)

		self.b_result = QPushButton("=", self)
		self.b_result.clicked.connect(self._result)
		self.hbox_result.addWidget(self.b_result)

	def _button(self, param):
		line = self.input.text()

		if param == "." and "." in line:
			return

		self.save_rhs = False
		self.input.setText(line + param)

	def _operation(self, op):
		lhs_text = self.input.text()

		self.op, self.save_rhs = op, False
		if not lhs_text:
			return

		self.lhs = float(self.input.text())
		self.input.setText("")

	def _result(self):
		if self.lhs is None or self.op is None:
			return

		rhs_text = self.input.text()
		if not rhs_text:
			return
		if not self.save_rhs:
			self.rhs = float(rhs_text)

		self.operations = {
			"+": lambda lhs, rhs: lhs + rhs, "-": lambda lhs, rhs: lhs - rhs,
			"*": lambda lhs, rhs: lhs * rhs, "/": lambda lhs, rhs: lhs / rhs
		}
		result = self.operations[self.op](self.lhs, self.rhs)
		self.input.setText("{:g}".format(result))

		self.save_rhs = True
		self.lhs = result


def main():
	app = QApplication(sys.argv)

	win = Calculator()
	win.show()

	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
