from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp, sp
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

THEMES = [
    {"name": "1. Cosmic ", "bg": "#1E2229", "card": "#2D333F", "input": "#3A4252", "accent": "#E0A899", "text": "#FFFFFF", "accent_text": "#1E2229", "muted": "#8FA0B3"},
    {"name": "2. Cyberpunk ", "bg": "#050505", "card": "#121212", "input": "#1C1C1C", "accent": "#00F5D4", "text": "#FFFFFF", "accent_text": "#050505", "muted": "#666666"},
    {"name": "3. Forest ", "bg": "#1B2421", "card": "#24302B", "input": "#2F3E37", "accent": "#A3C6B4", "text": "#FFFFFF", "accent_text": "#1B2421", "muted": "#6E8579"},
    {"name": "4. Midnight ", "bg": "#2E3440", "card": "#3B4252", "input": "#434C5E", "accent": "#88C0D0", "text": "#FFFFFF", "accent_text": "#2E3440", "muted": "#D8DEE9"},
    {"name": "5. Golden ", "bg": "#111111", "card": "#1A1A1A", "input": "#2A2A2A", "accent": "#D4AF37", "text": "#FFFFFF", "accent_text": "#111111", "muted": "#AA8C2C"},
    {"name": "6. Crimson ", "bg": "#1A0F11", "card": "#2A181B", "input": "#3D2327", "accent": "#FF4A5A", "text": "#FFFFFF", "accent_text": "#1A0F11", "muted": "#B3343F"},
    {"name": "7. Royal Amethyst", "bg": "#120E1A", "card": "#1F192B", "input": "#2D243F", "accent": "#9B5DE5", "text": "#FFFFFF", "accent_text": "#120E1A", "muted": "#7B46B8"},
    {"name": "8. Orlando Pirates", "bg": "#0D0D0D", "card": "#1A1A1A", "input": "#262626", "accent": "#FFFFFF", "text": "#FFFFFF", "accent_text": "#0D0D0D", "muted": "#999999"},
    {"name": "9. Mamelodi Sundowns", "bg": "#00529C", "card": "#00407A", "input": "#002F5C", "accent": "#FFD200", "text": "#FFFFFF", "accent_text": "#00529C", "muted": "#A2C4E3"},
    {"name": "10. Springbok Green", "bg": "#00462C", "card": "#003320", "input": "#002114", "accent": "#FFC222", "text": "#FFFFFF", "accent_text": "#00462C", "muted": "#99B5AB"},
    {"name": "11. Ocean", "bg": "#0A1128", "card": "#1C2541", "input": "#3B4465", "accent": "#00B4D8", "text": "#FFFFFF", "accent_text": "#0A1128", "muted": "#8D99AE"},
    {"name": "12. Sunset ", "bg": "#231105", "card": "#3A4252", "input": "#5C2E0F", "accent": "#F77F00", "text": "#FFFFFF", "accent_text": "#231105", "muted": "#A8846A"},
    {"name": "13. Platinum", "bg": "#E5E5E5", "card": "#FFFFFF", "input": "#F5F5F5", "accent": "#2B2D42", "text": "#1D3557", "accent_text": "#FFFFFF", "muted": "#6C757D"},
    {"name": "14. Solar Flare", "bg": "#1C0A00", "card": "#331400", "input": "#4D1F00", "accent": "#FFB703", "text": "#FFFFFF", "accent_text": "#1C0A00", "muted": "#9E7B66"},
    {"name": "15. Slime", "bg": "#0D1A0D", "card": "#1A331A", "input": "#264D26", "accent": "#39FF14", "text": "#FFFFFF", "accent_text": "#0D1A0D", "muted": "#739973"},
    {"name": "16. Retro ", "bg": "#200B3B", "card": "#34115C", "input": "#4C1C85", "accent": "#FF007F", "text": "#00FFFF", "accent_text": "#200B3B", "muted": "#A482D4"},
    {"name": "17. Electric Vapor", "bg": "#0F001A", "card": "#1D0033", "input": "#310052", "accent": "#BD00FF", "text": "#00FF99", "accent_text": "#0F001A", "muted": "#9475A8"},
    {"name": "18. Stealth", "bg": "#121315", "card": "#1E2022", "input": "#2B2E30", "accent": "#4A5056", "text": "#E3E4E6", "accent_text": "#FFFFFF", "muted": "#6A7075"},
    {"name": "19. Desert ", "bg": "#2C251E", "card": "#3D342A", "input": "#524639", "accent": "#C2A67D", "text": "#FFFFFF", "accent_text": "#2C251E", "muted": "#A19284"},
    {"name": "20. Matrix", "bg": "#000000", "card": "#050B05", "input": "#0A140A", "accent": "#00FF00", "text": "#33FF33", "accent_text": "#000000", "muted": "#005500"},
    {"name": "21. Blizzard", "bg": "#D8F3DC", "card": "#B7E4C7", "input": "#95D5B2", "accent": "#1B4332", "text": "#081C15", "accent_text": "#D8F3DC", "muted": "#40916C"},
    {"name": "22. Copper ", "bg": "#221A15", "card": "#332720", "input": "#47362C", "accent": "#D05A3F", "text": "#FFFFFF", "accent_text": "#221A15", "muted": "#967A6C"},
    {"name": "23. Birthday Amethyst", "bg": "#240046", "card": "#3C096C", "input": "#5A189A", "accent": "#EA54FF", "text": "#FFFFFF", "accent_text": "#240046", "muted": "#C77DFF"}
]

