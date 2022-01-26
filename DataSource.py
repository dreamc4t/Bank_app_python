
class DataSource:

    def __init__(self, path_t, path_c):
        self.path_transactions = path_t
        self.path_customers = path_c



    def datasource_conn(self, datasource):
        connected = True
        connection_tuple = tuple((connected, datasource))
        return connection_tuple

    def get_all(self):
        print('data')

    def update_by_id(self, id):
        print('data')

    def find_by_id(self, id):
        print('data')

    def remove_by_id(self, id):
        print('data')


