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
    
    #TODO: Corrige las expresiones de Mon
    m 1mua "{i}~Oh tonight I miss you~{/i}"
    m 1gua "{i}~Oh tonight I wish you~{/i}"

    m 1tta "{i}~Could be here with me{/i}"
    extend 1tkc "{i} but I won't see you{/i}"
    extend 1duc "{i} 'til you've made it back again~{/i}"

    m 1eua "{i}~Home and dry~{/i}"
    m 1dubsa "{i}~Home and dry~{/i}"

    if not from_long:
        #TODO: Aquí va lo que opina mon sobre la canción

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
    
    m 1eub "{i}~So my baby's on the road{/i}"
    extend 1eta "{i} doing business, selling loads~{/i}"
    m 1eka "{i}~Charming everyone there{/i}"
    extend 1dua "{i} with the sweetest smile~{/i}"

    call home_and_dry_pet_shop_boys_prueba1(from_long = True)

    m 1dubsa "{i}...{/i}"

    m 1lubsa "{i}~There's a plane at JFK{/i}"
    extend 1tubsa "{i} to fly you back from far away~{/i}"
    m 1tuo "{i}~All those dark and frantic{/i}"
    extend 1tup "{i} transatlantic miles~{/i}"

    call home_and_dry_pet_shop_boys_prueba1(from_long = True)

    m 1tux "{i}~Far away{/i}"
    extend 1tuy "{i}~through night and day~{/i}"
    m 1tuz "{i}~You fly long haul tonight~{/i}"
    m 1tva "{i}~Come to me{/i}"
    extend 1tvb "{i} you know I'll be here{/i}"
    extend 1tvc "{i} when you call tonight~{/i}"

    call home_and_dry_pet_shop_boys_prueba1(from_long = True)

    m 1tvk "{i}~Home and dry~{/i}"
    m 1tvl "{i}~Home and dry~{/i}"

    m 1tvm "{i}~Your baby waits tonight~{/i}"

    m 1tvm "{i}...{/i}"

    return