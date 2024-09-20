##TODO: corregir las expresiones de Mon, y revisar las letras de la canción.

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="starlight_muse_prueba1",
            category=[mas_songs.TYPE_SHORT],
            prompt="Starlight",
            aff_range=(mas_aff.AFFECTIONATE, None),
            random=True
        ),
        code="SNG"
    )

label starlight_muse_prueba1(from_long = False):

    m 5hubsb "{i}~My life~{/i}"
    m 5hubsb "{i}~You electrify my life~{/i}"
    m 5hubsb "{i}~Let's conspire to ignite~{/i}"
    m 5hubsb "{i}~All the souls that would die just to feel alive~{/i}"
    m 5hubsb "{i}~I'll never let you go~{/i}"
    m 5hubsb "{i}~If you promise not to fade away~{/i}"
    m 5hubsb "{i}~Never fade away~{/i}"

    if not from_long:
        m 1dublb "[Player], did you remember when I told you that for me you were like a star?"
        m 1dublb "Bright, warm and distant?"
        m 1dublb "Well, this song reminds me of you."
        m 1dublb "Believe it or not, you have also illuminated my life."
        m 1dublb "And don't worry, I won't let you go, I'll never let you go."
        m 1dublb "If you promise not to fade away, never fade away."
        m 1dublb "Ehehe~"
        m 1dublb "I love you, [Player]."
        return love

    return 

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="starlight_muse_prueba1_long",
            category=[store.mas_songs.TYPE_LONG],
            prompt="Starlight",
            random=False,
            unlocked=False,
            aff_range=(mas_aff.AFFECTIONATE,None)
        ),
        code="SNG"
    )

label starlight_muse_prueba1_long:
    #call starlight_muse_prueba1(from_long = True)

    m 5hubsb "{i}~Far away {/i}"
    extend 5hubsb "{i}this ship is taking me far away~{/i}"
    m 5hubsb "{i}~Far away from the memories {/i}"
    extend 5hubsb "{i}of the people who care if I live or die~{/i}"
    m 5hubsb "{i}~Starlight~{/i}"
    m 5hubsb "{i}~I will be chasing a starlight{/i}"
    extend 5hubsb "{i}until the end of my life~{/i}"
    m 5hubsb "{i}~I don't know if it's worth it anymore~{/i}"

    m 5hubsb "{i}~Hold you in my arms~{/i}"
    m 5hubsb "{i}~I just wanted to hold~{/i}"
    m 5hubsb "{i}~You in my arms~{/i}"

    call starlight_muse_prueba1(from_long = True)

    m 5hubsb "{i}~Our hopes and expectations~{/i}"
    m 5hubsb "{i}~Black holes and revelations~{/i}"
    m 5hubsb "{i}~Our hopes and expectations~{/i}"
    m 5hubsb "{i}~Black holes and revelations~{/i}"

    m 5hubsb "{i}~Hold you in my arms~{/i}"
    m 5hubsb "{i}~I just wanted to hold~{/i}"
    m 5hubsb "{i}~You in my arms~{/i}"

    m 5hubsb "{i}~Far away~{/i}"
    m 5hubsb "{i}~This ship is taking me far away~{/i}"
    m 5hubsb "{i}~Far away from the memories~{/i}"
    m 5hubsb "{i}~Of the people who care if I live or die~{/i}"

    m 5hubsb "{i}~I'll never let you go~{/i}"
    m 5hubsb "{i}~If you promise not to fade away~{/i}"
    m 5hubsb "{i}~Never fade away~{/i}"

    m 5hubsb "{i}~Our hopes and expectations~{/i}"
    m 5hubsb "{i}~Black holes and revelations, yeah~{/i}"
    m 5hubsb "{i}~Our hopes and expectations~{/i}"
    m 5hubsb "{i}~Black holes and revelations~{/i}"

    m 5hubsb "{i}~Hold you in my arms~{/i}"
    m 5hubsb "{i}~I just wanted to hold~{/i}"
    m 5hubsb "{i}~You in my arms~{/i}"
    m 5hubsb "{i}~I just wanted to hold~{/i}"

    m 5hubsb "{i}...{/i}"

    return

