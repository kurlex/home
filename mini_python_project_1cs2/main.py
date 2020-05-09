from pathlib import Path
from tkinter import *
from tkinter.messagebox import *
from functools import partial
import tkinter.ttk as kur
class style_OM(OptionMenu):
    def __init__(self,stri,master,status,*options):
        stri.set(status)
        OptionMenu.__init__(self,master,stri,*options)
        self.config(font=('ubuntu',10),bg="#ffd369",fg="#eee",width=12)
        self['menu'].config(font=('ubuntu',10),bg="#ffd369")
        self.bind("<Enter>",self.fun1)
        self.bind("<Leave>",self.fun2)
    def fun1(self,e):
         self['background']=self["activebackground"]
    def fun2(self,e):
         self['background']="#ffd369"
class style_BTN(Button):
    def __init__(self,master,**options):
        Button.__init__(self,master,**options)
        self.config(font=('ubuntu',10),bg="#ffd369",fg="#eee",width=12)
        self.bind("<Enter>",self.fun1)
        self.bind("<Leave>",self.fun2)
    def fun1(self,e):
         self['background']=self["activebackground"]
    def fun2(self,e):
         self['background']="#ffd369"
class style_BTN1(Button):
    def __init__(self,master,**options):
        Button.__init__(self,master,**options)
        self.config(font=('ubuntu',10),bg="#ffd369",fg="#eee",width=35)
        self.bind("<Enter>",self.fun1)
        self.bind("<Leave>",self.fun2)
    def fun1(self,e):
         self['background']=self["activebackground"]
    def fun2(self,e):
         self['background']="#ffd369"
def backi(a,b):
    
    global nbfl,jobof,offjob,jobappto,alljob
    f=open("skr_info.txt",'r')
    s=f.readlines()
    nbfl=len(s)
    f.close()
    f=open('job.cvs','r')
    con=0
    con1=0
    con2=0
    aa=[]
    con3=0
    while(name['text'][0]=='M'):
        s=f.readline()
        if(s==""):
            break
        lst=s.split(";")
        con1+=1
        if(p.get()==lst[0] and us.get()==lst[9]):
            con+=1
            aa.append(lst[1])
    f.close()
    f=open('apply.txt','r')
    while(name['text'][5]=='z'):
        s=f.readline()
        if(s==""):
            break
        lst=s.split(";")
        if(lst[0] in aa):
            con2+=len(lst)-2
        if(card in lst):
            con3+=1
    f.close()
    jobappto=con3
    jobof=con
    alljob=con1
    offjob=con2
    zz2['text']="Number of Freelancer registred with valid account: "+str(nbfl)+"\n\nNumber of tasks that you applied to : "+str(jobappto)+"\n\nTotal Number of tasks available : "+str(alljob)
    zz1['text']="Number of freelancer that applied to your job offers : "+str(offjob)+"\n\nNumber of tasks that you offred : "+str(jobof)+"\n\nTotal Number of tasks available : "+str(alljob)
    a.pack_forget()
    b.pack()
def update11(sfn,sidcard,spn,suad,sedu,des_us_set,p,us,test,setting_us,apply_us):
    global card
    war_sub_set.pack_forget()
    war_sub_set['text']="Please fill all boxs"
    f=open(".inter.txt","r")
    stri_toupdate11=f.read()
    f.close()
    s=tostore(des_us_set.get("0.0","end-1c"))
    if(te(sfn.get()) or te(sidcard.get())or te(spn.get()) or te(suad.get()) or te(s)):
        war_sub_set['text']="Please dont use ;"
        war_sub_set.pack()
        return
    if(sidcard.get()!=card):
        f=open("skr_info.txt","r")
        while(name['text'][20]=='r'):
            ss=f.read()
            if(ss==""):
                break
            lst=ss.split(";")
            if(lst[3]==sidcard.get()):
                war_sub_set['text']="the id card must be unique"
                war_sub_set.pack()
                return
        f.close()
    if(sidcard.get()!=card):
        x=""
        f=open(".inter1.txt","r")
        zzz=f.read()
        f.close()
        lst=zzz.split(';')
        for i in lst:
            if(i==card):
                x+=sidcard.get()+';'
            else:
                x+=i+';'
        zzz=x[:len(x)-1]
        f.close()
    stri_toupdate11+=p.get()+";"+us.get()+";"+sfn.get()+";"+sidcard.get()+";"+spn.get()+";"+suad.get()+";"+sedu.get()+";"+tostore(des_us_set.get("0.0","end-1c"))+";"+"\n"
    k=open("skr_info.txt","w")
    k.write(stri_toupdate11)
    k.close()
    if(test==1):
        if(sidcard.get()!=card):
            f=open("apply.txt","w")
            f.write(zzz)
            f.close()
        else:
            f=open(".inter1.txt","r")
            stri_toupdate11=f.read()
            f.close()
            f=open("apply.txt","w")
            f.write(stri_toupdate11)
            f.close()
    card=sidcard.get()
    showinfo("Done!")
    back(setting_us,apply_us)

def apply_job(tree,war_ap_exist,sbtn1,sbtn2,sl1,bbtn1,bbtn2,apply_us,setting_us,sfn,sidcard,spn,suad,sedu,des_us_set,p,us):
    ref_set(0,0,sfn,sidcard,spn,suad,sedu,des_us_set,p,us,1)
    sl1["text"]="Your seeting can increase your hiring chance \nUpdate your setting if you want to "
    bbtn1.pack(side=RIGHT,padx=10,pady=10)
    bbtn2.pack_forget()
    sbtn2.pack_forget()
    sbtn1.pack(side=RIGHT,padx=10,pady=10)
    war_ap_exist.pack_forget()
    focus_id=tree.item(tree.focus())['values'][0]
    f=open("apply.txt","r")
    s=""
    inte=""
    while(name['text'][9]=='B'):
        ss=f.readline()
        if(ss==""):
            break
        lst=ss.split(";")
        if(lst[0]==focus_id):
            inte+=lst[0]+";"
            for i in range(1,len(lst)):
                inte+=lst[i]+";"
                if(lst[i]==card):
                    war_ap_exist.pack()
                    return
        else:
            s+=ss
    f.close()
    sbtn1.pack_forget()
    sbtn2.pack(side=RIGHT,padx=10,pady=10)
    bbtn1.pack_forget()
    bbtn2.pack(side=RIGHT,padx=10,pady=10)
    back(apply_us,setting_us)
    if(inte==""):
        f=open("apply.txt","r")
        s=f.read()
        f.close()
        f=open(".inter1.txt","w")
        f.write(s+focus_id+";"+card+";"+"\n")
        f.close()
    else:
        f=open(".inter1.txt","w")
        f.write(s+inte[:len(inte)-2]+card+";"+"\n")
        f.close()
