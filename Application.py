import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

# importing database
import sqlite3
db = sqlite3.connect("RvetDatabase.db")
cur = db.cursor()

from pages.Customers import CustomerHandler
from pages.Products import ProductHandler
from pages.ProductCategories import CategoryHandler

class Home(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        # loading the ui file created/ designed
        uic.loadUi("ui/dashboard2.ui",self)
        # click events
        self.customersButton.clicked.connect(self.hide)
        self.productsButton.clicked.connect(self.hide)

class ApplicationHandler():
    def __init__(self, parent=None):
        # creating objects of the needed classes
        self.home = Home()
        self.customerHandler = CustomerHandler()
        self.productHandler = ProductHandler()
        self.categoryHandler = CategoryHandler()
        # initializing the Home Page
        self.home.show()
        # registering click events
        # home
        self.home.customersButton.clicked.connect(self.initCustomers)
        self.home.productsButton.clicked.connect(self.initProducts)
    def initCustomers(self):
        self.customerHandler.start()
        # registering customer click events
        self.customerHandler.customersInterface.homeButton.clicked.connect(self.home.show)
        self.customerHandler.customersInterface.productsButton.clicked.connect(self.initProducts)
    def initProducts(self):
        self.productHandler.start()
        # registering product click events
        self.productHandler.productsInterface.homeButton.clicked.connect(self.home.show)
        self.productHandler.productsInterface.customersButton.clicked.connect(self.initCustomers)
        self.productHandler.productsInterface.allCategoriesButton.clicked.connect(self.initCategories)
    def initCategories(self):
        self.categoryHandler.start()
        # registering categories click events
        self.categoryHandler.categoriesInterface.homeButton.clicked.connect(self.home.show)
        self.categoryHandler.categoriesInterface.customersButton.clicked.connect(self.initCustomers)
        self.categoryHandler.categoriesInterface.productsButton.clicked.connect(self.initProducts)
        self.categoryHandler.categoriesInterface.allProductsButton.clicked.connect(self.initProducts)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationHandler()
    # app.setStyleSheet(stylesheet)
    app.setQuitOnLastWindowClosed(True)
    app.exec_()