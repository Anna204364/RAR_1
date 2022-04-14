#Производственная задача, линейное программирование + график
from tkinter import * #Импортируем библиотеку по созданию графического интерфейса
import numpy as np #Импортируем библиотеку для математических вычислений
import matplotlib.pyplot as plt #Импортируем библиотеку для визуализации данных
   
def Draw(): 
    # Создаём рисунок с координатной плоскостью
    from matplotlib import ticker

    fig = plt.subplots()
    # Создаём область, в которой будет
    # - отображаться график
    x = np.arange(-1,170, 50)
    #x = np.linspace(-4, 16, 100)
    #  Устанавливаем интервал основных делений:
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
    #  Устанавливаем интервал вспомогательных делений:
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
    #  Добавляем подписи к осям:
    ax.set_xlabel('Товар X1', labelpad=-10)
    ax.set_ylabel('Товар X2', labelpad=-10)
    
    #Задаем ограничительные функции
    m1 = lambda x: int(t_mat1.get()) / int( t_prod21.get()) - int(t_prod11.get()) *x / int(t_prod21.get())
    m1_1 = 'X2=' + str(int(t_mat1.get()) / int( t_prod21.get())) + "-" + str(int(t_prod11.get()) / int(t_prod21.get())) + "*X1"

    m2 = lambda x: int(t_mat2.get()) / int( t_prod22.get()) - int(t_prod12.get()) *x / int(t_prod22.get())
    m2_2 ='X2=' + str(int(t_mat2.get()) / int( t_prod22.get())) + "-" + str(int(t_prod12.get()) / int(t_prod22.get())) + "*X1"

    m3 = lambda x: int(t_mat3.get()) / int( t_prod23.get()) - int(t_prod13.get()) *x / int(t_prod23.get())
    m3_3 ='X2=' + str(int(t_mat3.get()) / int( t_prod23.get())) + "-" + str(int(t_prod13.get()) / int(t_prod23.get())) + "*X1"   
    
    f0  = lambda x: 0 / int(t_price2.get()) -int(t_price1.get()) * x / int(t_price2.get())
    
    #Выводим на форму функции m1, m2, m3
    l_RRR4 = Label(root, text =m1_1 + '\n' + m2_2 + '\n' + m3_3)
    l_RRR4.grid(column=5, row=10, columnspan=2) 
    
    #Вычисление координат точки с высокой эффективностью, пересечение графика Материал 1 и Материал 2
    t_x1_max = m1_1[3:] +  '=' + m2_2[3:] 
    l_RRR5 = Label(root, text= t_x1_max)
    l_RRR5.grid(column=0, row=12, columnspan=2)
    
    #Рассчитаем координаты точки максимума эффективности
    l_RRR6 = Label(root, text= t_x1_max)
    X1_c = int(t_mat2.get()) / int( t_prod22.get()) - int(t_mat1.get()) / int( t_prod21.get())
    X1_k = -int(t_prod11.get()) / int(t_prod21.get()) + int(t_prod12.get()) / int(t_prod22.get())
    X1_max = str(X1_c) + '=' +str(X1_k) + '*X1'
    X2_max = str(int(t_mat2.get()) / int( t_prod22.get())) + '-' + str (int(t_prod12.get()) / int(t_prod22.get())) + '*' + str(X1_c/X1_k)
    X2_max_c = int(t_mat2.get()) / int( t_prod22.get()) - int(t_prod12.get()) / int(t_prod22.get())*(X1_c/X1_k)
    l_RRR6 = Label(root, text= t_x1_max +'\n' + X1_max + '\n x1 = ' + str(X1_c/X1_k) + '\n x2 = ' + X2_max + '\n X2 = ' + str(X2_max_c))
    l_RRR6.grid(column=0, row=12, columnspan=2)
    
    #Перенесем значения точки максимума на график и форму
    f_max =  t_price1.get() + '*' +  str(X1_c/X1_k) + '+' + t_price2.get() + '*' + str(X2_max_c)
    f_max_c =  int(t_price1.get()) *  (X1_c/X1_k) + int(t_price2.get()) * (X2_max_c)  
    l_RRR7 = Label(root, text= 'Максимум эффективности f1=' + f_max +'='+ str(f_max_c))
    l_RRR7.grid(column=0, row=13, columnspan=6)
    
    #Построим линии уровня по максимальной точке
    f1  = lambda x: (60*4+110*5) / int(t_price2.get()) -int(t_price1.get()) * x / int(t_price2.get())  
    plt.title('График производственной задачи', fontsize=12) #Нанесем заголовок

    #Отрисуем линейные графики на координатной плоскости
    plt.plot(x, m1(x), color='red')
    plt.plot(x, m2(x), color='blue')
    plt.plot(x, m3(x), color='green')
    plt.plot(x, f0(x), '--', color='grey')
    plt.plot(x, f1(x), '--', color='grey')
    plt.plot(60, 110, '.', color='black')
    
    plt.text(5, 90, l_mat1.cget("text") +': ' + m1_1, fontsize=8, color='red')
    plt.text(5, 170, l_mat2.cget("text") +': ' + m2_2, fontsize=8, color='blue')
    plt.text(5, 300, l_mat3.cget("text") +': ' + m3_3, fontsize=8, color='green')
    plt.text(5, 10, 'f0 -  минимум эффективности', fontsize=8, color='black')
    plt.text(60, 120, 'f1 -  максимум эффективности', fontsize=8, color='black')
    plt.text(80, 150, 'f1=' + f_max +'='+ str(f_max_c), fontsize=8, color='black')
    
    #Сохраненим изображение графика в файл
    plt.savefig('График.png') 

    img = Image.open('C://График.png')
    plt.show()
    
    #Добавим изображение
    #imm()
    
