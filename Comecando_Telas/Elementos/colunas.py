
from flet import *


def main(page: Page):
    page.title = "Coluna"
    page.on_scroll = True
    listView = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    gridView=GridView(
        expand=1,
        runs_count=50,
        max_extent=300,
        child_aspect_ratio=0.9,
        spacing=5,
        run_spacing=2,
        horizontal=1,


    )


    #---------------------------------------------------------------------------------------------
    # coluna=Column(spacing=10)
    # for i in range(10):
    #     coluna.controls.append(
    #         Container(content=Text(f"Texto{i}"),
    #                   width=200,
    #                   height=200,
    #                   bgcolor=colors.INDIGO_100,
    #                   shadow=BoxShadow(spread_radius=10,blur_radius=20,color=colors.INDIGO_400),
    #                   alignment=Alignment(0,0))
    #
    #     )
    #-----------------------------------------------------------------------------------------------

    for i in range(40):
        gridView.controls.append(
            Container(
                bgcolor=colors.BLUE_50,
                # width=200,
                # height=350,
                content=Column(
                    controls=[
                        Image(src="burg.png"),
                        Row(controls=[Text("Titulo", size=20, color=colors.INDIGO_900, weight=FontWeight.BOLD)],
                            alignment=MainAxisAlignment.CENTER),
                        Row(controls=[Column(
                                            controls=[
                                                Text(f"Loja{i}",size=16),
                                                Text("Lanches",size=10,color=colors.BLACK),
                                                Row(controls=[
                                                    Icon(icons.CIRCLE_SHARP,color=colors.GREY,size=8),
                                                    Text("Aberto", size=10)
                                                            ])
                                                ],alignment=MainAxisAlignment.START

                                            ),

                                      Column(controls=[
                                          Text("De R$ 45,90 por: ",size=16),
                                          Text("R$ 39.90",size=23,color=colors.BLACK)
                                      ],alignment=MainAxisAlignment.END)]),


                        Row(controls=[])
                    ],alignment=MainAxisAlignment.SPACE_BETWEEN

            )
        ))

    page.add(gridView)

    page.update()


if __name__ == '__main__':
    app(main)
