from source.header_operations import *
from source.header_common import *
from source.header_troops import *
from source.header_skills import *
from source.header_item_modifiers import *
from source.header_game_menus import mnf_disable_all_keys, menu_text_color

from source.module_constants import *


_a1_noble = "@You came into the world a {reg3?daughter:son} of declining " \
            "nobility, owning only the house in which they lived. However, " \
            "despite your family's hardships, they afforded you a good " \
            "education and trained you from childhood for the rigors of " \
            "aristocracy and life at court."

_a1_merchant = "@You were born the {reg3?daughter:son} of travelling merchants, " \
               "always moving from place to place in search of a profit. " \
               "Although your parents were wealthier than most and educated you " \
               "as well as they could, you found little opportunity to make " \
               "friends on the road, living mostly for the moments when you " \
               "could sell something to somebody."

_a1_guard = "@As a child, your family scrabbled out a meagre living from your " \
            "father's wages as a guardsman to the local lord. It was not an " \
            "easy existence, and you were too poor to get much of an education. " \
            "You learned mainly how to defend yourself on the streets, with or " \
            "without a weapon in hand."

_a1_forester = "@You were the {reg3?daughter:son} of a family who lived off " \
               "the woods, doing whatever they needed to make ends meet. " \
               "Hunting, woodcutting, making arrows, even a spot of poaching " \
               "whenever things got tight. Winter was never a good time for " \
               "your family as the cold took animals and people alike, but you " \
               "always lived to see another dawn, though your brothers and " \
               "sisters might not be so fortunate."

_a1_nomad = "@You were a child of the steppe, born to a tribe of wandering nomads who lived\
 in great camps throughout the arid grasslands.\
 Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
 how to ride almost before you learned how to walk. "

_a1_thief = "@As the {reg3?daughter:son} of a thief, you had very little 'formal' education.\
 Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
 until you learned how to pick locks, all the way through your childhood.\
 Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."

_a2_page = "@As a {reg3?girl:boy} growing out of childhood,\
 you were sent to live in the court of one of the nobles of the land.\
 There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
 But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
 and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."

_a2_apprentice = "@As a {reg3?girl:boy} growing out of childhood,\
 you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
 new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
 you wished to stay."

