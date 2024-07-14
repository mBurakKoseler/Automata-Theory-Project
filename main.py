#  Gerekli kütüphaneler
import tkinter as tk
from tkinter import *
import ply.lex as lex
import random
import customtkinter
from PIL import ImageTk, Image
import turtle
import tkinter
from collections import Counter


#                                            AÇIlAN İLK ARAYÜZ / GUI

#Bu arayüz kullanıcıdan txt nin adını alır ve daha sonrasında txt dosyasının içine girerek random bir program satırı seçer.

#Ana pencere
form = customtkinter.CTk()
form.title('Çizen Robot ( Drawing robot ) Arayüzü')
canvas = tk.Canvas(form, height=650, width=1000)
canvas.pack()

#SOL ÜST ÇERÇEVE
frame_sol = tk.Frame(form, bg='black')
frame_sol.place(relx=0.1, rely=0.1, relwidth=0.23, relheight=0.5)

# Txt dosyasının adını almak için metin kutusu
entry = tk.Entry(frame_sol, fg='black', bg='white')
entry.pack(padx=15, pady=85)

# TXT dosyasından rastgele bir satır seçerek onu (global) değişkene atayan fonksiyon
def verial():
        global data #global olarak tanımlanan değişkenler kodun her yerinde kullanılabilir olur
        fname = entry.get() #txt dosyasının adını tutar
        lines = open(fname).read().splitlines() #dosyayı satır satır okur
        data = random.choice(lines) #satırlardan birini rastgele olarak seçer
        print(data)


#BUTON: def verial() fonksiyonunu çalıştırır
button = tk.Button(frame_sol,text='veri al',fg='white',bg='green',command=verial)
button.pack(side=tk.BOTTOM,fill=tk.X)

#SAĞ ÜST ÇERÇEVE
frame_sag = tk.Frame(form,bg='black')
frame_sag.place(relx=0.34,rely=0.1, relwidth=0.56, relheight=0.5)

# Bu buton program satırlarından birisi seçildikten sonra kullanıcıya çizimi göstermek için ARAYÜZÜ kapatıyor.
button = tk.Button(frame_sag, text="ŞEKLİN ÇİZİMİNİ GÖRMEK İÇİN TIKLAYINIZ.", fg='white',bg='green', command=form.destroy)
button.pack()

#ALT ÇERÇEVE
frame_alt = tk.Frame(form,bg='black')
frame_alt.place(relx=0.1,rely=0.65, relwidth=0.8, relheight=0.1)

form.mainloop() #Kodun sınırsız döngü içinde çalışmasını sağlar.



#                                                           LEX KISMI

# Programda geçebilecek tokenlerin listesi ( çalışması için zorunludur )
tokens = (
   'NUMBER',
   'COMMAND', #Tüm fonksiyon ifade eden harfleri kapsar
   'LPAREN',
   'RPAREN',
)

# Tokenların tanımlanması
t_LPAREN  = r'\['
t_RPAREN  = r'\]'
t_COMMAND  = r'[a-zA-Z_][a-zA-Z0-9_]*'

#Int sayıların tanımlanması
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore  = ' \t'     # Yok sayılan karakterler (boşluklar ve sekmeler) için

def t_error(t):       #Token olarak girilmemiş bir karakter olursa o satırı ' hatalı karakter ' olarak yazdırır
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()  #lexer yapısını kurar

#TXT'den gelen programı(data) lexer a girdi olarak verir
lexer.input(data)


# Önce tokenize/tokenlere ayırma işlemini yapar ve onları b.txt adında yeni bir dosyada satırlar halinde tutar.
while True:
    tok = lexer.token()
    if not tok:
        break
    f = open("b.txt", "a")
    lex_ifadesi = tok.value
    print(lex_ifadesi, file=f)

# b.txt dosyasını açar ve ordaki tokenleri sırasıyla onları lines adındaki diziye, dizinin elemanları olarak yazar.
lines = []
with open('b.txt') as f:
   lines = [line.rstrip() for line in f]

#Programın çalıştırılacağı sonraki seferlerde problem çıkmaması için b.txt dosyasını temizler
file = open("b.txt","r+")
file.truncate(0)
file.close()

print(lines) #tokenlerden oluşan dizi


#                                   PROGRAMIN TURTLE'DA ÇİZDİRİLMESİ

t = turtle.Turtle()
t.speed(10)  #kalem hızı ayarı
turtle.bgcolor("white")  #isteğe bağlı olarak turtle arka plan rengi değiştirilebilir
t.fillcolor("red")

# PEN KOMUTUNUN FONKSİYONSAL KARŞILIĞI :
def PEN(n):
    if n==1:
        t.pensize(1)
    elif n==2:
        t.pensize(2)
    elif n==3:
        t.pensize(3)
    else:
        t.pensize(1)
        print("1/2/3 kalınlıklarından birini seçmezseniz varsayılan kalem kalınlığında çizdirilir.")

# COLOR KOMUTUNUN FONKSİYONSAL KARŞILIĞI :
def COLOR(f):
    if f == "K":
        t.pencolor("red")
    elif f == "Y":
        t.pencolor("green")
    elif f == "M":
        t.pencolor("blue")
    elif f == "S":
        t.pencolor("black")
    elif f == "P":
        t.pencolor("pink")
    else:
        t.pencolor("black")
        print("Renk girmediğinizde ve ya tanımsız renk girdiğinizde Sistem siyah renk kullanır.")

PEN(1)        #Kalem kalınlığı seçme
COLOR('S')    #Kalem rengi seçme

