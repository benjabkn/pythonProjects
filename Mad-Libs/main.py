# Este programa permite a los usuarios crear historias personalizadas ingresando sustantivos, verbos y nombres de personajes.
# Los usuarios pueden proporcionar múltiples entradas para algunos de los campos, lo que añade variabilidad y riqueza a la narrativa generada.


# Posibles mejoras:
# 1.- Buscar como hacer para que la historia sea diferente segun el intento
# 2.- Situar las vars en arreglos


def get_input(word_type: str) -> str:
    while True:
        user_input: str = input(f"Ingresa un {word_type}: ").strip()
        words = user_input.split()

        if len(words) == 2:
            return user_input
        else:
            print("Error, por favor ingresa solo una palabra.")



actor = get_input("nombre o sustantivo del protagonista. Ej: mago, caballero")
verbo = get_input("verbo en infinitivo")
sustantivo1 = get_input("sustantivo1")
verbo1 = get_input("verbo en infinitivo")
sustantivo2 = get_input("sustantivo2")

# Creando la historia
story = f"""
Había una vez un {actor} que deseaba {verbo} por encima de todo. Un día, decidió que era momento de comenzar su aventura.
Mientras viajaba, encontró un {sustantivo1} que parecía necesitar ayuda. Sin dudarlo, el {actor} decidió {verbo1} para salvarlo.
Esta acción llevó al {actor} a un lugar desconocido, donde descubrió un {sustantivo2} mágico. Este hallazgo no solo cambió su vida,
sino que también le permitió cumplir su mayor deseo.
"""
print(story)