# the last menu of this list is the one the hard-wired creation menu points to.
menus = [##added back in by gdw
    ("start_game_1st",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Welcome, adventurer, to Brdytenwalda. Before you can start playing the game you must create a character.",
    "none",
    [(try_begin),
        (neq, "$creation_canceled", 999),
        (call_script, "script_randomize_background", 0),
        (start_presentation, "prsnt_player_background"),
     (try_end),],
    [("start",[],"Create Character",[(start_presentation, "prsnt_player_background"),]), ##this has a jump to start_game_1
     ("quit",[],"Cancel",[(change_screen_quit),]),]),  

    ("start_game_1", menu_text_color(0xFF000000) | mnf_disable_all_keys,
     "Select your character's gender.",
     "none", [],
     [
         ("start_male", [], "Male",
          [
              (troop_set_type, "trp_player", 0),
              (assign, "$character_gender", tf_male),
              (jump_to_menu, "mnu_start_character_1"),
          ]),

         ("start_female", [], "Female",
          [
              (troop_set_type, "trp_player", 1),
              (assign, "$character_gender", tf_female),
              (jump_to_menu, "mnu_start_character_1"),
          ]),

         ("go_back", [], "Go back", [(change_screen_quit)]),
     ]),

    (
    "start_character_1",mnf_disable_all_keys,
    "You were born years ago, in a land far away. Your father was...",
    "none",
    [
    (str_clear,s10),
    (str_clear,s11),
    (str_clear,s12),
    (str_clear,s13),
    (str_clear,s14),
    (str_clear,s15),
    ],
    [
    ("start_noble",[],"An impoverished noble.",[
      (assign,"$background_type",cb_noble),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@You came into the world a {reg3?daughter:son} of declining nobility,\
 owning only the house in which they lived. However, despite your family's hardships,\
 they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
    (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_merchant",[],"A travelling merchant.",[
      (assign,"$background_type",cb_merchant),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@You were born the {reg3?daughter:son} of travelling merchants,\
 always moving from place to place in search of a profit. Although your parents were wealthier than most\
 and educated you as well as they could, you found little opportunity to make friends on the road,\
 living mostly for the moments when you could sell something to somebody."),
    (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_guard",[],"A veteran warrior.",[
      (assign,"$background_type",cb_guard),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@As a child, your family scrabbled out a meagre living from your father's wages\
 as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an\
 education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
    (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_forester",[],"A hunter.",[
      (assign,"$background_type",cb_forester),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@{reg3?daughter:son}"),
      (str_store_string,s10,"@You were the {reg3?daughter:son} of a family who lived off the woods,\
 doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows,\
 even a spot of poaching whenever things got tight. Winter was never a good time for your family\
 as the cold took animals and people alike, but you always lived to see another dawn,\
 though your brothers and sisters might not be so fortunate."),
    (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_nomad",[],"A steppe nomad.",[
      (assign,"$background_type",cb_nomad),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@{reg3?daughter:son}"),
      (str_store_string,s10,"@You were a child of the steppe, born to a tribe of wandering nomads who lived\
 in great camps throughout the arid grasslands.\
 Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
 how to ride almost before you learned how to walk. "),
    (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_thief",[],"A thief.",[
      (assign,"$background_type",cb_thief),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@As the {reg3?daughter:son} of a thief, you had very little 'formal' education.\
 Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
 until you learned how to pick locks, all the way through your childhood.\
 Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
    (jump_to_menu,"mnu_start_character_2"),
    ]),
##    ("start_priest",[],"Priests.",[
##      (assign,"$background_type",cb_priest),
##      (assign, reg3, "$character_gender"),
##      (str_store_string,s10,"@A {reg3?daughter:son} that nobody wanted, you were left to the church as a baby,\
## a foundling raised by the priests and nuns to their own traditions.\
## You were only one of many other foundlings and orphans, but you nonetheless received a lot of attention\
## as well as many years of study in the church library and before the altar. They taught you many things.\
## Gradually, faith became such a part of your life that it was no different from the blood coursing through your veins."),
##  (jump_to_menu,"mnu_start_character_2"),
##    ]),
    ("go_back",[],"Go back",
     [(jump_to_menu,"mnu_start_game_1"),
    ]),
    ]
  ),
  (
    "start_character_2",0,
    "{s10}^^ You started to learn about the world almost as soon as you could walk and talk. You spent your early life as...",
    "none",
    [],
    [
      ("page",[
          ],"A page at a nobleman's court.",[
      (assign,"$background_answer_2", cb2_page),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you were sent to live in the court of one of the nobles of the land.\
 There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
 But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
 and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
    (jump_to_menu,"mnu_start_character_3"),
    ]),
      ("apprentice",[
          ],"A craftsman's apprentice.",[
      (assign,"$background_answer_2", cb2_apprentice),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
 new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
 you wished to stay."),
    (jump_to_menu,"mnu_start_character_3"),
    ]),
      ("stockboy",[
          ],"A shop assistant.",[
      (assign,"$background_answer_2",cb2_merchants_helper),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans.\
 You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd\
 got the better deal."),
    (jump_to_menu,"mnu_start_character_3"),
    ]),
      ("urchin",[
          ],"A street urchin.",[
      (assign,"$background_answer_2",cb2_urchin),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you took to the streets, doing whatever you must to survive.\
 Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
 always one step ahead of the law and those who wished you ill."),
    (jump_to_menu,"mnu_start_character_3"),
    ]),
      ("nomad",[
          ],"A steppe child.",[
      (assign,"$background_answer_2",cb2_steppe_child),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you rode the great steppes on a horse of your own, learning the ways of the grass and the desert.\
 Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country.\
 Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}."),
    (jump_to_menu,"mnu_start_character_3"),
    ]),
     ("go_back",[],"Go back.",
     [(jump_to_menu,"mnu_start_character_1"),
    ]),
    ]
  ),

  (
    "start_character_3",mnf_disable_all_keys,
    "{s11}^^ Then, as a young adult, life changed as it always does. You became...",
    "none",
    [(assign, reg3, "$character_gender"),],
    [
##      ("bravo",[],"A travelling bravo.",[
##        (assign,"$background_answer_3",1),
##      (str_store_string,s14,"@{reg3?daughter:man}"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
## You left your old life behind to travel the roads as a mercenary, a bravo, guarding caravans for coppers\
## or bashing in heads for silvers. You became a {s14} of the open road, working with bandits as often as against.\
## Going from fight to fight, you grew experienced at battle, and you learned what it was to kill."),
##  (jump_to_menu,"mnu_start_character_4"),
##        ]),
##      ("merc",[],"A sellsword in foreign lands.",[
##        (assign,"$background_answer_3",2),
##      (str_store_string,s14,"@{reg3?daughter:man}"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
## You signed on with a mercenary company and travelled far from your home. The life you found was rough and\
## ready, marching to the beat of strange drums and learning unusual ways of fighting.\
## There were men who taught you how to wield any weapon you desired, and plenty of battles to hone your skills.\
## You were one of the charmed few who survived through every campaign in which you marched."),
##  (jump_to_menu,"mnu_start_character_4"),
##        ]),

      ("squire",[(eq,"$character_gender",tf_male)],"A squire.",[
        (assign,"$background_answer_3",cb3_squire),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 When you were named squire to a noble at court, you practiced long hours with weapons,\
 learning how to deal out hard knocks and how to take them, too.\
 You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals.\
 But in addition to learning the chivalric ideal, you also learned about the less uplifting side\
 -- old warriors' stories of ruthless power politics, of betrayals and usurpations,\
 of men who used guile as well as valor to achieve their aims."),
    (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("lady",[(eq,"$character_gender",tf_female)],"A lady-in-waiting.",[
        (assign,"$background_answer_3",cb3_lady_in_waiting),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things,\
 the wives and mistresses of noble men as well as maidens who had yet to find a husband.\
 However, even here you found politics at work as the ladies schemed for prominence and fought each other\
 bitterly to catch the eye of whatever unmarried man was in fashion at court.\
 You soon learned ways of turning these situations and goings-on to your advantage. With it came the\
 realisation that you yourself could wield great influence in the world, if only you applied yourself\
 with a little bit of subtlety."),
    (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("troubadour",[],"A troubadour.",[
        (assign,"$background_answer_3",cb3_troubadour),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You set out on your own with nothing except the instrument slung over your back and your own voice.\
 It was a poor existence, with many a hungry night when people failed to appreciate your play,\
 but you managed to survive on your music alone. As the years went by you became adept at playing the\
 drunken crowds in your taverns, and even better at talking anyone out of anything you wanted."),
    (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("student",[],"A university student.",[
        (assign,"$background_answer_3",cb3_student),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 You found yourself as a student in the university of one of the great cities,\
 where you studied theology, philosophy, and medicine.\
 But not all your lessons were learned in the lecture halls.\
 You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight.\
 However, you certainly were able to observe how a broken jaw is set,\
 or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),
    (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("peddler",[],"A goods peddler.",[
        (assign,"$background_answer_3",cb3_peddler),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 Heeding the call of the open road, you travelled from village to village buying and selling what you could.\
 It was not a rich existence, but you became a master at haggling even the most miserly elders into\
 giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
    (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("craftsman",[],"A smith.",[
        (assign,"$background_answer_3", cb3_craftsman),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
 As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
 With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
    (jump_to_menu,"mnu_start_character_4"),
        ]),
      ("poacher",[],"A game poacher.",[
        (assign,"$background_answer_3", cb3_poacher),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
 and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
 the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
 firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
    (jump_to_menu,"mnu_start_character_4"),
        ]),
##      ("preacher",[],"Itinerant preacher.",[
##        (assign,"$background_answer_3",6),
##      (str_store_string,s14,"@{reg3?daughter:man}"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
## You packed your few belongings and went out into the world to spread the word of God. You preached to\
## anyone who would listen, and impressed many with the passion of your sermons. Though you had taken a vow\
## to remain in poverty through your itinerant years, you never lacked for food, drink or shelter; the\
## hospitality of the peasantry was always generous to a rising {s13} of God."),
##  (jump_to_menu,"mnu_start_character_4"),
##        ]),
      ("go_back",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_2"),
        ]
       ),
    ]
  ),
(
    "start_character_4",mnf_disable_all_keys,
    "{s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was...",
    #Finally, what made you decide to strike out on your own as an adventurer?",
    "none",
    [],
    [
      ("revenge",[],"Personal revenge.",[
        (assign,"$background_answer_4", cb4_revenge),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
 You want vengeance. You want justice. What was done to you cannot be undone,\
 and these debts can only be paid in blood..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("death",[],"The loss of a loved one.",[
        (assign,"$background_answer_4",cb4_loss),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
 painful. Perhaps your new life will let you forget,\
 or honour the name that you can no longer bear to speak..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("wanderlust",[],"Wanderlust.",[
        (assign,"$background_answer_4",cb4_wanderlust),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
 wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
 freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
##      ("fervor",[],"Religious fervor.",[
##        (assign,"$background_answer_4",4),
##      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
## Regardless, the intense faith burning in your soul would not let you find peace in any single place.\
## There were others in the world, souls to be washed in the light of God. Now you preach wherever you go,\
## seeking to bring salvation and revelation to the masses, be they faithful or pagan. They will all know the\
## glory of God by the time you're done..."),
##        (jump_to_menu,"mnu_choose_skill"),
##        ]),
      ("disown",[],"Being forced out of your home.",[
        (assign,"$background_answer_4",cb4_disown),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
 now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
     ("greed",[],"Lust for money and power.",[
        (assign,"$background_answer_4",cb4_greed),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 To everyone else, it's clear that you're now motivated solely by personal gain.\
 You want to be rich, powerful, respected, feared.\
 You want to be the one whom others hurry to obey.\
 You want people to know your name, and tremble whenever it is spoken.\
 You want everything, and you won't let anyone stop you from having it..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("go_back",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_3"),
        ]
       ),
    ]
  ),


  (
    "choose_skill",mnf_disable_all_keys,
    "{s13}", 
    "none",
    [(assign,"$current_string_reg",10),
     (assign, ":difficulty", 0),
     
     (try_begin),
        (eq, "$character_gender", tf_female),
        (str_store_string, s14, "str_woman"),
        (val_add, ":difficulty", 1),
     (else_try),    
        (str_store_string, s14, "str_man"),
     (try_end),
    
     (try_begin),
        (eq,"$background_type",cb_noble),
        (str_store_string, s15, "str_noble"),
        (val_sub, ":difficulty", 1),
     (else_try),
        (str_store_string, s15, "str_common"),
     (try_end),
     
     (try_begin),
        (eq, ":difficulty", -1),
        (str_store_string, s16, "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
     (else_try),
        (eq, ":difficulty", 0),
        (str_store_string, s16, "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
     (else_try),
        (eq, ":difficulty", 1),
        (str_store_string, s16, "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
     (try_end),
    ],
    [
##      ("start_swordsman",[],"Swordsmanship.",[
##        (assign, "$starting_skill", 1),
##        (str_store_string, s14, "@You are particularly talented at swordsmanship."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_archer",[],"Archery.",[
##        (assign, "$starting_skill", 2),
##        (str_store_string, s14, "@You are particularly talented at archery."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_medicine",[],"Medicine.",[
##        (assign, "$starting_skill", 3),
##        (str_store_string, s14, "@You are particularly talented at medicine."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),

     ("begin_adventuring", [], "Become an adventurer and ride to your destiny.",
       [
           (set_show_messages, 1),

           (call_script, "script_build_character_from_answers"),

           (try_begin),
               (eq, "$background_type", cb_noble),
               (jump_to_menu, "mnu_auto_return"),
               (start_presentation, "prsnt_banner_selection"),
           (else_try),
               (change_screen_return, 0),
           (try_end),

           (set_show_messages, 1),
       ]),

      ("go_back_dot", [], "Go back.", [(jump_to_menu, "mnu_start_character_4")]),
      ]),
]


scripts = [
    ('build_character_from_answers', [
        (try_begin),
            (eq, "$character_gender", 0),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
        (else_try),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
        (try_end),

        (troop_raise_attribute, "trp_player", ca_strength, 1),
        (troop_raise_attribute, "trp_player", ca_agility, 1),
        (troop_raise_attribute, "trp_player", ca_charisma, 1),

        (troop_raise_skill, "trp_player", "skl_leadership", 1),
        (troop_raise_skill, "trp_player", "skl_riding", 1),

        (try_begin),
            (eq, "$background_type", cb_noble),
            (eq, "$character_gender", tf_male),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 2),
            (troop_raise_skill, "trp_player", skl_weapon_master, 1),
            (troop_raise_skill, "trp_player", skl_power_strike, 1),
            (troop_raise_skill, "trp_player", skl_riding, 1),
            (troop_raise_skill, "trp_player", skl_tactics, 1),
            (troop_raise_skill, "trp_player", skl_leadership, 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 10),

            (troop_add_item, "trp_player", "itm_crude_shield", imod_battered),
            (troop_set_slot, "trp_player", "slot_troop_renown", 100),
            (call_script, "script_change_player_honor", 3),

            (troop_add_gold, "trp_player", 100),
        (else_try),
            (eq, "$background_type", cb_noble),
            (eq, "$character_gender", tf_female),
            (troop_raise_attribute, "trp_player", ca_intelligence, 2),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_skill, "trp_player", skl_wound_treatment, 1),
            (troop_raise_skill, "trp_player", skl_riding, 2),
            (troop_raise_skill, "trp_player", skl_first_aid, 1),
            (troop_raise_skill, "trp_player", skl_leadership, 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),

            (troop_set_slot, "trp_player", "slot_troop_renown", 50),
            (troop_add_item, "trp_player", "itm_crude_shield", imod_battered),

            (troop_add_gold, "trp_player", 100),
        (else_try),
            (eq, "$background_type", cb_merchant),
            (troop_raise_attribute, "trp_player", ca_intelligence, 2),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_skill, "trp_player", skl_riding, 1),
            (troop_raise_skill, "trp_player", skl_leadership, 1),
            (troop_raise_skill, "trp_player", skl_trade, 2),
            (troop_raise_skill, "trp_player", skl_inventory_management, 1),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
            (troop_add_gold, "trp_player", 250),
            (troop_set_slot, "trp_player", "slot_troop_renown", 20),
        (else_try),
            (eq, "$background_type", cb_guard),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_skill, "trp_player", "skl_ironflesh", 1),
            (troop_raise_skill, "trp_player", "skl_power_strike", 1),
            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_leadership", 1),
            (troop_raise_skill, "trp_player", "skl_trainer", 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 15),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 20),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 10),
            (troop_add_item, "trp_player", "itm_cantabro_shield3", imod_battered),
            (troop_add_gold, "trp_player", 50),
            (troop_set_slot, "trp_player", "slot_troop_renown", 10),
        (else_try),
            (eq, "$background_type", cb_forester),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 2),
            (troop_raise_skill, "trp_player", "skl_power_draw", 1),
            (troop_raise_skill, "trp_player", "skl_tracking", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
            (troop_raise_skill, "trp_player", "skl_spotting", 1),
            (troop_raise_skill, "trp_player", "skl_athletics", 1),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_archery, 30),
            (troop_add_gold, "trp_player", 30),
        (else_try),
            (eq, "$background_type", cb_nomad),
            (eq, "$character_gender", tf_male),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_power_draw", 1),
            (troop_raise_skill, "trp_player", "skl_horse_archery", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
            (troop_raise_skill, "trp_player", "skl_riding", 2),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_archery, 30),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 10),
            (troop_add_item, "trp_player", "itm_shield_caledonian8", imod_battered),
            (troop_add_gold, "trp_player", 15),
            (troop_set_slot, "trp_player", "slot_troop_renown", 10),
        (else_try),
            (eq, "$background_type", cb_nomad),
            (eq, "$character_gender", tf_female),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
            (troop_raise_skill, "trp_player", "skl_first_aid", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
            (troop_raise_skill, "trp_player", "skl_riding", 2),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 5),
            (troop_raise_proficiency, "trp_player", wpt_archery, 20),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 5),
            (troop_add_item, "trp_player", "itm_shield_caledonian8", imod_battered),
            (troop_add_gold, "trp_player", 20),
        (else_try),
            (eq, "$background_type", cb_thief),
            (troop_raise_attribute, "trp_player", ca_agility, 3),
            (troop_raise_skill, "trp_player", "skl_athletics", 2),
            (troop_raise_skill, "trp_player", "skl_power_throw", 1),
            (troop_raise_skill, "trp_player", "skl_inventory_management", 1),
            (troop_raise_skill, "trp_player", "skl_looting", 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 20),
            (troop_add_item, "trp_player", "itm_wooden_javelins", 0),
            (troop_add_gold, "trp_player", 25),
        (try_end),

        (try_begin),
            (eq, "$background_answer_2", cb2_page),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_skill, "trp_player", "skl_power_strike", 1),
            (troop_raise_skill, "trp_player", "skl_persuasion", 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 5),
        (else_try),
            (eq, "$background_answer_2", cb2_apprentice),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_skill, "trp_player", "skl_engineer", 1),
            (troop_raise_skill, "trp_player", "skl_trade", 1),
        (else_try),
            (eq, "$background_answer_2", cb2_urchin),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_spotting", 1),
            (troop_raise_skill, "trp_player", "skl_looting", 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 5),
        (else_try),
            (eq, "$background_answer_2", cb2_steppe_child),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_skill, "trp_player", "skl_horse_archery", 1),
            (troop_raise_skill, "trp_player", "skl_power_throw", 1),
            (troop_raise_proficiency, "trp_player", wpt_archery, 15),
            (call_script, "script_change_troop_renown", "trp_player", 5),
        (else_try),
            (eq, "$background_answer_2", cb2_merchants_helper),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_skill, "trp_player", "skl_inventory_management", 1),
            (troop_raise_skill, "trp_player", "skl_trade", 1),
        (try_end),

        (try_begin),
            (eq, "$background_answer_3", cb3_poacher),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_skill, "trp_player", "skl_power_draw", 1),
            (troop_raise_skill, "trp_player", "skl_tracking", 1),
            (troop_raise_skill, "trp_player", "skl_spotting", 1),
            (troop_raise_skill, "trp_player", "skl_athletics", 1),
            (troop_add_gold, "trp_player", 10),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 10),
            (troop_raise_proficiency, "trp_player", wpt_archery, 35),

            (troop_add_item, "trp_player", "itm_axe_englet2", imod_chipped),
            (troop_add_item, "trp_player", "itm_rawhide_vest_green", 0),
            (troop_add_item, "trp_player", "itm_shoes1blue", 0),
            (troop_add_item, "trp_player", "itm_huntingbow", 0),
            (troop_add_item, "trp_player", "itm_barbed_arrows", 0),
            (troop_add_item, "trp_player", "itm_pony_horse", imod_heavy),
            (troop_add_item, "trp_player", "itm_dried_meat", 0),
            (troop_add_item, "trp_player", "itm_dried_meat", 0),
            (troop_add_item, "trp_player", "itm_furs", 0),
            (troop_add_item, "trp_player", "itm_furs", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_craftsman),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),

            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_engineer", 1),
            (troop_raise_skill, "trp_player", "skl_tactics", 1),
            (troop_raise_skill, "trp_player", "skl_trade", 1),

            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
            (troop_add_gold, "trp_player", 100),

            (troop_add_item, "trp_player", "itm_leather_boots1", imod_ragged),
            (troop_add_item, "trp_player", "itm_merch_tunicwt", 0),

            (troop_add_item, "trp_player", "itm_espada_historic1", imod_balanced),
            (troop_add_item, "trp_player", "itm_shortbow", 0),
            (troop_add_item, "trp_player", "itm_arrows1", 0),

            (troop_add_item, "trp_player", "itm_tools", 0),
            (troop_add_item, "trp_player", "itm_frankishhorse1", 0),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_peddler),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_riding", 1),
            (troop_raise_skill, "trp_player", "skl_trade", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
            (troop_raise_skill, "trp_player", "skl_inventory_management", 1),

            (troop_add_item, "trp_player", "itm_leather_gloves1", imod_plain),
            (troop_add_gold, "trp_player", 90),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 15),

            (troop_add_item, "trp_player", "itm_gaelic_jacketgray", 0),
            (troop_add_item, "trp_player", "itm_leather_boots1", imod_ragged),
            (troop_add_item, "trp_player", "itm_dena_helmgoat", 0),
            (troop_add_item, "trp_player", "itm_staff1", 0),
            (troop_add_item, "trp_player", "itm_shortbow", 0),
            (troop_add_item, "trp_player", "itm_arrows1", 0),
            (troop_add_item, "trp_player", "itm_frankishhorse1", 0),
            (troop_add_item, "trp_player", "itm_pony_horse", 0),

            (troop_add_item, "trp_player", "itm_linen", 0),
            (troop_add_item, "trp_player", "itm_pottery", 0),
            (troop_add_item, "trp_player", "itm_wool", 0),
            (troop_add_item, "trp_player", "itm_wool", 0),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_troubadour),
            (troop_raise_attribute, "trp_player", ca_charisma, 2),

            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_persuasion", 1),
            (troop_raise_skill, "trp_player", "skl_leadership", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),

            (troop_add_gold, "trp_player", 80),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 25),
            (troop_raise_proficiency, "trp_player", wpt_crossbow, 10),

            (troop_add_item, "trp_player", "itm_bluepantsbody_woad04", imod_sturdy),
            (troop_add_item, "trp_player", "itm_leather_boots1", imod_ragged),
            (troop_add_item, "trp_player", "itm_espada_historic1", imod_rusty),
            (troop_add_item, "trp_player", "itm_shortbow", 0),
            (troop_add_item, "trp_player", "itm_arrows1", 0),
            (troop_add_item, "trp_player", "itm_frankishhorse1", imod_swaybacked),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),

        (else_try),
            (eq, "$background_answer_3", cb3_squire),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_skill, "trp_player", "skl_riding", 1),
            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_power_strike", 1),
            (troop_raise_skill, "trp_player", "skl_leadership", 1),

            (troop_add_gold, "trp_player", 20),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 30),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 30),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 30),
            (troop_raise_proficiency, "trp_player", wpt_archery, 10),
            (troop_raise_proficiency, "trp_player", wpt_crossbow, 10),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 10),

            (troop_add_item, "trp_player", "itm_leather_tunic1", imod_ragged),
            (troop_add_item, "trp_player", "itm_leather_boots1", imod_tattered),

            (troop_add_item, "trp_player", "itm_espada_historic1", imod_rusty),
            (troop_add_item, "trp_player", "itm_shortbow", 0),
            (troop_add_item, "trp_player", "itm_arrows1", 0),
            (troop_add_item, "trp_player", "itm_frankishhorse1", imod_swaybacked),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_lady_in_waiting),
            (eq, "$character_gender", tf_female),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),

            (troop_raise_skill, "trp_player", "skl_persuasion", 2),
            (troop_raise_skill, "trp_player", "skl_riding", 1),
            (troop_raise_skill, "trp_player", "skl_wound_treatment", 1),

            (troop_add_item, "trp_player", "itm_seaxt3", 0),
            (troop_add_item, "trp_player", "itm_shortbow", 0),
            (troop_add_item, "trp_player", "itm_arrows1", 0),
            (troop_add_item, "trp_player", "itm_horsecourser2", imod_spirited),
            (troop_add_item, "trp_player", "itm_ptunic11", imod_sturdy),
            (troop_add_item, "trp_player", "itm_woolen_dressplain", imod_sturdy),
            (troop_add_gold, "trp_player", 100),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_crossbow, 15),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_student),
            (troop_raise_attribute, "trp_player", ca_intelligence, 2),

            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_surgery", 1),
            (troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
            (troop_raise_skill, "trp_player", "skl_persuasion", 1),

            (troop_add_gold, "trp_player", 80),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),
            (troop_raise_proficiency, "trp_player", wpt_crossbow, 20),

            (troop_add_item, "trp_player", "itm_ptunic3", imod_sturdy),
            (troop_add_item, "trp_player", "itm_shoes1blue", 0),
            (troop_add_item, "trp_player", "itm_espada_historic1", imod_rusty),
            (troop_add_item, "trp_player", "itm_shortbow", 0),
            (troop_add_item, "trp_player", "itm_arrows1", 0),
            (troop_add_item, "trp_player", "itm_frankishhorse1", imod_swaybacked),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
            (store_random_in_range, ":book_no", books_begin, books_end),
            (troop_add_item, "trp_player", ":book_no", 0),
        (try_end),

        (try_begin),
            (eq, "$background_answer_4", cb4_revenge),
            (troop_raise_attribute, "trp_player", ca_strength, 2),
            (troop_raise_skill, "trp_player", "skl_power_strike", 1),
        (else_try),
            (eq, "$background_answer_4", cb4_loss),
            (troop_raise_attribute, "trp_player", ca_charisma, 2),
            (troop_raise_skill, "trp_player", "skl_ironflesh", 1),
        (else_try),
            (eq, "$background_answer_4", cb4_wanderlust),
            (troop_raise_attribute, "trp_player", ca_agility, 2),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
        (else_try),
            (eq, "$background_answer_4", cb4_disown),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
        (else_try),
            (eq, "$background_answer_4", cb4_greed),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_looting", 1),
        (try_end),
    ]),
("update_strings",
 [(store_add, ":str_pointer", "$character_nationality", nationality_init),
  (str_store_string, s12, ":str_pointer"),
  (store_add, ":str_pointer", "$background_parent", parent_init),
  (str_store_string, s13, ":str_pointer"),
  (store_add, ":str_pointer", "$background_childhood", childhood_init),
  (str_store_string, s14, ":str_pointer"),
  (store_add, ":str_pointer", "$background_job", job_init),
  (str_store_string, s15, ":str_pointer"),
  (store_add, ":str_pointer", "$background_reason", reason_init),
  (str_store_string, s16, ":str_pointer"),
  (store_add, ":str_pointer", "$background_religion", religion_init),
  (str_store_string, s17, ":str_pointer"),
  (str_clear, s18),
  (store_add, ":str_pointer", "$character_nationality", story_nationality_init),
  (str_store_string, s1, ":str_pointer"),
  (str_store_string, s18, "str_story_all"),
  (store_add, ":str_pointer", "$background_parent", story_parent_init),
  (str_store_string, s1, ":str_pointer"),
  (str_store_string, s18, "str_story_all"),
  (store_add, ":str_pointer", "$background_childhood", story_childhood_init),
  (str_store_string, s1, ":str_pointer"),
  (str_store_string, s18, "str_story_all"),
  (store_add, ":str_pointer", "$background_job", story_job_init),
  (str_store_string, s1, ":str_pointer"),
  (str_store_string, s18, "str_story_all"),
  (store_add, ":str_pointer", "$background_reason", story_reason_init),
  (str_store_string, s1, ":str_pointer"),
  (str_store_string, s18, "str_story_all"),
  (store_add, ":str_pointer", "$background_religion", story_religion_init),
  (str_store_string, s1, ":str_pointer"),
  (str_store_string, s18, "str_story_all"),
  (overlay_set_text, "$g_presentation_obj_11", "str_gender_value"),
  (overlay_set_text, "$g_presentation_obj_12", "str_nationality_value"),
  (overlay_set_text, "$g_presentation_obj_13", "str_parent_value"),
  (overlay_set_text, "$g_presentation_obj_14", "str_childhood_value"),
  (overlay_set_text, "$g_presentation_obj_15", "str_jobs_value"),
  (overlay_set_text, "$g_presentation_obj_16", "str_reason_value"),
  (overlay_set_text, "$g_presentation_obj_17", "str_religion_value"),
  (overlay_set_text, "$g_presentation_obj_8", "str_story"),]),

("init_char_stat",
 [(set_show_messages, 1),#gdw
  # Gender     
  (try_begin),
     (eq,"$character_gender", tf_male),
     (troop_raise_attribute, player,ca_strength,1),
           (assign,"$wound_type",0), # 0-8 (0=not wounded, 1-8=type of wound) chief
           (assign,"$heal_day",0),   # day that wound heals chief
  (else_try),
     (eq,"$character_gender", tf_female), 
     (troop_raise_attribute, player,ca_charisma,1),
           (assign,"$wound_type",0), # 0-8 (0=not wounded, 1-8=type of wound) chief
           (assign,"$heal_day",0),   # day that wound heals chief
 (try_end),
##  (troop_raise_attribute, player,ca_strength,1),
##  (troop_raise_attribute, player,ca_agility,1),
##  (troop_raise_attribute, player,ca_charisma,1),
##     (troop_raise_attribute, player,ca_intelligence,1),
##  (troop_raise_skill, player,skl_inventory_management,1),
  ## Commented Parts : Only for my Mod
  ## Nationality
  (assign, ":char_type", "$character_gender"),
###para alturas chief
  (try_begin),
  (this_or_next|eq, "$character_nationality", 2),
  (this_or_next|eq, "$character_nationality", 5),
  (this_or_next|eq, "$character_nationality", 8),
  (this_or_next|eq, "$character_nationality", 11),
  (this_or_next|eq, "$character_nationality", 14),
  (this_or_next|eq, "$character_nationality", 17),
  (this_or_next|eq, "$character_nationality", 20),
  (eq, "$character_nationality", 23),
  (try_begin),
     (eq,"$character_gender", tf_male),
     (val_or, ":char_type", tf_alto),
(troop_raise_attribute, player,ca_strength,2), #F123 - Submod -> 1.41 (Going to quicktag a lot of this, TML left these uncommented.)
  (else_try),
     (eq,"$character_gender", tf_female),
     (val_or, ":char_type", tf_alta),  
 (troop_raise_attribute, player,ca_strength,2), #F123 (All signed comments are Submod -> 1.41)
  (else_try),
     (val_or, ":char_type", tf_alto),
  (try_end),
  (else_try),
  (this_or_next|eq, "$character_nationality", 3),
  (this_or_next|eq, "$character_nationality", 6),
  (this_or_next|eq, "$character_nationality", 9),
  (this_or_next|eq, "$character_nationality", 12),
  (this_or_next|eq, "$character_nationality", 15),
  (this_or_next|eq, "$character_nationality", 18),
  (this_or_next|eq, "$character_nationality", 21),
  (eq, "$character_nationality", 24),
  (try_begin),
     (eq,"$character_gender", tf_male),
     (val_or, ":char_type", tf_bajo),
  (troop_raise_attribute, player,ca_charisma,2),#gdw2agility f removed agilityskill
  (else_try),
     (eq,"$character_gender", tf_female),
     (val_or, ":char_type", tf_baja),
  (troop_raise_attribute, player,ca_charisma,2),#gdw2agility f removed agilityskill
  (else_try),
     (val_or, ":char_type", tf_bajo),
  (try_end),
(else_try), #F123
  (troop_raise_attribute, player,ca_charisma,1), #gdw from  1 byF123
  (troop_raise_attribute, player,ca_strength,1), #F123
  (try_end),
  (store_add, ":slot", ":char_type", slot_item_normal_male),
  (troop_set_type, player, ":char_type"),
  (troop_set_slot, player, slot_troop_gender, ":slot"),
###chief anadido para alturas
####hister empieza chief
  # Parent:
  (try_begin),
     (eq,"$background_parent",1),     #Lesser Lord (Noble)
     (eq,"$character_gender",tf_male),
     (troop_set_slot, player, slot_troop_renown, 70),   
  (else_try),
     (eq,"$background_parent",1),    #Lesser Lord (Noble)
     (eq,"$character_gender",tf_female),
     (troop_set_slot, player, slot_troop_renown, 60),
  (else_try),
     (eq,"$background_parent",2),   #Merchant
     (troop_set_slot, player, slot_troop_renown, 30),
  (else_try),
     (eq,"$background_parent",3),   #Retinue
     (troop_set_slot, player, slot_troop_renown, 40),
  (else_try),
     (eq,"$background_parent",4),    #Outlaw
     (troop_set_slot, player, slot_troop_renown, 5),
#     (call_script, "script_change_player_honor", -40),   
  (else_try),
     (eq,"$background_parent",5),   # Unfree Peasant (Serf)
     (troop_set_slot, player, slot_troop_renown, 1),
  (else_try),
     (eq,"$background_parent",6),   #Slave
     (troop_set_slot, player, slot_troop_renown, 1),
#     (troop_set_slot, player, slot_troop_renown, -20),   
  (else_try),
     (eq,"$background_parent",7),   #Free Peasant
     (troop_set_slot, player, slot_troop_renown, 10),
  (try_end),
  # Childhood
  (try_begin),
     (eq,"$background_childhood",1),  #Brought Up In a Noble Court ; STATS DONE
     (eq,"$character_gender",tf_male),
     (troop_raise_attribute, player,ca_strength,2),
     (troop_raise_attribute, player,ca_charisma,2),
##     (troop_raise_skill, player,skl_athletics,1),   
##     (troop_raise_skill, player,skl_leadership,2),
##     (troop_raise_skill, player,skl_trainer,1),   
##     (troop_raise_skill, player,skl_riding,2),   
##     (troop_raise_skill, player,skl_weapon_master,2),
##     (troop_raise_skill, player,skl_power_strike,1),
##     (troop_raise_skill, player,skl_power_throw,1),
##     (troop_raise_skill, player,skl_shield,2),
##     (troop_raise_skill, player,skl_spotting,2),
##     (troop_raise_skill, player,skl_entertain,1),
##     (troop_raise_skill, player,skl_tactics,2),   
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,30),
##     (troop_raise_proficiency, player,wpt_two_handed_weapon,15),
##     (troop_raise_proficiency, player,wpt_polearm,25),
##     (troop_raise_proficiency, player,wpt_throwing,20),   
##  (call_script,"script_change_troop_renown", player, 20),
  (else_try),
     (eq,"$background_childhood",1),  #Brought Up In a Noble Court ; STATS DONE
     (eq,"$character_gender",tf_female),   
     (troop_raise_attribute, player,ca_charisma,2),
     (troop_raise_attribute, player,ca_intelligence,2),     
  #   (troop_raise_attribute, player,ca_agility,1),
##     (troop_raise_skill, player,skl_persuasion,1),   
##     (troop_raise_skill, player,skl_leadership,1),
##     (troop_raise_skill, player,skl_riding,2),   
##     (troop_raise_skill, player,skl_weapon_master,1),   
##     (troop_raise_skill, player,skl_first_aid,1),
##     (troop_raise_skill, player,skl_entertain,1),   
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,15),
##     (troop_raise_proficiency, player,wpt_two_handed_weapon,5),
##     (troop_raise_proficiency, player,wpt_polearm,15),
##     (troop_raise_proficiency, player,wpt_throwing,5),   
##  (call_script,"script_change_troop_renown", player, 15),
  (else_try),
     (eq,"$background_childhood",2),   #Blacksmith's Apprentice ; STATS DONE
     (troop_raise_attribute, player,ca_strength,3),
     (troop_raise_attribute, player,ca_intelligence,1),     
##     (troop_raise_skill, player,skl_ironflesh,2),   
##     (troop_raise_skill, player,skl_power_strike,2),
##     (troop_raise_skill, player,skl_weapon_master,1),
##     (troop_raise_skill, player,skl_trade,1),   
##     (troop_raise_skill, player,skl_persuasion,1),   
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,20),   
##     (troop_raise_proficiency, player,wpt_two_handed_weapon,15),
##     (troop_raise_proficiency, player,wpt_polearm,10),   
   (else_try),
     (eq,"$background_childhood",3),   #Merchant's Apprentice/Market Seller ; STATS DONE
     (troop_raise_attribute, player,ca_charisma,1),
     (troop_raise_attribute, player,ca_intelligence,3),     
