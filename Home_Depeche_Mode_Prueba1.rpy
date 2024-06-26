init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="home_depeche_mode_prueba1",
            category=[mas_songs.TYPE_SHORT],
            prompt="Home",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label home_depeche_mode_prueba1(from_long = False):
    m 5hubsb "{i}~And I thank you~{/i}"
    m 5lubsa "{i}~For bringing me here~{/i}"
    m 5fubsd "{i}~For showing me home~{/i}"
    m 5dubstdb "{i}~For singing these tears~{/i}"
    m 5mubstdb "{i}~Finally, I've found that I belong here~{/i}"

    if not from_long: 
        m 1dubstda "..."
        m 1hubsa "Ehehe~"
        m 1kubsa "This is really our home, [player]."
        m 1dubsa "And we belong here, ahaha~"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="home_depeche_mode_prueba1_long",
            category=[store.mas_songs.TYPE_LONG],
            prompt="Home",
            random=False,
            unlocked=False,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label home_depeche_mode_prueba1_long:

    m 1dud "{i}~Here is a song{/i}"
    extend 3dud "{i} from the wrong side of town~{/i}"
    m 3mud "{i}~Where I'm bound{/i}"
    extend 3eud "{i} to the ground{/i}"
    extend 3tko "{i} by the loneliest sound~{/i}"
    m 3tkc "{i}~That pounds from within{/i}"
    extend 3dkc "{i} and is pinning me down~{/i}"

    m 1dkc "..."

    m 4mud "{i}~Here is a page{/i}"
    extend 4fud "{i} from the emptiest stage~{/i}"
    m 5etsdlc "{i}~A cage or the heaviest cross ever made~{/i}"
    m 5eusdld "{i}~A gauge of the deadliest trap ever laid~{/i}"

    call Home_Depeche_Mode_Prueba1(from_long = True)

    m 5dubstda "..."

    m 5mud "{i}~The heat and the sickliest{/i}"
    extend 5eud "{i} sweet smelling sheets~{/i}"
    m 5ltd "{i}That cling to the backs of my knees{/i}"
    extend 5mtd "{/i} and my feet~{/i}"
    m 5ekc But "{i}}~I'm drowning in time{/i}"
    extend 5dkc "{i} to a desperate beat~{/i}"

    m 5dku "{i}~And I thank you~{/i}"
    m 5mkblu "{i}~for bringing me here~{/i}"
    m 5fubsd "{i}~For showing me home~{/i}"
    m 5dubstdb "{i}~For singing these tears~{/i}"
    m 5mubstdb "{i}~Finally, I've found that I belong~{/i}"
    m 5fubstpb "{i}~Feels like ho{w=0.4}me~{/i}"
    m 5mubstub "{i}~I should have kn{w=0.4}own~{/i}" 
    m 5dubstda "{i}~From my first breath{/i}"

    m 1dubsa "..."

    m 1dubso "{i}~God send the only true friend{/i}"
    extend 1dubsa "{i} I call mine~{/i}"
    m 1ltbsa "{i}~Pretend that I'll make amends"
    extend 1eubsa "{i} the next time~{/i}"
    m 1eubsb "{i}~Befriend the glorious end{/i}"
    extend 1dubsb "{i} of the line~{/i}"

    m 5hubsb "{i}~And I thank you~{/i}"
    m 5lubsa "{i}~for bringing me here~{/i}"
    m 5fubsd "{i}~For showing me home~{/i}"
    m 5dubstdb "{i}~For singing these tears~{/i}"
    m 5mubstdb "{i}~Finally, I've found that I~{/i}"
    extend 5dubstua "{i}{w=0.6} belo{w=0.2}ng here~{/i}"
    return

