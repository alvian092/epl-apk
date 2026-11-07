from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

LIGAS = [
    ("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League", "EPL"),
    ("🇪🇸 La Liga", "La Liga"),
    ("🇮🇹 Serie A", "Serie A"),
    ("🇩🇪 Bundesliga", "Bundesliga"),
    ("🇫🇷 Ligue 1", "Ligue 1"),
    ("🇳🇱 Eredivisie", "Eredivisie"),
    ("🇵🇹 Liga Portugal", "Portugal"),
    ("🇸🇦 Saudi Pro League", "Saudi"),
    ("🇮🇩 BRI Liga 1", "Liga 1"),
    ("🇪🇺 Champions League", "UCL"),
    ("🇪🇺 Europa League", "UEL"),
    ("🌍 World Cup", "World Cup"),
]

class LigaApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        root.add_widget(Label(text='[b]SEMUA LIGA - LIVE SCORE[/b]', markup=True, size_hint_y=None, height=50, font_size=22))
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        for nama, kode in LIGAS:
            btn = Button(text=nama, size_hint_y=None, height=60, font_size=18)
            btn.bind(on_press=lambda x, k=kode: self.pilih_liga(k))
            grid.add_widget(btn)
        
        scroll.add_widget(grid)
        root.add_widget(scroll)
        
        self.info = Label(text='Pilih liga di atas', size_hint_y=None, height=50)
        root.add_widget(self.info)
        return root
    
    def pilih_liga(self, kode):
        self.info.text = f"Kamu pilih: {kode} - (Nanti bisa sambung API)"

if __name__ == '__main__':
    LigaApp().run()
