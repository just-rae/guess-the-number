import pygame
from sys import exit
from random import randint, choice
import os
pygame.mixer.init() 

BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('img/player/player_walk_1.png').convert_alpha()
		player_walk_2 = pygame.image.load('img/player/player_walk_2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('img/player/jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
		self.jump_sound.set_volume(0.5)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_z] and self.rect.bottom >= 300:
			self.gravity = -20
			self.jump_sound.play()

	#gravity when player jumps
	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):
		if self.rect.bottom < 300: 
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'hole':
			hole_1 = pygame.image.load('img/hole/hole1.png').convert_alpha()
			hole_2 = pygame.image.load('img/hole/hole2.png').convert_alpha()
			self.frames = [hole_1,hole_2]
			y_pos = 210
		else:
			ufo_1 = pygame.image.load('img/ufo/ufo1.png').convert_alpha()
			ufo_2 = pygame.image.load('img/ufo/ufo2.png').convert_alpha()
			self.frames = [ufo_1,ufo_2]
			y_pos  = 300

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()

#displays player's score
def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time

def obstacle_movement(obstacle_list):
	if obstacle_list:
		for obstacle_rect in obstacle_list:
			obstacle_rect.x -= 5

			if obstacle_rect.bottom == 300: screen.blit(ufo_surf,obstacle_rect)
			else: screen.blit(hole_surf,obstacle_rect)

		obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

		return obstacle_list
	else: return []

#Transitions before starting the game
class ScreenFade():
	def __init__(self ,color ,speed):
		self.color = color
		self.speed = speed
		self.fade_counter = 0

		
	def fade(self):
		fade_complete = False
		self.fade_counter += self.speed 
		pygame.draw.rect(screen , self.color,(0 -self.fade_counter ,0, 400, 400))
		pygame.draw.rect(screen , self.color,(400+ self.fade_counter ,0, 800, 400))
		pygame.draw.rect(screen , self.color,(0, 0 - self.fade_counter, 800, 200))
		pygame.draw.rect(screen , self.color,(0, 200+self.fade_counter, 800, 400))
		if self.fade_counter >= 400 :
			fade_complete = True 
		return fade_complete

start_fade= True
#create screen fade 
start_game_fade = ScreenFade(BLACK, 4)

#Explosion
class Explosion(pygame.sprite.Sprite):
	def __init__(self ,x ,y ,scale):
		pygame.sprite.Sprite.__init__(self)
		self.images=[]
		for num in range(1,4):
			img = pygame.image.load(f'img/explosion/exp{num}.png').convert_alpha()
			img = pygame.transform.scale(img, (int(img.get_width()* scale) ,int(img.get_height() * scale )))
			self.images.append(img)
			self.index = 0
			self.image=self.images[self.index]
			self.rect = self.image.get_rect()
			self.rect.center = (x,y)
			self.counter = 0

	def update(self):
		EXPLOSION_SPEED = 4
		#update explosion animation
		self.counter += 1
		if self.counter >= EXPLOSION_SPEED:
			self.counter = 0
			self.index += 1
			#if the animation is complete ,delete the explosion
			if self.index >= len(self.images):
				self.kill()
			else:
				self.image = self.images[self.index]

def collisions(player,obstacles):
	if obstacles:
		for obstacle_rect in obstacles:
			if player.colliderect(obstacle_rect): return False
	return True

health1 = 5

explosion_sound = pygame.mixer.Sound(os.path.join('audio','explosion_sound.wav'))


#handles collisions
def collision_sprite():
	global health1
	if health1 <= 0:
		health1=5
		return False
	elif pygame.sprite.spritecollide(player.sprite,obstacle_group,True):
		health1 = health1-1
		obstacle_group.empty()
		#explosion 
		explosion = Explosion (130, 200 , 1.5)
		explosion_group.add(explosion)
		explosion_sound.play()
		return True
	else:
		return True

#displays player's health
def display_health():
	global health1
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,True): health1 = health1-1 
	health_surf = test_font.render(f'health: {health1}',False,(64,64,64))
	health_rect = health_surf.get_rect(center = (70,50))
	screen.blit(health_surf,health_rect)


def player_animation():
	global player_surf, player_index

	if player_rect.bottom < 300:
		player_surf = player_jump
	else:
		player_index += 0.1
		if player_index >= len(player_walk):player_index = 0
		player_surf = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.mp3')
bg_music.play(loops = -1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

explosion_group = pygame.sprite.Group()

sky_surface = pygame.image.load('img/Sky.png').convert()
ground_surface = pygame.image.load('img/ground.png').convert()

# UFO 
ufo_frame_1 = pygame.image.load('img/ufo/ufo1.png').convert_alpha()
ufo_frame_2 = pygame.image.load('img/ufo/ufo2.png').convert_alpha()
ufo_frames = [ufo_frame_1, ufo_frame_2]
ufo_frame_index = 0
ufo_surf = ufo_frames[ufo_frame_index]

# Hole
hole_frame1 = pygame.image.load('img/hole/hole1.png').convert_alpha()
hole_frame2 = pygame.image.load('img/hole/hole2.png').convert_alpha()
hole_frames = [hole_frame1, hole_frame2]
hole_frame_index = 0
hole_surf = hole_frames[hole_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('img/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('img/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('img/player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('img/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Space Jumper',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

ufo_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(ufo_animation_timer,500)

hole_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(hole_animation_timer,200)

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
		if game_active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
					player_gravity = -20
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_z and player_rect.bottom >= 300:
					player_gravity = -20
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				
				start_time = int(pygame.time.get_ticks() / 1000)

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['hole','ufo','ufo','ufo'])))

			if event.type == ufo_animation_timer:
				if ufo_frame_index == 0: ufo_frame_index = 1
				else: ufo_frame_index = 0
				ufo_surf = ufo_frames[ufo_frame_index] 

			if event.type == hole_animation_timer:
				if hole_frame_index == 0: hole_frame_index = 1
				else: hole_frame_index = 0
				hole_surf = hole_frames[hole_frame_index]


	if game_active:
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
		score = display_score()
		display_health()
				
				
		if start_fade == True:
			if start_game_fade.fade(): 
				start_fade = False
				start_game_fade.fade_counter = 0

		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()


		# collision 
		game_active = collision_sprite()
		explosion_group.draw(screen)
		explosion_group.update()
	
	else:
		screen.blit(sky_surface,(0,0))
		screen.blit(player_stand,player_stand_rect)
		obstacle_rect_list.clear()
		player_rect.midbottom = (80,300)
		player_gravity = 0
		start_fade= True

		score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,330))
		screen.blit(game_name,game_name_rect)
		if score == 0: screen.blit(game_message,game_message_rect)
		else: screen.blit(score_message,score_message_rect)

	pygame.display.update()
	clock.tick(60)