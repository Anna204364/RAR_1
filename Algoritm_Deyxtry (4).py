# функции кнопок
#заполнение таблицы из списка графа
def view_tabl1(graf1, tbl1):
    for a in graf1:
         tbl1.insert("" , "end",    text=len(tbl1.get_children()) + 1, values=(a[0],  a[1], a[2], "Заполнено из graf1"))
#добавить строку с новыми данными в таблицу
def add_row_in_tbl1():
    clean_ent()
    #sts_add= "  Введите данные для новой записи "
    l13_from['text'] = sts_add    
    fr13.pack(expand =0 , fill = BOTH)
 #"Редактировать " - функция олучения данных из строки таблицы в форму редатирования
def edit_row_in_tbl1():
    if not tbl1.selection():
        #sts_str = "Не выбрана строка"
        l13_from['text'] = sts_str
        fr13.pack(expand =0 , fill = BOTH)
    # Получаем id первого выделенного элемента
    selected_item = tbl1.selection()[0]
    # Получаем значения в выделенной строке
    values = tbl1.item(selected_item, option="values")
    #print(values[0], values[1], values[2], values[3])
    clean_ent()
    e_from.insert(0,  values[0])
    e_to.insert(0,  values[1])
    e_w.insert(0,  values[2])
    e_d.insert(0,  values[3])
    #sts_edit= "  Данные для редактирования строки таблицы "
    l13_from['text'] = sts_edit
    fr13.pack(expand =0 , fill = BOTH)
#функция очистки данных из  формы редактирования данных строки
def clean_ent():
    e_from.delete(0,  END)
    e_to.delete(0,  END)
    e_w.delete(0,  END)
    e_d.delete(0,  END)  
#"Применить"функция считывания данных из строки таблицы в форму коректировки 
def edit_val_row():#редактировать строку
    if l13_from.cget("text") == sts_edit:
        selected_item = tbl1.selection()[0]
        tbl1.item(selected_item, values=(e_from.get() ,  e_to.get(), e_w.get(), e_d.get() ))
        edit_row_in_tbl1()
        
    if l13_from.cget("text") == sts_add: #добавить строку
        tbl1.insert("" , "end",    text=len(tbl1.get_children()) + 1, values=(e_from.get() ,  e_to.get(), e_w.get(), "Заполнено из программы"))
        
#функция формирует список графов
def read_tbl1():
    graf = []
    for row_id  in tbl1.get_children():
        row = tbl1.item(row_id)['values']
        r = (row[0], row[1], row[2])
        graf.append (r)
    return graf
# отображение графа на форме
def graf_form():
    graf1 = read_tbl1()
    fr14 = Frame(f1)
    fr14.pack(expand = 0 , fill = BOTH)
    l141_from =Label(fr14,  text="Сформированная матрица графа для последующих вычислений:", fg ='red')
    l141_from.grid(column=0, row=0, columnspan=6)
    l142_from =Label(fr14,  text=graf1, fg ='blue')
    l142_from.grid(column=0, row=1, columnspan=6)
    l22_from.config(text = graf1)

#функция на основе графа  строит визуализацию кнопка "Просмотр графа "
def  view_graf():
    graf = read_tbl1()
    G1= nx.DiGraph()
    G1.add_weighted_edges_from(graf)
    net1 = Network()
    net1.from_nx(G1)
    for node in net1.nodes:
        node['shape'] = 'circle'
    for ed in net1.edges:
        ed['label'] = ed['weight']
    #net1.show_buttons()
    net1.show("graf1_file.html")

    """frame = HtmlFrame(f1)
    fl = 'file:///C:/Users/petro/Downloads/graf1_file.html'
    #frame.load_file (fl, decode=None, force=False)
    frame.add_html(fl)
    frame.pack(fill="both", expand=0)"""
    

#функция кнопка "Данные \n по умолчанию",
def default():
    graf1 = [(1,2,3), (1,3,5),(1,4,4),(1,5,6),(1,6,13),(2,1,3),(2,3,3),(2,4,4),(2,5,5),(2,6,1),(3,1,5),(3,2,3),(3,4,6),(3,5,5),(3,6,2),(4,1,4),(4,2,4),(4,3,6),(4,5,5),(4,6,3),(5,1,6),(5,2,5),(5,3,5),(5,4,5),(5,6,4),(6,1,13),(6,2,1),(6,3,2),(6,4,3),(6,5,4)]
    #заполнение таблицы из списка graf1
    view_tabl1(graf1, tbl1)

