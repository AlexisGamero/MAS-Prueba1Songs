#TODO: reemplaza todo para que sea Home and Dry y no E-Mail

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="home_and_dry_pet_shop_boys_prueba1",
            category=[mas_songs.TYPE_SHORT],
            prompt="Home And Dry",
            aff_range=(mas_aff.AFFECTIONATE, None),
            random=True
        ),
        code="SNG"
    )

label home_and_dry_pet_shop_boys_prueba1(from_long = False):



    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="home_and_dry_pet_shop_boys_prueba1_long",
            category=[mas_songs.TYPE_LONG],
            prompt="Home And Dry",
            random=False,
            unlocked=False,
            aff_range=(mas_aff.AFFECTIONATE,None) 
        ),
        code="SNG"
    )

label home_and_dry_pet_shop_boys_prueba1_long:

    m 1tua "{i}~Communication's never been~{/i}" #ejemplo de verso de la canción
    #Cuándo empieza en minúscula, es un extend

    '''
    So my baby's on the road
    doing business, selling loads

    Charming everyone there
    with the sweetest smile

    Oh tonight I miss you
    Oh tonight I wish you

    Could be here with me
    but I won't see you
    'til you've made it back again

    Home and dry

    Home and dry

    ...

    There's a plane at JFK
    to fly you back from far away

    All those dark and frantic
    transatlantic miles

    Oh tonight I miss you
    Oh tonight I wish you

    Could be here with me
    but I won't see you
    'til you've made it back again

    Home and dry
    Home and dry

    Far away
    Through night and day
    You fly long haul tonight

    Come to me
    You know I'll be here
    When you call tonight
    Oh tonight I miss you
    Oh tonight I wish you
    Could be here with me
    But I won't see you
    'Til you've made it back again
    Home and dry
    Home and dry
    Home and dry
    Home and dry
    Your baby waits tonight
    '''
    m 1tua "{i}~So my baby's on the road~{/i}"
    extend 1tub "{i} doing business, selling loads~{/i}"
    m 1tuc "{i}~Charming everyone there~{/i}"
    extend 1tud "{i} with the sweetest smile~{/i}"

    m 1tue "{i}~Oh tonight I miss you~{/i}"
    m 1tuf "{i}~Oh tonight I wish you~{/i}"

    m 1tug "{i}~Could be here with me~{/i}"
    extend 1tuh "{i} but I won't see you~{/i}"
    extend 1tui "{i} 'til you've made it back again~{/i}"

    m 1tuj "{i}~Home and dry~{/i}"
    m 1tuk "{i}~Home and dry~{/i}"

    m 1tul "{i}~...~{/i}"

    m 1tum "{i}~There's a plane at JFK~{/i}"
    extend 1tun "{i} to fly you back from far away~{/i}"
    m 1tuo "{i}~All those dark and frantic~{/i}"
    extend 1tup "{i} transatlantic miles~{/i}"

    m 1tuq "{i}~Oh tonight I miss you~{/i}"
    m 1tur "{i}~Oh tonight I wish you~{/i}"

    m 1tus "{i}~Could be here with me~{/i}"
    extend 1tut "{i} but I won't see you~{/i}"
    extend 1tuu "{i} 'til you've made it back again~{/i}"

    m 1tuv "{i}~Home and dry~{/i}"
    m 1tuw "{i}~Home and dry~{/i}"

    m 1tux "{i}~Far away~{/i}"
    extend 1tuy "{i}~through night and day~{/i}"
    m 1tuz "{i}~You fly long haul tonight~{/i}"
    m 1tva "{i}~Come to me~{/i}"
    extend 1tvb "{i}~ you know I'll be here~{/i}"
    extend 1tvc "{i}~ when you call tonight~{/i}"

    m 1tvd "{i}~Oh tonight I miss you~{/i}"
    m 1tve "{i}~Oh tonight I wish you~{/i}"
    m 1tvf "{i}~Could be here with me~{/i}"
    extend 1tvg "{i} but I won't see you~{/i}"
    extend 1tvh "{i} 'til you've made it back again~{/i}"

    m 1tvi "{i}~Home and dry~{/i}"
    m 1tvj "{i}~Home and dry~{/i}"
    m 1tvk "{i}~Home and dry~{/i}"
    m 1tvl "{i}~Home and dry~{/i}"

    m 1tvm "{i}~Your baby waits tonight~{/i}"

    m 1tvm "{i}~...~{/i}"

    return