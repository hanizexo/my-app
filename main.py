import random
import string
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.uix.scrollview import ScrollView

def generate_password(length=16):
    """Generate a secure random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

class PasswordApp(App):
    def build(self):
        self.passwords = []  # store last 3 passwords

        # Main vertical layout with padding and spacing
        layout = BoxLayout(orientation='vertical', padding=30, spacing=25)

        # Title label
        self.label = Label(
            text="Tap the button to generate a password",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
        layout.add_widget(self.label)

        # Generate button styled bigger for touch
        btn = Button(
            text="🔑 Generate Password",
            font_size='22sp',
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 0.9, 1)  # nice blue
        )
        btn.bind(on_press=self.show_password)
        layout.add_widget(btn)

        # Scrollable history area for last 3 passwords
        scroll = ScrollView(size_hint=(1, 0.5))
        self.history_label = Label(
            text="Last 3 passwords:\nNone yet",
            font_size='18sp',
            halign='center',
            valign='top',
            size_hint_y=None
        )
        self.history_label.bind(texture_size=self._update_height)
        scroll.add_widget(self.history_label)
        layout.add_widget(scroll)

        return layout

    def _update_height(self, instance, value):
        instance.height = value[1]

    def show_password(self, instance):
        password = generate_password()
        self.label.text = f"✅ Copied to clipboard!\n{password}"

        # copy to clipboard
        Clipboard.copy(password)

        # keep only last 3
        self.passwords.append(password)
        if len(self.passwords) > 3:
            self.passwords.pop(0)

        # update history display
        history_text = "Last 3 passwords:\n" + "\n".join(self.passwords)
        self.history_label.text = history_text

if __name__ == "__main__":
    PasswordApp().run()
