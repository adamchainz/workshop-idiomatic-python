import shutil


def display(
    message: str,
    *,
    pre_dinosaur: bool = False,
    wrap_sparkles: bool = False,
    align: str = "left",
) -> None:
    if align not in ("left", "centre", "right"):
        raise ValueError("align must be one of 'left', 'centre', or 'right'.")

    if wrap_sparkles:
        message = "✨ " + message + " ✨"
    if pre_dinosaur:
        message = "🦖 " + message

    width, _height = shutil.get_terminal_size()
    width -= 1
    if align == "left":
        pass
    elif align == "centre":
        message = message.center(width)
    elif align == "right":
        message = message.rjust(width)

    print(message)


display("RAWR", pre_dinosaur=True)
display("Hello World", wrap_sparkles=True, align="centre")
display("RAWR", pre_dinosaur=True, align="right")
