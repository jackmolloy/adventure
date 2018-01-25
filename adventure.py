# Dewey's birthday
# great resource for syntax: https://stackoverflow.com/questions/1016814/what-to-do-with-unexpected-indent-in-python

print("You spent 17 hours building a confetti bomb to be detonated at a surprise birthday party for your best friend Dewey. The device was set to detonate when Dewey got home at 7PM, but Dewey is running late (typical Dewey). You open up the confetti bomb and must choose between cutting the red wire and the blue wire. Which do you choose?")
wire = input("Enter 1 for the red wire or 2 for the blue wire: ")
wire = int(wire)

if wire == 1:
    print("You take a deep breath and cut the red wire. Nothing happens. You sigh and wipe off the nervous sweat from your forehead. Now you must choose whether to recode the timer function or deploy it manually upon Dewey's arrival. Which do you choose?")
    red = input("Enter 1 to set a new timer or 2 to deploy it manually: ")
    red = int(red)

    if red == 1:
        print("You set a new timer for 8PM, because there's no way Dewey is an hour late... right? WRONG. Dewey still isn't there at 8PM, and the confetti bomb explodes. There's confetti everywhere. Do you try to sweep it up before Dewey sees or do you leave it there to make Dewey feel like the worst friend ever?")
        todo = input("Enter 1 to sweep up the confetti or 2 to leave it there and guilt-trip Dewey")
        todo = int(todo)

        if todo == 1:
            print("You sweep up the confetti just before Dewey gets home. When Dewey walks in the door, his face drops; Dewey was expecting a surprise party with lots of confetti. Dewey storms out crying. Your friendship with Dewey is ruined.")
        elif todo == 2:
            print("You leave the confetti all over the place to make Dewey feel bad. Dewey walks in and immediately starts weeping; Dewey feels terrible. Due to his extreme guilt, Dewey storms out crying. Your friendship with Dewey is ruined.")
        else:
            print("please choose either 1 or 2")



    elif red == 2:
        print("You choose to deploy the confetti bomb manually. You must decide whether to hang the device above the door or to keep it with you behind the couch. Which do you choose?")
        manual = input("Enter 1 to hang the device above the door or 2 to hold it behind the couch: ")
        manual = int(manual)

        if manual == 1:
            print("You hang the device above the door. Once Dewey walks in, you shoot the device with a BB gun and a confetti explosion happens. Dewey is covered from head to toe in confetti, and he is incredibly embarrased. You have ruined Dewey's birthday. Your friendship with Dewey is ruined.")
        elif manual == 2:
            print("You hold the confetti bomb and wait for Dewey to walk in the door. Once he enters the room, you detonate the device from behind the couch. The bomb makes a loud noise, but all of the confetti gets trapped behind the couch. Dewey thinks a real bomb just went off, so he pees himself and starts crying like a small mammal in front of all of his closest friends. Your friendship with Dewey is ruined.")
        else:
            print("please choose either 1 or 2")


    else:
        print("please choose either 1 or 2")


elif wire == 2:
    print("BOOM! Confetti flys everywhere. Your project is ruined, and you become extremely sad. You must decide whether you want to leave the party out of shame or stay and wait to see Dewey despite the mishap. Which do you choose?")
    blue = input("Enter 1 to stay at the party or 2 to leave: ")
    blue = int(blue)

    if blue == 1:
        print("You stay at the party, waiting for Dewey to show up. You must decide whether to tell him the truth about what happened or to make up a lie just to avoid the embarrasement. Which do you choose?")
        truth = input("Enter 1 to tell the truth or 2 to lie to Dewey's face: ")
        truth = int(truth)

        if truth == 1:
            print("When Dewey walks in the door, you immediately run up to him and tell him what happened. You begin tearing up while explaining the situation. Dewey asks you if you're crying, but you lie to him and say it's just allergies. Dewey hates liars. Your friendship with Dewey is ruined.")
        elif truth == 2:
            print("You make up an intricate lie about a confetti tornado ripping through Dewey's living room. Dewey knows you're lying, and Dewey hates liars. Your friendship with Dewey is ruined.")
        else:
            print("please choose either 1 or 2")



    elif blue == 2:
        print("You leave the party but must decide whether to go home or go to your favorite restaurant. Which do you choose?")
        leave = input("Enter 1 to go home or 2 to go to the restaurant: ")
        leave = int(leave)

        if leave == 1:
            print("You go home and binge watch Stranger Things on Netflix for 6 hours. You get a 'thx for showing up to my bday party' text from Dewey. The passive-aggressive remark lets you know that Dewey now hates you. Your friendship with Dewey is ruined.")
        elif leave == 2:
            print("You drive to your favorite restauant to eat your sorrows away. Upon entering the fine dining establishment, you notice your usual booth is currently occupied; you walk toward the booth to see who would dare to sit in your territory. Who is it? It's Dewey having dinner with your significant other. You feel betrayed, and tell both of them to never talk to you again. Your friendship with Dewey is ruined. And you're single now.")
        else:
            print("please choose either 1 or 2")


    else:
        print("please choose either 1 or 2")
