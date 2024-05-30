import pygame

class TaskLocation:
    def __init__(self, x, y, task, task_period):
        self.x = x
        self.y = y
        self.task = task
        self.task_period = task_period  # Time required to complete the task
        self.font = pygame.font.SysFont(None, 24)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x - 5, self.y - 5, 10, 10))
        task_text = self.font.render(self.task, True, (255, 255, 255))
        screen.blit(task_text, (self.x + 10, self.y - 10))