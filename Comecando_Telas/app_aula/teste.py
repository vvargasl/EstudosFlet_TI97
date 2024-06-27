from flet import *



def main(page: Page):

    page.window_width = 360
    page.window_height = 700

    page.window_center()

    page.title = "Trabalhando com Container"

    imageLogin = Image(src="login.png", width=200)

    tf_username = TextField(label="Usuário", bgcolor=colors.WHITE, icon=icons.LOGIN)
    tf_password = TextField(label="Senha", password=True, bgcolor=colors.WHITE, icon=icons.PASSWORD)

    btn_login = ElevatedButton(
        "Login",
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=3),
            bgcolor={
                MaterialState.DEFAULT: colors.BLUE,
                MaterialState.HOVERED: colors.LIGHT_BLUE
            },
            color=colors.WHITE
        )
    )


    tb_esqueciSenha = TextButton("Esqueci a senha")

    imgFace = Image(src="face.png", width=50)
    imgGmail = Image(src="gmail.png", width=50)

    lineImg = Row(controls=[imageLogin], alignment=MainAxisAlignment.CENTER)
    line1 = Row(controls=[tf_username], alignment=MainAxisAlignment.CENTER)
    line2 = Row(controls=[tf_password], alignment=MainAxisAlignment.CENTER)
    line3 = Row(controls=[btn_login], alignment=MainAxisAlignment.CENTER)
    line4 = Row(controls=[tb_esqueciSenha], alignment=MainAxisAlignment.CENTER)

    lineImages = Row(controls=[imgFace, imgGmail], alignment=MainAxisAlignment.SPACE_AROUND)

    coluna = Column(controls=[lineImg, line1, line2, line3, line4, lineImages])

    container1 = Container(
        content=coluna,
        width=340,
        height=640,
        border_radius=50,
        border=border.all(4, color=colors.BLUE_50),
        margin=margin.all(2),
        gradient=LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=[colors.BLUE_400, colors.BLUE_100]
        ),
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=colors.BLUE_800,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER
        ),
        alignment=alignment.center
    )

    page.add(container1)
    page.update()

if __name__ == '__main__':
    app(main)
