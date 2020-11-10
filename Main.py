import pygame
from pyautogui import size
from Animation import *
from Slide import *
from Label import *
from os import listdir
pygame.init()
window_width = size()[0]
window_height = size()[1]
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
font = pygame.font.Font("SFPixelate.ttf", 20)
big_font = pygame.font.Font("SFPixelate.ttf", 30)
animations = [
[PlayAnimation(1980 // 2, 1080 // 2, (255, 255, 255), [pygame.transform.scale(pygame.image.load("bg_image.png"), (1980, 1080))])],
[PlayAnimation(1980 // 2, 0, (0, 255, 255), [pygame.image.load("TrollHunters_image.png")]), PlayAnimation(0, 1080, (0, 255, 255), [pygame.image.load("jim_image.png")]), PlayAnimation(1980, 1080, (0, 255, 255), [pygame.transform.scale(pygame.image.load("blinky_and_argh_image.png"), (pygame.image.load("blinky_and_argh_image.png").get_width() * 2, pygame.image.load("blinky_and_argh_image.png").get_height() * 2))])],
[PlayAnimation(1980 // 2, 1080 // 2, (255, 255, 255), [pygame.transform.scale(pygame.image.load("bg_image_2.png"), (1980, 1080))], True)],
[PlayAnimation(1980 // 2, 0, (0, 255, 255), [pygame.image.load("3_below_image.png")])],
[PlayAnimation(1980 // 2, 1080 // 2, (255, 255, 255), [pygame.transform.scale(pygame.image.load("bg_image_3.png"), (1980, 1080))])],
[PlayAnimation(1980 // 2, 0, (0, 255, 255), [pygame.image.load("wizards_image.png")])]
]
animations[1][0].y += animations[1][0].max_height // 2
animations[1][1].y -= animations[1][1].max_height // 2 + 20
animations[1][1].x += animations[1][1].max_width // 2
animations[1][2].y -= animations[1][2].max_height // 2 + 20
animations[1][2].x -= animations[1][2].max_width // 2 + 20
animations[3][0].y += animations[3][0].max_height // 2
animations[5][0].y += animations[5][0].max_height // 2
labels = [
[Label(1980 // 2, 0, 500, "History of Troll Hunters", big_font, (0, 0, 0), "yes")],
[Label(animations[1][0].x, animations[1][0].y + animations[1][0].max_height // 2 + 10, animations[1][0].max_width * 2, "Jim became a trollhunter when he was just a teenage boy. Jim suddenly found an amulet that gave him trollhunter powers. With his friends on his side he came on a journey to defeat the evil troll GUMGUM!!!. In his arsenal he had his sword his shield, boomerang and of course hi armor		These are the word that make him become the trollhunter		For the honor of Merlin the daylight is mine to comand", big_font, (0, 0, 0), "yes"), Label(animations[1][1].x, animations[1][1].y - animations[1][1].max_height // 2 - 20, animations[1][1].max_width, "Claire, Jim and Toby", big_font, (0, 0, 0), "yes"), Label(animations[1][2].x, 1980, 500, "Blinky and Aaargh", big_font, (0, 0, 0), "yes")],
[Label(1980 // 2, 0, 500, "History Of 3 Below", big_font, (0, 255, 255), "yes")],
[Label(animations[3][0].x, animations[3][0].y + animations[3][0].max_height // 2 + 5, animations[3][0].max_width, "Ajay and Krel were the children of  king and queen of planet Akaridion 5 one day an evil general Val morando wich killed  king and queen Aja and Krel  flee from the planet with their bodyguard Varvatos who is obsessed whith glorious death they lend on planet earth and disguise as foregne students and by luck they end in the same school as trollhunters", big_font, (0, 0, 0), "yes")],
[],
[Label(animations[5][0].x, animations[5][0].max_height, animations[5][0].max_width, "It's a tale of a young boy named douxie he is the apprentice of legendary mage Merlin.the green night and evil sister of a secondary character are attacking Jim and hit him so hard he will die whitout a cure so they go back in time to help Jim with the cure             they find out the truth about green knight and Morgana so they help jim and win this battle of life and death", big_font, (0, 0, 0), "yes")]
]
labels[1][0].y += labels[1][0].height // 2
labels[0][0].y += labels[0][0].height // 2 + 5
labels[1][2].y -= animations[1][2].max_height + 20 + 40
labels[1][2].y += labels[1][2].height // 2 + 5
labels[2][0].y += labels[2][0].height // 2 + 5
labels[3][0].y += labels[3][0].height // 2 + 5
labels[5][0].y += labels[5][0].height // 2 + 5
colors = [[0, 100, 100], [0, 150, 150], [0, 100, 100], [0, 150, 150], [0, 100, 100], [0, 150, 150]]
slides_num = len(labels)
slides = []
for num in range(slides_num):
	slides.append(Slide(num * window_width, 0, slides_num, num + 1, window_width, window_height, colors[num], animations[num], labels[num]))
while True:
	window.fill((255, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		for slide in slides:
			boolian = slide.update(event, slides)
			if boolian == "undo":
				break
	for slide in slides:
		slide.move(slides)
		if slide.x in range(1 - window_width, window_width - 1):
			slide.draw(window)
	pygame.display.flip()