#функция кнопка "Удалить все \n по записи",
def clean_tbl():
    for row_id  in tbl1.get_children():
        tbl1.delete(row_id)

    
#Основная программа форма
from tkinter import *
import tkinter.ttk as ttk
#from tkinterweb import HtmlFrame
import networkx as nx
from pyvis.network import Network
import numpy as np
import math

sts_str = "Не выбрана строка"
sts_edit= "  Данные для редактирования строки таблицы "
sts_add= "  Введите данные для новой записи "
 
root = Tk()
root.title('Расчет минимального пути')
root.geometry('500x450')

nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')
f1 = Text(root)
f2 = Text(root)
nb.add(f1, text='Ввод данных')
nb.add(f2, text='Алгоритм Дейкстры')

#закладка Ввод данных
fr11 = Frame(f1, bg='grey')
fr11.pack(expand = 0 , fill = BOTH)
#таблица
tbl1 = ttk.Treeview(fr11)
tbl1.grid(row=1)
# столбцы - заголовки
tbl1['columns'] = ("#0","#1","#2","#3","#4")
tbl1.heading("#0",text="#",anchor=CENTER)
tbl1.heading("#1",text="Из узла",anchor=CENTER)
tbl1.heading("#2",text="В узел",anchor=CENTER)
tbl1.heading("#3",text="Расстояние (вес)",anchor=CENTER)
tbl1.heading("#4",text="Примечание",anchor=CENTER)
#размеры столбцов
tbl1.column("#0", width=30 )
tbl1.column("#1", width=50)
tbl1.column("#2", width=50)
tbl1.column("#3", width=100)
tbl1.column("#4", width=120)
tbl1.pack(expand =0 , fill = BOTH)
#группа кнопок команд
fr12 = Frame(f1)
fr12.pack(expand = 0 , fill = BOTH)
button0 = Button(fr12, text="Добавить ",  width=15, command=add_row_in_tbl1)
button0.grid(column=0, row=1)
button1 = Button(fr12, text="Редактировать ",  width=15, command=edit_row_in_tbl1)
button1.grid(column=1, row=1)
button2 = Button(fr12, text="Просмотр графа ",  width=15, command=view_graf)
button2.grid(column=2, row=1)
button3 = Button(fr12, text="Данные \n по умолчанию",  width=15, command=default)
button3.grid(column=0, row=2)
button5 = Button(fr12, text="Удалить все \n  записи",  width=15, command=clean_tbl)
button5.grid(column=1, row=2)
button6 = Button(fr12, text="Матрица графа \n  (список)",  width=15, command=graf_form)
button6.grid(column=2, row=2)
#группа кнопок для редактирования строк в таблице
fr13 = Frame(f1)
fr13.pack_forget ()
l13_from =Label(fr13,  text="x", fg ='red')
l13_from.grid(column=0, row=0, columnspan=2)
l_from =Label(fr13,  text="Из узла")
l_from.grid(column=0, row=3)
e_from =Entry(fr13, width=10)
e_from.grid(column=1, row=3)
l_to =Label(fr13,  text="В узел")
l_to.grid(column=0, row=4)
e_to =Entry(fr13, width=10)
e_to.grid(column=1, row=4)
l_w =Label(fr13,  text="Расстояние (вес)")
l_w.grid(column=0, row=5)
e_w =Entry(fr13, width=10)
e_w.grid(column=1, row=5)
l_d =Label(fr13,  text="Примечание")
l_d.grid(column=0, row=6)
e_d =Entry(fr13, width=50)
e_d.grid(column=1, row=6)
button4 = Button(fr13, text="Применить",  width=15, command=edit_val_row)
button4.grid(column=1, row=7)
#fr13.pack(expand =1 , fill = BOTH)

#закладка Алгоритм Дейкстры

# связи узла выбранный узел - связанные узлы и вес
def node_edge(node, gr):
    g_node = []
    for a in gr:
        if str(a[0]) == node:
            g_node.append(a)
    return(g_node)

#Кнопка "Симметричная \n матрица"
def sim_mtrx():
     graf1 = read_tbl1()
     G1= nx.DiGraph()
     G1.add_weighted_edges_from(graf1)
     G1_n = sorted(G1.nodes)
     c_n = int (G1.number_of_nodes()) #кол-во узлов в графе
     #D = np.append((c_n, c_n))
     D =np.full( (c_n, c_n), np.inf) #аготовка матрицы  D с заполнеными бесконечностями
     #заполнение симметричной матрицы D из графа
     for a1 in G1_n:
        st = node_edge(str(a1), graf1)
        for a2 in st:
            D[G1_n.index( a1)] [G1_n.index( a2[1]) ] = a2[2]
            D[G1_n.index( a2[1] )] [G1_n.index( a1) ] = a2[2]
     l23_from.config(text = D)
     return (D)