def ref(tree,war_ap_exist):
    war_ap_exist.pack_forget()
    x=tree.get_children()
    if(x!={}):
        for child in x:
            tree.delete(child)
    con=0
    f=open("job.cvs","r")
    while(name['text'][18]=='m'):
        ss=f.readline()
        if(ss==""):
            break
        lst=ss.split(";")
        con+=1
        tree.insert("",con,tag=str(con%2),text=lst[9],values=(lst[1],lst[2],lst[3],lst[7]))
    f.close()
def sub_us_info(p,us,fn,idcard,pn,uad,edu,des_us_info,war_sub_info,us_info,option_menu):
    war_sub_info['text']="Please fill all boxs"
    war_sub_info.pack_forget()
    if(fn.get()=="" or idcard.get()=="" or uad.get()=="" or pn.get()=="" ):
        war_sub_info.pack()
        return
    f=open("skr_info.txt","r")
    while(name['text'][3]==' '):
        ss=f.readline()
        if(ss==""):
            break
        lst=ss.split(";")
        if(lst[3]==idcard.get()):
            war_sub_info['text']="the id card must be unique"
            war_sub_info.pack()
            return
    f.close()    
    f=open("skr_info.txt","a")
    f.write(p.get()+";"+us.get()+";"+fn.get()+";"+idcard.get()+";"+pn.get()+";"+uad.get()+";"+edu.get()+";"+tostore(des_us_info.get("0.0","end-1c"))+";"+"\n")
    f.close()
    global card
    card=idcard.get()
    showinfo("DONE !")
    xbox2['text']="Welcome "+us.get()
    backi(us_info,option_menu)
    
def search_j(s3,search_op,tree,ref_sea,war_sear):
    x=tree.get_children()
    if(x!={}):
        for child in x:
            tree.delete(child)
    war_sear.pack_forget()
    test=0
    if(search_op.get()=="   ID   "):
        test=search_id(s3,tree,ref_sea)
    elif("Location"==search_op.get()):
        test=search_loc(s3,tree,ref_sea)
    else:
        test=search_dom(s3,tree,ref_sea)
    if(test==1):
        war_sear.pack(side=RIGHT,padx=5,pady=5)
def te(s):
    for i in s:
        if(i==";"):
            return True
    False
def sub_job(war_new_exist,des_new,ID,ca,cn,ce,rp,jd,lo,p,us):
    war_new_exist["text"]=""
    ss=""
    s=des_new.get("0.0","end-1c")
    if(te(s)or te(ID.get())or te(ca.get())or te(cn.get())or te(ce.get())or te(jd.get())or te(lo.get())):
        war_new_exist["text"]=" please dont use the ; special character"
        return   
    if(len(s)>50):
        war_new_exist["text"]="the discription lenght must be less than 50 characters !"
        return
    f=open("job.cvs","r")
    while (name['text'][12]==' '):
        ss=f.readline()
        if(ss==""):
            break
        else:
            lst=ss.split(";")
            if(lst[1]==ID.get()):
                war_new_exist["text"]="the ID is already exists !"
                return
    f.close()
    if(ID.get()==""or cn.get()=="" or ca.get()=="" or jd.get()=="" or lo.get()==""):
        war_new_exist["text"]="Fill in all mandatory fields !"
    else:
        ss=tostore(s)
        f=open("job.cvs","a")
        rp.get()
        f.write(p.get()+";"+ID.get()+";"+jd.get()+";"+lo.get()+";"+cn.get()+";"+ca.get()+";"+ce.get()+";"+rp.get()+";"+ss+";"+us.get()+";"+"\n")
        f.close()
        showinfo("Done !")
        ID.set("")
        cn.set("")
        ca.set("")
        ce.set("")
        rp.set("None")
        jd.set("")
        lo.set("")
        des_new.delete("0.0",END)
#42
def search_up(IDU,cau,cnu,ceu,rpu,jdu,lou,p,des_up,u10,back_up_btn,u2,war_up,us):
    def set_text(s):
        ss=""
        for i in s:
            if(i=="@"):
                ss+="\n"
            else:
                ss+=i
        des_up.delete("0.0",END)
        des_up.insert("0.0",ss)
    global stri_toupdate
    stri_toupdate=""
    u10.pack()
    test=1
    back_up_btn.pack()
    u2.pack_forget()
    war_up['text']=""
    s=IDU.get()
    f=open("job.cvs","r")
    while (name['text'][4]=='A'):
        ss=f.readline()
        if(ss==""):
            break
        else:
            lst=ss.split(";")
            if(lst[0]==p.get() and lst[1]==s and lst[9]==us.get()):
                test=0
                u10.pack_forget()
                back_up_btn.pack_forget()
                u2.pack()
                jdu.set(lst[2])
                lou.set(lst[3])
                cnu.set(lst[4])
                cau.set(lst[5])
                ceu.set(lst[6])
                rpu.set(lst[7])
                set_text(lst[8])
            else:
                stri_toupdate+=ss
    if(test==1):
        war_up['text']="the requested job ID does not exist or you dont own this offer"
#78
def update(IDU,cau,cnu,ceu,rpu,jdu,lou,p,des_up,u10,back_up_btn,u2,us):
    global stri_toupdate
    s=tostore(des_up.get("0.0","end-1c"))
    if(te(s)or te(IDU.get())or te(cau.get())or te(cnu.get())or te(ceu.get())or te(jdu.get())or te(lou.get())):
        war_up["text"]=" please dont use the ; special character"
        return 
    if(len(s)>50):
        war_up['text']="the discription lenght must be less than 50 characters !"
        return
    if(IDU.get()==""or cnu.get()=="" or cau.get()=="" or jdu.get()=="" or lou.get()==""):
        war_up['text']="Fill in all mandatory fields !"
    stri_toupdate+=p.get()+";"+IDU.get()+";"+jdu.get()+";"+lou.get()+";"+cnu.get()+";"+cau.get()+";"+ceu.get()+";"+rpu.get()+";"+tostore(des_up.get("0.0","end-1c"))+";"+us.get()+";"+"\n"
# jdu caan be empty
    f=open("job.cvs","w")
    f.write(stri_toupdate)
    f.close()
    showinfo("Done!")
    IDU.set("")
    cnu.set("")
    
    cau.set("")
    ceu.set("")
    jdu.set("")
    lou.set("")
    rpu.set("None")
    des_up.delete("0.0",END)
    u10.pack()
    back_up_btn.pack()
    u2.pack_forget()
    
