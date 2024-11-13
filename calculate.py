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
    if fig == 'circle':
        if func == 'area':
            return circle.area(*size)
        elif func == 'perimeter':
            return circle.perimeter(*size)
    elif fig == 'square':
        if func == 'area':
            return square.area(*size)
        elif func == 'perimeter':
            return square.perimeter(*size)
    elif fig == 'rectangle':
        if func == 'area':
            return rectangle.area(*size)
        elif func == 'perimeter':
            return rectangle.perimeter(*size)
    elif fig == 'triangle':
        if func == 'area':
            return triangle.area(*size)
        elif func == 'perimeter':
            return triangle.perimeter(*size)
    else:
        raise ValueError("Invalid figure or function")


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