#lines içinde tuttuğu diziyi fonksiyona sokmak için listeye yerleştirir.
global liste
liste= []
liste = lines


# 3 LOOP A KADAR ÇİZDİREBİLEN TURTLE FONKSİYONU

i = int(0)

if (liste[i] == 'L'):
    for x in range(int(liste[i+1])):

        if (liste[i+3] == 'L'):
            for y in range(int(liste[i + 4])):

                if (liste[i + 6] == 'L'):
                    for z in range(int(liste[i + 7])):

                        if (liste[i + 9] == 'F'):
                            t.forward(int(liste[i + 10]))

                        if (liste[i + 11] == 'R'):
                            t.right(int(liste[i + 12]))

                    if (liste[i + 14] == 'R'):
                        t.right(int(liste[i + 15]))


                else:
                  if (liste[i + 6] == 'F'):
                      t.forward(int(liste[i + 7]))

                  if (liste[i + 8] == 'R'):
                      t.right(int(liste[i + 9]))

            if (liste[i + 11] == 'R'):
                t.right(int(liste[i + 12]))

        else:
            if (liste[i+3] == 'F'):
                    t.forward(int(liste[i + 4]))

            if (liste[i+5] == 'R'):
                    t.right(int(liste[i + 6]))


#Fonksiyon çiziminin bir çerçevede gösterilmesi(ilerleyen aşamada eps dosyası olarak kaydedilebilmesi için)
canvas = t.getscreen().getcanvas()

canvas.postscript(file="file.eps")  #eps dosyası olarak turtle çıktısını kaydeder

#kaydedilen eps dosyasının görüntülenebilmesi için onu PNG dosyasına çevirir
img=Image.open("file.eps")
fig=img.convert("RGBA")
fig.save("File.png")

# İKİNCİ GUI = kullanıcıya görsel Karşılığını ve hata mesajlarını(varsa) göstermek için arayüz tekrar açılır

form = tkinter.Toplevel() #Yok edilen ilk GUI'nin İkinci GUI'yi engellememesi için
form.title('Çizen Robot ( Drawing robot ) Arayüzü')
canvas = tk.Canvas(form, height=650, width=1000)
canvas.pack()

frame_sol = tk.Frame(form, bg='black')
frame_sol.place(relx=0.1, rely=0.1, relwidth=0.23, relheight=0.5)

entry = tk.Entry(frame_sol, fg='black', bg='white')
entry.pack(padx=15, pady=85)

def verial():
        global data
        fname = entry.get()
        lines = open(fname).read().splitlines()
        data = random.choice(lines)
        print(data)

button = tk.Button(frame_sol,text='veri al',fg='white',bg='green',command=verial)
button.pack(side=tk.BOTTOM,fill=tk.X)

frame_sag = tk.Frame(form,bg='black')
frame_sag.place(relx=0.34,rely=0.1, relwidth=0.56, relheight=0.5)


#!PNG dosyasının sağ frame'in içine etiket olarak ekler ve gösterir
img = ImageTk.PhotoImage(Image.open("File.png"))
label = Label(frame_sag, image = img)
label.pack()

frame_alt = tk.Frame(form,bg='black')
frame_alt.place(relx=0.1,rely=0.65, relwidth=0.8, relheight=0.1)

#açılır kapanır parantez sayısı kontrolü yapar ve etiket olarak guide kullanıcıya gösterir.
c = Counter(liste)

if c['['] == c[']']:
    label = Label(frame_alt, text="Programda açılan ve kapanan köşeli parantez sayısı eşit." , bg="green", fg="white")
    label.pack()
else:
    label = Label(frame_alt, text="Programda açılan ve kapanan köşeli parantez sayısı eşit değil." , bg="green", fg="white")
    label.pack()

#Tanımsız komut ve ya karakter kontrolü

hataToplam =( c['A'] + c['B'] + c['C'] + c['D'] + c['E'] + c['G'] + c['Ğ'] + c['H'] + c['I']+ c['İ']+ c['J']+ c['K'] +
    c['M'] + c['N'] + c['O'] + c['P'] + c['S'] + c['T'] + c['U'] + c['V'] + c['Y']+ c['Z'] + c['!'] + c['*'] +
    c['/'] + c['.'] + c[','] + c[':'] + c['+'] + c['-'] + c['a']+ c['b'] + c['c'] + c['d'] + c['e'] + c['f'] + c['g'] +
    c['h'] + c['ı'] + c['i'] + c['j']+ c['k'] + c['l'] + c['m'] + c['n'] + c['o'] + c['p'] + c['s'] + c['t'] + c['u']
    + c['v'] + c['y'] + c['z'] + c['?'] )

if hataToplam != 0:
        label = Label(frame_alt, text="Tanımsız komut ve ya karakter kullandınız.", bg="green", fg="white")
        label.pack()

else:
    label = Label(frame_alt, text="Tanımsız komut ve ya karakter kullanmadınız.", bg="green", fg="white")
    label.pack()


#Komut sayısına eşit sayıda değer atanması yapılıp yapılmadığını kontrol etme
if c['F'] + c['R'] + c['L'] == len(liste) - (c['['] + c[']'] + c['F'] + c['R'] + c['L'] ):
    label = Label(frame_alt, text="Komut sayısına eşit sayıda değer atanması yapılmış.", bg="green", fg="white")
    label.pack()

else:
    label = Label(frame_alt, text="Komut sayısına eşit sayıda değer atanması yapılmamış.", bg="green", fg="white")
    label.pack()

# NOT: Kullanıcı komutların arasına yanlış komut girse bile şekli çizer ve hatayı belirtir.

form.mainloop()


