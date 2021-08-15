from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
import requests
from bs4 import BeautifulSoup
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

link = "https://vk.com/public204031350"

defense = 1
tests = requests.post(link).text
soup = BeautifulSoup(tests, 'html.parser')
block = soup.find('div', id="page_wall_posts")
block2 = block.find('div', class_="wall_post_text")
lst1 = []
lst2 = []
lst3 = []
most_scores = 0
s = 0
if str(block2)[28:-6].count("<br/>") < 9:
    block2 = str(block2)[28:-6].split("<br/>")
    mail = block2[-1]
    del block2[-1]
    for i in block2:
        s += 1
        if s % 3 == 0:
            lst3.append(i)
        elif s % 2 == 0:
            lst2.append(i)
        else:
            lst1.append(i)
        if s == 3:
            s = 0
else:
    block2 = str(block2)[28:-13].split("<br/>")
    del block2[5]
    mail = block2[-1]
    del block2[-1]
    for i in block2:
        s += 1
        if s % 3 == 0:
            lst3.append(i)
        elif s % 2 == 0:
            lst2.append(i)
        else:
            lst1.append(i)
        if s == 3:
            s = 0
user_scores = 0
for i in lst3:
    most_scores += float(i)
ans = len(lst1)

list = []
list2 = []
defense = 1
tests = requests.post(link).text
soup = BeautifulSoup(tests, 'html5lib')
block = soup.find_all('div', class_="wall_post_text")[-1].text.split(',')
block = " ".join(block)
block = block.split('Показать полностью...')
block = "".join(block)
block = block.split(" ")
for i in range(int(len(block) / 3)):
    list.append(block[:3])
    block.remove(block[0])
    block.remove(block[0])
    block.remove(block[0])
for i in list:
    list2.append(" ".join(i))


