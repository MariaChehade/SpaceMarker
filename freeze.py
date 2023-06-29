import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py", icon="icone.ico")
]
cx_Freeze.setup(
    name = "Space Marker",
    options={
        "build_exe":{
            "packages":["pygame",
                       "tkinter",
                       "pygame.locals",
                       "csv",
                       "os",
                       "funcoes"
                        ],
            "include_files":["icone.jpg",
                            "som.mp3",
                            "fundo.jpeg",
                            "icone.ico",
                            "README.md"
                            ]
        }
    }, executables = executables
)

#py geraSetup.py build
#py geraSetup.py bdist_msi