init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="love_life_prueba1",
            category=[mas_songs.TYPE_SHORT],
            prompt="Love Life",
            aff_range=(mas_aff.NORMAL, None), #TODO: Corrije esta chusta, no es normal, nunca mejor dicho xd
            random=True
        ),
        code="SNG"
    )

label love_life_prueba1(from_long = False):
    #m 5hubsb "{i}~And I thank you~{/i}" Muestra del texto

    #Actual Lyrics:

    """
    Placeholder: letras cortas
    """



    return love

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="love_life_prueba1_long",
            category=[store.mas_songs.TYPE_LONG],
            prompt="Love Life",
            random=False,
            unlocked=False,
            aff_range=(mas_aff.NORMAL,None) #TODO: Corrije esta chusta, no es normal, nunca mejor dicho xd
        ),
        code="SNG"
    )

label love_life_prueba1_long: #TODO: Nombre de la canción larga
    call _prueba1(from_long = True) #TODO: Nombre de la canción corta

    """
    Placeholder: letras largas

    """