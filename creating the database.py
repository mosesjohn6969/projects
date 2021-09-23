import sqlite3

db = sqlite3.connect("RvetDatabase.db")

# creating the categories table
# db.execute("CREATE table Categories (CategoryId INTEGER PRIMARY KEY, Category VARCHAR, Description VARCHAR NULL, Status VARCHAR, LastUpdate DATETIME DEFAULT CURRENT_TIMESTAMP)")
# db.execute("DROP TABLE IF EXISTS Customers")

# creating the products table
# db.execute("CREATE table Products (ProductId INTEGER PRIMARY KEY, CategoryId INTEGER, Product VARCHAR, UnitPrice DOUBLE, Content VARCHAR NULL, Description VARCHAR NULL, Image VARCHAR NULL, Stock INTEGER NULL, BarcodeNo VARCHAR UNIQUE NULL, Status VARCHAR NULL, LastUpdate DATETIME DEFAULT CURRENT_TIMESTAMP)")

# creating the Customers table
# db.execute("CREATE table Customers (CustomerId INTEGER PRIMARY KEY, FirstName VARCHAR, LastName VARCHAR, Gender VARCHAR, PhoneNo VARCHAR UNIQUE, Address VARCHAR NULL, Email VARCHAR UNIQUE NULL, Password VARCHAR NULL, AccountBalance DOUBLE NULL, IdentityNumber VARCHAR NULL, Status VARCHAR NULL, DateAdded DATETIME DEFAULT CURRENT_TIMESTAMP)")

# creating the Transactions table
# db.execute("CREATE table Transactions (TransactionId INTEGER PRIMARY KEY, CustomerId INTEGER, AmountTotal DOUBLE NULL, PaymentMethod VARCHAR NULL, TransactionPortal VARCHAR NULL, Status VARCHAR NULL, TransactionDate DATETIME DEFAULT CURRENT_TIMESTAMP)")

# creating the Sales table
# db.execute("CREATE table Sales (SaleId INTEGER PRIMARY KEY, TransactionId INTEGER, ProductId INTEGER, Quantity INTEGER, UnitPrice DOUBLE, TotalPrice DOUBLE NULL, Status VARCHAR NULL)")

# creating the Inventory table
# db.execute("CREATE table Inventory (EntryId INTEGER PRIMARY KEY, ProductId INTEGER, Quantity INTEGER, UnitPrice DOUBLE, Status VARCHAR NULL, DateAdded DATETIME DEFAULT CURRENT_TIMESTAMP)")