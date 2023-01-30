import logging
import sqlite3


class Database():
    def __init__(self, namebase: str):
        """Connect data base
        
        Args:
            namebase (str): write name for database
                ex: "profile"
        """
        self.namebase = namebase
        self.base = sqlite3.connect(f'{namebase}.db')
        self.cursor = self.base.cursor()
        
        if self.base:
            logging.info("Database connected!")
        else:
            logging.info(self.base)
    

class TableUser(Database):
    def __init__(self, namebase: str, name_tabel: str):
        super().__init__(namebase)
        
        self.name_tabel = name_tabel
        
        tabel = f'''CREATE TABLE IF NOT EXISTS {name_tabel}(
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            bank TEXT,
            currency TEXT,
            cryptocurrency TEXT)'''
        
        self.cursor.execute(tabel)
        self.base.commit()
    
    def create_user(self, user_id: int, username: str):
        user = self.cursor.execute(f'SELECT 1 FROM {self.name_tabel} WHERE user_id == {user_id}').fetchone()
        if not user:
            self.cursor.execute(f'INSERT INTO {self.name_tabel} VALUES(?, ?, ?, ?, ?)',
                                (user_id, username, "empty", "empty", "empty"))
            self.base.commit()
    
    def check_parameters(self, user_id: int, parameters: str) -> bool:
        """Parameter check for emptiness

        Args:
            user_id (int): user id
            parameters (str): "bank", "currency", "cryptocurrency"

        Returns:
            bool: False: parametres empty,
                  True: have parameters
        """
        parameters = str(self.cursor.execute(
            f'SELECT {parameters} FROM {self.name_tabel} WHERE user_id == {user_id}').fetchone())
        
        if parameters == "empty":
            return False
        else:
            return True
        
    def value_parameters(self, user_id: int, parameters: str) -> str:
        """Value parameters from the database

        Args:
            user_id (int): user id
            parameters (str): "bank", "currency", "cryptocurrency"

        Raises:
            ValueError: if parameter is empty

        Returns:
            str: parameter value
        """
        validation = self.check_parameters(user_id, parameters)
        if not validation:
            raise ValueError("Parameter is empty!")
        
        value = str(self.cursor.execute(
            f'SELECT {parameters} FROM {self.name_tabel} WHERE user_id == {user_id}').fetchone())
        
        return value
         

if __name__ == "__main__":
    ...
        