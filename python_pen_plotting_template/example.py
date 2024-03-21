import svg


DRAW_BORDER = True

def main():
    elements = []

    if DRAW_BORDER:
        border = svg.Rect(
            x=100,
            y=100,
            width=400,
            height=600,
            stroke="black",
            stroke_width=1,
            fill="none",
        )
        elements.append(border)

    for idx_row in range(30):
        for idx_col in range(20):
            value_x = 105 + (idx_col * 20)
            value_y = 105 + (idx_row * 20)

            square = svg.Rect(
                x=value_x,
                y=value_y,
                width=10,
                height=10,
                stroke="black",
                stroke_width=1,
                fill="none",
            )
            elements.append(square)

    canvas = svg.SVG(
        width="9in",
        height="12in",
        viewBox="0,0,600,800",
        elements=elements,
    )
    file_contents = f"{canvas}"

    with open('public/export.svg', 'w') as f:
        f.write(file_contents)


if __name__ == "__main__":
    main()
