import pygame

class LibraryWindow:

    _initialized = False

    @staticmethod
    def init():
        if not LibraryWindow._initialized:
            pygame.init()
            pygame.mixer.init()
            LibraryWindow._initialized = True

    @staticmethod
    def create_window(width=800, height=600, title="Game Window"):
        LibraryWindow.init()
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        return window

    @staticmethod
    def set_icon(image_path):
        try:
            icon = pygame.image.load(image_path)
            pygame.display.set_icon(icon)
        except FileNotFoundError:
            print("ERROR: Icon file not found")

    @staticmethod
    def fill_window(win, color=(255, 255, 255)):
        win.fill(color)

    @staticmethod
    def run(win, fps=60):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()

    @staticmethod
    def key_pressed(key):
        keys = pygame.key.get_pressed()
        return keys[key]

    @staticmethod
    def mouse_pressed(button=0):
        buttons = pygame.mouse.get_pressed()
        return buttons[button]

    @staticmethod
    def mouse_position():
        return pygame.mouse.get_pos()

    @staticmethod
    def play_sound(file_path):
        try:
            sound = pygame.mixer.Sound(file_path)
            sound.play()
        except FileNotFoundError:
            print("ERROR: Sound file not found")

    @staticmethod
    def play_music(file_path, loops=0):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(loops=loops)
        except FileNotFoundError:
            print("ERROR: Music file not found")

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()

    @staticmethod
    def load_sprite(image_path, scale=None):
        try:
            sprite = pygame.image.load(image_path).convert_alpha()
            if scale:
                sprite = pygame.transform.scale(sprite, scale)
            return sprite
        except FileNotFoundError:
            print("ERROR: Sprite file not found")
            return None

    @staticmethod
    def draw_sprite(win, sprite, x, y):
        if sprite:
            win.blit(sprite, (x, y))

    @staticmethod
    def rect_collision(rect1, rect2):
        return rect1.colliderect(rect2)

    @staticmethod
    def point_in_rect(point, rect):
        return rect.collidepoint(point)