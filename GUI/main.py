import flet as ft

#clase para la ventana principal de la aplicacion
class UI(ft.ResponsiveRow):
    def __init__(self, page):
        super().__init__(controls=[],expand=True)
        self.color_teal = "teal"
        #control switch para cambiar el modo de la aplicacion
        self.mode_sw = ft.Switch(
            value=True,
            thumb_color= "Black",
            thumb_icon={ft.ControlState.DEFAULT: ft.Icons.LIGHT_MODE,
                         ft.ControlState.SELECTED: ft.Icons.DARK_MODE},
            #configuracion del switch
            on_change=lambda e: page.update()
        )
        #Creacionde contenedor principal
        self.initial_container_1 = ft.Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=ft.Column(
                
                controls=[
                    ft.Text("PANEL DE CONTROL"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )
        self.initial_container_2 = ft.Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=ft.Column(
                
                controls=[
                    ft.Text("otro contenedor"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )
        #contenedores secundarios
        self.location_container_1 = ft.Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=ft.Column(
                
                controls=[
                    ft.Text("Ubicacion - dia"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )
        self.location_container_2= ft.Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=ft.Column(
                
                controls=[
                    ft.Text("Ubicacion- semana"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )
        
        #creacion de contenedores dinamicos
        self.container_list_1=[self.initial_container_1,]
        self.container_list_2=[self.initial_container_2,]
        #se encargar de ir cambiando el contenido de los contenedores dinamicos
        self.navigation_container1 = ft.Container(content=self.container_list_1[0], expand=True )
        self.navigation_container2 = ft.Container(content=self.container_list_2[0], expand=True )

        #Creacion de columnas responsivas
        self.navigation_container = ft.Container(
        #configuracion de la barra de navegacion
            col=1,
            bgcolor= self.color_teal,
            border_radius=10,
            #blur=ft.Blur(sigma_x=10, sigma_y=5),
            content=ft.Column(
                # Contenido de la barra de navegación
                controls=[
                    #se crean dos contenedores para los iconos de navegacion y boton inferior
                    ft.Container(
                        #blur=ft.Blur(sigma_x=10, sigma_y=5),
                        expand=True,
                        #configuracion del icono de navegacion
                        content= ft.NavigationRail(
                            #Configuracion del navegation rail
                            selected_index=0,
                            bgcolor= self.color_teal,
                            destinations=[
                                ft.NavigationRailDestination(
                                    icon=ft.Icons.HOME,
                                    
                                ),
                                ft.NavigationRailDestination(
                                    icon=ft.Icons.CALENDAR_MONTH_SHARP,
                                    
                                ),
                                ft.NavigationRailDestination(
                                    icon=ft.Icons.INFO,
                                    
                                ),
                                ft.NavigationRailDestination(
                                    icon=ft.Icons.SETTINGS,
                                    
                                )
                            ]
                        )
                    ),

                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        content= ft.Column(
                            expand=True,
                            #envia el contenido de la columna al final
                            alignment=ft.MainAxisAlignment.END,
                            controls=[ft.IconButton(
                                icon=ft.Icons.OUTPUT,  
                        ),
                        self.mode_sw
                        ]
                            
                    )
                    ),
                ]
            )
        )
        self.frame_2 = ft.Container(
        #configuracion columna 2
            col=6,
            #bgcolor= ft.Colors.WHITE,
            
            content=ft.Column(
                # Contenido de la columna 2
                controls= [
                    ft.Container(
                        border_radius=10,
                        padding=ft.padding.only(right=200),
                        alignment=ft.alignment.top_left,
                        content=ft.Container(
                            bgcolor=self.color_teal,
                            border_radius=20,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.Icons.SEARCH),
                                    ft.TextField(
                                        hint_text="Buscar",
                                        width=300,
                                        border = ft.InputBorder.NONE,
                                        border_radius=20,
                                        cursor_color=ft.Colors.BLACK54
                                    ),
                                    
                                ]
                            )
                        )
                    ),
                    self.navigation_container1,
                    self.navigation_container2,
                ]
            )
        )
        self.frame_3 = ft.Container(
            col=5,
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=ft.padding.only(left=150),
                        content=ft.Container(
                            bgcolor=self.color_teal,
                            border_radius=20,
                            content=ft.Dropdown(
                                border_radius=20,
                                alignment=ft.alignment.center_right,
                                hint_text="incio",
                                options=[
                                    ft.dropdown.Option("Inicio"),
                                    ft.dropdown.Option("Configuracion"),
                                    ft.dropdown.Option("Ayuda"),
                                    ft.dropdown.Option("Salir")
                                ],
                            )
                        )
                    ),
                    ft.Container(
                        
                        border_radius=20,
                        padding=10,
                        expand=True,
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Text("Contenido de la columna 3"),
                                ),
                                ft.ResponsiveRow(
                                    expand=True,
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        ft.Container(
                                            border_radius=20,
                                            padding=5,
                                            expand=True,
                                            bgcolor=self.color_teal,
                                            col=3,
                                        ),
                                        ft.Container(
                                            border_radius=20,
                                            padding=5,
                                            expand=True,
                                            bgcolor=self.color_teal,
                                            col=3,
                                        ),
                                        ft.Container(
                                            border_radius=20,
                                            padding=5,
                                            expand=True,
                                            bgcolor=self.color_teal,
                                            col=3,
                                        ),
                                        ft.Container(
                                            border_radius=20,
                                            padding=5,
                                            expand=True,
                                            bgcolor=self.color_teal,
                                            col=3,
                                        )
                                    ]
                                )
                            ]
                        )
                    ),
                ft.Container(
                    bgcolor=self.color_teal,
                    padding=5,
                    border_radius=20,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[

                            ft.Text("otras cosas"),
                            ft.Dropdown(
                                border_radius=20,
                                hint_text="Selecciona una opcion",
                                width=150,
                                options=[
                                ft.dropdown.Option("opcion 1"), 
                                ft.dropdown.Option("opcion 2"),
                                ft.dropdown.Option("opcion 3"),
                                ft.dropdown.Option("opcion 4"),
                                ]
                            )
                        ]
                    )
                ),    
                ft.Container(
                    expand=True,
                    border_radius=20,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        scroll="auto",
                        controls=[
                            ft.ResponsiveRow(
                                controls=[
                                    ft.Container(
                                        bgcolor=self.color_teal,
                                        padding=5,
                                        border_radius=10,
                                        height=100 ,
                                        col={"md":12, "lg":6 },
                                        content=ft.Text("Contenedor 1")
                                    ),
                                    ft.Container(
                                        bgcolor=self.color_teal,
                                        padding=5,
                                        border_radius=10,
                                        height=100 ,
                                        col={"md":12, "lg":6 },
                                        content=ft.Text("Contenedor 1")
                                    ),
                                    ft.Container(
                                        bgcolor=self.color_teal,
                                        padding=5,
                                        border_radius=10,
                                        height=100 ,
                                        col={"md":12, "lg":6 },
                                        content=ft.Text("Contenedor 1")
                                    ),
                                    ft.Container(
                                        bgcolor=self.color_teal,
                                        padding=5,
                                        border_radius=10,
                                        height=100 ,
                                        col={"md":12, "lg":6 },
                                        content=ft.Text("Contenedor 1")
                                    )
                                ]
                            )
                        ]
                    )
                )
                ]
            )
        )
         # Agregamos los contenedores hijos directamente a self.controls
        self.controls.extend([
            self.navigation_container,
            self.frame_2,
            self.frame_3
        ])
   

def main(page: ft.Page):
    #tamaño minimo de la ventana
    page.window_min_width = 800
    page.window_min_height = 600
    #tema por defecto del sistema 
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.add(UI(page))

ft.app(target=main)