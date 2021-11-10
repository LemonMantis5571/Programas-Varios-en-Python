
from typing import Coroutine
from easy_pil import Editor, Canvas, Font,font
                    #1200x753
background = Editor("DiscordBot/assets/bg2.jpg")
profile = Editor("DiscordBot/assets/pf.png").resize((100,100)).circle_image()
poppins = Font().poppins(size=20)
poppins_small = Font().poppins(size=10)

square = Canvas((500,500), "#0869A6")
square = Editor(square)
square.rotate(30, expand=True)


background.paste(square.image,(600, -250))
background.paste(profile.image,(30, 30))

background.rectangle((30, 220), width=650, outline="black", height=40,fill="white", radius=20)
background.bar((30, 220), max_width=650, percentage=30 ,height=40,fill="#0A5DA6", radius=20)
background.text((200, 50), "LemonMantis", font=poppins, color="white")
background.rectangle((200, 100), width=350, height=3,fill="#011126")
background.text((200, 130), "Level: 113 XP : 10k / 20k", font=poppins_small, color="white")


background.show()