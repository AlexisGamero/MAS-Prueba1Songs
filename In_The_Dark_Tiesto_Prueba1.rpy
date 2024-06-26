init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="InTheDark_Tiesto_Prueba1",
            category=[mas_songs.TYPE_SHORT],
            prompt="In The Dark",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label InTheDark_Tiesto_Prueba1:
    m 3rka "{i}~'Cause if it's coming for you~{/i}"
    m 3lksdla "{i}~Then it's coming for me~{/i}"
    m 3gka "{i}~'Cause I will be there~{/i}"
    m 4fkb "{i}~'Cause we need each other in the dark~{/i}"
    m 2gkb "{i}~And if it terrifies you~{/i}"
    m 2mkb "{i}~Then it terrifies me~{/i}"
    m 4ekb "{i}~'Cause I will be there~{/i}"
    m 4fkbfb "{i}~So we've got each other in the dark~{/i}"
    m 3fkbfd "[player], you are the love of my life..."
    m 5tkbfa "And I'm gonna look up to you, {w=5}{i}always.{i}"
    m 5mkbfc "Even if the life gets too dark or hard."
    m 5subfb "{i}~'Cause we'll be together in the dark.~{i}"
    m 5hubfa "Ehehe~"
    return