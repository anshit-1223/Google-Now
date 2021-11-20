## Google Now 
## Browser By Anshit Verma

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import * 


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #NavBar
        navbar = QToolBar()
        self.addToolBar(navbar)          
        
        #back button
        back_btn = QAction('<-',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        
        #forward button
        forward_btn = QAction('->',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
         
        #reload_btn 
        reload_btn = QAction('⟳',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        
        #HomeButton
        home_btn = QAction('⌂',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        #Add_bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        
        self.browser.urlChanged.connect(self.update_url)
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,u):
        self.url_bar.setText(u.toString())

#Endpoint
app = QApplication(sys.argv)
QApplication.setApplicationName('Google Now')
QApplication.setWindowIcon(QIcon(QPixmap('index.png')))
window= MainWindow()
app.exec_()