#!python


def figure_string(
        figure=505,
        primary_color=1,
        secondary_color=1,
        width=50,
        height=50,
        x=764,
        y=764,
        stroke=0,
        mirror=0,
        angle=0, ):
    FIGURE_FORMAT = "{figure}.{primary_color}.{secondary_color}.{width}.{height}.{x}.{y}.{stroke}.{mirror}.{angle}"
    return FIGURE_FORMAT.format(
        figure=figure,
        primary_color=primary_color,
        secondary_color=secondary_color,
        width=width,
        height=height,
        x=x,
        y=y,
        stroke=stroke,
        mirror=mirror,
        angle=angle,
    )


if __name__ == "__main__":
    background_figure = figure_string(width=1500, height=1500, primary_color=116, secondary_color=116)
    figures = [background_figure, figure_string(figure=505)]

    rows_count = 5  # 20
    columns_count = 5  # 20
    figure_size = 50

    for row_index in range(rows_count):
        for column_index in range(rows_count):
            x = row_index * figure_size + 764
            y = column_index * figure_size + 764
            figures.append(figure_string(figure=505, x=x, y=y, width=figure_size, height=figure_size))

    print(".".join(figures))
