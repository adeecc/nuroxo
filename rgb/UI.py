from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QDialogButtonBox
import sys
import json
from copy import deepcopy
tabspace = []
cache = []


def backtrack(west, east, state, keys):
    global tabspace
    global cache
    flag = -1
    for i in keys:
        if(state == 'west'):
            west[i] += 1
            east[i] -= 1
        elif(state == 'east'):
            east[i] += 1
            west[i] -= 1

    tabspace.append('\t')
    '''
    print("".join(tabspace)+"state:"+json.dumps(west) +
          " "+json.dumps(east)+" "+state)
    '''
    if(west['r'] == 0 and west['g'] == 0 and west['b'] == 0):
        tabspace = tabspace[:-1]
        cache.append("goal")
        flag = 1  # goal reached

    elif(state == "west"
         and ((west['r'] == 0 and west['g'] == 0)
              or (west['g'] == 0 and west['b'] == 0)
              or (west['r'] == 0 and west['b'] == 0))):
        flag = -1  # invalid state

    elif(state == "west"):
        if(west['r'] != 0 and west['g'] != 0):

            state = "east"
            res = backtrack(west, east, state,   ['r', 'g'])
            state = "west"

            if(res == 1):
                cache.append(deepcopy([west, east, state]))
                flag = 1
        if(flag != 1 and (west['g'] != 0 and west['b'] != 0)):

            state = "east"
            res = backtrack(west, east, state,   ['g', 'b'])
            state = "west"

            if(res == 1):
                cache.append(deepcopy([west, east, state]))
                flag = 1

        if(flag != 1 and (west['r'] != 0 and west['b'] != 0)):

            state = "east"
            res = backtrack(west, east, state,   ['r', 'b'])
            state = "west"

            if(res == 1):
                cache.append(deepcopy([west, east, state]))
                flag = 1

    elif(state == "east"):
        if(east['r'] != 0):

            state = "west"
            res = backtrack(west, east, state,   ['r'])
            state = "east"

            if(res == 1):
                cache.append(deepcopy([west, east, state]))
                flag = 1

        if(flag != 1 and (east['g'] != 0)):

            state = "west"
            res = backtrack(west, east, state,   ['g'])
            state = "east"

            if(res == 1):
                cache.append(deepcopy([west, east, state]))
                flag = 1

        if(flag != 1 and (east['b'] != 0)):
            state = "west"
            res = backtrack(west, east, state,   ['b'])
            state = "east"

            if(res == 1):
                cache.append(deepcopy([west, east, state]))
                flag = 1

    for i in keys:
        if(state == 'west'):
            west[i] -= 1
            east[i] += 1
        elif(state == 'east'):
            east[i] -= 1
            west[i] += 1
    tabspace = tabspace[:-1]
    return flag


def ip(r, g, b):
    west = {
        'r': r,
        'g': g,
        'b': b
    }
    east = {
        'r': 0,
        'g': 0,
        'b': 0
    }
    state = "west"
    if(backtrack(west, east, state,   []) == 1):
        print(cache)


class Dialog(QDialog):

    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""

        super().__init__(parent)

        self.setWindowTitle('QDialog')
        dlgLayout = QVBoxLayout()
        self.formLayout = QFormLayout()

        self.r = QLineEdit()
        self.g = QLineEdit()
        self.b = QLineEdit()

        self.formLayout.addRow('r:', QLineEdit())
        self.formLayout.addRow('g:', QLineEdit())
        self.formLayout.addRow('b:', QLineEdit())
        dlgLayout.addLayout(self.formLayout)

        self.btns = QDialogButtonBox()
        self.btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(self.btns)

        self.btns.accepted.connect(self.OnClick)
        self.btns.rejected.connect(self.reset)
        self.setLayout(dlgLayout)

    def OnClick(self):
        print("value: "+self.r.text())
        r = 3  # int(self.r.text())
        g = 3  # int(self.g.text())
        b = 3  # int(self.b.text())
        ip(r, g, b)

    def reset(self):
        pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
