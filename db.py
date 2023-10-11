import sqlite3
import random
import string

class Database:
    def __init__(self, db_file):
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
          with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))
                
    def add_user(self, user_id, referer_id=None):
        with self.connection:
            if referer_id is not None:
                # Начисляем пользователю 2 рубля
                self.cursor.execute("INSERT INTO `users` (`user_id`, `referer_id`, `balance`) VALUES (?,?,2)", (user_id, referer_id))
                
                # Увеличиваем баланс реферера на 2 рубля
                self.cursor.execute("UPDATE `users` SET `balance` = `balance` + 2 WHERE `user_id` = ?", (referer_id,))
                
                self.connection.commit()
            else:
                # Начисляем пользователю 1 рубль
                self.cursor.execute("INSERT INTO `users` (`user_id`, `balance`) VALUES (?,1)", (user_id,))
                self.connection.commit()

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT `user_id`, `active` FROM `users`").fetchall()
  
    def get_user_balance(user_id):
            # Подключение к базе данных
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

            # Выполнение SQL-запроса для получения баланса
        cursor.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
            
            # Извлечение баланса из результата запроса
        result = cursor.fetchone()

            # Закрытие соединения с базой данных
        connection.close()

            # Если пользователь существует, возвращаем его баланс, иначе возвращаем None
        return result[0] if result is not None else None
    
    def generate_ton_address(self):
    # Длина TON-подобного адреса
        length=64
        characters = string.ascii_lowercase + string.digits
        ton_address = ''.join(random.choice(characters) for _ in range(length))
        return ton_address

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `active` = ?", (active, user_id,))

   

    def count_referer(user_id):
    # Подключение к базе данных
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # SQL-запрос для подсчета количества строк
        cursor.execute("SELECT COUNT(*) FROM users WHERE referer_id = ?", (user_id,))
        
        # Извлечение результата подсчета
        result = cursor.fetchone()

        # Закрытие соединения с базой данных
        connection.close()

        # Возвращаем количество строк (рефералов)
        return result[0] if result is not None else 0


                