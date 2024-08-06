from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QLabel,QGridLayout,QPushButton,QVBoxLayout,QHBoxLayout

class Winner(QWidget):
        def __init__(self,winner_name) -> None:
            super().__init__()
            self.winner = winner_name
            self.setFixedSize(500,200)
            self.setStyleSheet('''
                    font-weight: bold;
                    font-size: 60px; 
                    border-radius: 20%; 
                    background: #008DDA;
        ''')
            self.hbox = QHBoxLayout()
            
            self.label2 = QLabel("Winner is  ",self)
            self.label2.setStyleSheet("font-size: 50 px; color: black;")

            self.label1 = QLabel(self.winner,self)
            self.label1.setStyleSheet("font-size: 80 px; color: red")
            


            self.hbox.addStretch()
            self.hbox.addWidget(self.label2)
            self.hbox.addWidget(self.label1)
            self.hbox.addStretch()

            self.setLayout(self.hbox)

            self.show()


class Button(QPushButton):
     def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(125,125)
        self.setStyleSheet('''
            font-weight: bold;
            font-size: 60px; 
            border: 3px solid black;
            border-radius: 20%; 
            background: #008DDA;
        ''')


class Game(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400,600)
        self.setWindowTitle("TIC_TAC_TOE")
        self.setStyleSheet("font-size: 50 px,color: black")

        self.label = QLabel("Start the game",self)
        self.label.setStyleSheet("font-size: 50px ")

        self.matrix = []
        self.grid = QGridLayout()
        self.check_turn = 1
        self.show()
        self.initUI()



    def initUI(self):
        self.create_empty_boxes()
        self.play_a_game()
        self.vbox = QVBoxLayout()
        self.vbox.addStretch()
        self.vbox.addWidget(self.label)
        



    def create_empty_boxes(self):
        index = 0

        for i in range(3):
            row = []
            for j in range(3):
                button = Button(" ")
                self.grid.addWidget(button,i,j)
                row.append(button)
                index += 1
            self.matrix.append(row)
        
       
        self.setLayout(self.grid)



    def play_a_game(self):
        for i in range(3):
            for j in range(3):
                self.matrix[i][j].clicked.connect(self.put_sign)
               

    

    def put_sign(self):
        btn = self.sender()


        for i in range(3):
            for j in range(3):
                if btn == self.matrix[i][j]:
                    if btn.text() == " " and  self.check_turn % 2 != 0:
                        self.matrix[i][j].setText("x")
                        self.check_turn += 1
                        self.label.setText("⭕️ turn")
                        if i == 0 and j == 0:
                            if self.matrix[0][1].text() == "x":
                                if self.matrix[0][2].text() == "x":
                                    print("win")

                        
                    elif btn.text() == " " and  self.check_turn % 2 == 0:
                        self.matrix[i][j].setText("0")
                        self.matrix[i][j].setStyleSheet("""
                                                        font-weight: bold;
                                                        font-size: 60px; 
                                                        border: 3px solid black;
                                                        border-radius: 20%; 
                                                        background: #008DDA;
                                                        color: red""")
                        self.label.setText("❌ turn")
                        self.check_turn += 1
        self.check_winner("0")
        self.check_winner("x")

    
    
    def new_window(self,veriable):
        self.close()
        self.window = Winner(veriable)
       



    def check_winner(self,veriable):
        a = veriable
        if self.matrix[0][0].text() == a and self.matrix[0][1].text() == a and self.matrix[0][2].text() == a:
            self.new_window(a)

        elif self.matrix[0][1].text() == a and self.matrix[1][1].text() == a and self.matrix[2][1].text() == a:
           self.new_window(a)

        elif self.matrix[0][2].text() == a and self.matrix[1][2].text() == a and self.matrix[2][2].text() == a:
           self.new_window(a)

        elif self.matrix[1][0].text() == a and self.matrix[1][1].text() == a and self.matrix[1][2].text() == a:
           self.new_window(a)

        elif self.matrix[2][0].text() == a and self.matrix[2][1].text() == a and self.matrix[2][2].text() == a:
           self.new_window(a)

        elif self.matrix[0][0].text() == a and self.matrix[1][0].text() == a and self.matrix[2][0].text() == a:
           self.new_window(a)

        elif self.matrix[0][0].text() == a and self.matrix[1][1].text() == a and self.matrix[2][2].text() == a:
           self.new_window(a)

        elif self.matrix[0][2].text() == a and self.matrix[1][1].text() == a and self.matrix[2][0].text() == a:
           self.new_window(a)
        
        

        



app = QApplication([])
window = Game()
app.exec_() 