# _*_coding:utf-8_*_
#encoding:utf-8
import re
list = {}
with open('/home/kynton/数据挖掘/作业/太空旅客.txt', 'r') as readFile:
    txt = readFile.read()

def run(string):
    with open(string, 'r') as readFile:
        for line in readFile.readlines():
            line = line.strip('\n')
            reg = re.findall(line, txt)
            num = len(reg)
            list[line] = num
    with open(r'/home/kynton/数据挖掘/作业/结果.txt', 'a') as writeFile:
        for line in list:
            writeFile.write(str(list[line]))
            writeFile.write(' ')
            writeFile.write(line)
            writeFile.write('\n')
    list.clear()

run('/home/kynton/数据挖掘/作业/词典/角色/反派.txt')
run('/home/kynton/数据挖掘/作业/词典/角色/角色.txt')
run('/home/kynton/数据挖掘/作业/词典/角色/角色中的其他.txt')
run('/home/kynton/数据挖掘/作业/词典/角色/男主角.txt')
run('/home/kynton/数据挖掘/作业/词典/角色/女主角.txt')
run('/home/kynton/数据挖掘/作业/词典/角色/配角.txt')
run('/home/kynton/数据挖掘/作业/词典/剧情/发展.txt')
run('/home/kynton/数据挖掘/作业/词典/剧情/结局.txt')
run('/home/kynton/数据挖掘/作业/词典/剧情/剧情.txt')
run('/home/kynton/数据挖掘/作业/词典/剧情/开头.txt')
run('/home/kynton/数据挖掘/作业/词典/剧情/泪点.txt')
run('/home/kynton/数据挖掘/作业/词典/剧情/笑点.txt')
run('/home/kynton/数据挖掘/作业/词典/视听/动作.txt')
run('/home/kynton/数据挖掘/作业/词典/视听/画面.txt')
run('/home/kynton/数据挖掘/作业/词典/视听/镜头.txt')
run('/home/kynton/数据挖掘/作业/词典/视听/试听效果中的其他.txt')
run('/home/kynton/数据挖掘/作业/词典/视听/视听.txt')
run('/home/kynton/数据挖掘/作业/词典/视听/音乐.txt')
run('/home/kynton/数据挖掘/作业/词典/制作/出品公司.txt')
run('/home/kynton/数据挖掘/作业/词典/制作/导演.txt')
run('/home/kynton/数据挖掘/作业/词典/制作/编剧.txt')
run('/home/kynton/数据挖掘/作业/词典/制作/选景.txt')
run('/home/kynton/数据挖掘/作业/词典/制作/制作.txt')
run('/home/kynton/数据挖掘/作业/词典/主题/风格.txt')
run('/home/kynton/数据挖掘/作业/词典/主题/题材内容.txt')
run('/home/kynton/数据挖掘/作业/词典/主题/主题.txt')