##     (troop_raise_skill, player,skl_inventory_management,1),
##     (troop_raise_skill, player,skl_persuasion,2),
##     (troop_raise_skill, player,skl_trade,2),
##     (troop_raise_skill, player,skl_pathfinding,2),
##     (troop_raise_skill, player,skl_riding,1),
##     (troop_raise_proficiency, player,wpt_polearm,20),
  (else_try),
     (eq,"$background_childhood",4),  #Street Urchin ; STATS DONE
     (troop_raise_attribute, player,ca_strength,2),   
     (troop_raise_attribute, player,ca_intelligence,2),   
##     (troop_raise_skill, player,skl_ironflesh,2),
##     (troop_raise_skill, player,skl_power_throw,2),   
##     (troop_raise_skill, player,skl_athletics,2),
##     (troop_raise_skill, player,skl_foraging,3),   
##     (troop_raise_skill, player,skl_looting,2),
##     (troop_raise_skill, player,skl_persuasion,1),
##     (troop_raise_skill, player,skl_entertain,1),   
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,15),
##     (troop_raise_proficiency, player,wpt_throwing,25),
##     (call_script, "script_change_player_honor", -10),   
  (else_try),
     (eq,"$background_childhood",5),   #Cottager ; STATS DONE
     (eq,"$character_gender",tf_male),   
     (troop_raise_attribute, player,ca_strength,2),
     (troop_raise_attribute, player,ca_intelligence,2),   
