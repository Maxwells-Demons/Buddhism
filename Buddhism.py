import base64
import random
from tkinter import Tk

truth_table=[
    '东', '殺', '諦', '曰', '至', '住', '藥', '忧', '蒙', '迦', '焰', '度', '謹', '妙', '智', '皂', 
    '药', '經', '牟', '麼', '在', '孝', '界', '诵', '婦', '弟', '蘇', '竟', '德', '粟', '路', '茶', 
    '栗', '特', '孤', '排', '西', '经', '慈', '行', '游', '訶', '難', '六', '精', '未', '輸', '楞', 
    '去', '寂', '盧', '过', '故', '金', '安', '羅', '參', '吼', '橋', '央', '即', '曳', '消', '閦', 
    '倒', '造', '稳', '戒', '藐', '親', '數', '普', '中', '朋', '释', '闍', '解', '夢', '鄉', '五', 
    '诸', '守', '刚', '彌', '名', '陰', '足', '劫', '帝', '清', '勒', '時', '伊', '求', '戏', '功', 
    '月', '除', '便', '贤', '宗', '灯', '夫', '者', '毒', '敬', '憐', '室', '号', '信', '姪', '灭', 
    '以', '通', '方', '遮', '穆', '亿', '百', '昼', '睦', '貧', '殊', '说', '積', '高', '利', '沙', 
    '僧', '奉', '花', '遠', '他', '亦', '孕', '心', '資', '福', '璃', '毘', '矜', '夷', '惜', '顛', 
    '藝', '文', '急', '恤', '令', '阿', '放', '涅', '和', '告', '老', '怖', '山', '尼', '舍', '孫', 
    '濟', '琉', '雙', '进', '廣', '想', '施', '師', '礙', '多', '休', '逝', '印', '愛', '友', '薩', 
    '先', '槃', '持', '提', '真', '乾', '幽', '此', '尊', '重', '究', '三', '兄', '北', '陵', '瑟', 
    '树', '紛', '哈', '善', '捐', '须', '胜', '隸', '困', '依', '創', '陀', '修', '万', '捨', '族', 
    '来', '死', '根', '實', '夜', '拔', '首', '虚', '量', '呼', '师', '耨', '祖', '豆', '下', '各', 
    '寡', '息', '知', '于', '千', '醯', '殿', '定', '禮', '如', '廟', '王', '数', '宇', '众', '恐', 
    '盡', '能', '七', '寫', '弥', '宝', '梭', '害', '生', '及', '开', '空', '教', '念', '凉', '护',
    '色', '命', '乖', '岚',
]

quotes=[
    ' ',
    '命由己造，相由心生',
    '一即一切，一切即一',
    '刹那便是永恒',
    '无穷般若心自在，语默动静体自然',
    '无悲无喜无梦无幻，无爱无恨四大皆空',
    '人无善恶，善恶存乎尔心',
    '春来花自青，秋至叶飘零',
    '一念愚即般若绝，一念智即般若生',
    '参不透，舍不得',
    '菩提本无树，明镜亦非台',
    '悠然，随心，随性，随缘',
    '心不动，万物皆不动',
    '渡己，亦是渡人',
    '但离妄缘，即如如佛',
    '心中业物',
    '业障物碍，肇源心中，佛力清净，一切皆消',
    '自见性者一切业障刹那灭却',
    '若欲求佛但求心，只这心心心是佛',
]

alpha_dict={
    '+':   0,'/':   4,'0':   8,'1':  12,'2':  16,'3':  20,'4':  24,'5':  28,
    '6':  32,'7':  36,'8':  40,'9':  44,'A':  48,'B':  52,'C':  56,'D':  60,
    'E':  64,'F':  68,'G':  72,'H':  76,'I':  80,'J':  84,'K':  88,'L':  92,
    'M':  96,'N': 100,'O': 104,'P': 108,'Q': 112,'R': 116,'S': 120,'T': 124,
    'U': 128,'V': 132,'W': 136,'X': 140,'Y': 144,'Z': 148,'a': 152,'b': 156,
    'c': 160,'d': 164,'e': 168,'f': 172,'g': 176,'h': 180,'i': 184,'j': 188,
    'k': 192,'l': 196,'m': 200,'n': 204,'o': 208,'p': 212,'q': 216,'r': 220,
    's': 224,'t': 228,'u': 232,'v': 236,'w': 240,'x': 244,'y': 248,'z': 252,
    '=': 256,
}

