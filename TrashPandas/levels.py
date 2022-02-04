"""Moduł zawierający funkcje odpowiedzialne za tworzenie poziomów."""

from turtle import right
import pygame
from units import TrashPanda
from window import *

intro = True  #: Zmienna określająca czy wejście przeciwników ma nastąpić.


def create_lvl_1_2(panda_grid: list):
    """Tworzy siatkę przeciwników dla 1 i 2 poziomu.

    Args:
        panda_grid (list): Lista reprezentująca siatkę przeciwników.
    """
    for i in range(4):
        for j in range(5):
            panda = TrashPanda(
                MID + 120*(j-2) - RACCOON.get_width()/2, MARGIN + 100*i - 600)
            panda_grid.append(panda)


def anim_lvl_1(panda_grid: list, bullets: list):
    """Animuje rozpoczęcie 1 poziomu.

    Args:
        panda_grid (list): Lista reprezentująca siatkę przeciwników.
        bullets (list): Lista reprezentująca pociski znajdujące się na ekranie.
    """
    if any(bullets):
        return
    if not all(panda_grid) or panda_grid[0].rect.y >= MARGIN:
        return
    for panda in panda_grid:
        if panda != 0:
            panda.rect.y += PANDAS_ENTRY_SPEED


def anim_lvl_2(panda_grid: list, bullets: list):
    """Animuje rozpoczęcie 2 poziomu.

    Args:
        panda_grid (list): Lista reprezentująca siatkę przeciwników.
        bullets (list): Lista reprezentująca pociski znajdujące się na ekranie.
    """
    global ANIM_SPEED
    for p in range(len(panda_grid)):
        if panda_grid[p] == 0:
            continue
        if (p//5) % 2:
            panda_grid[p].rect.x += ANIM_SPEED
        else:
            panda_grid[p].rect.x -= ANIM_SPEED
        if abs(panda_grid[p].rect.x - panda_grid[p].start_x) > 50:
            ANIM_SPEED *= -1
    if not all(panda_grid) or panda_grid[0].rect.y == MARGIN:
        return
    if any(bullets):
        return
    for panda in panda_grid:
        if panda != 0:
            panda.rect.y += PANDAS_ENTRY_SPEED


def spawn_level(panda_grid: list, bullets: list, level: int):
    """Rysuje na ekranie siatkę przeciwników

    Args:
        panda_grid (list): Lista reprezentująca siatkę przeciwników.
        bullets (list): Lista reprezentująca pociski znajdujące się na ekranie.
    """
    match level:
        case 1:
            anim_lvl_1(panda_grid, bullets)
        case 2:
            anim_lvl_2(panda_grid, bullets)
    for k in range(len(panda_grid)):
        if panda_grid[k]:
            panda_grid[k].spawn()