##     (troop_raise_skill, player,skl_athletics,1),
##     (troop_raise_skill, player,skl_foraging,2),   
##     (troop_raise_skill, player,skl_power_draw,1),
##     (troop_raise_skill, player,skl_power_throw,1),
##     (troop_raise_skill, player,skl_shield,1),
##     (troop_raise_skill, player,skl_ironflesh,2),
##     (troop_raise_skill, player,skl_pathfinding,1),
##     (troop_raise_skill, player,skl_spotting,1),
##     (troop_raise_skill, player,skl_tracking,1),   
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,10),
##     (troop_raise_proficiency, player,wpt_polearm,20),
##     (troop_raise_proficiency, player,wpt_archery,15),
##     (troop_raise_proficiency, player,wpt_throwing,20),   
  (else_try),
     (eq,"$background_childhood",5),   #Cottager ; STATS DONE
     (eq,"$character_gender",tf_female),   
     (troop_raise_attribute, player,ca_strength,2),
     (troop_raise_attribute, player,ca_charisma,2),   
##     (troop_raise_skill, player,skl_foraging,1),   
##     (troop_raise_skill, player,skl_first_aid,1),
##     (troop_raise_skill, player,skl_wound_treatment,1),   
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,5),
##     (troop_raise_proficiency, player,wpt_polearm,20),
  (else_try),
     (eq,"$background_childhood",6),    #Slave ; STATS DONE
     (troop_raise_attribute, player,ca_strength,2),   
     (troop_raise_attribute, player,ca_intelligence,1),   
     (troop_raise_attribute, player,ca_charisma,1),