def Clean(): #Очищение всех полей формы
    t_mat1.delete(0,END)
    t_mat2.delete(0,END)
    t_mat3.delete(0,END)
    t_prod11.delete(0,END)
    t_prod12.delete(0,END)
    t_prod13.delete(0,END)
    t_prod21.delete(0,END)
    t_prod22.delete(0,END)
    t_prod23.delete(0,END)
    t_price1.delete(0,END)
    t_price2.delete(0,END)

def Default(): #Назначение значений по умолчанию
    Clean()
    t_mat1.insert(0, '560')
    t_mat2.insert(0, '170')
    t_mat3.insert(0, '300')
    t_prod11.insert(0, '2')
    t_prod12.insert(0, '1')
    t_prod13.insert(0, '2')
    t_prod21.insert(0, '4')
    t_prod22.insert(0, '1')
    t_prod23.insert(0, '1')
    t_price1.insert(0, '4')
    t_price2.insert(0, '5')

def RRR(): #Обработка входных данных в виде пояснений на форме
    l_RRR = Label(root, text="Ограничения задачи:")
    l_RRR.grid(column=0, row=9, columnspan=2)
    txt_usl1 = t_prod11.get() + '*X1 + ' + t_prod21.get() + '*X2 <= ' + t_mat1.get() 
    txt_usl2 = t_prod12.get() +'*X1 + ' + t_prod22.get() + '*X2 <= ' + t_mat2.get() 
    txt_usl3 = t_prod13.get() +'*X1 + ' + t_prod23.get() + '*X2 <= ' + t_mat3.get() 
    l_RRR1 = Label(root, text = txt_usl1 +  "\n" + txt_usl2 + "\n" + txt_usl3)
    l_RRR1.grid(column=0, row=10, columnspan=2)
    

    l_RRR3 = Label(root, text="Уравнения задачи:")
    l_RRR3.grid(column=3, row=9, columnspan=2)
    u1 = 'X2 = ' + t_mat1.get() + '/' + t_prod21.get() + " - " + t_prod11.get() + '*X1/' + t_prod21.get() 
    u2 = 'X2 = ' + t_mat2.get() + '/' + t_prod22.get() + " - " + t_prod12.get() + '*X1/' + t_prod22.get() 
    u3 = 'X2 = ' + t_mat3.get() + '/' + t_prod23.get() + " - " + t_prod13.get() + '*X1/' + t_prod23.get() 
    l_RRR2 = Label(root, text =u1 + '\n' + u2 + '\n' + u3)
    l_RRR2.grid(column=2, row=10, columnspan=2) 

    F = 'F= ' + t_price1.get() + '*X1 + ' + t_price2.get() + '*X2'
    l_RRR3 = Label(root, text="Эффективность (производительность)задается уравнением: " + F)
    l_RRR3.grid(column=0, row=11, columnspan=6)
   
root = Tk() #Текущая форма пользовательского интерфейса
root.title("Введите данные")
root.geometry('500x400') #Размер формы

label_title = Label(root, text="Производственная задача")
label_title.grid(column=0, row=1, columnspan=6)

l_mat0 = Label(root, text="Материалы")
l_mat0.grid(column=0, row=2, columnspan=2)
l_mat01 = Label(root, text="Наименование")
l_mat01.grid(column=0, row=3)
l_mat02 = Label(root, text="Кол-во")
l_mat02.grid(column=1, row=3)

l_mat1 = Label(root, text="Материал 1")
l_mat1.grid(column=0, row=4)
l_mat2 = Label(root, text="Материал 2")
l_mat2.grid(column=0, row=5)
l_mat3 = Label(root, text="Материал 3")
l_mat3.grid(column=0, row=6)
t_mat1 = Entry(root, width=10)
t_mat1.grid(column=1, row=4)
t_mat2 = Entry(root, width=10)
t_mat2.grid(column=1, row=5)
t_mat3 = Entry(root, width=10)
t_mat3.grid(column=1, row=6)

l_prod0 = Label(root, text="Товары (расход материалов)")
l_prod0.grid(column=2, row=2, columnspan=2)
l_prod1 = Label(root, text="Товар 1 = X1")
l_prod1.grid(column=2, row=3)
l_prod2 = Label(root, text="Товар 2 = X2")
l_prod2.grid(column=3, row=3)

t_prod11 = Entry(root, width=10)
t_prod11.grid(column=2, row=4)
t_prod12 = Entry(root, width=10)
t_prod12.grid(column=2, row=5)
t_prod13 = Entry(root, width=10)
t_prod13.grid(column=2, row=6)

t_prod21 = Entry(root, width=10)
t_prod21.grid(column=3, row=4)
t_prod22 = Entry(root, width=10)
t_prod22.grid(column=3, row=5)
t_prod23 = Entry(root, width=10)
t_prod23.grid(column=3, row=6)

l_price = Label(root, text="Стоимость товаров")
l_price.grid(column=0, row=7, columnspan=2)
t_price1 = Entry(root, width=10)
t_price1.grid(column=2, row=7)
t_price2 = Entry(root, width=10)
t_price2.grid(column=3, row=7)

#Добавление кнопок на форму
button = Button(root, text="Применить \n данные",  width=10, command=RRR)
button.grid(column=2, row=8)
button0 = Button(root, text="Назначить \n данные",  width=10, command=Default)
button0.grid(column=1, row=8)
button1 = Button(root, text="Очистить \n данные",  width=10, command=Clean)
button1.grid(column=0, row=8)
button1 = Button(root, text="Построить \n графики",  width=10, command=Draw)
button1.grid(column=3, row=8)

root.mainloop() #Запуск формы на просмотр пользователю