def get_str():
    s=''
    with open('D:\\Users\\Legion\\Desktop\\Coding\\Python\\Buddhism\\test.txt') as f:
        s+=f.read()
    return s

def enc_b64(s):
    return base64.b64encode(s.encode()).decode()

def dec_b64(s):
    return base64.b64decode(s).decode()

def enc_str(s):
    s=enc_b64(s)
    newstr=''
    li=list()
    for i in range(len(s)):
        li.append(alpha_dict[s[i]])
    for i in range(len(li)):
        li[i]+= (i%4)
    for i in range(len(li)):
        newstr+=truth_table[li[i]]
    return newstr

def dec_str(s):
    newstr=''
    li=list()
    for i in range(len(s)):
        if s[i]=='\n':
            continue
        li.append(truth_table.index(s[i]))
    
    for i in range(len(li)):
        li[i]-= (i%4)

    for i in range(len(li)):
        for key in alpha_dict:
            if li[i]==alpha_dict[key]:
                newstr+=key
                break

    return dec_b64(newstr)

# s=get_str()
# print(enc_str(s))
# print(dec_str(enc_str(s)))


import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('与佛论禅')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1280x800')  # 这里的乘是小x
 
# 第4步，在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, text='与佛论禅', fg='black', font=('微软雅黑', 30, 'bold'), width=30, height=2)
# l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.place(x=250,y=-10)
 
# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名

def enc_but():
    var.set(random.choice(quotes))
    s=t1.get('0.0','end')
    t2.delete('0.0','end')
    t2.insert(tk.END,enc_str(s))

def dec_but():
    var.set(random.choice(quotes))
    s=t3.get('0.0','end')
    t4.delete('0.0','end')
    try:
        t4.insert(tk.END,dec_str(s))
    except ValueError:
        t4.insert(tk.END,'太深奥了，参悟不出个中真意……')

def help_but():
    help=tk.Tk()
    help.title('普渡众生')
    help.geometry('800x400')
    tk.Label(help,text='''
        在吾言处输入要加密的文字，点击听佛说宇宙的真谛，就能在下面得到打码后的文字。
        将吾闻处输入要加密的文字，点击参悟佛所言的真意，就能在上面得到解码后的文字。
        如果显示“太深奥了，参悟不出个中真意……”，请检查佛经是否有误。
        由于无法右键复制粘贴，请使用快捷键。
        作者：Maxwells_Demon
        QQ：2232972354
    ''').place(x=50,y=10)
    tk.Button(help,text='然也',font=('微软雅黑', 20),command=help.destroy).place(x=350,y=200)

# 第5步，在窗口界面设置放置Button按键
b1 = tk.Button(window, text='听佛说宇宙的真谛', font=('微软雅黑', 20), width=15, height=1, command=enc_but)
b1.place(x=160,y=100)
tk.Label(window,text='吾言：',height=1).place(x=30,y=180)
t1 = tk.Text(window, height=15,width=70)
t1.place(x=30,y=220)
tk.Label(window,text='佛曰：',height=1).place(x=30,y=480)
t2 = tk.Text(window, height=15,width=70)
t2.place(x=30,y=520)

b2 = tk.Button(window, text='参悟佛所言的真意', font=('微软雅黑', 20), width=15, height=1,command=dec_but)
b2.place(x=825,y=100)
tk.Label(window,text='吾闻：',height=1).place(x=675,y=180)
t3 = tk.Text(window, height=15,width=70)
tk.Label(window,text='佛曰：',height=1).place(x=675,y=480)
t3.place(x=675,y=220)
t4 = tk.Text(window, height=15,width=70)
t4.place(x=675,y=520)

b3 = tk.Button(window, text='普渡众生', font=('微软雅黑', 20),command=help_but)
b3.place(x=570,y=100)

var.set(quotes[1])
quote_label=tk.Label(window, textvariable=var,width=40, height=2)
quote_label.place(x=30,y=30)
# 第6步，主窗口循环显示
window.mainloop()