##     (troop_raise_skill, player,skl_ironflesh,3),
##     (troop_raise_skill, player,skl_athletics,2),
##     (troop_raise_skill, player,skl_looting,1),
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,20),
##     (troop_raise_proficiency, player,wpt_polearm,15),
##     (call_script,"script_change_troop_renown", player, -20),
  (else_try),
     (eq,"$background_childhood",7),    #Bard's Apprentice ; STATS DONE 
     (troop_raise_attribute, player,ca_charisma,3),
     (troop_raise_attribute, player,ca_intelligence,1),   
##     (troop_raise_skill, player,skl_athletics,1),
##     (troop_raise_skill, player,skl_persuasion,1),
##     (troop_raise_skill, player,skl_entertain,2),
##     (troop_raise_skill, player,skl_pathfinding,2),   
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,10),
##     (troop_raise_proficiency, player,wpt_two_handed_weapon,5),   
##     (troop_raise_proficiency, player,wpt_polearm,10),
##      (troop_raise_proficiency, player,wpt_throwing,20),
##     (troop_raise_proficiency, player,wpt_archery,10),
##     (call_script,"script_change_troop_renown", player, 10),
  (else_try),
     (eq,"$background_childhood",8),    #Retainer's Apprentice ; STATS DONE
     (eq,"$character_gender",tf_male),   
     (troop_raise_attribute, player,ca_strength,2),
     (troop_raise_attribute, player,ca_charisma,2),
##     (troop_raise_skill, player,skl_weapon_master,2),
##     (troop_raise_skill, player,skl_power_strike,2),
##     (troop_raise_skill, player,skl_power_throw,2),
##     (troop_raise_skill, player,skl_shield,1),
##     (troop_raise_skill, player,skl_athletics,1),
##     (troop_raise_skill, player,skl_trainer,2),
##     (troop_raise_skill, player,skl_looting,2),
##     (troop_raise_skill, player,skl_tactics,1),   
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,25),
##     (troop_raise_proficiency, player,wpt_two_handed_weapon,15),
##     (troop_raise_proficiency, player,wpt_polearm,30),
##     (troop_raise_proficiency, player,wpt_throwing,20),
##     (call_script,"script_change_troop_renown", player, 15),
  (else_try),
     (eq,"$background_childhood",8),    #Retainer's Apprentice ; STATS DONE
     (eq,"$character_gender",tf_female),   
     (troop_raise_attribute, player,ca_strength,2),
     (troop_raise_attribute, player,ca_charisma,2),