def delete_del(IDD,war_del,p):
    war_del['text']=""
    stri_del=""
    test=1
    f=open("job.cvs","r")
    while (name['text'][1]=='e'):
        ss=f.readline()
        if(ss==""):
            break
        else:
            lst=ss[:len(ss)-1].split(";")
            if(lst[0]==p.get() and lst[1]==IDD.get()and lst[9]==us.get()):
                test=0
            else:
                stri_del+=ss
    f.close()
    if(test==1):
        war_del['text']="the requested job ID does not exist or you dont own this offer"
        return
    f=open("job.cvs","w")
    f.write(stri_del)
    f.close()
    showinfo("Done !")
def listing(tree,username,option,list_fl,p):
    x=tree.get_children()
    if(x!={}):
        for child in x:
            tree.delete(child)
    f=open("skr_info.txt","r")
    usi={}
    while(name['text'][6]=='i'):
        ss=f.readline()
        if(ss==""):
            break
        lst=ss.split(";")
        usi[lst[3]]=(lst[2],lst[4],lst[6])
    f.close()
    f=open("job.cvs","r")
    job={}
    while(1==1):
        ss=f.readline()
        if(ss==""):
            break
        lst=ss.split(";")
        if(p.get()==lst[0] and username.get()==lst[9]):
            job[lst[1]]=(lst[2],lst[3],lst[7])
    f.close()
    f=open("apply.txt","r")
    con=0
    while(1==1):
        ss=f.readline()
        if(ss==""):
            break
        lst=ss.split(";")
        if (lst[0] in job):
            con+=1
            x=tree.insert("",con,tag=str(con%2),text=lst[0],values=job[lst[0]])
            for i in range(1,len(lst)-1):
                tree.insert(x,"end",text=lst[i],values=usi[lst[i]])
    f.close()
    option.pack_forget()
    list_fl.pack()
    
def ref_set(a,b,sfn,sidcard,spn,suad,sedu,des_us_set,p,us,test):
    if(test==0):
        bbtn1.pack(side=RIGHT,padx=10,pady=10)
        bbtn2.pack_forget()
        sbtn2.pack_forget()
        sbtn1.pack(side=RIGHT,padx=10,pady=10)
    stri_toupdate=""
    f=open("skr_info.txt","r")
    while(1==1):
        ss=f.readline()
        if(ss==""):
            break
        lst=ss.split(";")
        if(p.get()==lst[0] and us.get()==lst[1]):
            sfn.set(lst[2])
            sidcard.set(lst[3])
            spn.set(lst[4])
            suad.set(lst[5])
            sedu.set(lst[6])
            ss=""
            for i in lst[7]:
                if(i=="@"):
                    ss+="\n"
                else:
                    ss+=i
            des_us_set.delete("0.0",END)
            des_us_set.insert("0.0",ss)
            break
        else:
            stri_toupdate+=ss
    f=open(".inter.txt","w")
    f.write(stri_toupdate)
    f.close()
    if(test==0):
        a.pack_forget()
        b.pack()
def set_text(s,des_us_set):
    ss=""
    for i in s:
        if(i=="@"):
            ss+="\n"
        else:
            ss+=i
    des_us_set.delete("0.0",END)
    des_us_set.insert("0.0",ss)
def search_id(s3,tree,ref_sea):
    s3.pack_forget()
    tree.heading("#0",text="Domain")
    tree.heading("col2",text="Location")
    f=open("job.cvs","r")
    while(1==1):
        s=f.readline()
        if(s==""):
            break
        lst=s.split(";")
        if(lst[1]==ref_sea.get()):
            tree.insert("",1,tag="1",text=lst[2],values=(lst[3],lst[4],lst[7]))
            s3.pack()
            return
    return 1

def search_loc(s3,tree,ref_sea):
    s3.pack_forget()
    tree.heading("#0",text="ID")
    tree.heading("col2",text="Domain")
    f=open("job.cvs","r")
    con=0
    test=1
    while(1==1):
        s=f.readline()
        if(s==""):
            break
        lst=s.split(";")
        if(lst[3]==ref_sea.get()):
            test=0
            con+=1
            tree.insert("",con,tag=str(con%2),text=lst[1],values=(lst[2],lst[4],lst[7]))
    if(test==0):
        s3.pack()
    return test

def search_dom(s3,tree,ref_sea):
    s3.pack_forget()
    tree.heading("#0",text="ID")
    tree.heading("col2",text="Location")
    f=open("job.cvs","r")
    con=0
    test=1
    while(1==1):
        s=f.readline()
        if(s==""):
            break
        lst=s.split(";")
        if(lst[2]==ref_sea.get()):
            con+=1
            test=0
            tree.insert("",con,tag=str(con%2),text=lst[1],values=(lst[3],lst[4],lst[7]))
    if(test==0):
        s3.pack()
    return test
def tostore(s):
    ss=""
    for i in s:
        if(i=="\n"):
            ss+="@"
        else:
            ss+=i
    return ss

def sub(p,var,us):
    xbox['text']="Welcome "+us.get()
    war_log['text']=""
    f=open("account.txt","r")
    lst=f.readlines()
    if(len(lst)==0):
        showwarning("You must register!")
        return
    ss=log_op.get()
    ss=ss[0]+p.get()+";"+us.get()+"\n"
    for s in lst:
        if(s==ss):
            if(ss[0]=="A"):
                win.title("Admin")
                backi(win1,win2)
                f.close()
                return
            else:
                win.title("Freelancer")
                win1.pack_forget()
                win3.pack()
                k=open("skr_info.txt","r")
                while(1==1):
                    ss=k.readline()
                    if(ss==""):
                        break
                    ssi=ss.split(";")
                    if(ssi[0]==p.get() and ssi[1]==us.get()):
                        global card
                        card=ssi[3]
                        break
                k.close()
                if(ss==""):
                    xbox1['text']="Welcome "+us.get()+", Before we get started we need to know some information about you \n please fill the boxs bellow"
                    us_info.pack()
                    option_menu.pack_forget()
                else:
                    xbox2['text']="Welcome "+us.get()
                    backi(us_info,option_menu)
                f.close()
                return
    war_log["text"]="Wrong, Please verify your username and password"
    f.close()
def back(a,b):
    a.pack_forget()
    b.pack()
def add(s):
    f=open("account.txt","a")
    f.write(s)
    f.close()
