  
from tkinter import Tk, Label, Button, StringVar, W, E, filedialog
from tkinter import *
import calculadora

class calculadoraGui:

    def __init__(self, master):
        self.master = master
        master.title("Calculadora Hash")

        self.Archivo = ""
        self.sha1hash = ""
        self.sha224hash = ""
        self.sha256hash = ""
        self.sha384hash = ""
        self.sha512hash = ""
        self.hmac = ""
        self.hmac_md5 = ""
        self.hmac_256 = ""
        self.hmac_512 = ""
        self.md5hash = ""
        self.md4hash= ""
        self.textoA=" "
        self.clave=""

        self.filename_label_text = StringVar()
        self.filename_label_text.set(self.Archivo)
        self.filename_label = Label(master, textvariable=self.filename_label_text)
        self.textoA_label_text= StringVar()
        self.textoA_label_text.set(self.textoA)
        self.textoA_label= Label(master,textvariable=self.textoA_label_text,wraplength=600,relief='solid',pady=30,padx=150)
        # self.clave_label_text=StringVar()
        # self.clave_label_text.set(self.clave)
        self.clave_label= Label(master,text="Ingrese clave")
        self.entry=Entry(master,bd=5,width=20)
        # h=Scrollbar(master)
        # h.pack(side=RIGHT,fill=Y)
        # self.v=Scrollbar(self.master,orient='vertical',command=self.on_scrollbar_y)
        # self.Textbox.configure(yscrollcommand=self.h.set)


        # h.pack(side='right',fill='y')


        self.sha1hash_label_text = StringVar()
        self.sha1hash_label_text.set(self.sha1hash)
        self.sha1hash_label = Label(master, textvariable=self.sha1hash_label_text)
        self.sha224hash_label_text = StringVar()
        self.sha224hash_label_text.set(self.sha224hash)
        self.sha224hash_label = Label(master, textvariable=self.sha224hash_label_text)
        self.sha256hash_label_text = StringVar()
        self.sha256hash_label_text.set(self.sha256hash)
        self.sha256hash_label = Label(master, textvariable=self.sha256hash_label_text)
        self.sha384hash_label_text = StringVar()
        self.sha384hash_label_text.set(self.sha384hash)
        self.sha384hash_label = Label(master, textvariable=self.sha384hash_label_text)
        self.sha512hash_label_text = StringVar()
        self.sha512hash_label_text.set(self.sha512hash)
        self.sha512hash_label = Label(master, textvariable=self.sha512hash_label_text)
        self.hmac_label_text = StringVar()
        self.hmac_label_text.set(self.hmac)
        self.hmac_label = Label(master, textvariable=self.hmac_label_text)
        self.hmac_md5_label_text = StringVar()
        self.hmac_md5_label_text.set(self.hmac_md5)
        self.hmac_md5_label = Label(master, textvariable=self.hmac_md5_label_text)
        self.hmac_256_label_text = StringVar()
        self.hmac_256_label_text.set(self.hmac_256)
        self.hmac_256_label = Label(master, textvariable=self.hmac_256_label_text)
        self.hmac_512_label_text = StringVar()
        self.hmac_512_label_text.set(self.hmac_512)
        self.hmac_512_label = Label(master, textvariable=self.hmac_512_label_text)
        self.md5hash_label_text = StringVar()
        self.md5hash_label_text.set(self.md5hash)
        self.md5hash_label = Label(master, textvariable=self.md5hash_label_text)
        self.md4hash_label_text = StringVar()
        self.md4hash_label_text.set(self.md4hash)
        self.md4hash_label = Label(master, textvariable=self.md4hash_label_text)


        self.title_textoA_label=Label(master,text="Contenido del archivo:")
        self.title_filename_label = Label(master, text="Archivo a usar:")
        self.title_sha1hash_label = Label(master, text="SHA-1 Hash:")
        self.title_sha224hash_label = Label(master, text="SHA-224 Hash:")
        self.title_sha256hash_label = Label(master, text="SHA-256 Hash:")
        self.title_sha384hash_label = Label(master, text="SHA-384 Hash:")
        self.title_sha512hash_label = Label(master, text="SHA-512 Hash:")
        self.title_hmac_label = Label(master, text="HMAC SHA1:")
        self.title_hmac_md5_label = Label(master, text="HMAC-MD5 Hash:")
        self.title_hmac_256_label = Label(master, text="HMAC-SHA256 Hash:")
        self.title_hmac_512_label = Label(master, text="HMAC-SHA512 Hash:")
        self.title_md5hash_label = Label(master, text="MD5 Hash:")
        self.title_md4hash_label = Label(master, text="MD4 Hash:")


        # self.mostrar_button= Button(master,text="Mostrar", command=lambda: self.update("Mostrar Archivo"))
        self.browse_button = Button(master, text="Abrir Archivo", command=lambda: self.update("Abrir Archivo"))
        self.generate_button = Button(master, text="Generar", command=lambda: self.update("Generar"))
        self.reset_button = Button(master, text="Limpiar", command=lambda: self.update("limpiar"))
        self.save_button=Button(master,text="Guardar clave",command=lambda:self.update("save"))

        # Layout
        self.title_filename_label.grid(row=0, column=0, sticky=W)
        self.browse_button.grid(row=0, column=4, sticky=W+E)
        self.filename_label.grid(row=0, column=1, columnspan=3, sticky=W)
        self.generate_button.grid(row=2, column=0, columnspan=4, sticky=W+E)
        self.reset_button.grid(row=2, column=4, sticky=W+E)
        self.save_button.grid(row=3,column=4,sticky=W+E,columnspan=3)


        self.clave_label.grid(row=3,column=0,sticky=W,columnspan=3)
        self.entry.grid(row=3,column=1,sticky=W,columnspan=4)
        self.title_textoA_label.grid(row=4, column=0,sticky=W)
        self.title_md4hash_label.grid(row=11, column=0, sticky=W)
        self.md4hash_label.grid(row=11, column=1, columnspan=4, sticky=W)
        self.title_md5hash_label.grid(row=12, column=0, sticky=W)
        self.md5hash_label.grid(row=12, column=1, columnspan=4, sticky=W)
        self.title_sha1hash_label.grid(row=13, column=0, sticky=W)
        self.sha1hash_label.grid(row=13, column=1, columnspan=4, sticky=W)

        self.title_sha256hash_label.grid(row=14, column=0, sticky=W)
        self.sha256hash_label.grid(row=14, column=1, columnspan=4, sticky=W)
        self.title_sha224hash_label.grid(row=15, column=0, sticky=W)
        self.sha224hash_label.grid(row=15, column=1, columnspan=4, sticky=W)
        self.title_sha384hash_label.grid(row=16, column=0, sticky=W)
        self.sha384hash_label.grid(row=16, column=1, columnspan=4, sticky=W)
        self.title_sha512hash_label.grid(row=17, column=0, sticky=W)
        self.sha512hash_label.grid(row=17, column=1, columnspan=4, sticky=W)

        self.title_hmac_label.grid(row=18, column=0, sticky=W)
        self.hmac_label.grid(row=18, column=1, columnspan=4, sticky=W)
        self.title_hmac_md5_label.grid(row=19, column=0, sticky=W)
        self.hmac_md5_label.grid(row=19, column=1, columnspan=4, sticky=W)
        self.title_hmac_256_label.grid(row=20, column=0, sticky=W)
        self.hmac_256_label.grid(row=20, column=1, columnspan=4, sticky=W)
        self.title_hmac_512_label.grid(row=21, column=0, sticky=W)
        self.hmac_512_label.grid(row=21, column=1, columnspan=4, sticky=W)

        
        self.textoA_label.grid(row=4,column=0,sticky=W,columnspan=4,rowspan=4,pady=6)
        # self.h.grid(row=0,column=5,sticky='ns',columnspan=21)
       

    def update(self, method):
        if method == "Abrir Archivo":
            self.clearFields()
            root = Tk()
            file = filedialog.askopenfile(parent=root, mode='rb', title='Seleccione archivo .txt',filetypes=(("text files","*.txt"),("todos los archivos","*.")))
            if file != None:
                self.Archivo = file.name
                self.filename_label_text.set(self.Archivo)
                variable=open(self.Archivo,encoding='utf-8')
                self.textoA=variable.read()
                self.textoA_label_text.set(self.textoA)
            root.withdraw()
        elif method=="save":
            self.clave=self.entry.get()
            print(self.clave)
        elif method == "Generar":
            if (self.clave==""):
              self.entry.delete(0,END)
              self.entry.insert(0,"Guarde la clave")
              # self.entry.delete(0,END)
            else:
              Hashes = calculadora.generateHash(self.Archivo,self.clave)
              self.sha1hash = Hashes['sha1']
              self.sha1hash_label_text.set(self.sha1hash)
              self.sha224hash = Hashes['sha224']
              self.sha224hash_label_text.set(self.sha224hash)
              self.sha256hash = Hashes['sha256']
              self.sha256hash_label_text.set(self.sha256hash)
              self.sha384hash = Hashes['sha384']
              self.sha384hash_label_text.set(self.sha384hash)
              self.sha512hash = Hashes['sha512']
              self.sha512hash_label_text.set(self.sha512hash)
              self.hmac_md5 = Hashes['hmacmd5']
              self.hmac_md5_label_text.set(self.hmac_md5)
              self.hmac_256 = Hashes['hmac256']
              self.hmac_256_label_text.set(self.hmac_256)
              self.hmac_512 = Hashes['hmac512']
              self.hmac_512_label_text.set(self.hmac_512)
              self.md5hash = Hashes['md5']
              self.md5hash_label_text.set(self.md5hash)
              self.md4hash = Hashes['md4']
              self.md4hash_label_text.set(self.md4hash)
              self.hmac = Hashes['hmac']
              self.hmac_label_text.set(self.hmac)
        else: # reset
            self.clearFields()

    def clearFields(self):
       
        self.Archivo = "..."
        self.filename_label_text.set(self.Archivo)
        self.clave=""
        self.entry.delete(0,END)
        self.textoA=""
        self.textoA_label_text.set(self.textoA)
        self.sha1hash = "..."
        self.sha1hash_label_text.set(self.sha1hash)
        self.sha224hash = "..."
        self.sha224hash_label_text.set(self.sha224hash)
        self.sha256hash = "..."
        self.sha256hash_label_text.set(self.sha256hash)
        self.sha384hash = "..."
        self.sha384hash_label_text.set(self.sha384hash)
        self.sha512hash = "..."
        self.sha512hash_label_text.set(self.sha512hash)
        self.hmac = "..."
        self.hmac_label_text.set(self.hmac)
        self.hmac_md5 = "..."
        self.hmac_md5_label_text.set(self.hmac_md5)
        self.hmac_256 = "..."
        self.hmac_256_label_text.set(self.hmac_256)
        self.hmac_512 = "..."
        self.hmac_512_label_text.set(self.hmac_512)
        self.md5hash = "..."
        self.md5hash_label_text.set(self.md5hash)
        self.md4hash = "..."
        self.md4hash_label_text.set(self.md4hash)

root = Tk()
root.geometry('990x560') 
my_gui = calculadoraGui(root)
root.mainloop()