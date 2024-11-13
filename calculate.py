import circle
import square
import rectangle
import triangle

figs = ['circle', 'square', 'rectangle', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    "area-circle": 1,
    "perimeter-circle": 1,
    "area-square": 1,
    "perimeter-square": 1,
    "area-rectangle": 2,
    "perimeter-rectangle": 2,
    "area-triangle": 2,
    "perimeter-triangle": 3,
}


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs
    return eval(f'{fig}.{func}(*{size})')


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(
            map(
                int,
                input(
                    f"Input figure sizes separated by space, expected "
                    f"{sizes.get(f'{func}-{fig}', 1)} values:\n"
                ).split()
            )
        )

    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')
    