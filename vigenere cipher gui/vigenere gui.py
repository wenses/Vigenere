import vigenere_cipher

from flet import *

def main(page:Page):
	page.title="VIGIENER CIPHER GUI"
	page.theme_mode="Dark"

	iv=TextField(hint_text="Enter input text here: ",autofocus=True)
	cy=TextField(hint_text="Enter cycles of encryption here:",autofocus=True,value="0")
	ke=TextField(hint_text="Enter key to encrypt with:")
	ov=TextField(hint_text="Output text")

	def cipher_action(e):
		ov.value=vigenere_cipher.cycle_cipher(iv.value,ke.value,int(cy.value))
		page.update()
		
	def decipher_action(e):
		ov.value=vigenere_cipher.cycle_decipher(iv.value,ke.value,int(cy.value))
		page.update()

	cb=ElevatedButton("Encode",on_click=cipher_action)

	db=ElevatedButton("Deconde",on_click=decipher_action)

	
	r1=Row(
		controls=[Text("Input text:"),iv])

	r2=Row(
		controls=[Text("Enter cycles :"),cy])

	r3=Row(
		controls=[Text("Enter key:"),ke])

	r4=Row(
		controls=[Text("Output text:"),ov])


	mc=Column(controls=[r1,r2,r3,r4,cb,db])

	mrow=Row(
		alignment='center',
		controls=[mc])

	page.add(mrow)

app(target=main)