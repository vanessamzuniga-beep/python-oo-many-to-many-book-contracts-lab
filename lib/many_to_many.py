class Author:
    # Attribute
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # Methods
    def contracts(self):
        related_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                related_contracts.append(contract)
        return related_contracts 

    def books(self):
        related_books = []
        for contract in self.contracts():
            related_books.append(contract.book) 
        return related_books

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties) 
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts()) 


class Book:
    # Attribute
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    # Methods
    # Returns a list of related contracts
    def contracts(self):
        related_contracts = []
        for contract in Contract.all:
            if contract.book == self:
                related_contracts.append(contract)
        return related_contracts

    # Returns a list of related authors
    def authors(self):
        related_authors = []
        for contract in self.contracts():
            related_authors.append(contract.author)
        return related_authors
        


class Contract:
    # Attribute
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of the Author class")
        else:
            self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("book must be an instance of the Book class")
        else:
            self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("date must be a string")
        else:
            self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise TypeError("royalties must be an integer")
        else:
            self._royalties = value


    # Methods
    @classmethod
    def contracts_by_date(cls, date):
        same_date = []
        for contract in cls.all:
            if contract.date == date:
                same_date.append(contract)
        return same_date