LANGUAGES = {
    "English": {"total_lbl": "TOTAL FARE COST", "fare_lbl": "ENTER FARE FOR 1 PERSON: R", "grid_lbl": "TAP QUANTITY PAYING TOGETHER:", "note_lbl": "NOTE PASSED FORWARD: R", "calc_btn": "CALCULATE CHANGE", "init_status": "AWAITING CASH INPUT", "short_status": "SHORTAGE: IMALI ISHODILE!", "reset_btn": "RESET", "undo_btn": "UNDO LAST", "person": "People"},
    "isiZulu": {"total_lbl": "IMALI ENGEZIWE SEKUHLELO", "fare_lbl": "FAKA IPRESI YOMUNTU OY'1: R", "grid_lbl": "TAP ABANTU ABABHADALAYO:", "note_lbl": "I-NOTE EYI-FRONT: R", "calc_btn": "BALA U-SHINTSHO", "init_status": "INDLELA EYA PHRAMBILI", "short_status": "IMALI ISHODILE EPHRAMBILI!", "reset_btn": "SUSA", "undo_btn": "BUYISELA", "person": "Abantu"},
    "isiXhosa": {"total_lbl": "IMALI EDIBANISIWEYO", "fare_lbl": "FAKA INTLAWULO YOMNTU OY'1: R", "grid_lbl": "COFA ABANTU ABABHATALAYO:", "note_lbl": "I-NOTE EDIPHISIWEYO: R", "calc_btn": "BALA UTSHINTSHO", "init_status": "INDLELA EYA PHAMBILI", "short_status": "IMALI ENKILE IYASHOTA!", "reset_btn": "CIMA", "undo_btn": "BUYISELA", "person": "Abantu"},
    "Sesotho": {"total_lbl": "CHELETE E KOPANTSENG", "fare_lbl": "KENYA TEFO YA MOTHO A LE 1: R", "grid_lbl": "TLICHA BATHO BA LEFANG MAREO:", "note_lbl": "I-NOTE E FETISITSOENG: R", "calc_btn": "BALA CHENTJHI", "init_status": "TSELA E YA PELE", "short_status": "CHELETE EA TLHAELLA!", "reset_btn": "TLOSA", "undo_btn": "KHUTLISA", "person": "Batho"},
    "Afrikaans": {"total_lbl": "TOTALE REISGELD KOSTE", "fare_lbl": "VOER REISGELD PER PERSOON IN: R", "grid_lbl": "TIK AANTAL MENSE WAT SAAM BETAAL:", "note_lbl": "BANKNOOT DEURGEGEE: R", "calc_btn": "BEREKEN KLEINGELD", "init_status": "WAG VIR KONTANTINSET", "short_status": "TE KORT: REISGELD KORT!", "reset_btn": "HERSTEL", "undo_btn": "MAAK OP", "person": "Mense"},
    "Setswana": {"total_lbl": "TLHOTLHWA YA MADI PHATLALATSENG", "fare_lbl": "KENYA MADI FA LABONE MOTHO A LE 1: R", "grid_lbl": "COFA PALO YA BATHO BA BA LEFANG:", "note_lbl": "I-NOTE E ROMETSWEGO: R", "calc_btn": "BALA CHENTJHI", "init_status": "TSELA E YA PELE", "short_status": "MADI A A TLHAELLA!", "reset_btn": "TLOSA", "undo_btn": "BOEA", "person": "Batho"},
    "Xitsonga": {"total_lbl": "NTSENGO HINKWAWO WA MUKHAU", "fare_lbl": "NGHENISA MUKHAU WA MUNHU UN'WE: R", "grid_lbl": "TSHIKETA VUNYINGI BYA VAHAKERI:", "note_lbl": "XIPHEPHETA XA MALI: R", "calc_btn": "KONTOLA CHENTJHI", "init_status": "KUMBA MALI YA MUKHAU", "short_status": "MALI YA TLHAELLA!", "reset_btn": "BASISA", "undo_btn": "BUYISA", "person": "Vanhu"},
    "siSwati": {"total_lbl": "INHLANGANISO YETIMALI", "fare_lbl": "FAKA INTSENGO YEMUNTFU ENYE: R", "grid_lbl": "COFA LABABHADALA KANYE NEBANYE:", "note_lbl": "I-NOTE LELSEDLULISWE PHAMBILI: R", "calc_btn": "BALA USHINTSHO", "init_status": "INDLELA LEYA PHAMBILI", "short_status": "IMALANA IYASHOTA!", "reset_btn": "SUSA", "undo_btn": "BUYISA", "person": "Bantfu"},
    "Tshivenda": {"total_lbl": "MUTALADZI WA MADI KHATHI", "fare_lbl": "DZHENISANI MUTENGO WA MUTHU A LE 1: R", "grid_lbl": "NYIKADZANI PALO YA VHA HAKERAHO:", "note_lbl": "TSIENTSI E FHATSHILAKHO: R", "calc_btn": "VALA CHENTSHI", "init_status": "PHANDA HA MADI KHATHI", "short_status": "MADI A A THAHELA!", "reset_btn": "FHEDZISANI", "undo_btn": "VHUSELA", "person": "Vhathu"},
    "isiNdebele": {"total_lbl": "IMALI ENGEZIWEKO LELIZWE", "fare_lbl": "FAKA INTWALA YOMUNTU OY'1: R", "grid_lbl": "COFA ABANTU ABABHADALAKO BESALANA:", "note_lbl": "I-NOTE EDLULISWE PHAMBILI: R", "calc_btn": "BALA USHINTSHO", "init_status": "INDLELA EYA PHAMBILI", "short_status": "IMALI IYASHOTA PHAMBILI!", "reset_btn": "SUSA", "undo_btn": "BUYISELA", "person": "Abantu"},
    "Sepedi": {"total_lbl": "CHELETE E KOPANTSENG PHASHA", "fare_lbl": "KENYA TEFO YA MOTHO A LE 1: R", "grid_lbl": "TLICHA PALO YA BATHO BA LEFANG:", "note_lbl": "I-NOTE E SEPETSITSOENG: R", "calc_btn": "BALA CHENTJHI", "init_status": "TSELA E YA PELE", "short_status": "CHELETE EA TLHAELLA!", "reset_btn": "TLOSA", "undo_btn": "BUSA", "person": "Batho"}
}


