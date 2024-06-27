from flet import *

def main(page:Page):
    page.title="Estudando Elementos"
    produto=Card(
        content=Container(
            content=Column(
                controls=[
                    Image(src="burg.png"),
                    Text("Lanche Stake"),
                    Text("Lanche Feito"),
                    Row(controls=[
                        Icon(cupertino_icons.HEART),
                        Icon(icons.PAYMENT)
                    ]

                    )

                ]

            )

        )

    )

    page.add(produto)

if __name__ == '__main__':
    app(main)