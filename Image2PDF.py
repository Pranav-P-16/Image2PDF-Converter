import os,img2pdf,random,webbrowser
from PySimpleGUI import *

def alert(tx):
    theme("Topanga")
    lyt=[[Text("\t")]+[Text(tx,font=("Helvetica",15))]+[Text("\t")],
         [Button("OK",button_color="red",size=(10,1))]]
    wnd=Window("Alert !!!",lyt,element_justification="c",keep_on_top=True)
    event,values=wnd.read()
    wnd.close()
def activity(out,inp):
    lst=[]
    n=random.randint(1,100)
    p=random.randint(1,100)
    for i in os.listdir(inp):
        if i.endswith(".jpg"):
            lst.append(inp+"/"+i)
        elif i.endswith(".png"):
            lst.append(inp+"/"+i)
        elif i.endswith(".jpeg"):
            lst.append(inp+"/"+i)
    try:
        with open(out+"/output"+str(n)+str(p)+".pdf","wb") as f:
            f.write(img2pdf.convert(lst))
        theme("BrightColors")
        lt=[[Text("\tCompiled and Saved Successfully as\t",font=("Chilanka",15))],[Text(out+"/output"+str(n)+str(p)+".pdf",font=("Helvetica",15))],[Button("Home",size=(10,1))]+[Button("Show",size=(10,1))]]
        wn=Window("Success",lt,element_justification="c")
        e,v=wn.read()
        wn.close()
        if e=="Home" or e==None:
            mn()
        else:
            webbrowser.open_new(out+"/output"+str(n)+str(p)+".pdf")
    except ValueError:
        alert("No Images Found in Input Folder")
        dp()
    except:
        theme("HotDogStand")
        lt=[[Text("Task Failed as",font=("Chilanka",15))],[Text(out+"/output"+str(n)+str(p)+".pdf",font=("Helvetica",15))],[Button("Retry",size=(10,1))]+[Button("Home",size=(10,1))]]
        wn=Window("Failed",lt)
        e,v=wn.read()
        wn.close()
        try:
            os.remove(out+"/output"+str(n)+str(p)+".pdf")
        except:
            pass
        if e=="Home" or e==None:
            mn()
        else:
            activity(out,inp)
def help_():
    theme("DarkBrown")
    lt=[[Text("## HELP ##",font=("Helvetica",20))],
            [Text("---------------------------",font=("Helvetica",20))],
            [Text("* Move all your required images to a New Folder\n* Then select Input Folder as that Folder\n* Select output folder to where pdf created should be saved\n* .png , .jpg and .jpeg image formats are supported\n* Compiled and Created by PR@16 Creations\n* Credits: PR@16 Creations",font=("Helvetica",15))],
            [Text("---------------------------",font=("Helvetica",20))],
            [Button("OK",size=(80,2),button_color=("green2","black"))]]
    wn=Window("Help",lt)
    e,v=wn.read()
    wn.close()
    mn()
def dp():
    theme("DarkTeal7")
    lt=[[Text("Select Input Folder",font=("Chilanka",20))],[Input()]+[FolderBrowse()],[Text()],
        [Text("Select Output Folder",font=("Chilanka",20))],[Input()]+[FolderBrowse()],
        [Text()],
        [Button("Proceed",size=(10,1))]+[Button("Abort",size=(10,1))]]
    wn=Window("Configurations",lt)
    e,v=wn.read()
    wn.close()
    if e=="Abort":
        mn()
    elif e==None:
        mn()
    else:
        if v["Browse"] != "":
            if v["Browse0"] != "":
                activity(v["Browse0"],v["Browse"])
            else:
                dp()
        else:
            dp()
def mn():
    theme("BrightColors")
    layout1=[[Text("\nImage 2",font=("Chilanka",25))],[Text("PDF Converter\n",font=("Chilanka",25))],[Button("Start",font=("Helvetica",20),button_color=("black","green2"),size=(100,1),bind_return_key=True)],
                             [Button("Help",font=("Helvetica",20),size=(100,1),button_color=("black","yellow"),bind_return_key=True)],
                             [Button("Exit",font=("Helvetica",20),size=(100,1),button_color=("black","red"),bind_return_key=True)],[Text()],
                             [Text("\nVersion 2.5.0",font=("Chilanka"))]]
    window1=Window("Image 2 PDF Converter",layout1,size=(390, 400),element_justification="c")
    event,values=window1.read()
    window1.close()
    if event=="Start":
        dp()
    elif event=="Help":
        help_()
    else:
        exit()
mn()
