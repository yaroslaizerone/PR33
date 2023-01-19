from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class myApp(App):
    def build(self):
        Window.size = (360, 800)
        layout = BoxLayout(padding=10, orientation='vertical')
        self.label = Label(text='Привет!')
        self.label2 = Label(text='Цвет...')
        layout.add_widget(self.label)
        layout.add_widget(self.label2)
        colors = ['#ff0000', '#ff8800', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff']
        for i in range(7):
            btn = Button(text=colors[i], background_color=colors[i], background_normal='', on_press=self.change)
            layout.add_widget(btn)
        return layout


    def change(self, instance):
        self.label.text = instance.text
        colors = {'#ff0000': 'Красный',
                  '#ff8800': 'Оранжевый',
                  '#ffff00': 'Желтый',
                '#00ff00': 'Зеленый',
            '#00ffff': 'Голубой',
        '#0000ff': 'Синий',
        '#ff00ff': 'Фиолетовый'}
        self.label2.text = colors.get(instance.text)



if __name__ == "__main__":
    myApp().run()