def check():
    war_reg["text"]=""
    p2['bg']="white"
    if(te(usu_reg.get())or te(p1_reg.get())):
       war_reg["text"]="Please dont use ';'"
       return
    if(p1_reg.get()!=p2_reg.get()):
        war_reg["text"]="These passwords doesn't match, Please retry again"
        p2['bg']="#fa4120"
        p2_reg.set("")
        p1_reg.set("")
    else:
        f=open("account.txt","r")
        s=p1_reg.get()+";"+usu_reg.get()+"\n"
        while(1==1):
            stri=f.readline()
            if(stri==""):
                break
            elif(stri[1:]==s):
                war_reg["text"]="This account already exist!"
                return
        showinfo("DONE!")
        ss=reg_op.get()
        s=ss[0]+s
        add(s)
        war_log["text"]=""
        p2_reg.set("")
        p1_reg.set("")
        usu_reg.set("")
       
alljob=0
nbfl=0
jobappto=0
offjob=0
jobof=0
stri_toupadate=""
win=Tk()
win.title("Welcome!")
win.resizable(0,0)
W= win.winfo_screenwidth()
H = win.winfo_screenheight()
W=W/2-550
H=H/2-250
win.geometry("1100x530+"+str(int(W))+"+"+str(int(H)))
win["bg"]="#222831"
win1=Frame(win,bg="#222831")
win1.pack()
win2=Frame(win,bg="#222831",pady=20)
win3=Frame(win,bg="#222831")
name=Label(win,text="Med Aziz Bel Haj Amor",fg="#fff1cf",bg="#222831")
name.pack(side=BOTTOM,pady=10)
image=PhotoImage(file="kurlex.png")
image=image.subsample(11,11)
titel=Frame(win1,bg="#222831")
titel.pack(side=TOP)
Label(titel,image=image,bg="#222831").pack(side=LEFT)
x=Label(titel,text="Freelance Platform",fg="#eeeeee",bg="#222831")
x.pack(side=LEFT)
x.config(font=("ubuntu", 40))
log=Frame(win1,relief=GROOVE,bg="#eeeeee",highlightbackground="#ffd369",highlightthickness=2)
log.pack(side=LEFT,fill=None, expand=False,padx=70)
reg=Frame(win1,relief=GROOVE,bg="#eeeeee",highlightbackground="#ffd369",highlightthickness=2)
reg.pack(side=LEFT,padx=70)
#-----log window--------
log_op=StringVar()
p=StringVar()
l_1=Label(log,text="Sign in :",bg="#eeeeee")
l_1.pack(padx=10,pady=19)
l_1.config(font=("ubuntu", 20))
l=Frame(log,relief=GROOVE,bg="#eeeeee")
l.pack(padx=10)
l1=Frame(log,relief=GROOVE,bg="#eeeeee")
l1.pack()
l4=Frame(log,relief=GROOVE,bg="#eeeeee")
l4.pack(pady=8)
l2=Frame(log,relief=GROOVE,bg="#eeeeee")
l2.pack(pady=10)
l3=Frame(log,relief=GROOVE,bg="#eeeeee")
l3.pack()
us=StringVar()
Label(l,text="   Username :  ",bg="#eeeeee").pack(side=LEFT,padx=6)
us_log=Entry(l,textvariable=us,bd=2)
us_log.pack(side=LEFT,padx=10,pady=10)
Label(l1,text="   password :  ",bg="#eeeeee").pack(side=LEFT,padx=8)
p_log=Entry(l1,textvariable=p,show="*",bd=2)
p_log.pack(side=LEFT,padx=10,pady=10)
option_log=style_OM(log_op,l4,"Job seeker","Administrator","Job seeker")
option_log.pack(side=LEFT,padx=10,pady=15)
war_log=Label(l2,text="",fg="red",bg="#eeeeee")
war_log.pack()
log2=style_BTN(l3,text="Log in",activebackground="#fbd67b",command=partial(sub,p,log_op,us))
log2.pack(side=LEFT,padx=10,pady=10)

#-----reg window--------

r_1=Label(reg,text="Register :",bg="#eeeeee")
r_1.pack(pady=20)
r_1.config(font=("ubuntu", 20))
r=Frame(reg,bg="#eeeeee")
r.pack(padx=5,pady=5)
r1=Frame(reg,bg="#eeeeee")
r1.pack(padx=5,pady=5)
p1_reg=StringVar()
p2_reg=StringVar()
usu_reg=StringVar()
Label(r,text="Type username :  ",bg="#eeeeee").pack(side=LEFT,padx=6)
usu=Entry(r,textvariable=usu_reg,bd=2)
usu.pack(side=LEFT,padx=5)
Label(r1,text="Type password :  ",bg="#eeeeee").pack(side=LEFT,padx=7)
p1=Entry(r1,textvariable=p1_reg,show="*",bd=2)
p1.pack(side=LEFT,padx=5)
r2=Frame(reg,bg="#eeeeee")
r2.pack(padx=5,pady=5)
r3=Frame(reg,bg="#eeeeee")
r3.pack(padx=5,pady=5)
r4=Frame(reg,bg="#eeeeee")
r4.pack(padx=5,pady=5)
r5=Frame(reg,bg="#eeeeee")
r5.pack(padx=5,pady=5)
global reg_op
reg_op=StringVar()
reg_op.set("Job seeker")
Label(r2,text="Retype password :  ",bg="#eeeeee").pack(side=LEFT)
p2=Entry(r2,textvariable=p2_reg,show="*",bd=2)
p2.pack(side=LEFT,padx=5)
option_reg=style_OM(reg_op,r3,"Job seeker","Administrator","Job seeker")
option_reg.pack(side=LEFT,padx=10,pady=10)
bt=style_BTN(r5,text="Sign up",activebackground="#fbd67b",command=check)
bt.pack(side=LEFT,padx=10,pady=10)
bt.config(font=("ubuntu", 10,'bold'))
war_reg=Label(r4,text="",fg="red",bg="#eeeeee")
war_reg.pack()

