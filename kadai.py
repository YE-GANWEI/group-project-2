# -*- coding: utf-8 -*-
"""kadai.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GY8eZh5w3w-VabHnupLytOvw2dAyO-u1

#ハングマン
![フローチャート](http://a1.qpic.cn/psc?/V10LOwxy1o7r6C/wZu0*zqyEz4NDRuTFUPfB*9sDYBEVxXxApXBPRiokBHXUyXgjH282y75fAzo*xW2ydcoIW5aCTyhvcIDEvRPSQ!!/c&ek=1&kp=1&pt=0&bo=2gRZBdoEWQURGS4!&tl=3&vuin=1084585996&tm=1580295600&sce=60-2-2&rf=0-0)

1.出題者から出題する。
"""

ti = input(prompt='単語を入力してください',)

"""単語の文字数を表す下線を引く。"""

chang=len(ti)
chang_a="_"*chang
print(chang_a)

"""答えリストを生成する。"""

ti_list=[]
for x in ti:
  ti_list.append(x)
print(ti_list)

"""タイトルリストを生成する。"""

chang_list=[]
for y in chang_a:
  chang_list.append(y)
print(chang_list)

"""出題者は絞首刑台を描く準備する。"""

jiao=12
kaishi=0
def jianyi(a):
  kaishi=a+1
  return(a+1)

"""2.解答者がクイズを解く"""

caiti=input(prompt='文字(英語)を入力してください',)

"""3.この文字がタイトルに存在するかどうかを判断する。"""

if kaishi < jiao:
  if caiti in ti_list:
    if chang_list == ti_list:
      print("勝った")
    for index,value in enumerate(ti_list):
      if value==caiti:
        chang_list[index]=caiti
        print (chang_list)
        print(kaishi,"まだ",jiao-kaishi,"回のチャンスがある")
  else:
    kaishi=jianyi(kaishi)
    print("×")
    print(chang_list)
    print(kaishi,"まだ",jiao-kaishi,"回のチャンスがある")
elif kaishi==jiao:
  print("負けた")
  print(chang_list)
  print(ti_list)
else:
  print("間違いがあります。")

"""4.勝敗が決まるまで2.3.を繰り返す。"""