import rich

game_1_inputs = [2, 11, -3, -0.5, 6, 100, -8, 5, 0]


def game_1_rule(x):
    return 5 * x + 4


magenta = "#ff33ff"
orange = "#e65c00"
dodger_blue = "#005A9C"


def display_board(inputs, rule):
    rich.print(f"[italic {dodger_blue}] x  |  y [/ italic {dodger_blue}]".center(10))
    print("-" * 11)
    for x in inputs:
        print(f"{x}".rjust(4) + " | " + f"{rule(x)}".rjust(3))
    print()


rich.print("[bold] Game 1 [/bold]")
display_board(game_1_inputs, game_1_rule)