##     (troop_raise_skill, player,skl_weapon_master,2),
##     (troop_raise_skill, player,skl_power_strike,2),
##     (troop_raise_skill, player,skl_power_throw,2),
##     (troop_raise_skill, player,skl_shield,1),
##     (troop_raise_skill, player,skl_athletics,1),
##     (troop_raise_skill, player,skl_trainer,2),
##     (troop_raise_skill, player,skl_looting,2),
##     (troop_raise_skill, player,skl_tactics,1),     
##     (troop_raise_proficiency, player,wpt_one_handed_weapon,25),
##     (troop_raise_proficiency, player,wpt_two_handed_weapon,15),
##     (troop_raise_proficiency, player,wpt_polearm,30),
##     (troop_raise_proficiency, player,wpt_throwing,20),
##     (call_script,"script_change_troop_renown", player, 25),
  (else_try),
     (eq,"$background_childhood",9),   #Cleric Acolyte ; STATS DONE
    # (troop_raise_attribute, player,ca_strength,1),   
     (troop_raise_attribute, player,ca_intelligence,2),
     (troop_raise_attribute, player,ca_charisma,2),
##     (troop_raise_skill, player,skl_wound_treatment,2),
##     (troop_raise_skill, player,skl_surgery,1),
##     (troop_raise_skill, player,skl_first_aid,2),   
##     (troop_raise_proficiency, player,wpt_polearm,10),
##     (troop_raise_proficiency, player,wpt_throwing,15),
  (assign, "$sabe_leer", 1),
  (call_script,"script_change_troop_renown", player, 15),
  (call_script, "script_change_player_honor", 30),   
  (try_end),
  # Job
  (try_begin),
     (eq,"$background_job",1),    #Lesser Lord ; STATS DONE
     (eq,"$character_gender",tf_male),
#     (troop_raise_attribute, player,ca_strength, -4),
#    (troop_raise_attribute, player,ca_charisma, -4),
#     (troop_raise_attribute, player,ca_agility, -4),
#     (troop_raise_attribute, player,ca_intelligence, -4),   
#     (troop_raise_attribute, player,ca_strength,3),
#     (troop_raise_attribute, player,ca_charisma,2),
#     (troop_raise_attribute, player,ca_agility,3),
     (troop_raise_skill, player,skl_athletics,2),   
     (troop_raise_skill, player,skl_leadership,3),
     (troop_raise_skill, player,skl_trainer,2),   
     (troop_raise_skill, player,skl_riding,1),   
     (troop_raise_skill, player,skl_weapon_master,2),
     (troop_raise_skill, player,skl_power_strike,2),
     (troop_raise_skill, player,skl_power_throw,2),
     (troop_raise_skill, player,skl_shield,2),
     (troop_raise_skill, player,skl_spotting,2),
     (troop_raise_skill, player,skl_tactics,2),       
     (troop_raise_proficiency, player,wpt_one_handed_weapon,30),
     (troop_raise_proficiency, player,wpt_two_handed_weapon,25),
     (troop_raise_proficiency, player,wpt_polearm,25),
     (troop_raise_proficiency, player,wpt_throwing,10),   
     (troop_add_item, player,"itm_shoes2grey",0),
     (troop_add_item, player,"itm_ptunic3",0),
     (troop_add_item, player,"itm_banner_round_shield_ironrim",imod_battered),
     (troop_add_item, player,"itm_spear_hasta",imod_cracked),
     (troop_add_item, player,"itm_frankishhorse1",imod_swaybacked),
     (troop_add_item, player,"itm_talak_seaxkni",0),
     (troop_add_item, player,"itm_bread",0),
     (troop_add_item, player,"itm_dried_meat",0),
  (call_script,"script_change_troop_renown", player, 25),   
     (troop_add_gold, player, 100),   
  (else_try),
     (eq,"$background_job",1),  #Wife to a Lesser Lord ; STATS DONE
     (eq,"$character_gender",tf_female), 
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),
##     (troop_raise_attribute, player,ca_strength,1),   
##     (troop_raise_attribute, player,ca_charisma,3),
##     (troop_raise_attribute, player,ca_agility,1),
     (troop_raise_skill, player,skl_athletics,2),   
     (troop_raise_skill, player,skl_persuasion,3),   
     (troop_raise_skill, player,skl_leadership,2),
     (troop_raise_skill, player,skl_riding,2),   
     (troop_raise_skill, player,skl_weapon_master,1),
     (troop_raise_skill, player,skl_power_strike,1),
     (troop_raise_skill, player,skl_power_throw,1),
     (troop_raise_skill, player,skl_spotting,1),
     (troop_raise_skill, player,skl_shield,1),
     (troop_raise_skill, player,skl_first_aid,3),
     (troop_raise_skill, player,skl_entertain,3),   
     (troop_raise_proficiency, player,wpt_one_handed_weapon,15),
     (troop_raise_proficiency, player,wpt_two_handed_weapon,5),
     (troop_raise_proficiency, player,wpt_polearm,10),
     (troop_raise_proficiency, player,wpt_throwing,5),   
     (troop_add_item, player,"itm_noble_shoesorange",0), #chief cambiado
     (troop_add_item, player,"itm_banner_round_shield_ironrim",imod_battered), #chief cambiado
     (troop_add_item, player,"itm_wimple_with_veil",imod_thick),
     (troop_add_item, player,"itm_court_dress",imod_thick),
     (troop_add_item, player,"itm_spear_britonshortt2",imod_cracked),
     (troop_add_item, player,"itm_ornate_seaxt3",0),
     (troop_add_item, player,"itm_javelins", imod_bent),
     (troop_add_item, player,"itm_frankishhorse1",imod_swaybacked),
     (troop_add_item, player,"itm_talak_seaxkni",0),
     (troop_add_item, player,"itm_bread",0),
     (troop_add_item, player,"itm_dried_meat",0),
  (call_script,"script_change_troop_renown", player, 15),   
     (troop_add_gold, player, 265),   
  (else_try),
     (eq,"$background_job",2),    #Slave ; STATS DONE
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),   
##     (troop_raise_attribute, player,ca_strength,4),   
##     (troop_raise_attribute, player,ca_agility,4),
     (troop_raise_skill, player,skl_ironflesh,5),
     (troop_raise_skill, player,skl_athletics,4),
     (troop_raise_skill, player,skl_foraging,4), #F123  
     (troop_raise_skill, player,skl_spotting,2),
     (troop_raise_skill, player,skl_entertain,1),
     (troop_raise_skill, player,skl_looting,2),#F123
     (troop_raise_skill, player,skl_first_aid,2),
     (troop_raise_proficiency, player,wpt_one_handed_weapon,10),
     (troop_raise_proficiency, player,wpt_polearm,15),
     (troop_raise_proficiency, player,wpt_throwing,15),   
     (troop_add_item, player,"itm_cheap_shoes",imod_ragged),
     (troop_add_item, player,"itm_ptunic13",0),
     (troop_add_item, player,"itm_knifechp",0),   
     (troop_add_item, player,"itm_staff1",imod_bent),
     (troop_add_item, player,"itm_basic_sling", 0),
     (troop_add_item, player,"itm_slingrocks", 0),
     (troop_add_item, player,"itm_bread",0),
