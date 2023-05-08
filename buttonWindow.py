from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
import requests
from Movirec import recommend
import sqlite3
import sys
class ButtonWindow(QMainWindow):
    df=pd.read_csv('refinedMovies.csv',sep=',',index_col=0)
    def getLayout(self,id,parent=None):
        super(ButtonWindow, self).__init__(parent)
        self.win=QWidget()
        self.win.setStyleSheet('background-color:black')
        self.winLayout=QVBoxLayout()
        self.layout=QHBoxLayout()
        
        self.l1=['title','genres','overview','production_companies','release_date','credits','runtime']
        self.l2=[]
        self.l3=[]
        self.l4=[]

        self.d=dict(ButtonWindow.df.loc[id])
        url_img = "https://image.tmdb.org/t/p/original"+self.d['poster_path']
        image= QImage()
        image.loadFromData(requests.get(url_img).content)
        self.img=QPixmap(image).scaledToHeight(int(3*self.win.height()/2)+int(self.win.height()/2)-300)
        self.imgLabel=QLabel()
        self.imgLabel.setAlignment(Qt.AlignCenter)
        self.imgLabel.setPixmap(self.img)

        for key in self.l1:
            if key=='credits':
                i=0
                cast=(self.d[key].split(sep='-'))
                self.label=QLabel(','.join(cast[0:(15 if len(cast)>15 else len(cast))]))
            elif key=='runtime':
                self.label=QLabel(str(self.d[key])+'min')
            else:
                self.label=QLabel(self.d[key])
            self.label.setStyleSheet('font-size:12pt ; color:white')
            self.label.setAlignment(Qt.AlignJustify)
            self.label.setWordWrap(True)
            self.l4.append(self.label)

        self.l3=['Title:','Genres:','Overview:','Production Studio:','Release Date:','Cast and Crew:','Runtime:']
        for i in self.l3:
            self.label=QLabel(i)
            self.label.setStyleSheet('font-size:14pt; color:white')
            self.l2.append(self.label)


        self.hbox=[]
        self.vbox=QFormLayout()
        for i in range(len(self.l3)):
            
            self.vbox.addRow(self.l2[i],self.l4[i])

        self.rating=1
        # Create a layout for the stars
        self.star_layout = QHBoxLayout()
        # Create radio buttons for each star
        self.star1_button = QPushButton()
        self.star1_button.setFixedSize(50,50)
        self.star1_button.setIcon(QIcon('unCheckedStar.jpeg'))
        self.star1_button.setIconSize(QSize(50, 50))
        self.star1_button.clicked.connect(lambda: self.set_rating(1))
        self.star2_button = QPushButton()
        self.star2_button.setFixedSize(50,50)
        self.star2_button.setIcon(QIcon('unCheckedStar.jpeg'))
        self.star2_button.setIconSize(QSize(50, 50))
        self.star2_button.clicked.connect(lambda: self.set_rating(2))
        self.star3_button = QPushButton()
        self.star3_button.setFixedSize(50,50)
        self.star3_button.setIcon(QIcon('unCheckedStar.jpeg'))
        self.star3_button.setIconSize(QSize(50, 50))
        self.star3_button.clicked.connect(lambda: self.set_rating(3))
        self.star4_button = QPushButton()
        self.star4_button.setFixedSize(50,50)
        self.star4_button.setIcon(QIcon('unCheckedStar.jpeg'))
        self.star4_button.setIconSize(QSize(50, 50))
        self.star4_button.clicked.connect(lambda: self.set_rating(4))
        self.star5_button = QPushButton()
        self.star5_button.setFixedSize(50,50)
        self.star5_button.setIcon(QIcon('unCheckedStar.jpeg'))
        self.star5_button.setIconSize(QSize(50, 50))
        self.star5_button.clicked.connect(lambda: self.set_rating(5))
        self.set_rating()
        # Add stars to the layout
        self.star_layout.addWidget(self.star1_button)
        self.star_layout.addWidget(self.star2_button)
        self.star_layout.addWidget(self.star3_button)
        self.star_layout.addWidget(self.star4_button)
        self.star_layout.addWidget(self.star5_button)

        # Create a layout for the button
        self.button_layout = QVBoxLayout()

       

        # Create a button to submit the rating
        self.submit_button = QPushButton('Submit')
        self.submit_button.setStyleSheet('background-color:orange')
        self.submit_button.clicked.connect(self.submit_rating)

        # Add the submit button to the button layout
        self.button_layout.addLayout(self.star_layout)
        self.button_layout.addWidget(self.submit_button)
        
        self.rateLabel=QLabel('Rate It:')
        self.rateLabel.setStyleSheet('font-size:14pt; color:white')
        
        self.vbox.addRow(self.rateLabel,self.button_layout)
        

        self.recLabel=QLabel('You may also Like:')
        self.recLabel.setStyleSheet('font-size:16pt;color:white')
        self.vbox1=QHBoxLayout() 
        self.rec=recommend(self.d['title'])
        for i,s in enumerate(list(self.rec.keys())):
            if int(s) in list(ButtonWindow.df.index):
                vbox=QVBoxLayout()
                self.btn=QPushButton()
                self.btnlbl=QLabel(text=self.rec[s])
                url_img = "https://image.tmdb.org/t/p/original"+ButtonWindow.df.loc[int(s)]['poster_path']
                image= QImage()
                image.loadFromData(requests.get(url_img).content)
                self.btn.setIconSize(QSize(200,300))
                self.btn.setIcon(QIcon(QPixmap(image)))
                self.btn.clicked.connect(lambda checked, text=s : self.button_clicked(text))
                self.btn.setFixedHeight(300)
                self.btn.setFixedWidth(200)
                self.btnlbl.setStyleSheet('font-size:14pt;color:white')
                self.btnlbl.setFixedWidth(200)
                self.btnlbl.setWordWrap(True)
                vbox.addWidget(self.btn)
                vbox.addWidget(self.btnlbl)
                self.vbox1.addLayout(vbox)

        #buttun actions
        # self.ls=[]
        # self.i=0
        # for key in self.l5.keys():
        #         self.ls.append(key)
        #         k=0
        #         k+=1
        #         while(self.ls.pop(len(self.ls)-1)==key):
        #             self.l5[key].clicked.connect(lambda:self.button_clicked(b=self.l5[key]))
        #             break
        # self.l5[self.ls[self.i]].clicked.connect(lambda:self.button_clicked(b=self.ls[self.i]))
        

        #review scrollpane
        self.scrollArea1 = QScrollArea()
        self.scrollArea1.setFixedHeight(300)
        # scrollArea1.setLayout(hbox1)
        self.scrollAreaWidgetContest1 = QWidget()
        self.scrollAreaWidgetContest1.setGeometry(QRect(0 ,0 ,len(self.rec)*210,450))
        self.scrollAreaWidgetContest1.setLayout(self.vbox1)
        self.scrollArea1.setWidget(self.scrollAreaWidgetContest1)
        
        #vbox scrollArea
        self.scrollArea2 = QScrollArea()
        # self.scrollArea2.setFixedHeight(int(self.win.height()/2))
        #scrollArea1.setLayout(vbox)
        self.scrollAreaWidgetContest2 = QWidget()
        self.scrollAreaWidgetContest2.setGeometry(QRect(0 ,0 ,int(2*self.win.width()),int(3*self.win.height()/2)))
        self.scrollAreaWidgetContest2.setLayout(self.vbox)
        self.scrollArea2.setWidget(self.scrollAreaWidgetContest2)


        self.layout.addWidget(self.imgLabel)
        self.layout.addWidget(self.scrollArea2)
        self.winLayout.addLayout(self.layout)
        self.winLayout.addWidget(self.recLabel)
        self.winLayout.addWidget(self.scrollArea1)
        self.win.setLayout(self.winLayout)
        return self.win
        # self.win.showMaximized()
    def button_clicked(self,b):
        
        return self.getLayout(int(b))
        
        # self.win.close()

    def set_rating(self, rating=1):
        self.rating=rating
        # Set the icon for each star based on the selected rating
        if rating >= 1:
            self.star1_button.setIcon(QIcon('checkedStar.jpeg'))
        else:
            self.star1_button.setIcon(QIcon('unCheckedStar.jpeg'))
        if rating >= 2:
            self.star2_button.setIcon(QIcon('checkedStar.jpeg'))
        else:
            self.star2_button.setIcon(QIcon('unCheckedStar.jpeg'))
        if rating >= 3:
            self.star3_button.setIcon(QIcon('checkedStar.jpeg'))
        else:
            self.star3_button.setIcon(QIcon('unCheckedStar.jpeg'))
        if rating >=4:
            self.star4_button.setIcon(QIcon('checkedStar.jpeg'))
        else:
            self.star4_button.setIcon(QIcon('unCheckedStar.jpeg'))
        if rating >=5:
            self.star5_button.setIcon(QIcon('checkedStar.jpeg'))
        else:
            self.star5_button.setIcon(QIcon('unCheckedStar.jpeg'))

    def submit_rating(self):
        self.showdialog(self.rating)
        
    def showdialog(self,rate):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(self.d['title'])
        msg.setInformativeText("You rated {} stars.".format(rate))
        msg.setWindowTitle("Rating")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

        
# App=QApplication(sys.argv)
# win=QWidget()
# w=ButtonWindow()
# layout=w.getLayout(505642)
# win.setLayout(layout)
# sys.exit(App.exec_())