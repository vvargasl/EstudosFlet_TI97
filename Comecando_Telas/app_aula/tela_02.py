from flet import *

def main(page:Page):

    page.window_width = 360
    page.window_height = 700

    page.window_center()

    page.title = "Tabalhando com Container"

    containe1=Container(
            width=340,
            height=640,
            border_radius=50,
            border=border.all(4,color=colors.INDIGO_400),
            margin=margin.all(2),
            gradient=LinearGradient(
                begin=alignment.top_center,
                end=alignment.bottom_center,
                colors=[colors.INDIGO_400,colors.INDIGO_100]
            ),
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=colors.INDIGO_900,
                offset=Offset(0,0),
                blur_style=ShadowBlurStyle.OUTER
            ),

                alignment=Alignment(-1,0)
            )


    page.add(containe1)
    page.update()

if __name__ == '__main__':
    app(main)