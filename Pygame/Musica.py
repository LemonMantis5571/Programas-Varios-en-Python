from pygame import mixer
  
# inicializa el mezclador
mixer.init()
  
# Carga la musica
mixer.music.load("Pygame/ly.ogg")
  
# Settea el volumen
mixer.music.set_volume(0.7)
  
# Comienza a reproducir la musica
mixer.music.play()
  
# Hace un loop infinito
while True:
      
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
      
    if query == 'p':
  
        # pausa la musica
        mixer.music.pause()     
    elif query == 'r':
  
        # reanuda la musica
        mixer.music.unpause()
    elif query == 'e':
  
        # para el mezclador y sale del ciclo
        mixer.music.stop()
        break