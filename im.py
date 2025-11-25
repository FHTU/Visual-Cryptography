from PIL import Image 
import random
import webbrowser
import tkinter.filedialog

in1 = tkinter.filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
in2 = tkinter.filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
re  = tkinter.filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])


a = Image.open(in1)
b = Image.open(in2)
c = Image.open(re)

x = y = 400

a = a.resize((x,y))
b = b.resize((x,y))
c = c.resize((x,y))

pixa = a.load()
pixb = b.load()
pixc = c.load()
    

m_add = 125
m_cor = 0
rea = [0,0,0,255]
pixa_s = [0,0,0,255]
pixb_s = [0,0,0,255]
pixc_s = [0,0,0,255]

for i in range(a.size[0]) :
    for j in range(a.size[1]) :
        rand = random.randint(0,3)
        if rand == 0:
            for k in range(3):
                pixa_s[k] = int(pixa[i,j][k] * ((m_add) / 255))
                choi = pixa_s[k]
                pixc_s[k] = int(pixc[i,j][k] * ((m_add) / 255)) + m_add + m_cor
                rea[k] = pixc_s[k] - choi

            pixb[i,j] = tuple(rea)
            pixa[i,j] = tuple(pixa_s)
            pixc[i,j] = tuple(pixc_s)

        elif rand == 1 : 
            for k in range(3):
                pixb_s[k] = int(pixb[i,j][k] * ((m_add) / 255))
                choi = pixb_s[k]
                pixc_s[k] = int(pixc[i,j][k] * ((m_add) / 255)) + m_add + m_cor
                rea[k] = pixc_s[k] - choi

            pixa[i,j] = tuple(rea)
            pixb[i,j] = tuple(pixb_s)
            pixc[i,j] = tuple(pixc_s)


            
        elif rand == 2 :
            for k in range(3):
                pixa_s[k] = int(pixa[i,j][k] * ((m_add) / 255))
                choi = pixa_s[k]
                pixc_s[k] = random.randint(125,255)
                rea[k] = pixc_s[k] - choi

            pixb[i,j] = tuple(rea)
            pixa[i,j] = tuple(pixa_s)
            pixc[i,j] = tuple(pixc_s)
        
        elif rand == 3 :
            for k in range(3):
                pixb_s[k] = int(pixb[i,j][k] * ((m_add) / 255))
                choi = pixb_s[k]
                pixc_s[k] = random.randint(125,255)
                rea[k] = pixc_s[k] - choi

            pixa[i,j] = tuple(rea)
            pixb[i,j] = tuple(pixb_s)
            pixc[i,j] = tuple(pixc_s)
        
        pixc_s = [0,0,0,255]
        pixb_s = [0,0,0,255]
        pixa_s = [0,0,0,255]
        rea = [0,0,0,255]


                

            

a.save('output/a_f.png')
b.save('output/b_f.png')
c.save('output/c_f.png')

dir = tkinter.filedialog.askdirectory()

a.save(f'{dir}/a_f.png')
b.save(f'{dir}/b_f.png')
c.save(f'{dir}/c_f.png')

webbrowser.open_new_tab('index.html')
input()

