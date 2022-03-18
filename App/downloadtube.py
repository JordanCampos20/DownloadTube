#--------------------------------------------DownloadTube
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import yt_dlp
import threading
#----------------------------------------------Telas
class MainScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
#-------------------------------------------Aplicativo
class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        self.title = 'DownloadTube - Jordan'
        self.icon = '../Images/icon.png'
        Window.size = 800, 600

        return Builder.load_file('../Interface/downloadtube.kv')

#--------------------------------------------DOWNLOAD-REAL

    def download(self):

        link = self.root.get_screen("main").ids.download_input.text

        ydl_opts = {
            'outtmpl': '../Download/%(id)s.%(ext)s',
        }

        v_youtube = link.find('https://www.youtube.com', 0, 23)
        v_twitter = link.find('https://twitter.com', 0, 19)

#--------------------------------------------ZELDA

        if link == '':

            self.root.get_screen("main").ids.aviso_label.text = "[color=000000]AVISOS: Não Possui Link![/color]"

#-------------------------------------------ACERTOS

        elif v_youtube == 0:

            self.root.get_screen("main").ids.aviso_label.text = "[color=000000]AVISOS: Baixando Video do Youtube![/color]"

            link1 = [f'{link}']
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(link1)

                self.root.get_screen("main").ids.aviso_label.text = "[color=000000]Download Concluido com Sucesso![/color]"

        elif v_twitter == 0:
            self.root.get_screen("main").ids.aviso_label.text = "[color=000000]AVISOS: Baixando Video do Twitter![/color]"

            link1 = [f'{link}']
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(link1)

                self.root.get_screen("main").ids.aviso_label.text = "[color=000000]Download Concluido com Sucesso![/color]"

#---------------------------------------------ERROS

        elif v_youtube == -1:

            self.root.get_screen("main").ids.aviso_label.text = "[color=000000]LINK NÃO ACEITO![/color]"

        elif v_twitter == -1:

            self.root.get_screen("main").ids.aviso_label.text = "[color=000000]LINK NÃO ACEITO![/color]"

#--------------------------------------------BOTÃO

    def downloadbutton(self):
        thread = threading.Thread(target=self.download)
        thread.start()

MainApp().run()















