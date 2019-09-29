from tkinter import *
from tkinter import ttk
import os
import re
import time
import threading
import urllib.request


def calculate(*args):
	try:
		dresult.set(" 111")
	except ValueError:
		pass

def thread_it(func, *args):
    # 创建
    t = threading.Thread(target=func, args=args)
    # 服务进程
    t.setDaemon(True)
    # 启动
    t.start()		

def address_made(*args):
	try:
		year_s = "&year="+str(year.get())
		spc_s = "spc=" + str(spc.get()) + "&type=sdr"
		doy_s = "&Doy=" + str(wdoy.get().zfill(3))
		key_s = "https://ssusi.jhuapl.edu/data_retriver?"
		sq_url = key_s + spc_s + year_s + doy_s
		squrl.set(sq_url)
		url = str(squrl.get())
		headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
		opener = urllib.request.build_opener()
		opener.addheaders = [headers]
		urllib.request.install_opener(opener)
		file = urllib.request.urlopen(url).read()
		file = file.decode('utf-8')
		pattern = '(dataN[^\s)";]+SDR-DISK[^\s)";]+NC)'
		link = re.compile(pattern).findall(file)
		linklist = list(set(link))
		htmlresult.set("当前页面共有文件"+str(len(linklist)))
	except ValueError:
		pass
def download_res(*args):
	try:
		key_s = "https://ssusi.jhuapl.edu/data_retriver?"
		year_s = "&year="+str(year.get())
		spc_s = "spc=" + str(spc.get()) + "&type=sdr"
		for i in range(364):
			i = int(wdoy.get())
			doy_l = str(i).zfill(3)
			doy_s = "&Doy=" + doy_l
			doy_show.set("当前第"+ str (i)+"天")
			sq_url = key_s + spc_s + year_s + doy_s
			squrl.set(sq_url)
			url = str(squrl.get())
			headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
			opener = urllib.request.build_opener()
			opener.addheaders = [headers]
			urllib.request.install_opener(opener)
			file = urllib.request.urlopen(url).read()
			file = file.decode('utf-8')
			pattern = '(dataN[^\s)";]+SDR-DISK[^\s)";]+(\.(\w|/)*)NC)'
			link = re.compile(pattern).findall(file)
			linklist = list(set(link))
			htmlresult.set("当前页面共有文件"+str(len(linklist)))
			k = 1
			lcal = "./" +str(year.get())+ str(doy_l) +str(spc.get())+ "/"
			os.makedirs(lcal)
			for lurl in linklist:
						dresult.set("当前下载第"+ str(k) + "个")
						time.sleep(0.1)
						flink = "https://ssusi.jhuapl.edu/" + str(lurl[0])
						print(k)
						# print(lcal + str(flink[54:]))
						print(lurl[0])
						f = urllib.request.urlopen(flink)
						data = f.read()
						with open(lcal + str(flink[54:]), "wb") as code:     
								code.write(data)   					
						k = k + 1 
			i = i + 1
	except ValueError:
		pass

		


root = Tk()
root.resizable(0,0)
root.title("数据下载")
root.geometry("600x300")
# mainframe = ttk.Frame(root)
# mainframe.place()
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)




year = StringVar()
spc = StringVar()
wdoy = StringVar() 
doy = StringVar()
doy_show = StringVar()
htmlresult = StringVar()
dresult = StringVar()
squrl = StringVar()
linklist = StringVar()


ttk.Label(text="年份").place(x=20,y=30,bordermode=INSIDE)
feet_entry = ttk.Entry(textvariable=year )
feet_entry.place(x=100,y=30,bordermode=INSIDE)

ttk.Label(text="卫星").place(x=20,y=60,bordermode=INSIDE)
feet_entry = ttk.Entry(textvariable=spc )
feet_entry.place(x=100,y=60,bordermode=INSIDE)

ttk.Label(text="天数").place(x=20,y=90,bordermode=INSIDE)
ttk.Label(textvariable=doy_show).place(x=20,y=120,bordermode=OUTSIDE)
feet_entry = ttk.Entry(textvariable=wdoy )
feet_entry.place(x=100,y=90,bordermode=INSIDE)

# ttk.Label(mainframe, text="卫星").place(x=20,y=30,width=30,height=40,bordermode=INSIDE)
# feet_entry = ttk.Entry(mainframe, width=20, textvariable=spc)
# feet_entry.place(x=20,y=30,width=30,height=40,bordermode=INSIDE)


ttk.Label(textvariable=squrl).place(x=130,y=150,bordermode=OUTSIDE)
ttk.Label(textvariable=htmlresult).place(x=130,y=180,bordermode=OUTSIDE)
ttk.Label(textvariable=dresult).place(x=130,y=210,bordermode=OUTSIDE)
ttk.Label(text="请参考可用数据表格进行下载，无数据的页面会下载错误数据").place(x=20,y=240,bordermode=INSIDE)
ttk.Button(text="测试地址", command=lambda :thread_it(address_made)).place(x=20,y=150,bordermode=INSIDE)
ttk.Button(text="下载", command=lambda :thread_it(download_res)).place(x=20,y=210,bordermode=INSIDE)
# ttk.Button(text="test", command=calculate).place(x=20,y=220,bordermode=INSIDE)
# # ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# # ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind('<Return>', calculate)

root.mainloop()
