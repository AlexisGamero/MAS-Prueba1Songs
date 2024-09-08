init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="email_pet_shop_boys_prueba1",
            category=[mas_songs.TYPE_SHORT],
            prompt="E-Mail",
            aff_range=(mas_aff.AFFECTIONATE, None),
            random=True
        ),
        code="SNG"
    )

label email_pet_shop_boys_prueba1(from_long = False):

    m 1dud "{i}~Now time and distance{/i}"
    extend 3dub "{i} melt away~{/i}"
    m 3kub "{i}~No digital delay~{/i}"
    m 3mub "{i}~And some things{/i}"
    extend 2mkb "{i} can be written down{/i}"
    extend 2fkbsb "{i} that we're too shy to say~{/i}"
    m 2hubsb "{i}~Send me an e-mail{/i}"    
    extend 4dsbsd "{i} that says 'I love you'~{/i}"
    m 4kubsb "{i}~Send me an e-mail{/i}"
    extend 4subsb "{i} that says 'I love you'~{/i}"

    if not from_long:
        m 1hubsa "..."
        m 7rua "Maybe the e-mail's are not as popular as they used to be."
        m 1eua "But I still think they're a cute way to communicate."
        m 1eub "Sending an e-mail just to say 'I love you' feels so genuine, don't you think?"
        m 4dua "And talking about love..."
        m 4subsb "{i}I {w=0.5}love {w=0.5}you.{/i}"
        m 1dublb "Ehehe~"

        return "love"

    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="email_pet_shop_boys_prueba1_long",
            category=[mas_songs.TYPE_LONG],
            prompt="E-Mail",
            random=False,
            unlocked=False,
            aff_range=(mas_aff.AFFECTIONATE,None) 
        ),
        code="SNG"
    )

label email_pet_shop_boys_prueba1_long:

    m 1tua "{i}~Communication's never been~{/i}"
    extend 3tub "{i} as easy as today~{/i}"
    m 3sub "{i}~And it would make me happy{/i}"
    extend 3mub "{i} when you've gone so far away~{/i}"
    m 2fub "{i}~If you'd send me an e-mail{/i}"
    extend 2dub "{i} that says 'I love you'~{/i}"
    m 4fub "{i}~Send me an e-mail{/i}"
    extend 1hub "{i} that says 'I love you'~{/i}"

    m 1hua "{i}...{/i}"

    call email_pet_shop_boys_prueba1(from_long = True)

    m 1hubla "{i}...{/i}"

    m 1dkbld "{i}~There may be other{/i}"
    extend 1dkblo "{i} temptations in your life~{/i}"

    m 1dkblc "{i}~Don't want to add more{/i}"
    extend 1dsbld "{i} complications to your life~{/i}"

    m 1hubla "{i}~But I'm sending this e-mail{/i}"
    extend 1dublb "{i} to say 'I love you'~{/i}"

    m 1lublb "{i}~I'm sending this e-mail{/i}"
    extend 1subsb "{i} to say 'I love you'~{/i}"

    m 1tubsa "{i}...{/i}"

    m 3dsd "{i}~Now there's a ghost{/i}"
    extend 3msd "{i} within this house~{/i}"
    m 3dssdld "{i}~You're haunting me tonight~{/i}"
    m 3msbssdlu "{i}~I'm looking at some photographs{/i}"
    extend 3mtbssdlu "{i} and thinking that I might~{/i}"
    m 2mtbsa "{i}~Jump on a plane{/i}"
    extend 2ttbsa "{i} and surprise you where{/i}"
    extend 2tubsa "{i} you are~{/i}"
    m 2etbsc "{i}~But do you want me there?~{/i}" 
    m 2ekbsc "{i}~I'm so insecure{/i}"
    extend 2ekbsa "{i} but one thing would make me sure~{/i}"
    m 4ekbsa "{i}~If you'd{/i}"
    extend 5ekbsb "{i} send me an e-mail{/i}"
    extend 5dkbfb "{i} that says 'I love you'~{/i}"
    m 5fkbfb "{i}~Send me an e-mail{/i}"
    extend 5hubfu "{i} that says 'I love You'~{/i}"

    m 1hubfu "{i}...{/i}"

    m 1subfu "{i}~Send me an e-mail{/i}"
    extend 5hubfb "{i} that says {w=1} 'I {w=0.5}love {w=0.5}You'~{/i}" 
    
    return "love"