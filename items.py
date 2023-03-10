# Weapons types
WEAPON_GUN = 0
WEAPON_HAMMER = 1
WEAPON_GRENADE = 2
WEAPON_SHOTGUN = 3
WEAPON_LASER = 4
WEAPON_NINJA = 5
# Pickups types
PICKUP_ARMOR = 6
PICKUP_HEART = 7


class LaserLine:
	def __init__(self, x1: int, y1: int, x2: int, y2: int):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2


class Projectile:
	def __init__(self, x: int, y: int, proj_type: int):
		self.x = x
		self.y = y
		self.type = proj_type


class Pickup:
	def __init__(self, x: int, y: int, pickup_type: int):
		self.x = x
		self.y = y
		self.type = pickup_type
