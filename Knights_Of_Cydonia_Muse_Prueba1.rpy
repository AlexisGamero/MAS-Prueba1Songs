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

label KnightsOfCydonia_Muse_Prueba1(from_long = False):
    m 1tfb "{i}~No one's gonna take me alive~{/i}"
    m 2tub "{i}~Time has come to make things right~{/i}"
    m 4tkb "{i}~You and I must fight for our rights~{/i}"
    m 4tfb "{i}~You and I must fight to survive~{/i}"

    if not from_long:
        m 2dka "..."
        m 1eka "You know?"
        m 3eka "This song is... too powerful, [player]."
        m 1eua "And makes me want to be with you..."
        m 1kua "To face the world, together."
        m 1hua "Ehehe~"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="KnightsOfCydonia_Muse_Prueba1_Long",
            category=[mas_songs.TYPE_LONG],
            prompt="Knights of Cydonia",
            aff_range=(mas_aff.NORMAL, None),
            random=False,
            unlocked=False
        ),
        code="SNG"
    )

label KnightsOfCydonia_Muse_Prueba1_Long:
    m 2euc "..."
    m 2dkd "{i}~Come ride with me{/i}"
    extend 3lkd "{i} through the veins of history~{/i}"
    m 2tkd "{i}~I'll show you how God{/i}"
    extend 2tfd "{i} falls asleep on the job~{/i}"

    m 2ttc "{i}~And how can we win{/i}"
    extend 2tfd "{i} when fools can be kings?~{/i}"
    m 2ekd "{i}~Don't waste your time{/i}"
    extend 2wkd "{i} or time will waste you~{/i}"

    m 1tfa "..."

    call KnightsOfCydonia_Muse_Prueba1(from_long = True)
    call KnightsOfCydonia_Muse_Prueba1(from_long = True)

    m 1hua "..."

    call KnightsOfCydonia_Muse_Prueba1(from_long = True)

    return

