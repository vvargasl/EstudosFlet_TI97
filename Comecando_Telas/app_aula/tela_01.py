
from flet import *

colorPrimary = "#F2E3B3" # amarelo forte
secondColor = "#F2D272" # amarelo pastel
colorBar = "0A0A0D" #preto
backgroudColor = "#FFFFFF"  #branco
colorBlue = "#4386d5" #azul
azulClaro = "#5ed2f7"

def main(page:Page):
    page.title = "Login"

    page.window_width = 340
    page.window_height = 640

    page.window_min_width = 340
    page.window_min_height = 640

    page.window_max_width = 340
    page.window_max_height = 640

    page.window_center()

    page.bgcolor = backgroudColor

    imageLogin=Image(src="login.png", width=200)



    tf_username = TextField(label="Usuário", bgcolor=backgroudColor, icon=icons.LOGIN)
    tf_password = TextField(label="Senha", password=True, bgcolor=backgroudColor, icon=icons.PASSWORD)

    btn_login = ElevatedButton("Login",
                               style=ButtonStyle(
                                   shape=RoundedRectangleBorder(radius=3),
                                   bgcolor={
                                       MaterialState.DEFAULT:colorBlue,
                                       MaterialState.HOVERED:azulClaro
                                   },
                                   color=backgroudColor
                               ))



    tb_esqueciSenha = TextButton("Esqueci a senha")

    imgFace = Image(src="face.png", width=50)
    imgGmail = Image(src="gmail.png", width=50)

    lineImg=Row(controls=[imageLogin],alignment=MainAxisAlignment.CENTER)
    line1=Row(controls=[tf_username],alignment=MainAxisAlignment.CENTER)
    line2=Row(controls=[tf_password],alignment=MainAxisAlignment.CENTER)
    line3=Row(controls=[btn_login],alignment=MainAxisAlignment.CENTER)
    line4 = Row(controls=[tb_esqueciSenha], alignment=MainAxisAlignment.CENTER)


    lineImages = Row(controls=[imgFace, imgGmail], alignment=MainAxisAlignment.SPACE_AROUND)


    coluna = Column(controls=[lineImg, line1, line2, line3, line4, lineImages])

    page.add(coluna)
    page.update()

if __name__ == '__main__':
    app(main)