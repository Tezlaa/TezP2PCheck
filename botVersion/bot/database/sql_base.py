import typing
import datetime
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
    def __init__(self, namebase: str, name_table: str):
        super().__init__(namebase)
        
        self.name_table_user = name_table
        
        tabel = f'''CREATE TABLE IF NOT EXISTS {self.name_table_user}(
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            bank TEXT,
            fiat TEXT,
            asset TEXT)'''
        
        self.cursor.execute(tabel)
        self.base.commit()
    
    def create_user(self, user_id: int, username: str):
        user = self.cursor.execute(f'SELECT 1 FROM {self.name_table_user} WHERE user_id == {user_id}').fetchone()
        if not user:
            self.cursor.execute(f'INSERT INTO {self.name_table_user} VALUES(?, ?, ?, ?, ?)',
                                (user_id, username, "empty", "empty", "empty"))
            self.base.commit()
    
    def check_parameters(self, user_id: int, parameters: str) -> bool:
        """Parameter check for emptiness

        Args:
            user_id (int): user id
            parameters (str): "bank", "fiat", "asset"

        Returns:
            bool: False: parametres empty,
                  True: have parameters
        """
        parameters = str(self.cursor.execute(
            f'SELECT {parameters} FROM {self.name_table_user} WHERE user_id == {user_id}').fetchone())
        
        if parameters == "empty":
            return False
        else:
            return True
        
    def value_parameters(self, user_id: int, parameters: str) -> str:
        """Value parameters from the database

        Args:
            user_id (int): user id
            parameters (str): "bank", "fiat", "asset"

        Raises:
            ValueError: if parameter is empty

        Returns:
            str: parameter value
        """
        validation = self.check_parameters(user_id, parameters)
        if not validation:
            raise ValueError("Parameter is empty!")
        
        value = str(self.cursor.execute(
            f'SELECT {parameters} FROM {self.name_table_user} WHERE user_id == {user_id}').fetchone())
        
        return value
    

class NotificationDatabase(TableUser):
    def __init__(self, name_table: str):
        
        self.name_table_notifi = name_table
        
        tabel = f'''CREATE TABLE IF NOT EXISTS {self.name_table_notifi}(
            user_id INTEGER PRIMARY KEY,
            notification_time INTEGER,
             TEXT)'''
        
        self.cursor.execute(tabel)
        self.base.commit()
    
    def create_notification(self, user_id: int) -> None:
        user = self.cursor.execute(f'SELECT 1 FROM {self.name_table_notifi} WHERE user_id == {user_id}').fetchone()
        if not user:
            self.cursor.execute(f'INSERT INTO {self.name_table_notifi} VALUES(?, ?,)',
                                (user_id, 0))
            self.base.commit()
            
    def get_notifacation_time(self, user_id: int) -> int:
        text_execute = f'SELECT notification_time FROM {self.name_table_notifi} WHERE user_id == {user_id}'
        return int(self.cursor.execute(text_execute).fetchone())
    
    def set_notifacation_time(self, user_id: int, time: int) -> None:
        text_execute = f'UPDATE {self.name_table_notifi} SET notification_time = ? WHERE user_id == {user_id}'
        self.cursor.execute(text_execute, str(time))
        

if __name__ == "__main__":
    pass
        