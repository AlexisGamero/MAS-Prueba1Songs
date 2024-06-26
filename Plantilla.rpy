init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="_prueba1", #TODO: Nombre de la canción
            category=[mas_songs.TYPE_SHORT],
            prompt="", #TODO: Nombre de la canción
            aff_range=(mas_aff.NORMAL, None), #TODO: Corrije esta chusta, no es normal, nunca mejor dicho xd
            random=True
        ),
        code="SNG"
    )

label _prueba1(from_long = False):
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
            eventlabel="_prueba1_long", #TODO: Nombre de la canción
            category=[store.mas_songs.TYPE_LONG],
            prompt="", #TODO: Nombre de la canción
            random=False,
            unlocked=False,
            aff_range=(mas_aff.NORMAL,None) #TODO: Corrije esta chusta, no es normal, nunca mejor dicho xd
        ),
        code="SNG"
    )

label _prueba1_long: #TODO: Nombre de la canción larga
    call _prueba1(from_long = True) #TODO: Nombre de la canción corta

    """
    Placeholder: letras largas

    """