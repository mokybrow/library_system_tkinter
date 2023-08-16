from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as mb
import sqlite3
import customtkinter
from datetime import date
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from collections import defaultdict
import re

root = customtkinter.CTk()
root.geometry('400x300')
root.title("Библиотечная система")


def admin():
    def password():
        if login_etry.get() == 'admin':
            toplevel3.destroy()
            root.geometry('1250x600')
            root.resizable(False, False)
            global cal, values, table_book, values_book, choose_take_day, entry_book_search, serch_farme, frame, nightmode_frame, btn_frame, entry_name, entry_surname, choose_type, choose_sex, last_lookup
            global values, conn, cur, switch_1, table, file_counter, registr_frame, all_result, checks, cal, take_book_frame, values_book, table_book, triple_request, table_info, values_status, entry_search, selections

            values = ()
            all_result = []
            checks = []
            values_book = ()
            triple_request = []
            values_status = ()
            last_lookup = ""
            selections = defaultdict(list)

            def search_user():
                global user_etry, table_info, last_lookup, selections, triple_request, user_etry, show_info_frame
                cur.execute("""
                                                SELECT  orders.orderid, users.username, users.usertype,  books.title, orders.start_date, orders.end_date, orders.status, books.number FROM orders
                                                LEFT JOIN users ON users.userid = orders.userid
                                                LEFT JOIN books ON books.bookid = orders.bookid; 
                                                """)

                triple_request = cur.fetchall()
                d = [item for item in triple_request if item[1] == user_etry.get()]
                if user_etry.get() != '':
                    if (re.search('[А-Я а-я]', user_etry.get())):
                        if d:
                            for item in table_info.get_children():
                                table_info.delete(item)
                            d = [item for item in triple_request if item[1] == user_etry.get()]
                            for row in d:
                                table_info.insert('', END, values=row)
                            user_etry.delete(0, END)
                        else:
                            for item in table_info.get_children():
                                table_info.delete(item)
                            for row in triple_request:
                                table_info.insert('', END, values=row)
                            user_etry.delete(0, END)
                            mb.showinfo('Внимание!', 'Такого Пользователя не существует!')
                    else:
                        user_etry.delete(0, END)
                        mb.showerror('Внимание!', 'Вы ввели недопустимые символы!')
                else:
                    user_etry.delete(0, END)
                    mb.showerror('Внимание!', 'Вы не заполнили поле!')

            def search_title():
                global user_etry, table_info, last_lookup, selections, triple_request, user_etry, show_info_frame, title_etry
                cur.execute("""
                                                SELECT  orders.orderid, users.username, users.usertype,  books.title, orders.start_date, orders.end_date, orders.status, books.number FROM orders
                                                LEFT JOIN users ON users.userid = orders.userid
                                                LEFT JOIN books ON books.bookid = orders.bookid; 
                                                """)

                triple_request = cur.fetchall()
                d = [item for item in triple_request if item[3] == title_etry.get()]
                if title_etry.get() != '':
                    if (re.search('[А-Я а-я]', title_etry.get())):
                        if d:
                            for item in table_info.get_children():
                                table_info.delete(item)
                            d = [item for item in triple_request if item[3] == title_etry.get()]
                            for row in d:
                                table_info.insert('', END, values=row)
                            title_etry.delete(0, END)
                        else:
                            for item in table_info.get_children():
                                table_info.delete(item)
                            for row in triple_request:
                                table_info.insert('', END, values=row)
                            title_etry.delete(0, END)
                            mb.showinfo('Внимание!', 'Эту книгу не брали!')
                    else:
                        title_etry.delete(0, END)
                        mb.showerror('Внимание!', 'Вы ввели недопустимые символы!')
                else:
                    mb.showerror('Внимание!', 'Вы не заполнили поле!')

            def search_usertype():
                global user_etry, table_info, last_lookup, selections, triple_request, user_etry, show_info_frame, title_etry, choose_usertype
                cur.execute("""
                                                SELECT  orders.orderid, users.username, users.usertype,  books.title, orders.start_date, orders.end_date, orders.status, books.number FROM orders
                                                LEFT JOIN users ON users.userid = orders.userid
                                                LEFT JOIN books ON books.bookid = orders.bookid; 
                                                """)

                triple_request = cur.fetchall()
                d = [item for item in triple_request if item[2] == choose_usertype.get()]
                if choose_usertype.get() != 'Род деятельности':
                    if d:
                        for item in table_info.get_children():
                            table_info.delete(item)
                        d = [item for item in triple_request if item[2] == choose_usertype.get()]
                        for row in d:
                            table_info.insert('', END, values=row)
                    else:
                        for item in table_info.get_children():
                            table_info.delete(item)
                        for row in triple_request:
                            table_info.insert('', END, values=row)
                        choose_usertype.set("Род деятельности")
                else:
                    mb.showerror('Внимание!', 'Вы не заполнили поле!')

            def search_status():
                global user_etry, table_info, last_lookup, selections, triple_request, user_etry, show_info_frame, title_etry, choose_usertype, choose_status
                cur.execute("""
                                                SELECT  orders.orderid, users.username, users.usertype,  books.title, orders.start_date, orders.end_date, orders.status, books.number FROM orders
                                                LEFT JOIN users ON users.userid = orders.userid
                                                LEFT JOIN books ON books.bookid = orders.bookid; 
                                                """)

                triple_request = cur.fetchall()
                d = [item for item in triple_request if item[6] == choose_status.get()]
                if choose_status.get() != 'Статус книги':
                    if d:
                        for item in table_info.get_children():
                            table_info.delete(item)
                        d = [item for item in triple_request if item[6] == choose_status.get()]
                        for row in d:
                            table_info.insert('', END, values=row)
                    else:
                        mb.showinfo('Внимание!', 'Книг с таким статусом нет')
                        for item in table_info.get_children():
                            table_info.delete(item)
                        for row in triple_request:
                            table_info.insert('', END, values=row)
                        choose_status.set("Статус книги")
                else:
                    mb.showerror('Внимание!', 'Вы не заполнили поле!')

            def upd_btn():
                global values_status, triple_request, conn, cur, table_info, show_info_frame, title_etry, choose_usertype, choose_status
                # Обновляем таблицу
                cur.execute("""
                                                                SELECT  orders.orderid, users.username, users.usertype, books.title, orders.start_date, orders.end_date, orders.status, books.number FROM orders
                                                                LEFT JOIN users ON users.userid = orders.userid
                                                                LEFT JOIN books ON books.bookid = orders.bookid; 
                                                                """)
                new_date = cur.fetchall()

                def list_replace(lst: list, value_search, value_replace):
                    res = []
                    for item in lst:  # Итерируем входной список
                        if isinstance(item, (list, set, tuple)):
                            res.append(
                                list_replace(item, value_search,
                                             value_replace))  # На этом уровне уходим в список, сет, кортеж глубже
                        else:
                            res.append(
                                item if item != value_search else value_replace)  # добавляем значение в результирующий список, если совпадает с искомым значением, то меняем его
                    return type(lst)(res)

                new_date = list_replace(new_date, None, '(Пользователь Удалён)')
                # Обновляем таблицу
                for item in table_info.get_children():
                    table_info.delete(item)
                for row in new_date:
                    table_info.insert('', END, values=row)
                choose_status.set("Статус книги")
                title_etry.delete(0, END)
                choose_usertype.set("Род деятельности")
                user_etry.delete(0, END)

            # РАБОЧИЙ ПОИСК
            def search2():
                global entry_book_search, table_book
                global last_lookup, selections
                query = entry_book_search.get()
                if not query:
                    return
                children = table_book.get_children()
                for child in children:
                    curr = table_book.item(child)["values"][2]
                    if query in curr and child not in selections[query]:
                        selections[query].append(child)
                        table_book.selection_set(child)
                        table_book.focus(child)
                        table_book.see(child)
                        last_lookup = query
                        return
                    elif query != last_lookup:
                        selections = defaultdict(list)

            def on_closing():
                global values_status, triple_request, conn, cur, table_info, toplevel2
                toplevel2.destroy()
                values_status = ()

            # Функция кнопки КНИГУ СДАЛ
            def order_status():
                global values_status, triple_request, conn, cur, table_info
                if values_status:
                    if values_status[6] == 'Не сдано':

                        strsam1 = """UPDATE books SET  number = ? WHERE title = ?"""
                        number = int(values_status[7]) + 1
                        data = (number, values_status[3])
                        cur.execute(strsam1, data)

                        strsam = """UPDATE orders SET status = ? WHERE orderid = ?"""
                        new_status = 'Сдано'
                        data = (new_status, values_status[0])
                        cur.execute(strsam, data)
                        conn.commit()
                        # Обновляем таблицу
                        cur.execute("""
                                                SELECT  orders.orderid, users.username, users.usertype, books.title, orders.start_date, orders.end_date, orders.status, books.number FROM orders
                                                LEFT JOIN users ON users.userid = orders.userid
                                                LEFT JOIN books ON books.bookid = orders.bookid; 
                                                """)
                        new_date = cur.fetchall()

                        # Обновляем таблицу
                        for item in table_info.get_children():
                            table_info.delete(item)
                        for row in new_date:
                            table_info.insert('', END, values=row)
                    else:
                        mb.showinfo('Внимание!', 'Заказ уже сдан!')
                else:
                    mb.showerror('Внимание!', 'Вы не выбрали заказ!')
                values_status = ()

            # ПОКАЗАТЬ СПИСОК ЗАКАЗОВ
            def show_orders_info():
                global triple_request, table_info, toplevel2, values_status, user_etry, show_info_frame, title_etry, choose_usertype, choose_status

                cur.execute("""
                                SELECT  orders.orderid, users.username, users.usertype,  books.title, orders.start_date, orders.end_date, orders.status, books.number FROM orders
                                LEFT JOIN users ON users.userid = orders.userid
                                LEFT JOIN books ON books.bookid = orders.bookid; 
                                """)

                triple_request = cur.fetchall()

                def list_replace(lst: list, value_search, value_replace):
                    res = []
                    for item in lst:  # Итерируем входной список
                        if isinstance(item, (list, set, tuple)):
                            res.append(
                                list_replace(item, value_search,
                                             value_replace))  # На этом уровне уходим в список, сет, кортеж глубже
                        else:
                            res.append(
                                item if item != value_search else value_replace)  # добавляем значение в результирующий список, если совпадает с искомым значением, то меняем его
                    return type(lst)(res)

                triple_request = list_replace(triple_request, None, '(Пользователь Удалён)')

                toplevel2 = customtkinter.CTkToplevel(root)
                toplevel2.title("Библиотечная система")
                toplevel2.grab_set()
                toplevel2.protocol("WM_DELETE_WINDOW", on_closing)
                # Рамка
                show_info_frame = customtkinter.CTkFrame(toplevel2, corner_radius=15)
                show_info_frame.grid(row=0, column=0, padx=15, pady=5, sticky="we")
                # Рамка для кнопки
                btn_frame2 = customtkinter.CTkFrame(toplevel2, corner_radius=15)
                btn_frame2.grid(row=2, column=0, padx=15, pady=10, sticky="ns")
                # Рамка для поиска
                btn2_frame = customtkinter.CTkFrame(toplevel2, corner_radius=15)
                btn2_frame.grid(row=3, column=0, padx=15, pady=10, sticky="n")

                btn3_frame = customtkinter.CTkFrame(toplevel2, corner_radius=15)
                btn3_frame.grid(row=1, column=0, padx=5, pady=5, sticky="e")

                user_etry = customtkinter.CTkEntry(btn2_frame, placeholder_text='Введите ФИО')
                user_etry.grid(row=0, column=0, padx=5, pady=5, sticky="n")

                title_etry = customtkinter.CTkEntry(btn2_frame, placeholder_text='Введите Название Книги', width=200)
                title_etry.grid(row=0, column=2, padx=5, pady=5, sticky="n")

                choose_usertype = customtkinter.CTkOptionMenu(master=btn2_frame, values=["Студент", "Преподаватель"],
                                                              fg_color='#979aaa')
                choose_usertype.grid(pady=5, padx=5, row=0, column=4)
                choose_usertype.set("Род деятельности")

                choose_status = customtkinter.CTkOptionMenu(master=btn2_frame, values=["Сдано", "Не сдано"],
                                                            fg_color='#979aaa')
                choose_status.grid(pady=5, padx=5, row=0, column=6)
                choose_status.set("Статус книги")
                # Таблица
                heads = ['№ ВЫДАЧИ', 'ФИО', 'РОД ЗАНЯТИЯ', ' НАЗВАНИЕ КНИГИ', 'ДАТА ВЫДАЧИ', 'ДАТА СДАЧИ', 'СТАТУС']
                table_info = ttk.Treeview(show_info_frame, show='headings')
                table_info['columns'] = heads

                def on_select(event):
                    global values_status, table_info
                    if not table_info.selection():
                        return
                    # Получаем id первого выделенного элемента
                    selected_item = table_info.selection()

                    # Получаем значения в выделенной строке
                    values_status = table_info.item(selected_item, option="values")

                table_info.bind('<<TreeviewSelect>>', on_select)
                for header in heads:
                    table_info.heading(header, text=header, anchor='center')
                    table_info.column(header, anchor='center')
                for row in triple_request:
                    table_info.insert('', END, values=row)
                # Кнопки

                status_btn = customtkinter.CTkButton(btn_frame2, command=order_status, text='Книгу сдал',
                                                     fg_color='#228b22').grid(
                    row=0, column=0, padx=5, pady=5, sticky="w")
                search_btn = customtkinter.CTkButton(btn2_frame, text='Поиск', command=search_user).grid(
                    row=0,
                    column=1,
                    padx=5,
                    pady=5,
                    sticky="n",
                    columnspan=1)
                search_btn2 = customtkinter.CTkButton(btn2_frame, text='Поиск', command=search_title).grid(
                    row=0,
                    column=3,
                    padx=5,
                    pady=5,
                    sticky="n",
                    columnspan=1)

                search_btn3 = customtkinter.CTkButton(btn2_frame, text='Поиск', command=search_usertype).grid(
                    row=0,
                    column=5,
                    padx=5,
                    pady=5,
                    sticky="n",
                    columnspan=1)
                search_btn3 = customtkinter.CTkButton(btn2_frame, text='Поиск', command=search_status).grid(
                    row=0,
                    column=7,
                    padx=5,
                    pady=5,
                    sticky="n",
                    columnspan=1)
                upd_btn3 = customtkinter.CTkButton(btn3_frame, text='Обновить таблицу', command=upd_btn,
                                                   fg_color='red').grid(
                    row=0,
                    column=8,
                    padx=5,
                    pady=5,
                    sticky="n",
                    columnspan=1)
                # Скроллер
                scroller = customtkinter.CTkScrollbar(show_info_frame, command=table_info.yview, fg_color=None)
                scroller.grid(row=0, column=1, padx=0, pady=15, sticky="nsew")
                # Дополнения для таблицы и её упаковка
                table_info.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
                table_info.configure(yscrollcommand=scroller.set)

            # ФУНКЦИЯ КНОПКИ ПОДТВЕРЖДЕНИЯ
            def confirm_btn():
                global cal, values, table_book, values_book, choose_take_day
                if values_book:
                    if choose_take_day.get() != 'Кол-во дней':
                        if int(values_book[4]) != 0:
                            strsam = """UPDATE books SET autor = ?, title = ?, genre = ?, number = ? WHERE bookid = ?"""
                            new_number = int(values_book[4]) - 1
                            data = (values_book[1], values_book[2], values_book[3], new_number, values_book[0])

                            cur.execute(strsam, data)
                            conn.commit()
                            # Обновляем таблицу
                            for item in table_book.get_children():
                                table_book.delete(item)
                            cur.execute("SELECT * FROM books;")
                            book_result = cur.fetchall()
                            for row in book_result:
                                table_book.insert('', END, values=row)

                            a = choose_take_day.get()
                            # Открываем файл счётчик для чтения текущего значение из файла
                            with open("counters\order_counter.txt", 'r') as f:
                                order_counter = f.read().splitlines()
                            order_counter = int(''.join(map(str, order_counter))) + 1
                            # Открываем файл счётчик для записи данных в файл
                            with open("counters\order_counter.txt", "w") as file:
                                file.write(str(order_counter))
                            star_date = date.today()
                            current_date_string = star_date.strftime('%d/%m/%y')
                            end_date = star_date + timedelta(days=int(a))
                            end_date_new = end_date.strftime('%d/%m/%y')
                            status = 'Не сдано'
                            order_list = (
                                order_counter, values[0], values_book[0], current_date_string, end_date_new, status)
                            cur.execute("INSERT INTO orders VALUES(?, ?, ?, ?, ?, ?);", order_list)
                            conn.commit()
                            values_book = ()
                            choose_take_day.set("Кол-во дней")
                            mb.showinfo('Внимание!', 'Заказ успешно выдан!')
                        else:
                            mb.showerror('Внимание!', 'Книг не осталось в наличии!')
                    else:
                        mb.showerror('Внимание!', 'Вы не ввели кол-во дней!')
                else:
                    mb.showerror('Внимание!', 'Вы не выбрали книгу')

            # ВЫДАТЬ КНИГУ---------------------------------------------------------------------------
            def book_list():
                global cal, values, table_book, values_book, choose_take_day, entry_book_search

                if values:
                    toplevel = customtkinter.CTkToplevel(root)
                    toplevel.title("Библиотечная система")
                    toplevel.grab_set()
                    cur.execute("SELECT * FROM books;")
                    book_result = cur.fetchall()
                    # conn.commit()
                    # Рамки
                    take_book_frame = customtkinter.CTkFrame(toplevel, corner_radius=15)
                    take_book_frame.grid(row=0, column=0, padx=15, pady=20, sticky="we")
                    book_frame = customtkinter.CTkFrame(toplevel, corner_radius=15)
                    book_frame.grid(row=2, column=0, padx=15, pady=20, sticky="n")
                    btn2_frame = customtkinter.CTkFrame(toplevel, corner_radius=15)
                    btn2_frame.grid(row=1, column=0, padx=15, pady=20, sticky="n")
                    # Таблица
                    heads = ['№КНИГИ', 'АВТОР', 'НАЗВАНИЕ', 'ЖАНР', 'КОЛ-ВО']
                    table_book = ttk.Treeview(take_book_frame, show='headings')
                    table_book['columns'] = heads

                    def on_select(event):
                        global values_book
                        if not table_book.selection():
                            return
                        # Получаем id первого выделенного элемента
                        selected_item = table_book.selection()[0]

                        # Получаем значения в выделенной строке
                        values_book = table_book.item(selected_item, option="values")

                    table_book.bind('<<TreeviewSelect>>', on_select)
                    for header in heads:
                        table_book.heading(header, text=header, anchor='center')
                        table_book.column(header, anchor='center')
                    for row in book_result:
                        table_book.insert('', END, values=row)

                    # Скроллер
                    scroller = customtkinter.CTkScrollbar(take_book_frame, command=table_book.yview, fg_color=None)
                    scroller.grid(row=0, column=1, padx=0, pady=15, sticky="nsew")
                    # Дополнения для таблицы и её упаковка
                    table_book.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
                    table_book.configure(yscrollcommand=scroller.set)
                    search_btn = customtkinter.CTkButton(btn2_frame, text='Поиск', command=search2,
                                                         fg_color='#979aaa').grid(
                        row=0,
                        column=2,
                        padx=20,
                        pady=10,
                        sticky="e",
                        columnspan=1)

                    # Выбор количества дней на выдачу
                    choose_take_day = customtkinter.CTkOptionMenu(book_frame,
                                                                  values=['1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8',
                                                                          ' 9',
                                                                          '10', '11', '12', '13', '14'],
                                                                  fg_color='#979aaa')
                    # Строка поиска
                    entry_book_search = customtkinter.CTkEntry(btn2_frame, placeholder_text="Название книги")
                    entry_book_search.grid(pady=12, padx=10, row=0, column=0)

                    choose_take_day.grid(pady=12, padx=10, row=0, column=0)
                    choose_take_day.set("Кол-во дней")
                    conf_btn = customtkinter.CTkButton(book_frame, text='Подтвердить', command=confirm_btn,
                                                       fg_color='#228b22').grid(
                        row=0, column=2, padx=10, pady=10, sticky="w")
                else:
                    mb.showerror('Внимание!', 'Вы не выбрали читателя')

            # ВЫДАТЬ КНИГУ---------------------------------------------------------------------------
            def add_book():
                global cal, table_book, values_book, entry_book_search, entry_autor, entry_title, entry_genre, entry_number

                addlevel = customtkinter.CTkToplevel(root)
                addlevel.title("Библиотечная система")
                addlevel.grab_set()
                cur.execute("SELECT * FROM books;")
                book_result = cur.fetchall()
                # conn.commit()
                # Рамки
                add_book_frame = customtkinter.CTkFrame(addlevel, corner_radius=15)
                add_book_frame.grid(row=0, column=0, padx=15, pady=20, sticky="we")
                book_frame = customtkinter.CTkFrame(addlevel, corner_radius=15)
                book_frame.grid(row=2, column=0, padx=15, pady=20, sticky="n")
                btn2_frame = customtkinter.CTkFrame(addlevel, corner_radius=15)
                btn2_frame.grid(row=1, column=0, padx=15, pady=20, sticky="n")
                # Таблица
                heads = ['№КНИГИ', 'АВТОР', 'НАЗВАНИЕ', 'ЖАНР', 'КОЛ-ВО']
                table_book = ttk.Treeview(add_book_frame, show='headings')
                table_book['columns'] = heads
                # Поля для заполения
                entry_autor = customtkinter.CTkEntry(master=book_frame, placeholder_text="Автор")
                entry_autor.grid(pady=12, padx=10, row=0, column=0)
                entry_title = customtkinter.CTkEntry(master=book_frame, placeholder_text="Название")
                entry_title.grid(pady=12, padx=10, row=0, column=1)
                entry_genre = customtkinter.CTkEntry(master=book_frame, placeholder_text="Жанр")
                entry_genre.grid(pady=12, padx=10, row=0, column=2)
                entry_number = customtkinter.CTkEntry(master=book_frame, placeholder_text="Кол-во")
                entry_number.grid(pady=12, padx=10, row=0, column=3)

                def on_select(event):
                    global values_book
                    if not table_book.selection():
                        return
                    # Получаем id первого выделенного элемента
                    selected_item = table_book.selection()[0]

                    # Получаем значения в выделенной строке
                    values_book = table_book.item(selected_item, option="values")

                table_book.bind('<<TreeviewSelect>>', on_select)
                for header in heads:
                    table_book.heading(header, text=header, anchor='center')
                    table_book.column(header, anchor='center')
                for row in book_result:
                    table_book.insert('', END, values=row)

                # Скроллер
                scroller = customtkinter.CTkScrollbar(add_book_frame, command=table_book.yview, fg_color=None)
                scroller.grid(row=0, column=1, padx=0, pady=15, sticky="nsew")
                # Дополнения для таблицы и её упаковка
                table_book.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
                table_book.configure(yscrollcommand=scroller.set)

                search_btn = customtkinter.CTkButton(btn2_frame, text='Поиск', command=search2,
                                                     fg_color='#979aaa').grid(
                    row=0,
                    column=2,
                    padx=20,
                    pady=10,
                    sticky="e",
                    columnspan=1)

                # Строка поиска
                entry_book_search = customtkinter.CTkEntry(btn2_frame, placeholder_text="Название книги")
                entry_book_search.grid(pady=12, padx=10, row=0, column=0)

                conf_btn = customtkinter.CTkButton(book_frame, text='Подтвердить', command=add_book2,
                                                   fg_color='#228b22').grid(
                    row=0, column=5, padx=10, pady=10, sticky="w")

            def add_book2():
                global entry_autor, entry_title, entry_genre, entry_number
                if entry_autor.get() != '' and entry_title != '' and entry_genre.get() != ' ' and entry_number.get() != ' ':
                    if entry_number.get().isdigit() and int(entry_number.get()):
                        if (re.search('[А-Я а-я]', entry_autor.get())) and (re.search('[А-Я а-я]', entry_genre.get())):
                            # Открываем файл счётчик для чтения текущего значение из файла
                            with open("counters/book_counter.txt", 'r') as f:
                                file_counter = f.read().splitlines()
                            file_counter = int(''.join(map(str, file_counter))) + 1
                            # Открываем файл счётчик для записи данных в файл
                            with open("counters/book_counter.txt", "w") as file:
                                file.write(str(file_counter))
                            book_list = (
                                file_counter, entry_autor.get(), entry_title.get(), entry_genre.get(),
                                entry_number.get())
                            cur.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?);", book_list)
                            conn.commit()

                            # Обновляем таблицу
                            for item in table_book.get_children():
                                table_book.delete(item)
                            cur.execute("SELECT * FROM books;")
                            one_result = cur.fetchall()
                            for row in one_result:
                                table_book.insert('', END, values=row)
                            # ----------------------------------
                            entry_autor.delete(0, END)
                            entry_title.delete(0, END)
                            entry_genre.delete(0, END)
                            entry_number.delete(0, END)
                        else:
                            mb.showerror('Внимание!', 'В поле автор и жанр можно вводить только буквы!')
                    else:
                        mb.showerror('Внимание!', 'Ведите целое число книг!')
                else:
                    mb.showerror('Внимание!', 'Вы не заполнили все поля!')

            # Функция скрывающая рамку с регистрацией пользователя
            def close_frame():
                global values, conn, cur, switch_1, table, file_counter, registr_frame, change_frame, take_book_frame, checks
                if len(table.selection()) > 0:
                    table.selection_remove(table.selection()[0])
                values = ()
                if checks[0] == 'reg':
                    registr_frame.grid_forget()
                elif checks[0] == 'change':
                    change_frame.grid_forget()
                elif checks[0] == 'take':
                    take_book_frame.grid_forget()

            # ИЗМЕНЕНИНЕ ДАННЫХ ПОЛЬЗОВАТЕЛЯ------------------------------------------------------------------------------------
            def mod_info():
                global values, conn, cur, switch_1, table, file_counter, registr_frame, entry_name, entry_surname, choose_type, choose_sex, cal, checks
                if entry_name.get() != '' and choose_type.get() != 'Род деятельности' and choose_sex.get() != 'Пол':
                    dt = cal.get_date()
                    str_dt = dt.strftime("%d-%m-%Y")
                    # Подсчёт возраста
                    nowdays = date.today()
                    birth = cal.get_date()
                    user_age_check = relativedelta(nowdays, birth)
                    strsam = """UPDATE users SET username = ?,  usertype = ?, gender = ?, datebirth=? WHERE userid = ?"""
                    data = (entry_name.get(), choose_type.get(), choose_sex.get(), str_dt, values[0])

                    if user_age_check.years >= 16:
                        if (re.search('[А-Я а-я]', entry_name.get())):
                            cur.execute(strsam, data)
                            # Обновляем таблицу
                            for item in table.get_children():
                                table.delete(item)
                            cur.execute("SELECT * FROM users;")
                            one_result = cur.fetchall()
                            for row in one_result:
                                table.insert('', END, values=row)
                            # ----------------------------------
                            values = ()
                            change_frame.grid_forget()
                            conn.commit()
                            mb.showinfo('Внимание!', 'Данные успешно изменены!')
                        else:
                            mb.showerror('Внимание!',
                                         'Имя может состоять только из букв!')
                    else:
                        cal = DateEntry(change_frame, selectmode='day', date_pattern='dd-MM-yyyy',
                                        style='my.DateEntry',
                                        font=20, state='readonly')
                        cal.grid(row=0, column=4, padx=20, pady=30)
                        cal.set_date(values[4])
                        mb.showerror('Внимание!',
                                     'Читателю не может быть меньше 16 лет!')

                else:
                    mb.showerror('Внимание!', 'Вы не заполнили все поля')

            def change_user_info():
                global values, conn, cur, switch_1, table, file_counter, registr_frame, entry_name, choose_type, choose_sex, checks, change_frame, cal

                # Рамка
                if values:
                    change_frame = customtkinter.CTkFrame(BIG_FRAME, corner_radius=15)
                    change_frame.grid(row=3, column=0, padx=15, pady=20, sticky="we")
                    # Поля ввода
                    entry_name = customtkinter.CTkEntry(master=change_frame, placeholder_text="Имя", width=250)
                    entry_name.insert(0, values[1])
                    entry_name.grid(pady=12, padx=10, row=0, column=1)

                    choose_type = customtkinter.CTkOptionMenu(master=change_frame, values=["Студент", "Преподаватель"],
                                                              fg_color='#979aaa')
                    choose_type.grid(pady=12, padx=10, row=0, column=2)
                    choose_type.set(values[2])

                    choose_sex = customtkinter.CTkOptionMenu(master=change_frame, values=["М", "Ж"], fg_color='#979aaa')
                    choose_sex.grid(pady=12, padx=10, row=0, column=3)
                    choose_sex.set(values[3])
                    # календарь
                    cal = DateEntry(change_frame, selectmode='day', date_pattern='dd-MM-yyyy', style='my.DateEntry',
                                    font=20, state='readonly')
                    cal.grid(row=0, column=4, padx=20, pady=30)
                    cal.set_date(values[4])
                    mod = customtkinter.CTkButton(change_frame, text='Применить', command=mod_info,
                                                  fg_color='#228b22').grid(
                        row=0, column=5, padx=10, pady=10, sticky="w")
                    close = customtkinter.CTkButton(change_frame, text='Скрыть', command=close_frame,
                                                    fg_color='#cb4154').grid(
                        row=0,
                        column=6,
                        padx=10,
                        pady=10,
                        sticky="w")
                    # Проверятель очистки фрейма--------------
                    checks = ['change']
                    # Проверятель очистки фрейма--------------

                else:
                    mb.showerror(
                        "Внимание",
                        "Вы не выбрали запись для изменения")

            # РЕГИСТРАЦИЯ------------------------------------------------------------------------------------------------------------
            def add_user():
                global values, conn, cur, switch_1, table, file_counter, registr_frame, entry_name, entry_surname, choose_type, choose_sex, cal

                if entry_name.get() != '' and choose_type.get() != 'Род деятельности' and choose_sex.get() != 'Пол':
                    # Открываем файл счётчик для чтения текущего значение из файла
                    with open("counters\id_counter.txt", 'r') as f:
                        file_counter = f.read().splitlines()
                    file_counter = int(''.join(map(str, file_counter))) + 1
                    # Открываем файл счётчик для записи данных в файл
                    with open("counters\id_counter.txt", "w") as file:
                        file.write(str(file_counter))
                    # изменяем формат даты
                    dt = cal.get_date()
                    userage = dt.strftime("%d-%m-%Y")
                    # Подсчёт возраста
                    nowdays = date.today()
                    birth = cal.get_date()
                    user_age_check = relativedelta(nowdays, birth)
                    if user_age_check.years >= 16 and (re.search('[А-Я а-я]', entry_name.get())):

                        users_list = (
                            file_counter, entry_name.get(), choose_type.get(), choose_sex.get(), userage)
                        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?);", users_list)
                        conn.commit()

                        # Обновляем таблицу
                        for item in table.get_children():
                            table.delete(item)
                        cur.execute("SELECT * FROM users;")
                        one_result = cur.fetchall()
                        for row in one_result:
                            table.insert('', END, values=row)
                        # ----------------------------------
                        entry_name.delete(0, END)
                        choose_type.set("Род деятельности")
                        choose_sex.set("Пол")
                        cal.set_date(date.today())
                        mb.showinfo('Внимание!', 'Читатель успешно добавлен')
                        values = ()
                    else:
                        cal = DateEntry(registr_frame, selectmode='day', date_pattern='dd-MM-yyyy',
                                        style='my.DateEntry',
                                        font=20, state='readonly')
                        cal.grid(row=0, column=4, padx=20, pady=30)
                        mb.showerror('Внимание!',
                                     'Проверьте данные на коректность\nЧитателю не может быть меньше 16 лет\nИмя может состоять только из букв')



                else:
                    mb.showerror('Внимание!', 'Вы не заполнили все поля')

            def rigistration():
                global values, conn, cur, switch_1, table, file_counter, registr_frame, entry_name, entry_surname, choose_type, choose_sex, checks, cal
                # рамка
                registr_frame = customtkinter.CTkFrame(BIG_FRAME, corner_radius=15)
                registr_frame.grid(row=3, column=0, padx=15, pady=20, sticky="we")
                # Поля для заполения
                entry_name = customtkinter.CTkEntry(master=registr_frame, placeholder_text="ФИО", width=200)
                entry_name.grid(pady=12, padx=10, row=0, column=1)

                choose_type = customtkinter.CTkOptionMenu(master=registr_frame, values=["Студент", "Преподаватель"],
                                                          fg_color='#979aaa')
                choose_type.grid(pady=12, padx=10, row=0, column=2)
                choose_type.set("Род деятельности")

                choose_sex = customtkinter.CTkOptionMenu(master=registr_frame, values=["М", "Ж"], fg_color='#979aaa')
                choose_sex.grid(pady=12, padx=10, row=0, column=3)
                choose_sex.set("Пол")

                cal = DateEntry(registr_frame, selectmode='day', date_pattern='dd-MM-yyyy', style='my.DateEntry',
                                font=20, state='readonly')
                cal.grid(row=0, column=4, padx=20, pady=30)

                # Проверятель очистки фрейма--------------
                checks = ['reg']
                # Проверятель очистки фрейма--------------
                regstration = customtkinter.CTkButton(registr_frame, text='Добавить', command=add_user,
                                                      fg_color='#228b22').grid(
                    row=0, column=5, padx=10, pady=10, sticky="w")
                close = customtkinter.CTkButton(registr_frame, text='Скрыть', command=close_frame,
                                                fg_color='#cb4154').grid(
                    row=0,
                    column=6,
                    padx=10,
                    pady=10,
                    sticky="w")

            # УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ----------------------------------------------------------------
            def delete_user():
                global values, conn, cur
                if values:
                    answer = mb.askyesno("Вопрос", "Вы уверены что хотите УДАЛИТЬ пользователя?")
                    if answer:
                        sql_delete_query = """DELETE from users where userid = ?"""
                        cur.execute(sql_delete_query, (values[0],))

                        conn.commit()
                        selected_item = table.selection()[0]
                        table.delete(selected_item)
                        mb.showinfo(
                            "Ошибка",
                            "Запись успешно удалена")
                        values = ()

                else:
                    mb.showerror("Ошибка", "Вы не выбрали удаляемого читателя")

            # РАБОЧИЙ ПОИСК
            def search():
                global last_lookup, selections
                query = entry_search.get()
                if entry_search.get() != '':
                    if not query:
                        return
                    children = table.get_children()
                    for child in children:
                        curr = table.item(child)["values"][1]
                        if query in curr and child not in selections[query]:
                            selections[query].append(child)
                            table.selection_set(child)
                            table.focus(child)
                            table.see(child)
                            last_lookup = query
                            return

                        elif query != last_lookup:
                            selections = defaultdict(list)
                else:
                    mb.showerror('Внимание!', 'Вы не заполнили поле!')

                if not selections:
                    mb.showinfo('Внимание!', 'Такого пользователя не существует!')

            # ПОЛУЧЕНИЕ ЗНАЧЕНИЕ ВЫДЕЛЕННОЙ СТРОКИ
            def on_select(event):
                global values

                if not table.selection():
                    return

                selected_item = table.selection()[0]
                values = table.item(selected_item, option="values")

            # ОТКРЫТИЕ ФАЙЛА
            def edit_click():
                toplevel_help = customtkinter.CTkToplevel(root)
                toplevel_help.title("Справка")
                toplevel_help.grab_set()
                f = open("help.txt", "r", encoding="UTF8").read()
                Label(toplevel_help, text=f, font='Times 15').grid(row=0)

            def exit():
                BIG_FRAME.grid_forget()
                root.geometry('400x300')

            conn = sqlite3.connect(r'datebase/readers.db')
            cur = conn.cursor()
            # Три основные таблицы
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                           userid INT PRIMARY KEY,
                           username TEXT,
                           usertype TEXT,
                           gender TEXT,
                           datebirth TEXT);
                        """)

            cur.execute("""CREATE TABLE IF NOT EXISTS books(
                           bookid INT PRIMARY KEY,
                           autor TEXT,
                           title TEXT,
                           genre TEXT,
                           number INT);
                        """)
            cur.execute("""CREATE TABLE IF NOT EXISTS orders(
                           orderid INT PRIMARY KEY,
                           userid TEXT,
                           bookid TEXT,
                           start_date TEXT,
                           end_date TEXT,
                           status TEXT);
                        """)

            # users = [('0001', 'Mikhail', 'Panin', 'student', 'M', '08-03-2002'), ('0002', 'Julia', 'Samsonova', 'student', 'W', '04-07-2002')]
            # cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?,?);", users)
            # books = [('000000001', 'Фрэнк Герберт', 'Дюна', 'Научная фантастика', 150), ('000000002', 'Томас Харрис', 'Молчание ягнят', 'Детектив', 150)]
            # cur.executemany("INSERT INTO books VALUES(?, ?, ?, ?, ?);", books)

            cur.execute("SELECT * FROM users;")
            all_result = cur.fetchall()
            conn.commit()

            # root.resizable(False, False)
            # Окно
            mainmenu = Menu(root)
            root.config(menu=mainmenu)
            mainmenu.add_command(label='Справка', command=edit_click)

            style = ttk.Style()
            style.theme_use('clam')
            # Шрифт

            style_value = ttk.Style()
            style_head = ttk.Style()
            style_head.configure("Treeview.Heading", font=("Times", 12), background='#979aaa')
            # style_value.configure("Treeview", rowheight=30, font=("font", 15))
            ttk.Style().configure(".", font="Times", foreground="black", background="#979aaa")
            # рамка
            BIG_FRAME = customtkinter.CTkFrame(root, corner_radius=1, fg_color=None)
            BIG_FRAME.grid(row=0, column=0, padx=5, pady=2, sticky="n")
            frame = customtkinter.CTkFrame(BIG_FRAME, corner_radius=1)
            frame.grid(row=0, column=0, padx=5, pady=2, sticky="n")
            # Рамка для строки поиска
            search_frame = customtkinter.CTkFrame(BIG_FRAME, corner_radius=15)
            search_frame.grid(row=2, column=0, padx=15, pady=20, sticky="n")
            # Рамка для кнопок
            btn_frame = customtkinter.CTkFrame(BIG_FRAME, corner_radius=15)
            btn_frame.grid(row=3, column=0, padx=15, pady=20, sticky="we")
            # Рамка дляя выхода
            exit_frame = customtkinter.CTkFrame(BIG_FRAME, corner_radius=1, fg_color=None)
            exit_frame.grid(row=4, column=0, padx=5, pady=2, sticky="n")
            # определяем столбцы

            # Таблица
            heads = ['№БИЛЕТА', 'ФИО', 'РОД ЗАНЯТИЯ', 'ПОЛ', 'ДАТА РОЖДЕНИЯ']
            table = ttk.Treeview(frame, show='headings')
            table['columns'] = heads
            table["show"] = "headings"

            for header in heads:
                table.heading(header, text=header, anchor='center')
                table.column(header, anchor='center')
            for row in all_result:
                table.insert('', END, values=row)

            # Скроллер
            scroller = customtkinter.CTkScrollbar(frame, command=table.yview, fg_color=None)
            scroller.grid(row=0, column=2, padx=2, pady=15, sticky="e")
            # Дополнения для таблицы и её упаковка
            table.grid(row=0, column=0, padx=2, pady=0, sticky="we")
            table.configure(yscrollcommand=scroller.set)

            # -----------------------------------Кнопки
            regstration = customtkinter.CTkButton(btn_frame, text='Зарегистрировать читателя',
                                                  command=rigistration, fg_color='#979aaa').grid(row=0, column=0,
                                                                                                 padx=20, pady=10
                                                                                                 , sticky="w",
                                                                                                 columnspan=1)
            delete = customtkinter.CTkButton(btn_frame, text='Удалить читателя', command=delete_user,
                                             fg_color='#979aaa').grid(
                row=0, column=1,
                padx=20, pady=10,
                sticky="n", columnspan=1)

            change_user_info = customtkinter.CTkButton(btn_frame, text='Изменить данные читателя',
                                                       command=change_user_info, fg_color='#979aaa').grid(row=0,
                                                                                                          column=2,
                                                                                                          padx=10,
                                                                                                          pady=10,
                                                                                                          sticky="w")

            take_book = customtkinter.CTkButton(btn_frame, text='Выдать книгу', command=book_list,
                                                fg_color='#979aaa').grid(row=0,
                                                                         column=3,
                                                                         padx=20,
                                                                         pady=10,
                                                                         sticky="e",
                                                                         columnspan=1)

            show_orders = customtkinter.CTkButton(btn_frame, text='Показать список заказов', command=show_orders_info,
                                                  fg_color='#979aaa'
                                                  ).grid(row=0, column=5, padx=10, pady=10, sticky="w")

            add_book = customtkinter.CTkButton(btn_frame, text='Добавить книгу', command=add_book,
                                               fg_color='#979aaa'
                                               ).grid(row=0, column=6, padx=10, pady=10, sticky="w")

            search_btn = customtkinter.CTkButton(search_frame, text='Поиск', command=search,
                                                 fg_color='#979aaa').grid(row=0,
                                                                          column=1,
                                                                          padx=20,
                                                                          pady=10,
                                                                          sticky="n",
                                                                          columnspan=1)

            exit_btn = customtkinter.CTkButton(exit_frame, text='Назад в меню', command=exit,
                                               fg_color='red').grid(row=0,
                                                                    column=1,
                                                                    padx=20,
                                                                    pady=10,
                                                                    sticky="n",
                                                                    columnspan=1)
            # -----------------------------------
            # Строка поиска
            entry_search = customtkinter.CTkEntry(search_frame, placeholder_text="Фамилия", width=300)
            entry_search.grid(pady=12, padx=10, row=0, column=0, sticky="n")

            table.bind('<<TreeviewSelect>>', on_select)

        else:
            login_etry.delete(0, END)
            mb.showerror('Внимание', 'Неверный пароль!')

    toplevel3 = customtkinter.CTkToplevel(root)
    toplevel3.geometry('300x300')
    toplevel3.title("Вход")
    toplevel3.grab_set()
    login_etry = customtkinter.CTkEntry(toplevel3, placeholder_text='Введите пароль', show="*")
    login_etry.place(relx=0.5, rely=0.45, anchor=CENTER)
    login_btn = customtkinter.CTkButton(toplevel3, text='Войти', command=password)
    login_btn.place(relx=0.5, rely=0.6, anchor=CENTER)


def user():
    root.geometry('1050x530')
    root.resizable(False, False)
    conn = sqlite3.connect(r'datebase/readers.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books;")
    book_result = cur.fetchall()
    conn.commit()

    def edit_click():
        toplevel_help = customtkinter.CTkToplevel(root)
        toplevel_help.title("Справка")
        toplevel_help.grab_set()
        f = open("help.txt", "r", encoding="UTF8").read()
        Label(toplevel_help, text=f, font='Times 15').grid(row=0)

    def exit():
        BIG_FRAME.grid_forget()
        root.geometry('400x300')

    def autor_request():

        autor = request_autor_etry.get()
        sql_select_query = """select * from books where autor = ?"""
        cur.execute(sql_select_query, (autor,))
        autor_books = cur.fetchall()

        if request_autor_etry.get() != '':
            if (re.search('[А-Я а-я]', request_autor_etry.get())):
                if autor_books:
                    autor_top = customtkinter.CTkToplevel(root)
                    autor_top.grab_set()
                    # Таблица
                    heads = ['№ Книги', 'Автор', 'Название', 'Жанр', 'Кол-во в наличии']
                    table = ttk.Treeview(autor_top, show='headings')
                    table['columns'] = heads
                    table["show"] = "headings"
                    table['displaycolumns'] = ['Название', 'Жанр', 'Кол-во в наличии']

                    for header in heads:
                        table.heading(header, text=header, anchor='center')
                        table.column(header, anchor='center')
                    for row in autor_books:
                        table.insert('', END, values=row)

                    # Скроллер
                    scroller = customtkinter.CTkScrollbar(autor_top, command=table.yview, fg_color=None)
                    scroller.grid(row=0, column=2, padx=2, pady=15, sticky="e")
                    # Дополнения для таблицы и её упаковка
                    table.grid(row=0, column=0, padx=2, pady=0, sticky="we")
                    table.configure(yscrollcommand=scroller.set)
                    request_autor_etry.delete(0, END)

                else:
                    request_autor_etry.delete(0, END)
                    mb.showinfo('Внимание!', 'Такого автора нет!')
            else:
                request_autor_etry.delete(0, END)
                mb.showerror('Внимание!', 'Вы ввели недопустимые символы!')
        else:
            mb.showerror('Внимание!', 'Вы не ввели автора!')

    def title_request():

        autor = request_title_etry.get()
        sql_select_query = """select * from books where title = ?"""
        cur.execute(sql_select_query, (autor,))
        autor_books = cur.fetchall()

        if request_title_etry.get() != '':
            if autor_books:
                autor_top = customtkinter.CTkToplevel(root)
                autor_top.grab_set()
                # Таблица
                heads = ['№ Книги', 'Автор', 'Название', 'Жанр', 'Кол-во']
                table = ttk.Treeview(autor_top, show='headings')
                table['columns'] = heads
                table["show"] = "headings"
                table['displaycolumns'] = ['№ Книги', 'Автор', 'Кол-во']

                for header in heads:
                    table.heading(header, text=header, anchor='center')
                    table.column(header, anchor='center')
                for row in autor_books:
                    table.insert('', END, values=row)

                # Скроллер
                scroller = customtkinter.CTkScrollbar(autor_top, command=table.yview, fg_color=None)
                scroller.grid(row=0, column=2, padx=2, pady=15, sticky="e")
                # Дополнения для таблицы и её упаковка
                table.grid(row=0, column=0, padx=2, pady=0, sticky="we")
                table.configure(yscrollcommand=scroller.set)
                request_title_etry.delete(0, END)
            else:
                request_title_etry.delete(0, END)
                mb.showinfo('Внимание!', 'Такой книги нет!')
        else:
            request_title_etry.delete(0, END)
            mb.showerror('Внимание!', 'Вы не ввели название книги!')

    def genre_request():

        autor = request_genre_etry.get()
        sql_select_query = """select * from books where genre = ?"""
        cur.execute(sql_select_query, (autor,))
        autor_books = cur.fetchall()

        if request_genre_etry.get() != '':
            if (re.search('[А-Я а-я]', request_genre_etry.get())):
                if autor_books:
                    autor_top = customtkinter.CTkToplevel(root)
                    autor_top.grab_set()
                    # Таблица
                    heads = ['№ Книги', 'Автор', 'Название', 'Жанр', 'Кол-во в наличии']
                    table = ttk.Treeview(autor_top, show='headings')
                    table['columns'] = heads
                    table["show"] = "headings"
                    table['displaycolumns'] = ['№ Книги', 'Автор', 'Название', 'Кол-во в наличии']

                    for header in heads:
                        table.heading(header, text=header, anchor='center')
                        table.column(header, anchor='center')
                    for row in autor_books:
                        table.insert('', END, values=row)

                    # Скроллер
                    scroller = customtkinter.CTkScrollbar(autor_top, command=table.yview, fg_color=None)
                    scroller.grid(row=0, column=2, padx=2, pady=15, sticky="e")
                    # Дополнения для таблицы и её упаковка
                    table.grid(row=0, column=0, padx=2, pady=0, sticky="we")
                    table.configure(yscrollcommand=scroller.set)
                    request_genre_etry.delete(0, END)
                else:
                    request_genre_etry.delete(0, END)
                    mb.showinfo('Внимание!', 'Книг такого жанра нет!')
            else:
                request_genre_etry.delete(0, END)
                mb.showerror('Внимание!', 'Вы ввели недопустимые символы!')

        else:
            mb.showerror('Внимание!', 'Вы не ввели жанр!')

    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    mainmenu.add_command(label='Справка', command=edit_click)

    style_value = ttk.Style()
    style_value.configure("Treeview", rowheight=30, font=("Times", 15))
    style_head = ttk.Style()
    style_head.configure("Treeview.Heading", font=("Times", 20))

    # рамка
    BIG_FRAME = customtkinter.CTkFrame(root, corner_radius=1, fg_color=None)
    BIG_FRAME.grid(row=0, column=0, padx=5, pady=2, sticky='n')
    take_book_frame = customtkinter.CTkFrame(BIG_FRAME)
    take_book_frame.grid(row=0, column=0, padx=15, pady=20, sticky="n")
    # ЗАПРОСЫ
    request_frame = customtkinter.CTkFrame(BIG_FRAME)
    request_frame.grid(row=1, column=0, padx=15, pady=20, sticky="n")
    request_autor_etry = customtkinter.CTkEntry(request_frame, placeholder_text='Введите автора')
    request_autor_etry.grid(row=0, column=0, padx=5, pady=5, sticky="n")
    autor_request = customtkinter.CTkButton(request_frame, text='Найти', command=autor_request).grid(row=0,
                                                                                                     column=1,
                                                                                                     padx=5,
                                                                                                     pady=5,
                                                                                                     sticky="n",
                                                                                                     columnspan=1)

    request_title_etry = customtkinter.CTkEntry(request_frame, placeholder_text='Введите название книги', width=200)
    request_title_etry.grid(row=0, column=2, padx=5, pady=5, sticky="n")
    name_request = customtkinter.CTkButton(request_frame, text='Найти', command=title_request).grid(row=0,
                                                                                                    column=3,
                                                                                                    padx=5,
                                                                                                    pady=5,
                                                                                                    sticky="n",
                                                                                                    columnspan=1)
    request_genre_etry = customtkinter.CTkEntry(request_frame, placeholder_text='Введите жанр книги')
    request_genre_etry.grid(row=0, column=4, padx=5, pady=5, sticky="n")
    ganre_request = customtkinter.CTkButton(request_frame, text='Найти', command=genre_request).grid(row=0,
                                                                                                     column=5,
                                                                                                     padx=5,
                                                                                                     pady=5,
                                                                                                     sticky="n",
                                                                                                     columnspan=1)
    # Рамка дляя выхода
    exit_frame = customtkinter.CTkFrame(BIG_FRAME, corner_radius=15)
    exit_frame.grid(row=2, column=0, padx=5, pady=2, sticky="n")
    exit_btn = customtkinter.CTkButton(exit_frame, text='Назад в меню', command=exit,
                                       fg_color='red').grid(row=0,
                                                            column=1,
                                                            padx=5,
                                                            pady=5,
                                                            sticky="n",
                                                            columnspan=1)
    # Таблица
    heads = ['№КНИГИ', 'АВТОР', 'НАЗВАНИЕ', 'ЖАНР', 'КОЛ-ВО']
    table_book = ttk.Treeview(take_book_frame, show='headings')
    table_book['columns'] = heads

    for header in heads:
        table_book.heading(header, text=header, anchor='center')
        table_book.column(header, anchor='center')
    for row in book_result:
        table_book.insert('', END, values=row)

    # Скроллер
    scroller = customtkinter.CTkScrollbar(take_book_frame, command=table_book.yview, fg_color=None)
    scroller.grid(row=0, column=1, padx=0, pady=15, sticky="nsew")
    # Дополнения для таблицы и её упаковка
    table_book.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
    table_book.configure(yscrollcommand=scroller.set)


def edit_click():
    toplevel_help = customtkinter.CTkToplevel(root)
    toplevel_help.title("Справка")
    toplevel_help.grab_set()
    f = open("help.txt", "r", encoding="UTF8").read()
    Label(toplevel_help, text=f, font='Times 15').grid(row=0)


mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label='Справка', command=edit_click)
#############################################################################################
main_frame = customtkinter.CTkFrame(root, corner_radius=1, fg_color=None)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid(row=0, column=0, sticky="nsew")
#############################################################################################
user_btn = customtkinter.CTkButton(main_frame, text='Войти как пользователь', command=user,
                                   fg_color='#979aaa').grid(row=0,
                                                            column=0,
                                                            padx=20,
                                                            pady=10, sticky="nswe")

admin_btn = customtkinter.CTkButton(main_frame, text='Войти как сотрудник', command=admin,
                                    fg_color='#979aaa').grid(row=0,
                                                             column=1,
                                                             padx=20,
                                                             pady=10, sticky="nswe")

root.mainloop()
