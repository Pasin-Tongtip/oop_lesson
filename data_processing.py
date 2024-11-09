class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        name = self.search(table.table_name)
        if name is None:
            self.table_database.append(table)

    def search(self, table_name):
        for table in range(len(self.table_database)):
            if self.table_database[table].table_name == table_name:
                return table
        return None


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        # dont understand krub🥹


    def aggregate(self, aggregation_function, aggregation_key):
        # dont know what to do krub🥹

    def __str__(self):
        # ???😭
