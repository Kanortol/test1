from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.button import Button


KV="""
MyBL:

	orientation: "vertical"
	size_hint: (0.95, 0.95)
	pos_hint: {"center_x":0.5, "center_y":0.5}

	Label:
		font_size: '55sp'
		text: root.data_label_text
		multiline: True

	Button:
		text: "Button1Text"
		bold: True
		background_color: "#9933ff"
		size_hint: (1, 0.5)
		on_press: root.callback1()

	Button:
		text: "Button2Text"
		bold: True
		background_color: "#336699"
		size_hint: (1, 0.5)
		on_press: root.callback2()

	Button:
		text: "Button3Text"
		bold: True
		background_color: "#99ffcc"
		size_hint: (1, 0.5)
		on_press: root.callback3()

"""

class MyBL(BoxLayout):
	
	data_label_text = StringProperty("MyStringProperty in data_label")

	def callback1(self):
		self.data_label_text = "Button1 pressed"

	def callback2(self):
		self.data_label_text = "Button2 pressed"

	def callback3(self):
		self.data_label_text = "Button3 pressed"

class MyApp(App):

	running = True

	def build(self):
		return Builder.load_string(KV)

	def on_stop(self):
		self.running = False

MyApp().run()