#  (call_script,"script_change_troop_renown", player, -40),
     (troop_add_gold, player, 10),
  (else_try),
     (eq,"$background_job",3),   #Lesser Lord's Retainer ; STATS DONE   
     (eq,"$character_gender",tf_male),
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),   
##     (troop_raise_attribute, player,ca_strength,4),
##     (troop_raise_attribute, player,ca_agility,3),
     (troop_raise_skill, player,skl_weapon_master,4),
     (troop_raise_skill, player,skl_power_strike,2),
     (troop_raise_skill, player,skl_power_throw,2),
     (troop_raise_skill, player,skl_shield,2),
     (troop_raise_skill, player,skl_athletics,2),
     (troop_raise_skill, player,skl_ironflesh,1),
     (troop_raise_skill, player,skl_trainer,2),
     (troop_raise_skill, player,skl_spotting,1),
     (troop_raise_skill, player,skl_looting,2),
     (troop_raise_skill, player,skl_tactics,2),   
     (troop_raise_proficiency, player,wpt_one_handed_weapon,35),
     (troop_raise_proficiency, player,wpt_two_handed_weapon,30),
     (troop_raise_proficiency, player,wpt_polearm,40),
     (troop_raise_proficiency, player,wpt_throwing,30),
     (troop_add_item, player,"itm_german_tunica",0), 
     (troop_add_item, player,"itm_ankleboots",0),
     (troop_add_item, player,"itm_leather_gloves1",0),
     (troop_add_item, player,"itm_skullcapt1",0),
     (troop_add_item, player,"itm_shieldtarcza19",0),
     (troop_add_item, player,"itm_spear_hasta",0),
     (troop_add_item, player,"itm_javelins",0),   
     (troop_add_item, player,"itm_talak_seaxkni",0),   
     (troop_add_item, player,"itm_bread",0),
     (troop_add_item, player,"itm_honey",0),
  (call_script,"script_change_troop_renown", player, 5),   
     (troop_add_gold, player, 180),   
  (else_try),
     (eq,"$background_job",3),   #Lesser Lord's Retainer ; STATS DONE
     (eq,"$character_gender",tf_female),
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),   
##     (troop_raise_attribute, player,ca_strength,4),
##     (troop_raise_attribute, player,ca_agility,3),
     (troop_raise_skill, player,skl_weapon_master,2),
     (troop_raise_skill, player,skl_power_strike,1),
     (troop_raise_skill, player,skl_power_throw,2),
     (troop_raise_skill, player,skl_shield,2),
     (troop_raise_skill, player,skl_athletics,3),
     (troop_raise_skill, player,skl_ironflesh,2),
     (troop_raise_skill, player,skl_trainer,2),
     (troop_raise_skill, player,skl_spotting,2),
     (troop_raise_skill, player,skl_looting,2),
     (troop_raise_skill, player,skl_tactics,2),     
     (troop_raise_proficiency, player,wpt_one_handed_weapon,25),
     (troop_raise_proficiency, player,wpt_two_handed_weapon,25),
     (troop_raise_proficiency, player,wpt_polearm,30),
     (troop_raise_proficiency, player,wpt_throwing,40),
     (troop_raise_proficiency, player,wpt_archery,30),
     (troop_add_item, player,"itm_german_tunica",0), 
     (troop_add_item, player,"itm_ankleboots",0),
     (troop_add_item, player,"itm_leather_gloves1",0),
     (troop_add_item, player,"itm_skullcapt1",0),
     (troop_add_item, player,"itm_shieldtarcza19",0),
     (troop_add_item, player,"itm_spear_hasta",0),
     (troop_add_item, player,"itm_javelins",0),   
     (troop_add_item, player,"itm_talak_seaxkni",0),   
     (troop_add_item, player,"itm_bread",0),   
     (troop_add_item, player,"itm_honey",0),
  (call_script,"script_change_troop_renown", player, 10),   
     (troop_add_gold, player, 155),
  (else_try),
     (eq,"$background_job",4),   #Bard ; STATS DONE
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),   
##     (troop_raise_attribute, player,ca_strength,1),   
##     (troop_raise_attribute, player,ca_charisma,5),
##     (troop_raise_attribute, player,ca_intelligence,3),
##     (troop_raise_attribute, player,ca_agility,2),
     (troop_raise_skill, player,skl_power_draw,3),   
     (troop_raise_skill, player,skl_power_throw,1),
     (troop_raise_skill, player,skl_athletics,3),
     (troop_raise_skill, player,skl_persuasion,3),
     (troop_raise_skill, player,skl_entertain,4),
     (troop_raise_skill, player,skl_spotting,2),
     (troop_raise_skill, player,skl_foraging,2),   
     (troop_raise_skill, player,skl_pathfinding,2),   
     (troop_raise_proficiency, player,wpt_one_handed_weapon,10),
     (troop_raise_proficiency, player,wpt_two_handed_weapon,5),   
     (troop_raise_proficiency, player,wpt_polearm,10),
     (troop_raise_proficiency, player,wpt_throwing,10),
     (troop_raise_proficiency, player,wpt_archery,25),
     (troop_add_item, player,"itm_cloaked_tunic2",imod_thick),
     (troop_add_item, player,"itm_cheap_shoes",imod_ragged),
     (troop_add_item, player,"itm_scianshswordt1", 0),
     (troop_add_item, player,"itm_shortbow", 0),
     (troop_add_item, player,"itm_arrows1", 0),
     (troop_add_item, player,"itm_lyre",0),
     (troop_add_item, player,"itm_honey",0),
  (assign, "$sabe_leer", 1),   
     (store_random_in_range, ":book_no", books_begin, books_end),
     (troop_add_item, player,":book_no",0),   
  (call_script,"script_change_troop_renown", player, 3),   
     (troop_add_gold, player, 50),   
  (else_try),
     (eq,"$background_job",5),   #Free Peasant ; STATS DONE   
     (eq,"$character_gender",tf_male),
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),   
##     (troop_raise_attribute, player,ca_strength,4),
##     (troop_raise_attribute, player,ca_agility,3),   
     (troop_raise_skill, player,skl_athletics,3),
     (troop_raise_skill, player,skl_foraging,2),   
     (troop_raise_skill, player,skl_power_draw,1),
     (troop_raise_skill, player,skl_power_throw,1),
     (troop_raise_skill, player,skl_shield,1),
     (troop_raise_skill, player,skl_ironflesh,3),
     (troop_raise_skill, player,skl_spotting,2),
     (troop_raise_skill, player,skl_tracking,2),   
     (troop_raise_skill, player,skl_first_aid,1),
     (troop_raise_skill, player,skl_inventory_management,1),#F123
     (troop_raise_skill, player,skl_looting,2),
     (troop_raise_skill, player,skl_trade,1),
     (troop_raise_proficiency, player,wpt_one_handed_weapon,5),
     (troop_raise_proficiency, player,wpt_polearm,20),
     (troop_raise_proficiency, player,wpt_archery,10),
     (troop_raise_proficiency, player,wpt_throwing,15),   
     (troop_add_item, player,"itm_hoodnewblk",0),
     (troop_add_item, player,"itm_peasant_ftunic",0),
     (troop_add_item, player,"itm_hunting_knife",0),
     (troop_add_item, player,"itm_cheap_shoes",imod_ragged),
     (troop_add_item, player,"itm_spearboar", imod_bent),
     (troop_add_item, player,"itm_javelins",imod_swaybacked),
     (troop_add_item, player,"itm_cheap_buckler",0),
     (troop_add_item, player,"itm_smoked_fish",0),
     (troop_add_item, player,"itm_bread", 0),
  (call_script,"script_change_troop_renown", player, 2),   
     (troop_add_gold, player, 110),   
  (else_try),   
     (eq,"$background_job",5),   #Wife to a Free Peasant ; STATS DONE
     (eq,"$character_gender",tf_female),
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),   
##     (troop_raise_attribute, player,ca_strength,2),
##     (troop_raise_attribute, player,ca_agility,2),   
     (troop_raise_skill, player,skl_inventory_management,2),#F123
     (troop_raise_skill, player,skl_power_throw,1),
     (troop_raise_skill, player,skl_ironflesh,2),
     (troop_raise_skill, player,skl_athletics,3),
     (troop_raise_skill, player,skl_foraging,2),
     (troop_raise_skill, player,skl_tracking,1),   
     (troop_raise_skill, player,skl_power_draw,1),
     (troop_raise_skill, player,skl_shield,1),
     (troop_raise_skill, player,skl_spotting,3),   
     (troop_raise_skill, player,skl_first_aid,3),
     (troop_raise_skill, player,skl_wound_treatment,1),   
     (troop_raise_proficiency, player,wpt_one_handed_weapon,10),
     (troop_raise_proficiency, player,wpt_polearm,15),
     (troop_raise_proficiency, player,wpt_archery,20),   
     (troop_add_item, player,"itm_peasant_dressblue", 0),
     (troop_add_item, player,"itm_leather_shoes", 0),
     (troop_add_item, player,"itm_spearboar", imod_bent),
     (troop_add_item, player,"itm_huntingbow", 0), 
     (troop_add_item, player,"itm_buckler_2", 0),
     (troop_add_item, player,"itm_butchering_knife", 0),
     (troop_add_item, player,"itm_arrows1",0),
     (troop_add_item, player,"itm_bread", 0),
  (call_script,"script_change_troop_renown", player, 2),   
    (troop_add_gold, player, 120),
  (else_try),
     (eq,"$background_job",6),  #Merchant ; STATS DONE
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),
##     (troop_raise_attribute, player,ca_strength,1),   
##      (troop_raise_attribute, player,ca_charisma,2),
##     (troop_raise_attribute, player,ca_intelligence,2),   
     (troop_raise_skill, player,skl_inventory_management,5),
     (troop_raise_skill, player,skl_persuasion,4),
     (troop_raise_skill, player,skl_trade,5),
     (troop_raise_skill, player,skl_pathfinding,3),
     (troop_raise_skill, player,skl_foraging,2),
     (troop_raise_skill, player,skl_riding,1),
     (troop_raise_proficiency, player,wpt_one_handed_weapon,10),
     (troop_raise_proficiency, player,wpt_polearm,20),   
     (troop_add_item, player,"itm_german_tunica",0),   #Long Tunic
     (troop_add_item, player,"itm_cheap_shoes",imod_ragged),
     (troop_add_item, player,"itm_germanshortspeart2",0),
     (troop_add_item, player,"itm_knifechp",0),
     (troop_add_item, player,"itm_bread",0),
     (troop_add_item, player,"itm_grain",0),
     (troop_add_item, player,"itm_pottery",0),
     (troop_add_item, player,"itm_wool",0),
  (call_script,"script_change_troop_renown", player, 5),   
     (troop_add_gold, player,300),     
  (else_try),
     (eq,"$background_job",7),   #Blacksmith ; STATS DONE
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),   
##     (troop_raise_attribute, player,ca_strength,5),
##     (troop_raise_attribute, player,ca_intelligence,1),     
     (troop_raise_skill, player,skl_athletics,2),
     (troop_raise_skill, player,skl_ironflesh,5),   
     (troop_raise_skill, player,skl_power_strike,2),
     (troop_raise_skill, player,skl_weapon_master,2),
     (troop_raise_skill, player,skl_trade,2),
     (troop_raise_skill, player,skl_inventory_management,4),   
     (troop_raise_skill, player,skl_persuasion,1),
     (troop_raise_skill, player,skl_engineer,2),   
     (troop_raise_proficiency, player,wpt_one_handed_weapon,20),   
     (troop_raise_proficiency, player,wpt_two_handed_weapon,15),
     (troop_raise_proficiency, player,wpt_polearm,20),   
     (troop_add_item, player,"itm_cheap_shoes",imod_ragged),
     (troop_add_item, player,"itm_leather_aprontunic",imod_ragged),
     (troop_add_item, player,"itm_leather_gloves1",0),
     (troop_add_item, player,"itm_axe1",0),  
     (troop_add_item, player,"itm_bread",0),
     (troop_add_item, player,"itm_smoked_fish",0),   
     (troop_add_item, player,"itm_mineral",0),
     (troop_add_item, player,"itm_tools",0),
  (call_script,"script_change_troop_renown", player, 2),   
     (troop_add_gold, player, 230),   
  (else_try),
     (eq,"$background_job",8),    #Poacher ; STATS DONE
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),   
##     (troop_raise_attribute, player,ca_strength,3),
##     (troop_raise_attribute, player,ca_agility,4),
     (troop_raise_skill, player,skl_power_draw,2),
     (troop_raise_skill, player,skl_power_throw,2),
     (troop_raise_skill, player,skl_tracking,5),
   #  (troop_raise_skill, player,skl_foraging,1),#F123gdw2
     (troop_raise_skill, player,skl_pathfinding,2),
     (troop_raise_skill, player,skl_spotting,5),
     (troop_raise_skill, player,skl_athletics,2),
     (troop_raise_skill, player,skl_looting,2),#gdw
     (troop_raise_proficiency, player,wpt_one_handed_weapon,20),   
     (troop_raise_proficiency, player,wpt_throwing,25),   
     (troop_raise_proficiency, player,wpt_archery,50),
     (troop_add_item, player,"itm_rawhide_vest_green",imod_ragged),
     (troop_add_item, player,"itm_hoodnewblk",0),
     (troop_add_item, player,"itm_cheap_shoes",imod_ragged),
     (troop_add_item, player,"itm_knisxclearvert3",0),
     (troop_add_item, player,"itm_huntingbow",0),
     (troop_add_item, player,"itm_arrows1",0),
     (troop_add_item, player,"itm_dried_meat",0),
     (troop_add_item, player,"itm_furs",0),
