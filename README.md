# 周波数周期変換

## 環境
OS: Windows 10
Python: 3.10.4

## 利用ライブラリ
tkinter

## 概要
周期または周波数を入力して、変換ボタンを押すと周期⇒周波数、周波数⇒周期に変換された値が出力されます。
完成したプログラムのGUIはこのようになりました。

![GUI_frequency_convert.png.jpg](https://github.com/zume0606/python_frequency_convert/blob/c98925da4da5c2f0451827232d0dcd56e3b1ce7c/GUI_frequency_convert.png.jpg)

## プログラム解説
tkinterを使って

### ウィンドウ表示
```
root = tk.Tk()
root.geometry("480x360")
root.title("周期周波数変換")

root.mainloop()
```
Tk関数を使うことでウィンドウを表示させることができます。
ウィンドウのサイズはgeometryメソッドを使い、引数で指定してあげます。
ウィンドウの上に表示する名前はtitleメソッドの引数に記述します。
mainloop()を最後に入れてあげて実行すると、ウィンドウが表示されます。

### フレームの実装と配置
```
frame = tk.Frame(root,width=480,heigh=360,padx=10,pady=10)
frame.pack()
```
ウィンドウと同じサイズのフレームを作成し、pack関数で配置しました。

### テキストボックスとラベルの作成と配置
```

```

### 周期、周波数選択のプルダウンの作成と配置
```
module_period =("s","ms","us","ns","ps",)
period_select = ttk.Combobox(frame, height=5, width = 4, values=module_period)
period_select.place(x=150,y=30)
module_frequency = ("Hz","KHz","MHz","GHz","THz",)
frequency_select = ttk.Combobox(frame, height=5, width = 4, values=module_frequency)
frequency_select.place(x=400,y=30)
```
プルダウンを作成するにはttkのウェジットであるComboboxを使います。
配置するフレーム、プルダウンのサイズ、配列で用意した選択肢を引数に記述します。

### ボタンの作成と配置
```
button_y = 70
button_period = tk.Button(frame, text = "周期⇒周波数",width=10, height=1)
button_period.place(x = 50, y = button_y)
button_frequency = tk.Button(frame, text = "周波数⇒周期",width=10, height=1)
button_frequency.place(x = 300, y = button_y)
```
Buttonメソッドを使ってボタンを作成し、placeでflameに配置します。
(placeで調整して配置しないとうまく表示できなかった。pack使えるようになりたい。)

### 周期⇒周波数変換関数の作成
```
period_to_frequency()
```
get()メソッドを使い、TextBoxに入力された周期を取得します。
同じくget()メソッドを使い、プルダウンで選択した単位を取得します。
取得した単位によって単位を変換します。

### 周波数挿入関数の作成

### 周波数⇒周期変換関数の作成
```

```
### ボタンのイベントに変換関数を配置
```
button_y = 70
button_period = tk.Button(frame, text = "周期⇒周波数",width=10, height=1, command=period_to_frequency)
button_period.place(x = 50, y = button_y)
button_frequency = tk.Button(frame, text = "周波数⇒周期",width=10, height=1, command=frequency_to_period)
button_frequency.place(x = 300, y = button_y)
```

### Enterキーでボタンが押されるようにBind(未実装)
```
def press_enter():
    period_to_frequency()
    frequency_to_period()

root.bind("<Return>", lambda event: press_enter())
```
これでpress_enter関数がEnterキーにBindされて呼び出されるはずなのに、反応がない、、、
