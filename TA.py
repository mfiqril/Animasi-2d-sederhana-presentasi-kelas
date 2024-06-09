from ursina import *

app = Ursina()

tembok1 = Entity(model="quad", position=(-5.9, 0, 0), scale=(3, 8.5, 2), rotation=(0, -45, 0), texture="tembok00")
tembok2 = Entity(model="quad", position=(5.9, 0, 0), scale=(3, 8.5, 2), rotation=(0, 45, 0), texture="tembok00")
tembok3 = Entity(model="quad", position=(0, 0, 1), scale=(10, 8.5, 2), rotation=(0, 0, 0), texture="tembok00")

atap = Entity(model="quad", position=(0, 2, 0), scale=(15, 15, 2), rotation=(-80, 0, 0), color=color.white)
lantai = Entity(model="quad", position=(0, -4, 0), scale=(15, 5, 2), rotation=(80, 0, 0), texture="lantai")
lampu = Entity(model="quad", position=(0, 1.8, -6), scale=(2, 1, 2), retation=(0, 0, 0), texture="lampu")
pintu = Entity(model="quad", position=(-5.7, -2.7, 0), scale=(2, 2.5, 2), rotation=(0, -70, 0), texture="pintu")
ac = Entity(model="quad", position=(5.9, 1.5, 0), scale=(2, 2.8, 0), rotation=(0, 45, 0), texture="ac")

whitebor = Entity(model="quad", position=(0, -1, 1), scale=(5, 3, 2), rotation=(0, 0, 0), color=color.white)
presentation = Animation("presentation", position=(0, -1, .8),fps=1, scale=(4, 2, 2), rotation=(0, 0, 0), autoplay=True, loop=True)

meja = Entity(model="meja.glb", position=(3.8, -4.2, .1), scale=(0.05, 0.03, 0.01), rotation=(0, 180, 0), collider=None)
kursi = Entity(model="quad", position=(3.9, -3.2, .6), scale=(1.8, 2, 0), texture="chair")

dosen = Entity(model="quad", position=(3.8, -2.8, .5), scale=(1, 1.7, 2), texture="mark2")

woman = Animation("woman", position=(0, -3, .5), fps=5, scale=(1.2, 2, 2), autoplay=True, loop=True)
mahasiswa2 = Entity(model="quad", position=(-3, -3, .5), scale=(2, 2.7, 2), texture="mark3")
mahasiswa3 = Entity(model="quad", position=(-3.8, -3, .5), scale=(1.5, 2.6, 2), texture="mark4")

mahasiswa1 = Entity(model="quad", position=(-1, -4, -4), scale=(1, 1.7, 2), texture="mark17")
mahasiswa2 = Entity(model="quad", position=(-2, -4, -4), scale=(1, 1.7, 2), texture="mark17")
mahasiswa3 = Entity(model="quad", position=(-3, -4, -4), scale=(1, 1.7, 2), texture="mark17")
mahasiswa4 = Entity(model="quad", position=(-4, -4, -4), scale=(1, 1.7, 2), texture="mark17")
mahasiswa5 = Entity(model="quad", position=(-5, -4, -4), scale=(1, 1.7, 2), texture="mark17")
mahasiswa6 = Entity(model="quad", position=(1, -4, -4), scale=(1, 1.7, 2), texture="mark17")
mahasiswa7 = Entity(model="quad", position=(2, -4, -4), scale=(1, 1.7, 2), texture="mark17")
mahasiswa8 = Entity(model="quad", position=(3, -4, -4), scale=(1, 1.7, 2), texture="mark17")
mahasiswa9 = Entity(model="quad", position=(4, -4, -4), scale=(1, 1.7, 2), texture="mark17")
mahasiswa10 = Entity(model="quad", position=(5, -4, -4), scale=(1, 1.7, 2), texture="mark17")

mahasiswa1 = Entity(model="quad", position=(-1, -4, -1), scale=(1, 1.7, 2), texture="mark17")
mahasiswa2 = Entity(model="quad", position=(-2, -4, -1), scale=(1, 1.7, 2), texture="mark17")
mahasiswa3 = Entity(model="quad", position=(-3, -4, -1), scale=(1, 1.7, 2), texture="mark17")
mahasiswa4 = Entity(model="quad", position=(-4, -4, -1), scale=(1, 1.7, 2), texture="mark17")
mahasiswa5 = Entity(model="quad", position=(-5, -4, -1), scale=(1, 1.7, 2), texture="mark17")
mahasiswa6 = Entity(model="quad", position=(1, -4, -1), scale=(1, 1.7, 2), texture="mark17")
mahasiswa7 = Entity(model="quad", position=(2, -4, -1), scale=(1, 1.7, 2), texture="mark17")
mahasiswa8 = Entity(model="quad", position=(3, -4, -1), scale=(1, 1.7, 2), texture="mark17")
mahasiswa9 = Entity(model="quad", position=(4, -4, -1), scale=(1, 1.7, 2), texture="mark17")
mahasiswa10 = Entity(model="quad", position=(5, -4, -1), scale=(1, 1.7, 2), texture="mark17")

player = Entity(model="quad", position=(0, -3, .5), scale=(2, 2.8, 2), texture="player_00")

def update():
    if held_keys['a']:
        player.x -= time.dt * 1
        player.texture = "player_01"
    elif held_keys['d']:
        player.x += time.dt * 1
        player.texture = "player_00"
    else:
        player.texture = "player_00"
        
    if player.x < -3:
        player.x = -3
    elif player.x > 3:
        player.x = 3
     
app.run()