def color_from_hex(value):
    value = value.lstrip("#")
    return [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)] + [1]


class ColorPanel(BoxLayout):
    panel_color = ListProperty([0, 0, 0, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self._color_instruction = Color(*self.panel_color)
            self._rectangle = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_rectangle, size=self._update_rectangle)
        self.bind(panel_color=self._update_color)

    def _update_rectangle(self, *_):
        self._rectangle.pos = self.pos
        self._rectangle.size = self.size

    def _update_color(self, *_):
        self._color_instruction.rgba = self.panel_color


class TaxiCalcZA(App):
    def _fit_label(self, instance, size):
        instance.text_size = size

    def make_label(self, text, height=dp(24), font_size=sp(10), bold=False):
        lbl = Label(text=text, font_size=font_size, bold=bold, halign="left", valign="middle", size_hint_y=None, height=height)
        lbl.bind(size=self._fit_label)
        return lbl

    def make_input(self, hint):
        return TextInput(hint_text=hint, multiline=False, input_filter="float", font_size=sp(16), size_hint_y=None, height=dp(42), padding=[dp(10), dp(10)])

    def build(self):
        self.title = "Amethyst Matrix 23"
        self.total = 0.0
        self.entry_log = []
        self.theme_index = 0
        self.status_kind = "awaiting"

        self.root_layout = BoxLayout(orientation="vertical", spacing=dp(4))

        self.theme_button = Button(size_hint_y=None, height=dp(44), font_size=sp(12), bold=True, background_normal="", background_down="", on_release=self.cycle_theme)
        self.root_layout.add_widget(self.theme_button)

        scroll = ScrollView()
        self.content = BoxLayout(orientation="vertical", size_hint_y=None, padding=[dp(16), dp(4), dp(16), dp(10)], spacing=dp(5))
        self.content.bind(minimum_height=self.content.setter("height"))
        scroll.add_widget(self.content)
        self.root_layout.add_widget(scroll)

        # Language selector
        language_row = BoxLayout(size_hint_y=None, height=dp(38), spacing=dp(5))
        self.language_label = self.make_label("CHOOSE LANGUAGE:", height=dp(38), font_size=sp(9), bold=True)
        self.language_label.size_hint_x = 0.55
        self.language_spinner = Spinner(text="English", values=list(LANGUAGES.keys()), size_hint_x=0.45, font_size=sp(11), background_normal="")
        self.language_spinner.bind(text=self.switch_language)
        language_row.add_widget(self.language_label)
        language_row.add_widget(self.language_spinner)
        self.content.add_widget(language_row)

        # Total card
        self.dashboard = ColorPanel(orientation="vertical", size_hint_y=None, height=dp(84), padding=[dp(10), dp(4)])
        self.total_label = self.make_label("TOTAL FARE COST", height=dp(20), font_size=sp(9), bold=True)
        self.bill_label = self.make_label("R 0.00", height=dp(48), font_size=sp(26), bold=True)
        self.dashboard.add_widget(self.total_label)
        self.dashboard.add_widget(self.bill_label)
        self.content.add_widget(self.dashboard)

        # Fare input box
        fare_box = BoxLayout(orientation="vertical", size_hint_y=None, height=dp(64), spacing=dp(2))
        self.fare_label = self.make_label("ENTER FARE FOR 1 PERSON: R", height=dp(20), bold=True)
        self.fare_input = self.make_input("0.00")
        fare_box.add_widget(self.fare_label)
        fare_box.add_widget(self.fare_input)
        self.content.add_widget(fare_box)

        # Quantity buttons grid
        self.grid_label = self.make_label("TAP QUANTITY PAYING TOGETHER:", height=dp(22), bold=True)
        self.content.add_widget(self.grid_label)

        grid = GridLayout(cols=2, spacing=dp(4), size_hint_y=None, height=dp(120))
        self.quantity_buttons = []
        for quantity in range(1, 7):
            button = Button(text=f"{quantity} People", font_size=sp(11), bold=True, background_normal="", background_down="")
            button.bind(on_release=lambda _btn, count=quantity: self.add_fare(count))
            self.quantity_buttons.append(button)
            grid.add_widget(button)
        self.content.add_widget(grid)

        # Calculation log
        self.console = TextInput(text="", readonly=True, multiline=True, size_hint_y=None, height=dp(56), font_size=sp(10), padding=[dp(6), dp(4)])
        self.content.add_widget(self.console)

        # Tendered amount
        self.settle_card = ColorPanel(orientation="vertical", size_hint_y=None, height=dp(68), padding=[dp(10), dp(4)])
        self.note_label = self.make_label("NOTE PASSED FORWARD: R", height=dp(20), bold=True)
        self.tendered_input = self.make_input("0.00")
        self.settle_card.add_widget(self.note_label)
        self.settle_card.add_widget(self.tendered_input)
        self.content.add_widget(self.settle_card)

        # Notes row
        notes_row = BoxLayout(size_hint_y=None, height=dp(36), spacing=dp(3))
        self.note_buttons = []
        for label, val in [("R10", 10), ("R20", 20), ("R50", 50), ("R100", 100), ("R200", 200)]:
            btn = Button(text=label, font_size=sp(10), bold=True, background_normal="", background_down="")
            btn.bind(on_release=lambda _btn, v=val: self.quick_cash(v))
            self.note_buttons.append(btn)
            notes_row.add_widget(btn)
        self.content.add_widget(notes_row)

        # Coins row
        coins_row = BoxLayout(size_hint_y=None, height=dp(36), spacing=dp(3))
        self.coin_buttons = []
        for label, val in [("R1 Coin", 1), ("R2 Coin", 2), ("R5 Coin", 5)]:
            btn = Button(text=label, font_size=sp(10), bold=True, background_normal="", background_down="")
            btn.bind(on_release=lambda _btn, v=val: self.quick_cash(v))
            self.coin_buttons.append(btn)
            coins_row.add_widget(btn)
        self.content.add_widget(coins_row)

        # Calculate button
        self.calc_button = Button(text="CALCULATE CHANGE", size_hint_y=None, height=dp(42), font_size=sp(11), bold=True, background_normal="", background_down="", on_release=self.calculate_change)
        self.content.add_widget(self.calc_button)

        # Status & Delta output
        self.status_label = Label(text="AWAITING CASH INPUT", font_size=sp(10), bold=True, size_hint_y=None, height=dp(20))
        self.delta_label = Label(text="R 0.00", font_size=sp(22), bold=True, size_hint_y=None, height=dp(30))
        self.content.add_widget(self.status_label)
        self.content.add_widget(self.delta_label)

        # Bottom Action Bar (Reset + Undo)
        bottom_bar = BoxLayout(size_hint_y=None, height=dp(40), spacing=dp(4))
        self.reset_button = Button(text="RESET", font_size=sp(10), bold=True, background_normal="", background_down="", on_release=self.reset_app)
        self.undo_button = Button(text="UNDO LAST", font_size=sp(10), bold=True, background_normal="", background_down="", on_release=self.undo_last)
        bottom_bar.add_widget(self.reset_button)
        bottom_bar.add_widget(self.undo_button)
        self.root_layout.add_widget(bottom_bar)

        self.apply_theme()
        return self.root_layout

    def cycle_theme(self, *_):
        self.theme_index = (self.theme_index + 1) % len(THEMES)
        self.apply_theme()

    def apply_theme(self):
        t = THEMES[self.theme_index]
        bg = color_from_hex(t["bg"])
        card = color_from_hex(t["card"])
        inp = color_from_hex(t["input"])
        accent = color_from_hex(t["accent"])
        text = color_from_hex(t["text"])
        accent_text = color_from_hex(t["accent_text"])
        muted = color_from_hex(t["muted"])

        Window.clearcolor = bg
        self.theme_button.text = t["name"].upper()
        self.theme_button.background_color = accent
        self.theme_button.color = accent_text

        self.language_label.color = muted
        self.language_spinner.background_color = card
        self.language_spinner.color = text

        self.dashboard.panel_color = card
        self.total_label.color = muted
        self.bill_label.color = text

        self.fare_label.color = muted
        self.fare_input.background_color = inp
        self.fare_input.foreground_color = text

        self.grid_label.color = muted
        for btn in self.quantity_buttons:
            btn.background_color = card
            btn.color = accent

        self.console.background_color = inp
        self.console.foreground_color = accent

        self.settle_card.panel_color = card
        self.note_label.color = muted
        self.tendered_input.background_color = inp
        self.tendered_input.foreground_color = accent

        for btn in self.note_buttons:
            btn.background_color = accent
            btn.color = accent_text
        for btn in self.coin_buttons:
            btn.background_color = card
            btn.color = accent

        self.calc_button.background_color = inp
        self.calc_button.color = text

        if self.status_kind == "short":
            self.status_label.color = color_from_hex("#D97272")
            self.delta_label.color = color_from_hex("#D97272")
        elif self.status_kind == "settled":
            self.status_label.color = accent
            self.delta_label.color = accent
        else:
            self.status_label.color = muted
            self.delta_label.color = accent

        self.reset_button.background_color = card
        self.reset_button.color = text
        self.undo_button.background_color = inp
        self.undo_button.color = text

    def switch_language(self, _spinner, lang):
        s = LANGUAGES[lang]
        self.total_label.text = s["total_lbl"]
        self.fare_label.text = s["fare_lbl"]
        self.grid_label.text = s["grid_lbl"]
        self.note_label.text = s["note_lbl"]
        self.calc_button.text = s["calc_btn"]
        self.reset_button.text = s["reset_btn"]
        self.undo_button.text = s["undo_btn"]

        person_word = s["person"]
        for i, btn in enumerate(self.quantity_buttons, start=1):
            btn.text = f"{i} {person_word}"

        if self.status_kind == "awaiting":
            self.status_label.text = s["init_status"]
        elif self.status_kind == "short":
            self.status_label.text = s["short_status"]

    def add_fare(self, count):
        try:
            if not self.fare_input.text.strip():
                return
            fare = float(self.fare_input.text)
            subtotal = fare * count
            self.total += subtotal
            
            log_entry = {"amount": subtotal, "text": f"Added: {count} x R{fare:.2f} -> R{subtotal:.2f}\n"}
            self.entry_log.append(log_entry)
            
            self.console.text += log_entry["text"]
            self.bill_label.text = f"R {self.total:.2f}"
        except ValueError:
            pass

    def undo_last(self, *_):
        if self.entry_log:
            last = self.entry_log.pop()
            self.total -= last["amount"]
            if self.total < 0:
                self.total = 0.0
            self.bill_label.text = f"R {self.total:.2f}"
            self.console.text = "".join([item["text"] for item in self.entry_log])

    def quick_cash(self, amount):
        """Accumulates notes and coins together (e.g., R200 + R5 = R205)."""
        try:
            current_val = float(self.tendered_input.text) if self.tendered_input.text.strip() else 0.0
        except ValueError:
            current_val = 0.0
        
        new_total = current_val + amount
        
        if new_total.is_integer():
            self.tendered_input.text = str(int(new_total))
        else:
            self.tendered_input.text = str(new_total)
            
        self.calculate_change()

    def calculate_change(self, *_):
        lang = self.language_spinner.text
        s = LANGUAGES[lang]
        try:
            if self.total == 0 or not self.tendered_input.text.strip():
                return
            tendered = float(self.tendered_input.text)
            delta = tendered - self.total
            if delta < 0:
                self.status_kind = "short"
                self.status_label.text = s["short_status"]
                self.delta_label.text = f"- R {abs(delta):.2f}"
            else:
                self.status_kind = "settled"
                self.status_label.text = "U-SHINTSHO LUKHIPHILE!" if lang == "isiZulu" else "CHANGE SETTLED"
                self.delta_label.text = f"R {delta:.2f}"
            self.apply_theme()
        except ValueError:
            pass

    def reset_app(self, *_):
        lang = self.language_spinner.text
        self.total = 0.0
        self.entry_log.clear()
        self.fare_input.text = ""
        self.tendered_input.text = ""
        self.bill_label.text = "R 0.00"
        self.console.text = ""
        self.status_kind = "awaiting"
        self.status_label.text = LANGUAGES[lang]["init_status"]
        self.delta_label.text = "R 0.00"
        self.apply_theme()


if __name__ == "__main__":
    TaxiCalcZA().run()
