import pygame
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QInputDialog

pygame.init()

setting = {
    "BG": (300, 330),
    "CROSSES": (74, 74),
    "NOUGHT": (74, 74)
}
cords = {
    1: [(13, 13), False],
    2: [(110, 13), False],
    3: [(210, 13), False],
    4: [(13, 110), False],
    5: [(110, 110), False],
    6: [(210, 110), False],
    7: [(13, 211), False],
    8: [(110, 211), False],
    9: [(210, 211), False]
}

moves = list()

abs_path = os.path.abspath(__file__ + "/..")

bg_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bg.png")), (setting["BG"][0], 300))
cross_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "cross.png")), setting["CROSSES"])
nought_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "nought.png")), setting["NOUGHT"])