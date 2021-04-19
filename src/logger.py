from click import secho

def success(message: str):
    display("[ SUCCESS ] {}".format(message), "green")

def info(message: str):
    display("[ INFO    ] {}".format(message), "blue")

def warn(message: str):
    display("[ WARN    ] {}".format(message), "yellow")

def verbose(message: str, verbose_flag: bool):
    if verbose_flag:
        display("[ DEBUG   ] {}".format(message), "cyan")

def error(message: str):
    display("[ ERROR   ] {}".format(message), "red")

def display(formatted_message, color):
    secho(formatted_message, fg=color)