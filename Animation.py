from pygame import Surface
class PlayAnimation():
	def __init__(self, x, y, bg_color, animation, repeat = False):
		self.x = x
		self.y = y
		widths = []
		heights = []
		for frame in animation:
			widths.append(frame.get_width())
			heights.append(frame.get_height())
		self.max_width = max(widths)
		self.max_height = max(heights)
		self.width = 0
		self.height = 0
		self.repeat = repeat
		self.animation = animation
		self.anim_count = 0
		self.frame_length = 5
		self.bg_color = bg_color
	def draw(self, window):
		self.width += 15
		self.height += 15
		if self.width > self.max_width:
			self.width = self.max_width
		if self.height > self.max_height:
			self.height = self.max_height
		if self.anim_count // self.frame_length == len(self.animation):
			if self.repeat:
				self.anim_count = 0
			else:
				self.anim_count -= 1
		surface = Surface((self.width, self.height))
		surface.fill(self.bg_color)
		surface.blit(self.animation[self.anim_count // self.frame_length], (0, 0))
		window.blit(surface, (self.x - self.width // 2, self.y - self.height // 2))
		self.anim_count += 1