#     (call_script, "script_change_player_honor", -20),   
     (troop_add_gold, player, 50),   
  (else_try),
     (eq,"$background_job",9),    #Itinerant Preacher ; STATS DONE
##     (troop_raise_attribute, player,ca_strength, -4),
##    (troop_raise_attribute, player,ca_charisma, -4),
##     (troop_raise_attribute, player,ca_agility, -4),
##     (troop_raise_attribute, player,ca_intelligence, -4),
##     (troop_raise_attribute, player,ca_strength,2),   
##     (troop_raise_attribute, player,ca_intelligence,3),
##     (troop_raise_attribute, player,ca_charisma,4),
     (troop_raise_skill, player,skl_persuasion,5),
     (troop_raise_skill, player,skl_wound_treatment,2),
     (troop_raise_skill, player,skl_surgery,2),
     (troop_raise_skill, player,skl_first_aid,3),
     (troop_raise_skill, player,skl_trade,3),
     (troop_raise_skill, player,skl_pathfinding,3),   
     (troop_raise_skill, player,skl_inventory_management,2),   
     (troop_raise_proficiency, player,wpt_polearm,15),
     (troop_raise_proficiency, player,wpt_throwing,15),
     (troop_add_item, player,"itm_mineral",imod_ragged),
     (troop_add_item, player,"itm_quarter_staff",imod_bent),
     (troop_add_item, player,"itm_pilgrim_hood",imod_ragged),
     (troop_add_item, player,"itm_monk_robe",imod_ragged),
     (troop_add_item, player,"itm_bread", 0),
     (troop_add_item, player,"itm_bread", 0),
     (troop_add_item, player,"itm_smoked_fish",0),
     (store_random_in_range, ":book_no", books_begin, books_end),
     (troop_add_item, player,":book_no",0),   
  (assign, "$sabe_leer", 1),
  (call_script,"script_change_troop_renown", player, 4),   
  (call_script, "script_change_player_honor", 50),       
     (troop_add_gold, player, 70),   
  (try_end),
# Reason
  (try_begin),
     (eq,"$background_reason",1),
     (troop_raise_attribute, player,ca_strength,1),
     (troop_raise_skill, player,skl_power_strike,1),
  (else_try),
     (eq,"$background_reason",2),
     (troop_raise_skill, player,skl_wound_treatment,1),
     (troop_raise_skill, player,skl_ironflesh,1),
  (else_try),
     (eq,"$background_reason",3),
     (troop_raise_attribute, player,ca_agility,1),
     (troop_raise_skill, player,skl_pathfinding,1),
  (else_try),
     (eq,"$background_reason",4),
     (troop_raise_attribute, player,ca_charisma,1),
     (troop_raise_skill, player,skl_persuasion,1),
  (else_try),
     (eq,"$background_reason",5),
     (troop_raise_attribute, player,ca_intelligence,1),
     (troop_raise_skill, player,skl_spotting,1),
  (else_try),
     (eq,"$background_reason",6),
  (call_script,"script_change_troop_renown", player, 20),   
     (troop_raise_skill, player,skl_looting,1),
    (troop_raise_attribute, player,ca_intelligence,1), #F123thengdwagility-intel
  (try_end),

  ## Religion
  (try_begin),
     (eq,"$background_religion",1),
     (assign, "$g_sod_faith", 4),
     (call_script, "script_change_player_honor", 5),
    (troop_raise_skill, player,skl_pathfinding,1), #F123 
  (else_try),
     (eq,"$background_religion",2),
     (assign, "$g_sod_faith", 2),
  (call_script,"script_change_troop_renown", player, 5),   
   (troop_raise_skill, player,skl_spotting,1), #F123
  (else_try),
     (eq,"$background_religion",3),
     (assign, "$g_sod_faith", 3),
  (call_script,"script_change_troop_renown", player, 5), #F123 
  (troop_raise_skill, player,skl_power_strike,1), #F123    
  (else_try),
     (eq,"$background_religion",4),
     (assign, "$g_sod_faith", 4),
     (call_script, "script_change_player_honor", 5), #F123
     (troop_raise_skill, player,skl_persuasion,1),   
  (try_end),
  (set_show_messages, 1),
  ]),
  #hister cambios acaban
  ("randomize_background",
 [(store_script_param_1, ":in_presentation"),
#  (store_random_in_range, reg11,   0,  500),
  (store_random_in_range, reg12, 100,  2500),   #MOTO chief fix for full range
  (store_random_in_range, reg13, 100,  800),
  (store_random_in_range, reg14, 100, 1000),
  (store_random_in_range, reg15, 100, 1000),
  (store_random_in_range, reg16, 100,  700),
  (store_random_in_range, reg17, 100,  500),

#  (store_div, "$character_gender", reg11, 100),
  (store_div, "$character_nationality", reg12, 100),
  (store_div, "$background_parent", reg13, 100),
  (store_div, "$background_childhood", reg14, 100),
  (store_div, "$background_job", reg15, 100),
  (store_div, "$background_reason", reg16, 100),
  (store_div, "$background_religion", reg17, 100),

  (try_begin),
     (eq, ":in_presentation", 1),
     (store_mul, reg11, "$character_gender", 100),
     (store_mul, reg12, "$character_nationality", 100),
     (store_mul, reg13, "$background_parent", 100),
     (store_mul, reg14, "$background_childhood", 100),
     (store_mul, reg15, "$background_job", 100),
     (store_mul, reg16, "$background_reason", 100),     
     (store_mul, reg17, "$background_religion", 100),     

     (overlay_set_val, "$g_presentation_obj_21", reg11),
     (overlay_set_val, "$g_presentation_obj_22", reg12),
     (overlay_set_val, "$g_presentation_obj_23", reg13),
     (overlay_set_val, "$g_presentation_obj_24", reg14),
     (overlay_set_val, "$g_presentation_obj_25", reg15),
     (overlay_set_val, "$g_presentation_obj_26", reg16),
     (overlay_set_val, "$g_presentation_obj_27", reg17),
  (try_end), ]),   
#-- Dunde's Player Background END  chief creacion pj

]
