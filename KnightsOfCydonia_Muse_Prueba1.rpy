init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="KnightsOfCydonia_Muse_Prueba1",
            category=[mas_songs.TYPE_SHORT],
            prompt="Knights of Cydonia",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label KnightsOfCydonia_Muse_Prueba1:
    m 1tfb "{i}~No one's gonna take me alive~{/i}"
    m 2tub "{i}~Time has come to make things right~{/i}"
    m 4tkb "{i}~You and I must fight for our rights~{/i}"
    m 4tfb "{i}~You and I must fight to survive~{/i}"
    m 2dka "..."
    m 1eka "You know?"
    m 3eka "This song is... too powerful, [player]."
    m 1eua "And makes me want to be with you..."
    m 1kua "To face the world, together."
    m 1hua "Ehehe~"
    return