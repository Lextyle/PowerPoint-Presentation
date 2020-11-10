from pygame import Surface, KEYDOWN, K_LEFT, K_RIGHT
from pygame.transform import scale as scale_image
class Slide():
	def __init__(self, x, y, slides_num, slide_num, width, height, color, animations, labels):
		self.x = x
		self.y = y
		self.canvas = Surface((1980, 1080))
		self.width = width
		self.height = height
		self.animations = animations
		self.left = False
		self.right = False
		self.slide_num = slide_num
		self.slides_num = slides_num
		self.color = color
		self.labels = labels
	def update(self, event, slides):
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				if not(self.slide_num == 1 and self.x == 0):
					self.right = True
					self.left = False
				else:
					self.right = False
					return "undo"
			if event.key == K_RIGHT:
				if not(self.slide_num == self.slides_num and self.x == 0):
					self.left = True
					self.right = False
				else:
					for slide in slides:
						slide.left = False
	def move(self, slides):
		if self.left:
			self.x -= self.width
			for animation in self.animations:
				animation.width = -15
				animation.height = -15
			if self.x == 0:
				for slide in slides:
					slide.left = False
				for slide in slides[self.slide_num: self.slides_num]:
					slide.x -= self.width
		if self.right:
			self.x += self.width
			for animation in self.animations:
				animation.width = -15
				animation.height = -15
			if self.x == 0:
				for slide in slides:
					slide.right = False
				for slide in slides[self.slide_num: self.slides_num]:
					slide.x += self.width
	def draw(self, window):
		self.canvas.fill(self.color)
		for animation in self.animations:
			animation.draw(self.canvas)
		for label in self.labels:
			label.draw(self.canvas)
		window.blit(scale_image(self.canvas, (self.width, self.height)), (self.x, self.y))