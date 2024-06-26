init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="here_pet_shop_boys_prueba1",
            category=[mas_songs.TYPE_SHORT],
            prompt="Here",
            aff_range=(mas_aff.AFFECTIONATE, None),
            random=True
        ),
        code="SNG"
    )

label here_pet_shop_boys_prueba1(from_long = False):

    #TODO: Corrige las expresiones de Mon

    m 5hubsb "{i}~You've got a home here {w=1}~{/i}"
    extend 5hubsb "{i}~,call it what you want~{/i}"
    extend 5hubsb "{i}~you've got a home here~{/i}"
    m 5hubsb "{i}~You're gonna want it when you can't~{/i}"
    extend 5hubsb "{i}~face the world and you need~{/i}"
    extend 5hubsb "{i}~some support to succeed~{/i}"
    m 5hubsb "{i}~You've got a home~{/i}"

    if not from_long:
        #TODO: Aquí va lo que opina mon sobre la canción
        m 1dublb "Ehehe~"

    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="here_pet_shop_boys_prueba1_long",
            category=[store.mas_songs.TYPE_LONG],
            prompt="Here",
            random=False,
            unlocked=False,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="SNG"
    )

label here_pet_shop_boys_prueba1_long:

    #TODO: Corrige las expresiones de Mon

    m 5hubsb "{i}~We all have a dream~{/i}"
    extend 5hubsb "{i}~of a place we belong~{/i}"

    m 5hubsb "{i}~The fire is burning~{/i}"
    extend 5hubsb "{i}~and the radio's on~{/i}"

    m 5hubsb "{i}~Somebody smiles~{/i}"
    extend 5hubsb "{i}~and it means 'I love you'~{/i}"

    m 5hubsb "{i}~But sometimes we don't notice~{/i}"
    extend 5hubsb "{i}~when the dream has come true~{/i}"

    m 5hubsb "{i}~...~{/i}"

    call here_pet_shop_boys_prueba1 (from_long = True)

    m 5hubsb "{i}~...~{/i}"

    m 5hubsb "{i}~We all make a mess~{/i}"
    extend 5hubsb "{i}~of our lives from time to time~{/i}"

    m 5hubsb "{i}~It's part of the process~{/i}"
    extend 5hubsb "{i}~that you stumble as you climb~{/i}"

    m 5hubsb "{i}~And if you ever feel~{/i}"
    extend 5hubsb "{i}~the pain is far too big a deal~{/i}"

    m 5hubsb "{i}~I say with pride~{/i}"
    extend 5hubsb "{i}~I'll be on your side~{/i}"

    m 5hubsb "{i}~You've got a home here~{/i}"
    m 5hubsb "{i}~(You've got a home)~{/i}"
    m 5hubsb "{i}~Call it what you want~{/i}"
    extend 5hubsb "{i}~you've got a home here~{/i}"
    m 5hubsb "{i}~(You've got a home)~{/i}"
    m 5hubsb "{i}~You're gonna want it when you can't~{/i}"
    extend 5hubsb "{i}~face the world and you need~{/i}"
    extend 5hubsb "{i}~some support to succeed~{/i}"
    
    m 5hubsb "{i}~You've got a home~{/i}"
    m 5hubsb "{i}~You've got a home~{/i}"

    return
