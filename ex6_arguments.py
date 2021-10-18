import shutil


def display(
    message: str,
    pre_dinosaur: bool,
    wrap_sparkles: bool,
    left: bool,
    centre: bool,
    right: bool,
) -> None:
    given_alignments = [x for x in [left, centre, right] if x]
    if len(given_alignments) == 0:
        alignment = "left"
    elif len(given_alignments) == 1:
        if left:
            alignment = "left"
        elif centre:
            alignment = "centre"
        elif right:
            alignment = "right"
    else:
        raise ValueError("Only one alignment (left, centre, right) should be given")

    if wrap_sparkles:
        message = "✨ " + message + " ✨"
    if pre_dinosaur:
        message = "🦖 " + message

    width, _height = shutil.get_terminal_size()
    width -= 1
    if alignment == "left":
        pass
    elif alignment == "centre":
        message = message.center(width)
    elif alignment == "right":
        message = message.rjust(width)

    print(message)


display("RAWR", True, False, True, False, False)
display("Hello World", False, True, False, True, False)
display("RAWR", True, False, False, False, True)
