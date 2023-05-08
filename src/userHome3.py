from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import requests
import sqlite3
import pandas as pd   
from Movirec import recommend,get_index_from
from recTopAnime import recTop1
from rec_on_rating import rec_on_top
from recTopPicks import recTop
import UpdateUser as up
class mainWindow(QMainWindow):
    df=pd.read_csv("refinedMovies.csv",index_col=0)
    def __init__(self,username,parent=None):
        super(mainWindow, self).__init__(parent)
        self.win=QWidget()
        self.username=username
        self.win.setWindowTitle(f"MovieMatch({self.username})")
        self.win.setStyleSheet("background-color:black;color:white;font-size:20")
        #Menubar defination
        self.home=QPushButton(icon=QIcon(QPixmap('home (2).png')))
        self.home.setStyleSheet('width:35px;height:35px;color:black;font-size:20px;border:1px solid white')
        self.home.clicked.connect(lambda:self.home_clicked())
        
        self.searchText=QLineEdit()
        self.searchText.setStyleSheet('background-color:white;color:black;font-size:20px')
        self.searchText.setFixedHeight(35)
        self.searchButton=QPushButton(icon=QIcon(QPixmap('search1 (2).png')))
        self.searchButton.setStyleSheet('width:35;height:35;color:black;font-size:20px;border:1px solid white')
        self.searchButton.clicked.connect(lambda:self.getSearch())
        self.profile=QPushButton(icon=QIcon(QPixmap('profile (2).png')))
        self.profile.clicked.connect(lambda checked:up.Update_User_Page(self.username))
        self.profile.setStyleSheet('height:35px;width:35;color:black;font-size:20px;border:1px solid white')
       
        #layout defination
        self.layout=QVBoxLayout()
        self.hbox=QHBoxLayout()
        
        
        #hbox styling
        self.hbox.addWidget(self.home)
        self.hbox.addWidget(self.searchText)
        self.hbox.addWidget(self.searchButton)
        self.hbox.addWidget(self.profile)
        self.layout.addLayout(self.hbox)
        
       
        #adding scroll to main window
        self.scrollArea = QScrollArea()
        self.layout.addWidget(self.scrollArea)
        self.scrollArea.setFixedHeight(2*self.win.height())
        # self.scrollArea.setLayout(self.box)
        self.scrollAreaWidgetContests =QWidget()
        self.scrollAreaWidgetContests.setGeometry(QRect(0 ,0 ,3*self.win.width(),5*self.win.height()))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.horizontalScrollBar().setDisabled(True)
        # self.scrollAreaWidgetContests.setLayout(self.box)
        # self.scrollArea.setWidgetResizable(True)
        
        self.scrollArea.setWidget((self.scrollAreaWidgetContests)) 
        self.box=self.home_clicked()
        self.scrollArea.setWidget(self.box)
        
        self.layout.addWidget(self.scrollArea)
        self.win.setLayout(self.layout)
        self.win.showMaximized()
        
    def getHomeLayout(self):
        
        w=QWidget()
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()
        hbox3=QHBoxLayout()
        hbox4=QHBoxLayout()
        hbox5=QHBoxLayout()
        box=QVBoxLayout()
        
        #button defination
        b1=QPushButton()
        b2=QPushButton()
        b3=QPushButton()
        b4=QPushButton()
        b5=QPushButton()
        
        
        
        # b1 styling 
        b1.setText("Top picks for you ->")
        b1.setStyleSheet("background-color:orange;color:black;font-size:20px;text-align:left")
        b1.setFixedHeight(30)
        
        # b2 styling 
        b2.setText("Newly Released ->")
        b2.setStyleSheet("background-color:orange;color:black;font-size:20px;text-align:left")
        b2.setFixedHeight(30)
        
        # b3 styling 
        b3.setText("Top Animes for you ->")
        b3.setStyleSheet("background-color:orange;color:black;font-size:20px;text-align:left")
        b3.setFixedHeight(30)
        
        # b4 styling 
        b4.setText("Top picks for you ->")
        b4.setStyleSheet("background-color:orange;color:black;font-size:20px;text-align:left")
        b4.setFixedHeight(30)
        
        # b5 styling 
        b5.setText("Top picks for you ->")
        b5.setStyleSheet("background-color:orange;color:black;font-size:20px;text-align:left")
        b5.setFixedHeight(30)
        
        img=QPixmap('sv1xJUazXeYqALzczSZ3O6nkH75.jpg').scaledToWidth(200)

        

        bl1=[]
        # hbox1 styling
        self.topRec=recTop(self.username)
        for i,id in enumerate(list(self.topRec)):
            if id in list(mainWindow.df.index):
                print(id)
                vbox=QVBoxLayout()
                self.btn=QPushButton()
                self.btnlbl=QLabel(text=mainWindow.df.loc[id]['title'])
                url_img = "https://image.tmdb.org/t/p/original"+mainWindow.df.loc[id]['poster_path']
                image= QImage()
                image.loadFromData(requests.get(url_img).content)
                self.btn.setIconSize(QSize(200,300))
                self.btn.setIcon(QIcon(QPixmap(image)))
                self.btn.clicked.connect(lambda checked, text=str(id) : self.button_clicked(text))
                self.btn.setFixedHeight(300)
                self.btn.setFixedWidth(200)
                self.btnlbl.setStyleSheet('font-size:14pt;color:white')
                self.btnlbl.setFixedWidth(200)
                self.btnlbl.setWordWrap(True)
                vbox.addWidget(self.btn)
                vbox.addWidget(self.btnlbl)
                hbox1.addLayout(vbox)

        bl2=[]
        # hbox2 styling
        self.rec_top=rec_on_top()
        for i,id in enumerate(list(self.rec_top)):
            if id in list(mainWindow.df.index):
                print(id)
                vbox=QVBoxLayout()
                self.btn=QPushButton()
                self.btnlbl=QLabel(text=mainWindow.df.loc[id]['title'])
                url_img = "https://image.tmdb.org/t/p/original"+mainWindow.df.loc[id]['poster_path']
                image= QImage()
                image.loadFromData(requests.get(url_img).content)
                self.btn.setIconSize(QSize(200,300))
                self.btn.setIcon(QIcon(QPixmap(image)))
                self.btn.clicked.connect(lambda checked, text=str(id) : self.button_clicked(text))
                self.btn.setFixedHeight(300)
                self.btn.setFixedWidth(200)
                self.btnlbl.setStyleSheet('font-size:14pt;color:white')
                self.btnlbl.setFixedWidth(200)
                self.btnlbl.setWordWrap(True)
                vbox.addWidget(self.btn)
                vbox.addWidget(self.btnlbl)
                hbox2.addLayout(vbox)

        bl3=[]
        # hbox3 styling
        self.topRec1=recTop1(self.username)
        for i,id in enumerate(list(self.topRec1)):
            if id in list(mainWindow.df.index):
                print(id)
                vbox=QVBoxLayout()
                self.btn=QPushButton()
                self.btnlbl=QLabel(text=mainWindow.df.loc[id]['title'])
                url_img = "https://image.tmdb.org/t/p/original"+mainWindow.df.loc[id]['poster_path']
                image= QImage()
                image.loadFromData(requests.get(url_img).content)
                self.btn.setIconSize(QSize(200,300))
                self.btn.setIcon(QIcon(QPixmap(image)))
                self.btn.clicked.connect(lambda checked, text=str(id) : self.button_clicked(text))
                self.btn.setFixedHeight(300)
                self.btn.setFixedWidth(200)
                self.btnlbl.setStyleSheet('font-size:14pt;color:white')
                self.btnlbl.setFixedWidth(200)
                self.btnlbl.setWordWrap(True)
                vbox.addWidget(self.btn)
                vbox.addWidget(self.btnlbl)
                hbox3.addLayout(vbox)

        # bl4=[]
        # # hbox4 styling
        # for i in range(15):
        #     bl4.append(QPushButton(f"button{i}"))
        #     bl4[i].setStyleSheet("color:orange;text-align:left;font-size:20")
        #     hbox4.addWidget(bl4[i])
            
        # bl5=[]
        # # hbox5 styling
        # for i in range(15):
        #     bl5.append(QPushButton(f"button{i}"))
        #     bl5[i].setStyleSheet("color:orange;text-align:left;font-size:20")
        #     hbox5.addWidget(bl5[i])
        
        
        
        
        #adding scroll to top picks hbox1
        scrollArea1 = QScrollArea()
        scrollArea1.setFixedHeight(400)
        # box.addWidget(scrollArea1)
        scrollAreaWidgetContest1 = QWidget()
        scrollAreaWidgetContest1.setGeometry(QRect(0 ,0 ,len(self.topRec)*210,400))
        scrollAreaWidgetContest1.setLayout(hbox1)
        scrollArea1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea1.setWidget(scrollAreaWidgetContest1)
        
        #adding scroll to top picks hbox2
        scrollArea2 = QScrollArea()
        scrollArea2.setFixedHeight(400)
        # box.addWidget(scrollArea1)
        scrollAreaWidgetContest2 = QWidget()
        scrollAreaWidgetContest2.setGeometry(QRect(0 ,0 ,len(self.rec_top)*210,400))
        scrollAreaWidgetContest2.setLayout(hbox2)
        scrollArea2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea2.setWidget(scrollAreaWidgetContest2)
        
        #adding scroll to top animes hbox3
        scrollArea3 = QScrollArea()
        scrollArea3.setFixedHeight(400)
        # box.addWidget(scrollArea1)
        scrollAreaWidgetContest3 = QWidget()
        scrollAreaWidgetContest3.setGeometry(QRect(0 ,0 ,len(self.topRec1)*210,400))
        scrollAreaWidgetContest3.setLayout(hbox3)
        scrollArea3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea3.setWidget(scrollAreaWidgetContest3)
        
        #setLayout 
        box.addWidget(b1)
        box.addWidget(scrollArea1)
        box.addWidget(b2)
        box.addWidget(scrollArea2)
        box.addWidget(b3)
        box.addWidget(scrollArea3)
        # box.addWidget(b4)
        # box.addLayout(hbox4)
        # box.addWidget(b5)
        # box.addLayout(hbox5)
        w.setLayout(box)
        return w
        
        
    df=pd.read_csv('refinedMovies.csv',sep=',',index_col=0)
    def getLayout(self,id,parent=None):
        win=QWidget()
        win.setStyleSheet('background-color:black')
        winLayout=QVBoxLayout()
        self.layout=QHBoxLayout()
        
        self.l1=['title','genres','overview','production_companies','release_date','credits','runtime']
        self.l2=[]
        self.l3=[]
        self.l4=[]

        self.d=dict(mainWindow.df.loc[id])
        url_img = "https://image.tmdb.org/t/p/original"+self.d['poster_path']
        image= QImage()
        image.loadFromData(requests.get(url_img).content)
        self.img=QPixmap(image).scaledToHeight(int(3*win.height()/2)+int(win.height()/2)-350)
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

        con=sqlite3.connect("userRating.db")
        cur=con.cursor()
        cur.execute(f"select rating from userMovieRating where username='{self.username}' and  movieID={id}")
        res=cur.fetchone()
        if res==None:
            self.rating=1
        else:
            self.rating=int(res[0])
        
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
        self.set_rating(self.rating)
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
        self.submit_button.clicked.connect(lambda checked, text=id : self.submit_rating(text))

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
            if int(s) in list(mainWindow.df.index):
                print(s)
                vbox=QVBoxLayout()
                self.btn=QPushButton()
                self.btnlbl=QLabel(text=self.rec[s])
                url_img = "https://image.tmdb.org/t/p/original"+mainWindow.df.loc[int(s)]['poster_path']
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
        

        #review scrollpane
        self.scrollArea1 = QScrollArea()
        self.scrollArea1.setFixedHeight(350)
        # scrollArea1.setLayout(hbox1)
        self.scrollAreaWidgetContest1 = QWidget()
        self.scrollAreaWidgetContest1.setGeometry(QRect(0 ,0 ,len(self.rec)*210,450))
        self.scrollAreaWidgetContest1.setLayout(self.vbox1)
        self.scrollArea1.setWidget(self.scrollAreaWidgetContest1)
        
        #vbox scrollArea
        self.scrollArea2 = QScrollArea()
        # self.scrollArea2.setFixedHeight(int(win.height()/2))
        #scrollArea1.setLayout(vbox)
        self.scrollAreaWidgetContest2 = QWidget()
        self.scrollAreaWidgetContest2.setGeometry(QRect(0 ,0 ,int(2*win.width()),int(3*win.height()/2)))
        self.scrollAreaWidgetContest2.setLayout(self.vbox)
        self.scrollArea2.setWidget(self.scrollAreaWidgetContest2)


        self.layout.addWidget(self.imgLabel)
        self.layout.addWidget(self.scrollArea2)
        winLayout.addLayout(self.layout)
        winLayout.addWidget(self.recLabel)
        winLayout.addWidget(self.scrollArea1)
        win.setLayout(winLayout)
        return win
        # self.win.showMaximized()
        
    def getSearch(self):
        win=QWidget()
        vbox=QVBoxLayout()
        movie=self.searchText.text()
        ls=[]
        for i in mainWindow.df['title']:
            if str.lower(i).__contains__(str.lower(movie)):
                index=get_index_from(mainWindow.df,str(i))
                ls.append(int(index))
                
        print(ls)
        if len(ls)>0:
            grid=QGridLayout()

            j=0
            for z,s in enumerate(ls):
                if s in mainWindow.df.index and z<50:
                        
                    vbox=QVBoxLayout()
                    btn=QPushButton()
                    btnlbl=QLabel(mainWindow.df.loc[s]['title'])
                    url_img = "https://image.tmdb.org/t/p/original"+mainWindow.df.loc[s]['poster_path']
                    image= QImage()
                    image.loadFromData(requests.get(url_img).content)
                    btn.setIconSize(QSize(200,300))
                    btn.setIcon(QIcon(QPixmap(image)))
                    btn.clicked.connect(lambda checked, text=str(s) : self.button_clicked(text))
                    btn.setFixedHeight(300)
                    btn.setFixedWidth(200)
                    btnlbl.setStyleSheet('font-size:14pt;color:white')
                    btnlbl.setFixedWidth(200)
                    btnlbl.setWordWrap(True)
                    vbox.addWidget(btn)
                    vbox.addWidget(btnlbl)
                    print(s)
                    if z%5==0:
                        j+=1
                        grid.addLayout(vbox,j,(z+1 if z<5 else z%5+1))
                    else:
                        grid.addLayout(vbox,j,(z+1 if z<5 else z%5+1))
                                
            win.setLayout(grid)
            win.setFixedHeight(10*500 if len(ls)>50 else (len(ls)//5+1)*500)
        else:
            label=QLabel("Movie Not Found...")
            label.setStyleSheet("color:white;background-color:black;font-size:40px;font-family:Lora")
            hbox=QHBoxLayout()
            hbox.addWidget(label)
            win.setLayout(hbox)
        win.setFixedWidth(int(self.win.width()))
        self.scrollArea.setWidget(win)
                    
             
           
            
        
    def home_clicked(self):
        
        print("a")
        self.box=self.getHomeLayout()
        self.box.setFixedHeight(1500)
        self.box.setFixedWidth(1920)
        self.scrollArea.setWidget(self.box)
        
    def button_clicked(self,id):
        print('a')
        # box=QVBoxLayout()
        # self.scrollArea.setLayout(box)
        
        self.box=self.getLayout(int(id))
        self.box.setFixedHeight(self.scrollArea.height())
        self.box.setFixedWidth(self.scrollArea.width())
        self.scrollArea.setWidget(self.box)
        print("b")
        
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

    def submit_rating(self,id):
        con=sqlite3.connect('userRating.db')
        cur=con.cursor()
        cur.execute(f"delete from userMovieRating where username='{self.username}' and movieID={id}")
        cur.execute('INSERT INTO userMovieRating(username,movieID,rating) VALUES(?,?,?)',(self.username,id,self.rating))
        con.commit()
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
# w=mainWindow('sanketdalvi362@gmail.com')
# sys.exit(App.exec_())