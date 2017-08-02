import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread
from os import path
import jieba
import jieba.analyse
import time


def getContent():
    text = open('ciyun.txt','r',encoding= 'utf-8').read()
    testjieba = jieba.cut(text,cut_all = True)
    wk_split = " ".join(testjieba)
    return wk_split

#词云
def getWordCloud(pathname,fontname,content,img,width,height,max_font_size,min_font_size):

    my_wordcloud = WordCloud(
                        font_path = fontname,
                        background_color = "white",
                        mask = img,
                        width = width,
                        height = height,
                        max_words = 1000,
                        max_font_size = max_font_size,
                        min_font_size = min_font_size,
                        random_state=42,
                        scale =1.5,
                         ).generate(content)

    plt.imshow(my_wordcloud,cmap=plt.cm.gray)
    plt.axis("off")
    my_wordcloud.to_file(pathname)

#词出现次数统计
def textCiYunTJ():
    # 分词
    word_lst = []
    word_dict = {} 
    for line in open('ciyun.txt',encoding='utf-8'):

        item = line.strip() #制表格切分  
        # print (item)  
        tags = jieba.analyse.extract_tags(item) #jieba分词  
        for t in tags:  
            word_lst.append(t)
        # print (word_lst)
        for item in word_lst:
            if item not in word_dict:
                word_dict[item] = 1
            else:
                word_dict[item] += 1

    with open("wordCount.txt",'w') as wf2: #打开文件  

        orderlist = list(word_dict.values())
        orderlist.sort(reverse=True)
        for i in range(len(orderlist)):
            for key in word_dict:
                if word_dict[key] == orderlist[i]:
                    wf2.write(key+' '+str(word_dict[key]) + '\n')

        print (orderlist)
        

if __name__ == '__main__':

    fontname = path.join('msyh.ttc')
    img = imread('.././pythonSucai/hbperson.jpg')
    content = getContent()
    getWordCloud('wordCloud.jpg',fontname,content,img,500,300,50,2)
    
    # textCiYunTJ()
    