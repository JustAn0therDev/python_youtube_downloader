from colored import fg, stylize


class Utils:

    @staticmethod
    def log_debug_message(message: str):
        color = fg('green')
        print(stylize('[DEBUG] - {}'.format(message), color))

    @staticmethod
    def log_warning_message(message: str):
        color = fg('yellow')
        print(stylize('[WARNING] - {}'.format(message), color))

    @staticmethod
    def log_error_message(message: str):
        color = fg('red')
        print(stylize('[ERROR] - {}'.format(message), color))