#-------Windows 101------------------
option=Frame(win2,relief=GROOVE,bg="#fff1cf",width=1100)
new_offer=Frame(win2,relief=GROOVE,bg="#fff1cf")
update_offer=Frame(win2,relief=GROOVE,bg="#fff1cf")
del_offer=Frame(win2,relief=GROOVE,bg="#fff1cf",pady=30)
list_fl=Frame(win2,relief=GROOVE,bg="#fff1cf",pady=30)
#-------Admin window 105----------
option.pack(padx=100,pady=10)
xbox=Label(option,text="Welcome "+us.get(),fg="#eeeeee",bg="#fff1cf",width=1100)
xbox.pack(side=TOP,padx=10,pady=10)
xbox.config(font=("ubuntu", 40),fg="#015668")
image1=PhotoImage(file="./engineer.png")
image1=image1.subsample(4,4)
prof_adm=Frame(option,bg="#fff1cf")
prof_adm.pack(padx=10,pady=5)
Label(prof_adm,image=image1,bg="#fff1cf").pack(side=LEFT,padx=10)
zz1=Label(prof_adm,bg="#fff1cf",text="",justify=LEFT)
zz1.pack(side=BOTTOM)
zz1.config(font=("ubuntu",9),fg="#263f44")
o1=Frame(option,relief=GROOVE,bg="#fff1cf")
o1.pack(padx=10,pady=10)
o2=Frame(option,relief=GROOVE,bg="#fff1cf")
o2.pack(padx=10,pady=10)
o3=Frame(option,relief=GROOVE,bg="#fff1cf")
o3.pack(padx=10,pady=10)
o4=Frame(option,relief=GROOVE,bg="#fff1cf")
o4.pack()
zz=Label(o1,bg="#fff1cf",text="For more details please choose one of the options bellow")
zz.pack(padx=10,pady=10)
zz.config(font=("ubuntu",15),fg="#263f44")
btn_adm1=style_BTN1(o2,text="           Add new job offer          ",activebackground="#fbd67b",command=partial(back,option,new_offer)).pack(side=LEFT,padx=20)
btn_adm2=style_BTN1(o2,text=" Brows and Update a job offer ",activebackground="#fbd67b",command=partial(back,option,update_offer)).pack(side=LEFT,padx=20)
btn_adm2=style_BTN1(o3,text="          Delete a job offer           ",activebackground="#fbd67b",command=partial(back,option,del_offer)).pack(side=LEFT,padx=20)
x=style_BTN(o4,text="          Log out           ",activebackground="#fbd67b",command=partial(back,win2,win1))
x.pack(side=LEFT,padx=20,pady=10)

