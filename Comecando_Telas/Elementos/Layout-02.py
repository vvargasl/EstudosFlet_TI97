from flet import *

def main(page: Page):
    page.title = "Coluna"
    page.padding = 20

    gridView = GridView(
        expand=1,
        runs_count=50,
        max_extent=300,
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,
        horizontal=1,
    )

    for i in range(40):
        gridView.controls.append(
            Container(
                bgcolor=colors.WHITE,
                border=border.all(2, color=colors.RED_700),
                border_radius=20,
                padding=10,
                content=Column(
                    controls=[
                        Row(
                            controls=[
                                Image(src="burg.png", width=100, height=100)
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        Row(
                            controls=[
                                Text("Burger 100 gramas", size=18, color=colors.BLACK, weight=FontWeight.BOLD, font_family="Consolas")
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        Row(
                            controls=[
                                Column(
                                    controls=[
                                        Text(f"Combo  {i}", size=16),
                                        Text("Lanches", size=12, color=colors.BLACK),
                                        Row(
                                            controls=[
                                                Icon(icons.CIRCLE_SHARP, color=colors.GREEN, size=10),
                                                Text("Aberto", size=15)
                                            ]
                                        )
                                    ],
                                    alignment=MainAxisAlignment.START
                                ),
                                Column(
                                    controls=[
                                        Text("De R$ 45,90", size=14,color=colors.RED),
                                        Text("      por", size=14),
                                        Text("R$ 39,90", size=20, color=colors.GREEN,weight=FontWeight.BOLD)
                                    ],
                                    alignment=MainAxisAlignment.END
                                )
                            ],
                            alignment=MainAxisAlignment.SPACE_BETWEEN
                        ),
                        Container(
                            content=ElevatedButton(
                                text="Comprar",
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=13),
                                    padding=12,
                                    bgcolor=colors.RED_500,
                                    color=colors.WHITE

                                )
                            ),
                            width=700,
                            margin=margin.only(top=5)
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )
        )

    page.add(gridView)
    page.update()


if __name__ == '__main__':
    app(main)