#
def arg_min(T, S):
    amin = -1
    m = math.inf  # максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin

# формирование оптимального маршрута:
"""def opt_route(n,e):
    start = int(n)
    end = int(e)
    P = [end]
    while end != start:
        end = M[P[-1]]
        P.append(end)
    
    return(P)"""
    
#Кнопка "Рассчитать \n кратчайший путь",
def simulatte():
    D = sim_mtrx() 
    N = len(D)  # число вершин в графе
    T = [math.inf]*N   # "последняя строка таблицы"
    v = 0       # стартовая вершина (нумерация с нуля)
    S = {v}     # просмотренные вершины
    T[v] = 0    # нулевой вес для стартовой вершины
    M = [0]*N   # оптимальные связи между вершинами
    while v != -1:          # цикл, пока не просмотрим все вершины 
        for j, dw in enumerate(D[v]):   # перебираем все связанные вершины с вершиной v
            if j not in S:           # если вершина еще не просмотрена
                w = T[v] + dw
                if w < T[j]:
                    T[j] = w
                    M[j] = v        # связываем вершину j с вершиной v

        v = arg_min(T, S)            # выбираем следующий узел с наименьшим весом
        if v >= 0:                    # выбрана очередная вершина
            S.add(v)                 # добавляем новую вершину в рассмотрение
    #пояснение расчета на форму
    RM = [] # список для итоговых данных
    txt = "Минимальные расстояния от точки узел 1" 
    i =0
    for b in T:
        i = i+1 #смещение число для вывода на форму +1, так как в массиве у нас нумерация с 0
        start = 0
        end = i-1
        P = [end]
        while end != start:
            end = M[P[-1]]
            P.append(end)    # список оптимального маршрута от узла    start до end
        f =list(map(lambda x: x+1, P)) #смещение число для вывода на форму +1,
        RM.append( [i, b , sorted(f)])
        txt = txt + "\n до узла " +str(i) + " min составляет =" + str(b) + " оптимальный маршрут: " + str(sorted(f))
    #l24_from.config(text = txt)
    k=5 # с какой строки в форме интерфейса начинаем писать
    for c in RM:
        k =k+1
        l21_c0 =Label(lf_3,  text= "От узла 1 до узла: " + str(c[0]) )
        l21_c0.grid(column=0, row=k, sticky = 'w') 
        l21_c1 =Label(lf_3,  text= " min составляет =" +  str( int(c[1])) )
        l21_c1.grid(column=1, row=k, sticky = 'w') 
        t_rout = (" => ".join(map(str, c[2])))
        l21_c2 =Label(lf_3,  text= "  оптимальный маршрут:  "  +  t_rout, relief=RIDGE)
        l21_c2.grid(column=2, row=k, columnspan=3, sticky = 'w') 


fr21 = Frame(f2)
fr21.pack(expand = 0 , fill = BOTH)

lf_1 = LabelFrame(fr21, text="Исходные даные графа")
lf_1.pack(expand = 0 , fill = X)

l21_from =Label( lf_1,  text="На основе данных матрицы графа:")
l21_from.grid(column=0, row=0, columnspan=6)
l22_from =Label( lf_1,  text="", fg ='blue')
l22_from.grid(column=0, row=1, columnspan=6)


lf_2 = LabelFrame(fr21, text="Вспомогательные данные")
lf_2.pack(expand = 0 , fill = X)

button7 = Button( lf_2, text="Симметричная \n матрица",  width=15, command=sim_mtrx)
button7.grid(column=0, row=2)

fr21 = Frame(f2)
fr21.pack(expand = 0 , fill = BOTH)

l23_from =Label(lf_2,  text="", fg ='blue')
l23_from.grid(column=1, row=2, columnspan=5,  rowspan=3 )

lf_3 = LabelFrame(fr21, text="Результаты вычислений")
lf_3.pack(expand = 0 , fill = X)

button8 = Button( lf_3, text="Рассчитать \n кратчайший путь",  width=15, command=simulatte)
button8.grid(column=0, row=3)
l24_from =Label( lf_3,  text="", fg ='red')
l24_from.grid(column=2, row=3, columnspan=5)

root.mainloop()