class ТыклассApp(App):
    def build(self):
        self.mail = mail
        self.user_scores = 0
        self.al = AnchorLayout()
        self.al3 = AnchorLayout(anchor_x='center', anchor_y='top')
        self.al4 = AnchorLayout(anchor_x='center', anchor_y='top')
        self.bl1 = BoxLayout(orientation="horizontal")
        self.bl2 = BoxLayout()
        self.bl4 = BoxLayout()
        self.bl6 = BoxLayout(orientation="horizontal")
        self.bl3 = BoxLayout(orientation="horizontal", spacing=4)
        self.bl5 = BoxLayout(orientation="vertical", spacing=7, size_hint=[0.8, 0.3])
        self.bl = BoxLayout(orientation="vertical", size_hint=[0.8, 0.2], spacing=7)
        self.al2 = AnchorLayout(anchor_x='center', anchor_y='center')
        self.i = 0
        self.bl2.add_widget(Label(text='Введите ваши данные'))
        self.bl1.add_widget(Label(text='Фамилия и имя', size_hint=[1, 1]))
        self.bl1.add_widget(Label(text='Класс'))
        self.bl5.add_widget(self.bl2)
        self.bl5.add_widget(self.bl1)
        self.namee = TextInput(font_size='20sp', multiline=False)
        self.clas = TextInput(font_size='20sp', multiline=False)
        self.bl3.add_widget(self.namee)
        self.bl3.add_widget(self.clas)
        self.bl5.add_widget(self.bl3)
        self.bl4.add_widget(Button(text='Далее', on_press=self.start))
        self.bl5.add_widget(self.bl4)
        self.al.add_widget(self.bl5)
        global namee
        namee = self.namee
        global clas
        clas = self.clas
        return self.al

    def build2(self, instance):
        self.al.clear_widgets()
        self.al3.clear_widgets()
        self.bl1.clear_widgets()
        self.bl2.clear_widgets()
        self.bl4.clear_widgets()
        self.bl3.clear_widgets()
        self.bl5.clear_widgets()
        self.bl.clear_widgets()
        self.al2.clear_widgets()
        self.bl2.add_widget(Label(text='Введите ваши данные'))
        self.bl1.add_widget(Label(text='Фамилия и имя', size_hint=[1, 1]))
        self.bl1.add_widget(Label(text='Класс'))
        self.bl5.add_widget(self.bl2)
        self.bl5.add_widget(self.bl1)
        self.namee = TextInput(font_size='20sp', multiline=False)
        self.clas = TextInput(font_size='20sp', multiline=False)
        self.bl3.add_widget(self.namee)
        self.bl3.add_widget(self.clas)
        self.bl5.add_widget(self.bl3)
        self.bl4.add_widget(Button(text='Далее', on_press=self.start))
        self.bl5.add_widget(self.bl4)
        self.al.add_widget(self.bl5)
        global namee
        namee = self.namee
        global clas
        clas = self.clas

    def start(self, instance):
        self.bl1.clear_widgets()
        self.bl2.clear_widgets()
        self.bl3.clear_widgets()
        self.bl4.clear_widgets()
        self.bl5.clear_widgets()
        self.bl.clear_widgets()
        self.al.clear_widgets()
        self.bl2.add_widget(Label(text=''))
        self.bl5.add_widget(self.bl2)
        self.pasword = TextInput(font_size='20sp', multiline=False)
        self.bl1.add_widget(Label(text='Пароль'))
        self.bl3.add_widget(self.pasword)
        self.bl4.add_widget(
            Button(text='Начать тест', on_press=self.on_press_button))
        self.bl5.add_widget(self.bl1)
        self.bl5.add_widget(self.bl3)
        self.bl5.add_widget(self.bl4)
        self.al.add_widget(self.bl5)

    def on_press_button(self, instance):
        user = self.namee.text + ' ' + self.pasword.text
        global list2
        if user in list2:
            global defense
            defense = 0
            self.start_test = datetime.datetime.now().strftime(
                "  Начало тестирования: \n  %D %H:%M:%S")
            self.start_test2 = datetime.datetime.now().strftime("%D %H:%M:%S")
            if self.i != 0:
                if str(self.text.text) == str(lst2[self.i - 1]):
                    self.user_scores += float(lst3[self.i - 1])
            self.i += 1
            self.al.clear_widgets()
            self.bl.clear_widgets()
            self.al2.clear_widgets()

            class WrappedLabel1(Label):
                # Based on Tshirtman's answer
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.bind(
                        width=lambda *x:
                        self.setter('text_size')(self, (self.width, None)),
                        texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

            my_label1 = WrappedLabel1(
                text=lst1[self.i - 1],
                font_size="15sp")
            self.al3.add_widget(
                Label(text=str(self.i) + " вопрос из " + str(len(lst2)), size_hint=[1, .1],
                      font_size='20sp'))
            self.al.add_widget(self.al3)
            self.bl.add_widget(my_label1)

            self.text = TextInput(multiline=False, font_size="20sp")
            self.bl.add_widget(self.text)

            if self.i != ans:
                self.bl.add_widget(Button(text="Ответить", on_press=self.on_press_button))
            else:
                class WrappedLabel(Label):
                    # Based on Tshirtman's answer
                    def __init__(self, **kwargs):
                        super().__init__(**kwargs)
                        self.bind(
                            width=lambda *x:
                            self.setter('text_size')(self, (self.width, None)),
                            texture_size=lambda *x: self.setter('height')(self,
                                                                          self.texture_size[1]))

                my_label = WrappedLabel(
                    text=lst1[self.i - 1],
                    font_size="15sp")

                self.bl.clear_widgets()
                self.al3.clear_widgets()
                self.al.clear_widgets()
                self.bl6.clear_widgets()
                self.al3.add_widget(
                    Label(text=str(self.i) + " вопрос из " + str(len(lst2)), size_hint=[1, .1],
                          font_size='20sp'))
                self.al.add_widget(self.al3)
                self.bl.add_widget(my_label)

                self.text = TextInput(multiline=False, font_size="20sp")
                self.bl.add_widget(self.text)
                self.bl.add_widget(
                    Button(text="Завершить тест", on_press=self.on_press_tex))
            self.al.add_widget(self.bl)
            self.al.add_widget(self.al2)
        else:
            self.al.clear_widgets()
            self.bl.clear_widgets()
            self.al2.clear_widgets()
            self.bl.add_widget(Label(text="Ошибка входа"))
            self.bl.add_widget(
                Button(text="Попобовать снова", on_press=self.build2))
            self.al.add_widget(self.bl)

    def on_press_tex(self, instance):
        self.bl.clear_widgets()
        end_test = datetime.datetime.now().strftime(" Конец тестирования: \n %D %H:%M:%S")
        end_test2 = datetime.datetime.now().strftime("%D %H:%M:%S")
        if self.text.text == lst2[self.i - 1]:
            self.user_scores += float(lst3[self.i - 1])
        self.al.clear_widgets()
        self.bl.add_widget(
            Label(text="       Вы набрали \n" + str(self.user_scores) + " балла(ов) из " + str(
                most_scores)))

        self.bl.add_widget(Label(text=self.start_test))

        self.bl.add_widget(Label(text=end_test))
        self.al.add_widget(self.bl)
        self.mail = self.mail + '.ru'
        msg = MIMEMultipart()

        message = f'{self.namee.text} из {self.clas.text} класса сдал тест на {self.user_scores} балла(ов) из {most_scores}. Начало тестирования: {self.start_test2}, конец тестирования: {end_test2}'

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.mail.ru: 25')
        server.starttls()
        server.login("test_system_489@mail.ru", "Tes_sys2021")
        server.sendmail("test_system_489@mail.ru", self.mail, msg.as_string())
        server.quit()
        global defense
        defense = 1


if __name__ == '__main__':
    app = ТыклассApp()
    app.run()

if defense != 1:
    msg = MIMEMultipart()

    message = f'{namee.text} из {clas.text} класса не сдал(а) тест'

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.mail.ru: 25')
    server.starttls()
    server.login("test_system_489@mail.ru", "Tes_sys2021")
    server.sendmail("test_system_489@mail.ru", mail + ".ru", msg.as_string())
    server.quit()
    defense = 1