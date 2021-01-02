import urllib.request
from bs4 import BeautifulSoup

fro = 'http://www.acmicpc.sdnu.edu.cn/user/info/'

def main():
    my_res = ""
    its_res = ""

    my_url = ""
    it_url = ""

    print("Please input your Username:")
    my_url = input()
    my_url = fro + my_url
    print("Please input his or her Username:")
    its_url = input()
    its_url = fro + its_url
    # print(my_url)
    # print(its_url)

    # 获得html文档
    try:
        my_res = urllib.request.urlopen(my_url)
        its_res = urllib.request.urlopen(its_url)
    except Exception as e:
        print(e)

    if my_res is "":
        print("Your Username is wrong")
    elif its_res is "":
        print("His or her Username is wrong")
    else:
        # print(my_res.getcode())
        # print(its_res.getcode())

        # 创建BeautifulSoup对象
        my_bs = BeautifulSoup(my_res, features='html.parser', from_encoding='utf-8')
        its_bs = BeautifulSoup(its_res, features='html.parser', from_encoding='utf-8')

        # 找到所有 标签为"div",class_ 属性为"row"的内容,返回一个列表
        my_list = my_bs.find_all("div", class_="row")
        its_list = its_bs.find_all("div", class_="row")
        # print(my_list[4]) # 共七个元素，我们发现第五个是我们想要的,它本身是一个标签(Tag)

        # print(type(my_list))
        # print(type(my_list[4]))

        # 将该标签通过str强转为字符串作为文本，再次构建一个BeautifulSoup对象
        # my_soup = BeautifulSoup(unicode(my_list[4]), features='html.parser') # py2 -> unicode / py3 -> str
        my_soup = BeautifulSoup(str(my_list[4]), features='html.parser')
        its_soup = BeautifulSoup(str(its_list[4]), features='html.parser')

        # 在此范围内查找所有的'a'标签，即链接
        my_soup = my_soup.find_all('a')
        its_soup = its_soup.find_all('a')
        # print(my_soup.find_all('a'))

        # 用  .string  取出其中的NavigableString（可操纵字符串）对象，即已通过题目的题号,生成列表
        my_sloved = []
        for i in my_soup:
            my_sloved.append(i.string)

        its_sloved = []
        for i in its_soup:
            its_sloved.append(i.string)

        for i in its_sloved:
            if i not in my_sloved:
                print(i)
            else:
                continue

        print("No more!")

if __name__ == "__main__":
    print("针对SDNUOJ，先输入你的用户名，再输入ta的用户名，可比较得出 你没通过而ta通过了 的题目")
    print("------------------------------Developed by fireworks99------------------------------")
    while(1):
        main()
