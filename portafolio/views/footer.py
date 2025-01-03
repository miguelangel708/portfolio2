import reflex as rx
from portafolio.components.media import media
from portafolio.data import Media
from portafolio.styles.styles import Size
from portafolio.components.icon_button import icon_button


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Este portafolio se ha usado en base al proyecto hecho por mouredev, todo un crack"),
        rx.hstack(
            icon_button(
                "github",
                "https://github.com/mouredev/portafolio-template?tab=readme-ov-file"
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value
    )
