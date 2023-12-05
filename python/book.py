class SQL:

    seq = 0

    def create(self, table_name="books", *args, **kwargs):
        print("Creando registro nuevo")
        print(table_name)
        print(args)
        print(kwargs)
        SQL.seq += 1
        return SQL.seq

    def update(self, record_id, table_name="books", *args, **kwargs):
        print(f"Actulizando {table_name} con id: {record_id}")
        print(f"Valores: {args}")
        print(kwargs)

    def list(self, table_name="books"):
        print(f"Lista de {table_name}")

    def retrieve(self, record_id, table_name="books"):
        print(f"Se obtiene {record_id} desde {table_name}")

    def delete(self, record_id, table_name="books"):
        print(f"Se elimino {record_id} desde {table_name}")


class Book:
    """Aquí implementar la clase"""

    def __init__(self, SQL, title, author, year):
        self.SQL = SQL
        self.record_id = None
        self.title = title
        self.author = author
        self.year = year

    def save_in_db(self):
        self.record_id = self.SQL.create(
            "books", self.title, author=self.author, year=self.year)

    def update_db(self, title=None, author=None, year=None):
        if not self.record_id:
            print("No se puede actualizar un registro sin id")
            return
        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year
        self.SQL.update(self.record_id, 'books',
                        self.title, self.author, year=self.year)


sql = SQL()
book = Book(sql, "El Principito", "Antoine de Saint Exupery", 1943)
book_2 = Book(sql, "Moby Dick", "Herman Melville", 1851)

book.save_in_db()
book.update_db(author="Juan Perez")


book_2.update_db(author="Armando Paredes")
book_2.save_in_db()
book_2.update_db(author="Armando Paredes")
