from flet import *

def main(page:Page):
    page.title="Estudando Elementos"
    produto=Card(
        content=Container(
            bgcolor=colors.AMBER_100,
            width=200,

            content=Column(
                controls=[
                    Row(controls=[Image(src="burg.png")],alignment=MainAxisAlignment.CENTER),
                    Row(controls=[Text("Stake de Frango")],alignment=MainAxisAlignment.CENTER),
                    Row(controls=[Text("Lanche Feito",max_lines=2)],
                        alignment=MainAxisAlignment.CENTER),
                    Row(controls=[
                        Icon(cupertino_icons.HEART,color=colors.RED),
                        Icon(icons.MONEY,color=colors.GREEN)
                    ],alignment=MainAxisAlignment.CENTER)

                ]
            ),


        )

    )

    page.add(produto)

if __name__ == '__main__':
    app(main)