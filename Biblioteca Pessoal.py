from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import*
import sys
import sqlite3
import time
import os

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.setWindowIcon(QIcon('icon/booksicon.png'))
        self.QBtn = QPushButton()
        self.QBtn.setText('Registrar: ')

        self.setWindowTitle("Add Aluno: ")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Dados do Livro: ")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.addLivro)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText('Nome')
        layout.addWidget(self.nameinput)

        self.generoinput = QComboBox()
        self.generoinput.addItem("Artes")
        self.generoinput.addItem("Autoajuda")
        self.generoinput.addItem("Aventura")
        self.generoinput.addItem("Ciências")
        self.generoinput.addItem("Contos")
        self.generoinput.addItem("Dicionário")
        self.generoinput.addItem("Diversos")
        self.generoinput.addItem("Fantasia")
        self.generoinput.addItem("Ficção Ciêntifica")
        self.generoinput.addItem("Filosofia")
        self.generoinput.addItem("História")
        self.generoinput.addItem("Humor")
        self.generoinput.addItem("Infanto Juvenil")
        self.generoinput.addItem("Linguistica")
        self.generoinput.addItem("Poesia")
        self.generoinput.addItem("Policial")
        self.generoinput.addItem("Programação")
        self.generoinput.addItem("Regimes")
        self.generoinput.addItem("Sociologia")
        self.generoinput.addItem("Suspense")
        self.generoinput.addItem("Terror")
        layout.addWidget(self.generoinput)

        self.autorinput = QLineEdit()
        self.autorinput.setPlaceholderText('Autor')
        layout.addWidget(self.autorinput)

        self.midiainput = QComboBox()
        self.midiainput.addItem("Livro Fisico")
        self.midiainput.addItem("Ebook")
        layout.addWidget(self.midiainput)

        self.editorainput = QLineEdit()
        self.editorainput.setPlaceholderText('Editora')
        layout.addWidget(self.editorainput)

        self.comentarioinput = QLineEdit()
        self.comentarioinput.setPlaceholderText('Comentario')
        layout.addWidget(self.comentarioinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addLivro(self):
        name = ''
        genero = ''
        autor = -1
        midia = ''
        editora = ''
        comentario = ''

        name = self.nameinput.text()
        genero = self.generoinput.itemText(self.generoinput.currentIndex())
        autor = self.autorinput.text()
        midia = self.midiainput.itemText(self.midiainput.currentIndex())
        editora = self.editorainput.text()
        comentario = self.comentarioinput.text()
        try:
            self.conn = sqlite3.connect('databaseBiblio.db')
            self.c = self.conn.cursor()
            self.c.execute('INSERT INTO biblioteca (Nome,Genero,Autor,Midia,Editora,Comentario)VALUES (?,?,?,?,?,?)', (name, genero, autor, midia, editora, comentario))

            self.conn.commit()
            self.c.close()
            self.conn.close()

            QMessageBox.information(QMessageBox(), 'Cadastro', 'LIVRO CADASTRADO COM SUCESSO, ATUALIZE A BIBLIOTECA')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'anfisope10@hotmIL.com', 'Não foi possivel realizar seu cadastro')



class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/booksicon.png'))
        self.QBtn = QPushButton()
        self.QBtn.setText('Pesquisar: ')

        self.setWindowTitle("Pesquisar Livro: ")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.QBtn.clicked.connect(self.searchLivro)

        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText('Inscrição ')
        layout.addWidget(self.searchinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchLivro(self):
        searchrol = ''
        searchrol = self.searchinput.text()


        try:
            self.conn = sqlite3.connect('databaseBiblio.db')
            self.c = self.conn.cursor()
            result = self.c.execute('SELECT * from biblioteca WHERE roll =' + str(searchrol))
            row = result.fetchone()
            searchresult = 'INSCRICAO: '+str(row[0])+'\n'+'NOME : '+str(row[1])+'\n'+'GÊNERO : '+str(row[2])+'\n'+'AUTOR : '+str(row[3])+'\n'+'MIDIA : '+str(row[4])+'\n'+'EDITORA : '+str(row[5])+'\n'+'COMENTARIOS : '+str(row[6])
            QMessageBox.information(QMessageBox(), 'Sucesso na pesquisa', searchresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'anfisope10@hotmIL.com', 'Sua pesquisa não foi encontrada')

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText('Deletar: ')

        self.setWindowTitle("Deletar Inscricao: ")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.QBtn.clicked.connect(self.deleteLivro)

        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText('Delete ')
        layout.addWidget(self.deleteinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deleteLivro(self):
        delrol = ''
        delrol = self.deleteinput.text()

        try:
            self.conn = sqlite3.connect('databaseBiblio.db')
            self.c = self.conn.cursor()
            self.c.execute('DELETE from biblioteca WHERE roll =' + str(delrol))

            self.conn.commit()
            self.c.close()
            self.conn.close()

            QMessageBox.information(QMessageBox(), 'anfisope10@hotmail.com', 'DELETADO COM SUCESSO')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'anfisope10@hotmIL.com', 'Não foi possivel deletar')
class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/booksicon.png'))
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.accepted.connect(self.reject)

        layout = QVBoxLayout()


        self.setWindowTitle("Sobre")
        title = QLabel('Biblioteca Pessoal')
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/san.png')
        pixmap = pixmap.scaledToWidth(275)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)

        layout.addWidget(QLabel('V1.0'))
        layout.addWidget(QLabel("Sistema da Computação UFF"))
        layout.addWidget(QLabel("Copyright AndersonFSP 2019"))
        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/booksicon.png'))
        #Conexão BANCO DE DADOS#
        self.conn = sqlite3.connect('databaseBiblio.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS biblioteca(roll INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT, Genero TEXT, Autor TEXT, Midia TEXT, Editora TEXT, Comentario TEXT)")
        self.c.close()

        fileMenu = self.menuBar().addMenu('&File')
        help_menu = self.menuBar().addMenu('&Sobre')
        self.setWindowTitle('BIBLIOTECA PESSOAL')
        self.setMinimumSize(840, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(('Inscrição No', 'Nome', 'Gênero', 'Autor', 'Midia', 'Editora','Comentarios Sobre a Obra'))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add1.jpg"), "Adicionar livro", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Adicionar Livros")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("icon/atuali.jpg"), "Atualizar dados", self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Atualizar Dados")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/search.png"), "Pesquisar por livro", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Pesquisar Livros")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icon/delete.png"), "Deletar cadastro", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.triggered.connect(self.loaddata)
        btn_ac_delete.setStatusTip("Deletar livros")
        toolbar.addAction(btn_ac_delete)

        #######################################
        adduser_action = QAction(QIcon("icon/add1.jpg"), "Adicionar livro", self)
        adduser_action.triggered.connect(self.insert)
        fileMenu.addAction(adduser_action)

        searchuser = QAction(QIcon("icon/search.png"), "Pesquisar ", self)
        searchuser.triggered.connect(self.search)
        fileMenu.addAction(searchuser)

        deluser = QAction(QIcon("icon/delete.png"), "Deletar cadastro", self)
        deluser.triggered.connect(self.delete)
        fileMenu.addAction(deluser)
        #######################################

        about_action = QAction(QIcon("icon/about.png"), "Desenvolvedor", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):
        self.connection = sqlite3.connect('databaseBiblio.db')
        query = 'SELECT * FROM biblioteca'
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for columm_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, columm_number, QTableWidgetItem(str(data)))
        self.connection.close()
    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

app = QApplication(sys.argv)
if(QDialog.Accepted == True):
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())

