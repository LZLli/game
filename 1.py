import play
play.screen.width=1000
play.screen.height=600
play.set_backdrop("light green")
area_list=[]
y=200
for n in range(9):
    if n%3==0:
        x=-100
        y-=100
    area_list.append(
        play.new_image(image='imgs/agxtn-t816a.png',x=x,y=y,size=200))
    x+=100
plants_img={
    "tomato":["tomatoes1","tomatoes2","tomatoes3","tomatoes4"],
    "carrot":["carrots1","carrots2","carrots3","carrots4"],
    "eggplant":["eggplants1","eggplants2","eggplants3","eggplants4","eggplants5"]
}
plants_icon_list=[]
y=120
for i in range(3):
    plants_icon_list.append(
        play.new_image(image="imgs/%s.png"%list(plants_img.keys())[i],
        x=410,y=y,size=80
    ))
    y-=80
@play.when_sprite_clicked(plants_icon_list[0])
async def do (sprite):
    pass
@play.when_sprite_clicked(area_list[0])
async def do (sprite):
    pass
play.start_program()