#-------Add new offer 121--------
x=Label(new_offer,text="Fill the boxs to add new job offer",fg="#eeeeee",bg="#fff1cf",width=1100)
x.pack(side=TOP,padx=10,pady=30)
x.config(font=("ubuntu", 20),fg="#015668")
first_n=Frame(new_offer,relief=GROOVE,bg="#fff1cf")
first_n.pack(side=LEFT,padx=50,pady=10)
second_n=Frame(new_offer,relief=GROOVE,bg="#fff1cf")
second_n.pack(side=LEFT,padx=50,pady=10)
n1=Frame(first_n,relief=GROOVE,bg="#fff1cf")
n1.pack(padx=10,pady=10)
n8=Frame(first_n,relief=GROOVE,bg="#fff1cf")
n8.pack(padx=10,pady=10)
n2=Frame(first_n,relief=GROOVE,bg="#fff1cf")
n2.pack(padx=10,pady=10)
n3=Frame(first_n,relief=GROOVE,bg="#fff1cf")
n3.pack(padx=10,pady=10)
n9=Frame(first_n,relief=GROOVE,bg="#fff1cf")
n9.pack(padx=10,pady=10)
n4=Frame(second_n,relief=GROOVE,bg="#fff1cf")
n4.pack(padx=10,pady=10)
n5=Frame(second_n,relief=GROOVE,bg="#fff1cf")
n5.pack(padx=10,pady=10)
n6=Frame(second_n,relief=GROOVE,bg="#fff1cf")
n6.pack(padx=10,pady=10)
war_new_exist=Label(second_n,text="",fg="red",bg="#fff1cf")
war_new_exist.pack()
n7=Frame(second_n,relief=GROOVE,bg="#fff1cf")
n7.pack(padx=10,pady=10)
ID=StringVar()
x=Label(n1,text="Job ID (*): ",bg="#fff1cf")
x.pack(side=LEFT,padx=51,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
n=Entry(n1,textvariable=ID)
n.pack(side=LEFT,padx=10,pady=10)
n.focus_set()
jd=StringVar()
lo=StringVar()
cn=StringVar()
ca=StringVar()
ce=StringVar()
rp=StringVar()
x=Label(n8,text="Job domain (*): ",bg="#fff1cf")
x.pack(side=LEFT,padx=34,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(n8,textvariable=jd).pack(side=LEFT,padx=10,pady=10)
x=Label(n9,text="Location (*): ",bg="#fff1cf")
x.pack(side=LEFT,padx=40,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(n9,textvariable=lo).pack(side=LEFT,padx=10,pady=10)
x=Label(n2,text="Company name (*): ",bg="#fff1cf")
x.pack(side=LEFT,padx=18,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(n2,textvariable=cn).pack(side=LEFT,padx=10,pady=10)
x=Label(n3,text="Company address (*): ",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(n3,textvariable=ca).pack(side=LEFT,padx=10,pady=10)
x=Label(n5,text="Company email : ",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(n5,textvariable=ce).pack(side=LEFT,padx=30,pady=10)
x=Label(n4,text="Requested profile :",bg="#fff1cf")
x.pack(side=LEFT,padx=30,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")

x=style_OM(rp,n4,"None","Degree", "Qualification", "Experience","None")
x.pack(side=LEFT,padx=10,pady=10)
Label(n6,text="Mission description :",bg="#fff1cf").pack(side=LEFT,padx=10,pady=10)
des_new=Text(n6,width=30,height=5)
des_new.pack(side=LEFT,padx=10,pady=5)
x=style_BTN(n7,text="submit",activebackground="#fbd67b",command=partial(sub_job,war_new_exist,des_new,ID,ca,cn,ce,rp,jd,lo,p,us))
x.pack(side=RIGHT,padx=30,pady=5)
x=style_BTN(n7,text="Back",activebackground="#fbd67b",command=partial(backi,new_offer,option))
x.pack(side=RIGHT,padx=10,pady=5)

#-------Update a job 168-----
u1=Frame(update_offer,relief=GROOVE,bg="#fff1cf")
u1.pack(padx=10,pady=10)
x=Label(u1,text="Enter the job ID to be updated :",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
IDU=StringVar()
eu=Entry(u1,textvariable=IDU)
eu.pack(side=LEFT,padx=10,pady=10)
eu.focus_set()
u11=Frame(update_offer,relief=GROOVE,bg="#fff1cf")
u11.pack(padx=10,pady=10)
u10=Frame(update_offer,relief=GROOVE,bg="#fff1cf")
u10.pack(padx=10,pady=10)
war_up=Label(u11,text="",fg="red",bg="#fff1cf")
war_up.pack()
back_up_btn=style_BTN(u10,text="Back",activebackground="#fbd67b",command=partial(back,update_offer,option))
back_up_btn.pack()
u2=Frame(update_offer,relief=GROOVE,bg="#fff1cf")
x=Label(u2,text="change then commit your changes",bg="#fff1cf")
x.pack(padx=10,pady=10)
x.config(font=("ubuntu",13),fg="#263f44")
first_u=Frame(u2,relief=GROOVE,bg="#fff1cf")
first_u.pack(side=LEFT,padx=10,pady=10)
second_u=Frame(u2,relief=GROOVE,bg="#fff1cf")
second_u.pack(side=LEFT,padx=10,pady=10)
u9=Frame(first_u,relief=GROOVE,bg="#fff1cf")
u9.pack(padx=10,pady=10)
u12=Frame(first_u,relief=GROOVE,bg="#fff1cf")
u12.pack(padx=10,pady=10)
u3=Frame(first_u,relief=GROOVE,bg="#fff1cf")
u3.pack(padx=10,pady=10)
u4=Frame(first_u,relief=GROOVE,bg="#fff1cf")
u4.pack(padx=10,pady=10)
u13=Frame(first_u,relief=GROOVE,bg="#fff1cf")
u13.pack(padx=10,pady=10)
u5=Frame(second_u,relief=GROOVE,bg="#fff1cf")
u5.pack(padx=10,pady=10)
u6=Frame(second_u,relief=GROOVE,bg="#fff1cf")
u6.pack(padx=10,pady=10)
u7=Frame(second_u,relief=GROOVE,bg="#fff1cf")
u7.pack(padx=10,pady=10)
stri_toupdate=""
jdu=StringVar()
lou=StringVar()
cnu=StringVar()
cau=StringVar()
ceu=StringVar()
rpu=StringVar()
x=Label(u12,text="Job domain (*): ",bg="#fff1cf")
x.pack(side=LEFT,padx=34,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(u12,textvariable=jdu).pack(side=LEFT,padx=10,pady=10)
x=Label(u13,text="Location (*): ",bg="#fff1cf")
x.pack(side=LEFT,padx=40,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(u13,textvariable=lou).pack(side=LEFT,padx=10,pady=10)
x=Label(u9,text="Company name (*): ",bg="#fff1cf")
x.pack(side=LEFT,padx=18,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(u9,textvariable=cnu).pack(side=LEFT,padx=10,pady=10)
x=Label(u3,text="Company address (*): ",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(u3,textvariable=cau).pack(side=LEFT,padx=10,pady=10)
x=Label(u4,text="Company email : ",bg="#fff1cf")
x.pack(side=LEFT,padx=26,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
Entry(u4,textvariable=ceu).pack(side=LEFT,padx=10,pady=10)
x=Label(u5,text="Requested profile :",bg="#fff1cf")
x.pack(side=LEFT,padx=30,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
x=style_OM(rpu,u5,"None","Degree", "Qualification", "Experience","None")
x.pack(side=LEFT,padx=10,pady=10)
x=Label(u6,text="Mission description :",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",11),fg="#263f44")
des_up=Text(u6,width=30,height=5)
des_up.pack(side=LEFT,padx=10,pady=10)
x=style_BTN(u7,text="Submit",activebackground="#fbd67b",command=partial(update,IDU,cau,cnu,ceu,rpu,jdu,lou,p,des_up,u10,back_up_btn,u2,us))
x.pack(side=RIGHT,padx=30,pady=10)
x=style_BTN(u7,text="Back",activebackground="#fbd67b",command=partial(back,update_offer,option))
x.pack(side=RIGHT,padx=10,pady=10)
x=style_BTN(u1,text="Search",activebackground="#fbd67b",command=partial(search_up,IDU,cau,cnu,ceu,rpu,jdu,lou,p,des_up,u10,back_up_btn,u2,war_up,us))
x.pack(side=LEFT,padx=10,pady=10)

#------delete window 223 ------
d1=Frame(del_offer,relief=GROOVE,bg="#fff1cf")
d1.pack(padx=10,pady=10)
x=Label(d1,text="Enter the job's ID to be deleted :",bg="#fff1cf")
x.config(font=("ubuntu", 10),fg="#015668")
x.pack(side=LEFT,padx=10,pady=10)
IDD=StringVar()
ed=Entry(d1,textvariable=IDD)
ed.pack(side=LEFT,padx=10,pady=10)
ed.focus_set()
d2=Frame(del_offer,relief=GROOVE,bg="#fff1cf")
d2.pack(padx=10,pady=10)
d3=Frame(del_offer,relief=GROOVE,bg="#fff1cf")
d3.pack(padx=10,pady=10)
war_del=Label(d2,text="",fg="red",bg="#fff1cf")
war_del.pack()
back_del_btn=style_BTN(d3,text="Back",activebackground="#fbd67b",command=partial(backi,del_offer,option))
back_del_btn.pack(side=LEFT,padx=5,pady=5)
x=style_BTN(d3,text="Delete",activebackground="#fbd67b",command=partial(delete_del,IDD,war_del,p))
x.pack(side=LEFT,padx=5,pady=5)

#------listing FL----
style = kur.Style()
style.configure("TR",bd=2,font=('ubuntu',10))
style.configure("TR.Heading",font=('ubuntu',13,'bold'),background="#fbd67b",foreground="#eee")
style.layout("TR",[('TR.treearea',{'sticky':'nswe'})])
x=Label(list_fl,text="List of Applied Freelancer",bg="#fff1cf")
x.pack(padx=10,pady=10)
x.config(font=("ubuntu",20),fg="#263f44")
ap1=Frame(list_fl,relief=GROOVE,bg="#fff1cf")
ap1.pack()
applytree=kur.Treeview(ap1,style="TR",columns=("Domain","Location","Requested profile"))
applytree.column("#0",minwidth=50)
applytree.column("Domain",minwidth=50)
applytree.column("Location",minwidth=50)
applytree.column("Requested profile",minwidth=50)
applytree.heading("#0",text="Job ID")
applytree.heading("Domain",text="Domain")
applytree.heading("Location",text="Location")
applytree.heading("Requested profile",text="Requested profile")
applytree.tag_configure('0',background="#E8E8E8")
applytree.tag_configure('1',background="#DFDFDF")
applytree.pack(side=TOP,padx=20,pady=20)
x=style_BTN(ap1,text=" Back ",activebackground="#fbd67b",command=partial(back,list_fl,option))
x.pack(side=LEFT,padx=20,pady=10)

btn_adm2=style_BTN1(o3,text="  Brows the list of job seekers  ",activebackground="#fbd67b",command=partial(listing,applytree,us,option,list_fl,p))
btn_adm2.pack(side=LEFT,padx=20)
#-------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
card=""
us_info=Frame(win3,relief=GROOVE,bg="#fff1cf")
option_menu=Frame(win3,relief=GROOVE,bg="#fff1cf")
search=Frame(win3,relief=GROOVE,bg="#fff1cf")
apply_us=Frame(win3,relief=GROOVE,bg="#fff1cf")
setting_us=Frame(win3,relief=GROOVE,bg="#fff1cf")
#----option menu
xbox2=Label(option_menu,text="",fg="#eeeeee",bg="#fff1cf",width=1100)
xbox2.pack(side=TOP,padx=10,pady=10)
xbox2.config(font=("ubuntu", 40),fg="#015668")
image2=PhotoImage(file="./engineer.png")
image2=image2.subsample(4,4)
prof_us=Frame(option_menu,bg="#fff1cf")
prof_us.pack(padx=10,pady=5)
Label(prof_us,image=image2,bg="#fff1cf").pack(side=LEFT,padx=10)
zz2=Label(prof_us,bg="#fff1cf",text="",justify=LEFT)
zz2.pack(side=BOTTOM)
zz2.config(font=("ubuntu",9),fg="#263f44")
zz=Label(option_menu,bg="#fff1cf",text="For more details please choose one of the options bellow")
zz.pack(padx=10,pady=20)
zz.config(font=("ubuntu",15),fg="#263f44")
option_menu1=Frame(option_menu,bg="#fff1cf")
option_menu1.pack()
style_BTN1(option_menu1,text="Brows and Apply for a job offer ",activebackground="#fbd67b",command=partial(back,option_menu,apply_us)).pack(side=LEFT,padx=10,pady=10)

#-------search----
s1=Frame(search,relief=GROOVE,bg="#fff1cf")
s1.pack()
x=Label(s1,text="type to search for a job offer by the selected option",bg="#fff1cf")
x.pack(padx=10,pady=10)
x.config(font=("ubuntu", 12),fg="#015668")
s2=Frame(search,relief=GROOVE,bg="#fff1cf")
s2.pack()
ref_sea=StringVar()
search_op=StringVar()
se=Entry(s2,textvariable=ref_sea,width=15)
se.pack(side=LEFT,padx=10,pady=10)
se.focus_set()
style_OM(search_op,s2,"   ID   ","   ID   ", "Location", "Domain ").pack(side=LEFT,padx=10,pady=10)
s4=Frame(search,relief=GROOVE,bg="#fff1cf")
s4.pack(padx=10,pady=10)
war_sear=Label(s4,text="Sorry, the requested job offer does not exist",fg="red",bg="#fff1cf")
s3=Frame(search,relief=GROOVE,bg="#fff1cf")
tree=kur.Treeview(s3,style="TR",columns=("col2","Company name","Requested profile"))
tree.column("#0",minwidth=50)
tree.column("col2",minwidth=50)
tree.column("Company name",minwidth=50)
tree.column("Requested profile",minwidth=50)
tree.heading("Company name",text="Company name")
tree.heading("Requested profile",text="Requested profile")
tree.tag_configure('0',background="#E8E8E8")
tree.tag_configure('1',background="#DFDFDF")
tree.pack(side=TOP,fill=X,padx=20,pady=20)
style_BTN(s2,text="search",activebackground="#fbd67b",command=partial(search_j,s3,search_op,tree,ref_sea,war_sear)).pack(side=LEFT,padx=10,pady=10)
style_BTN(s2,text="back",activebackground="#fbd67b",command=partial(back,search,option_menu)).pack(side=LEFT,padx=10,pady=10)

#------USER info----
xbox1=Label(us_info,text="",bg="#fff1cf")
xbox1.pack(pady=15,padx=15)
xbox1.config(font=("ubuntu",14),fg="#263f44")
usin1=Frame(us_info,bg="#fff1cf")
usin1.pack(side=LEFT,padx=5,pady=5)
usin2=Frame(us_info,bg="#fff1cf")
usin2.pack(side=LEFT,padx=5,pady=5)
us1=Frame(usin1,relief=GROOVE,bg="#fff1cf")
us1.pack()
us2=Frame(usin1,relief=GROOVE,bg="#fff1cf")
us2.pack()
us3=Frame(usin1,relief=GROOVE,bg="#fff1cf")
us3.pack()
us4=Frame(usin1,relief=GROOVE,bg="#fff1cf")
us4.pack()
us5=Frame(usin2,relief=GROOVE,bg="#fff1cf")
us5.pack()
us6=Frame(usin2,relief=GROOVE,bg="#fff1cf")
us6.pack()
us8=Frame(usin2,relief=GROOVE,bg="#fff1cf")
us8.pack()
us7=Frame(usin2,relief=GROOVE,bg="#fff1cf")
us7.pack()
fn=StringVar()
idcard=StringVar()
pn=StringVar()
uad=StringVar()
edu=StringVar()
fl=StringVar()
x=Label(us1,text="Full name :",bg="#fff1cf")
x.pack(side=LEFT,padx=25,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
Entry(us1,textvariable=fn).pack(side=LEFT,padx=8,pady=10)
x=Label(us2,text="ID card :",bg="#fff1cf")
x.pack(side=LEFT,padx=34,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
Entry(us2,textvariable=idcard).pack(side=LEFT,padx=10,pady=10)
x=Label(us3,text="Phone number :",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
Entry(us3,textvariable=pn).pack(side=LEFT,padx=10,pady=10)
x=Label(us4,text="Your address :",bg="#fff1cf")
x.pack(side=LEFT,padx=15,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
Entry(us4,textvariable=uad).pack(side=LEFT,padx=10,pady=10)
x=Label(us5,text="Education level :",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
style_OM(edu,us5,"High school","Bachelor", "Master", "Doctoral","High school","Other").pack(side=LEFT,padx=10,pady=10)
x=Label(us6,text="tell us about your       \n skills and Experiences ",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
des_us_info=Text(us6,width=30,height=5)
des_us_info.pack(side=LEFT,padx=10,pady=10)
war_sub_info=Label(us8,text="Please fill all boxs",fg="red",bg="#fff1cf")
style_BTN(us7,text="submit",activebackground="#fbd67b",command=partial(sub_us_info,p,us,fn,idcard,pn,uad,edu,des_us_info,war_sub_info,us_info,option_menu)).pack(side=RIGHT,padx=30,pady=10)
style_BTN(us7,text="Log out",activebackground="#fbd67b",command=partial(back,win3,win1)).pack(side=RIGHT,padx=10,pady=10)

#------Apply for job----
x=Label(apply_us,text="Please select any offer available \nthen click on apply now to send a notification to the employer",bg="#fff1cf")
x.pack(padx=10,pady=10)
x.config(font=("ubuntu", 12),fg="#015668")
ap=Frame(apply_us,relief=GROOVE,bg="#fff1cf")
ap.pack()
style_BTN(ap,text=" Back ",activebackground="#fbd67b",command=partial(backi,apply_us,option_menu)).pack(side=LEFT,padx=20,pady=10)
ap1=Frame(apply_us,relief=GROOVE,bg="#fff1cf")
ap1.pack()
applytree1=kur.Treeview(apply_us,style="TR",columns=("Job ID","Domain","Location","Requested profile"))
applytree1.column("#0",minwidth=50)
applytree1.column("Job ID",minwidth=50)
applytree1.column("Domain",minwidth=50)
applytree1.column("Location",minwidth=50)
applytree1.column("Requested profile",minwidth=50)
applytree1.heading("#0",text="Employer")
applytree1.heading("Job ID",text="Job ID")
applytree1.heading("Domain",text="Domain")
applytree1.heading("Location",text="Location")
applytree1.heading("Requested profile",text="Requested profile")
applytree1.tag_configure('0',background="#E8E8E8")
applytree1.tag_configure('1',background="#DFDFDF")
applytree1.pack(side=TOP,fill=X,padx=20,pady=20)
war_ap_exist=Label(ap1,text="you already applied to this task !",fg="red",bg="#fff1cf")

style_BTN(ap,text="Refrech",activebackground="#fbd67b",command=partial(ref,applytree1,war_ap_exist)).pack(side=LEFT,padx=20,pady=10)


#---
sl1=Label(setting_us,text="Please dont forget to commit your changes",bg="#fff1cf")
sl1.pack(pady=10)
sl1.config(font=("ubuntu", 11),fg="#015668")
stt1=Frame(setting_us,bg="#fff1cf")
stt1.pack(side=LEFT,padx=5,pady=5)
stt2=Frame(setting_us,bg="#fff1cf")
stt2.pack(side=LEFT,padx=5,pady=5)
st1=Frame(stt1,relief=GROOVE,bg="#fff1cf")
st1.pack()
st2=Frame(stt1,relief=GROOVE,bg="#fff1cf")
st2.pack()
st3=Frame(stt1,relief=GROOVE,bg="#fff1cf")
st3.pack()
st4=Frame(stt1,relief=GROOVE,bg="#fff1cf")
st4.pack()
st5=Frame(stt2,relief=GROOVE,bg="#fff1cf")
st5.pack()
st6=Frame(stt2,relief=GROOVE,bg="#fff1cf")
st6.pack()
st8=Frame(stt2,relief=GROOVE,bg="#fff1cf")
st8.pack()
st7=Frame(stt2,relief=GROOVE,bg="#fff1cf")
st7.pack()
sfn=StringVar()
sidcard=StringVar()
spn=StringVar()
suad=StringVar()
sedu=StringVar()
x=Label(st1,text="Full name :",bg="#fff1cf")
x.pack(side=LEFT,padx=25,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
Entry(st1,textvariable=sfn).pack(side=LEFT,padx=8,pady=10)
x=Label(st2,text="ID card :",bg="#fff1cf")
x.pack(side=LEFT,padx=34,pady=10)
x.config(font=("ubuntu", 10),fg="#015668")
Entry(st2,textvariable=sidcard).pack(side=LEFT,padx=10,pady=10)
x=Label(st3,text="Phone number :",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
Entry(st3,textvariable=spn).pack(side=LEFT,padx=10,pady=10)
x=Label(st4,text="Your address :",bg="#fff1cf")
x.pack(side=LEFT,padx=15,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
Entry(st4,textvariable=suad).pack(side=LEFT,padx=10,pady=10)
x=Label(st5,text="Education level :",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
style_OM(sedu,st5,"High school","Bachelor", "Master", "Doctoral","High school","Other").pack(side=LEFT,padx=10,pady=10)
x=Label(st6,text="tell us about your       \n skills and Experiences ",bg="#fff1cf")
x.pack(side=LEFT,padx=10,pady=10)
x.config(font=("ubuntu",10),fg="#263f44")
des_us_set=Text(st6,width=30,height=5)
des_us_set.pack(side=LEFT,padx=10,pady=10)
war_sub_set=Label(st8,text="Please fill all boxs",fg="red",bg="#fff1cf")

sbtn1=style_BTN(st7,text="submit",activebackground="#fbd67b",command=partial(update11,sfn,sidcard,spn,suad,sedu,des_us_set,p,us,0,setting_us,option_menu))
sbtn1.pack(side=RIGHT,padx=30,pady=10)
sbtn2=style_BTN(st7,text="Update & Apply",activebackground="#fbd67b",command=partial(update11,sfn,sidcard,spn,suad,sedu,des_us_set,p,us,1,setting_us,apply_us))
bbtn1=style_BTN(st7,text="Back",activebackground="#fbd67b",command=partial(backi,setting_us,option_menu))
bbtn1.pack(side=RIGHT,padx=10,pady=10)
bbtn2=style_BTN(st7,text="Undo",activebackground="#fbd67b",command=partial(back,setting_us,apply_us))
style_BTN1(option_menu1,text=" Update job seeker information ",activebackground="#fbd67b",command=partial(ref_set,option_menu,setting_us,sfn,sidcard,spn,suad,sedu,des_us_set,p,us,0)).pack(side=LEFT,padx=10,pady=10)
style_BTN1(option_menu,text="            Search a job offer           ",activebackground="#fbd67b",command=partial(back,option_menu,search)).pack(padx=10,pady=15)
style_BTN(option_menu,text="Log out",activebackground="#fbd67b",command=partial(back,win3,win1)).pack(padx=10,pady=10)

style_BTN(ap,text=" Apply ",activebackground="#fbd67b",command=partial(apply_job,applytree1,war_ap_exist,sbtn1,sbtn2,sl1,bbtn1,bbtn2,apply_us,setting_us,sfn,sidcard,spn,suad,sedu,des_us_set,p,us)).pack(side=LEFT,padx=20,pady=10)



win.mainloop()


