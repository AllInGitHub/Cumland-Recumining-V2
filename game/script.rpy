# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define snailpi = Character("SnailPi")
define mc = Character("You")

define appearDisappear = MoveTransition(0.5, enter_time_warp=_warper.easeout_quad, leave_time_warp=_warper.easein_quad)

define config.font_name_map["con"] = "consola.ttf"
define config.font_name_map["c64"] = "Commodore-64-v6.3.ttf"
define config.font_name_map["bae"] = "HakoeTimer.otf"
define config.font_name_map["ps2p"] = "PressStart2P-Regular.ttf"
define config.font_name_map["ppix"] = "PublicPixel.ttf"
define config.font_name_map["utdr"] = "8bitoperator_jve.ttf"

default money = 0

# The game starts here

label start:

    scene park outside

    show snailpi greet with appearDisappear

    snailpi "WelCUM to Cumland!"
    show snailpi smile
    snailpi "Tickets here cost $69,419.99{w}\nper person!"
    snailpi "But VIPs (Very Important People) can pay $65,535.99 and EMIPs (Even More Important People) can pay $255.99"
    snailpi "Pay up, bitch!"

    "You currently have $[money] on you"
    if money < 69420:
        extend "\nThat's not enough"
        if money < 256:
            extend ". Even for EMIPs"
        elif money < 65536:
            extend ". Even for VIPs"

        menu pay_notenough:
            "Would you like to pay anyway?"
            "Yes":
                "You pull out your wallet"
                "SnailPi checks your wallet"
                jump pay_scam
            "No":
                mc "Ah, sorry. I don't have enough money for a ticket"
                show snailpi worried
                snailpi "Ah. Well, that sucks"
                hide snailpi with appearDisappear
                jump make_money
                # jump start
    elif money == 69420:
        extend "\nThat's enough!"
    else:
        extend "\nThat's MORE than enough!"
    return

label pay_scam:
    show snailpy pissed
    "SnailPi was not happy with your broke ass"
    snailpi "OHHHHH BITCH! YOU THINK YOU CAN SCAM ME!?"
    snailpi "I have worked here for 5 years, since 2021! Don't think I don't know you!"
    "SnailPi pulls out his glock"
    mc "Oh no! Please don't shoot me! I'm just here because I wanted to make a funny little YouTube video!"
    mc "SHOW MERCY!"
    snailpi "SO WHAT!? If you're not gonna pay enough, just don't pay at all and LEAVE!"
    "SnailPi aims it at you and shoots"
    mc "Fuck. Thought I'd at least get a YouTuber pass or something"
    hide snailpi with dissolve
    "YOU DIED"
    return


label make_money:
    menu:
        "How do you want to make money? You have $[money] on you"
        "Fight whoever tries to steal your car (GTA BATCH)":
            jump gta_batch
    jump start

label gta_batch:
    # Start Ren'Py port of GTA BATCH by Enderman Dan on itch.io
    "GTA BATCH"
    menu:
        "1)begin\n2) exit\n\nResponce"
        "1":
            jump start_gta_bat
        "2":
            jump start
    jump gta_batch

default dudeHP = 100
default urHP = 100
label start_gta_bat:
    # Start gameloop of Ren'Py port of GTA BATCH by Enderman Dan on itch.io
    "Money : [money]\nYou : [urHP]\nDude : [dudeHP]"
    menu:
        "1)attack\n2)DIP\n3)TRY-HARD\n\nResponce"
        "1":
            if dudeHP > 50:
                $ dudeHP -= 7
                $ money -= 93
            elif dudeHP > 0:
                $ money -= dudeHP
                $ dudeHP -= 10
            else:
                $ dudeHP -= 16
                $ money += 256
            jump start_gta_bat
        "2":
            pass
        "3":
            pass
    jump gta_batch
