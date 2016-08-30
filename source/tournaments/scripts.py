from ..header_operations import *
from ..header_common import *

from ..module_constants import *


scripts = [

    ("start_feast_tournament",
     [
         (store_script_param_1, ":center_no"),
         (try_begin),
            (is_between, ":center_no", towns_begin, towns_end),
            (party_set_slot, ":center_no", "slot_town_has_tournament", 2),
         (try_end),
     ]),

    ("end_feast_tournament", [
        (store_script_param_1, ":center_no"),
        (party_set_slot, ":center_no", "slot_town_has_tournament", 0),
    ]),

    ("initialize_tournaments",
     [
        (try_for_range, ":town_no", towns_begin, towns_end),
            (party_set_slot, ":town_no", "slot_town_tournament_max_teams", 4),
            (party_set_slot, ":town_no", "slot_town_tournament_max_team_size", 8),

            # first tournaments
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", 20),
            (store_random_in_range, ":random_days", 12, 15),
            (party_set_slot, ":town_no", "slot_town_has_tournament", ":random_days"),
        (try_end),

        # this town is different for whatever reason.
        (party_set_slot, "p_town_6", "slot_town_tournament_max_team_size", 2),
     ]),

  # script_fill_tournament_participants_troop
  # Input: arg1 = center_no, arg2 = player_at_center
  # Output: none (fills trp_tournament_participants)
  ("fill_tournament_participants_troop",
    [(store_script_param, ":center_no", 1),
     (store_script_param, ":player_at_center", 2),
     (assign, ":cur_slot", 0),

     (try_begin),
       (eq, ":player_at_center", 1),
       (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
       (try_for_range, ":stack_no", 0, ":num_stacks"),
         (party_stack_get_troop_id, ":cur_troop", "p_main_party", ":stack_no"),
         (troop_is_hero, ":cur_troop"),
         (neq, ":cur_troop", "trp_kidnapped_girl"),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":cur_troop"),
         (val_add, ":cur_slot", 1),
       (try_end),
     (try_end),

     (party_collect_attachments_to_party, ":center_no", "p_temp_party"),
     (party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
     (try_for_range, ":stack_no", 0, ":num_stacks"),
       (party_stack_get_troop_id, ":cur_troop", "p_temp_party", ":stack_no"),
       (troop_is_hero, ":cur_troop"),
       (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":cur_troop"),
       (val_add, ":cur_slot", 1),
     (try_end),

     (try_begin),
       (store_random_in_range, ":random_no", 0, 100),
       (lt, ":random_no", 50),
       (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_xerina"),
       (val_add, ":cur_slot", 1),
     (try_end),
     (try_begin),
       (store_random_in_range, ":random_no", 0, 100),
       (lt, ":random_no", 50),
       (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_dranton"),
       (val_add, ":cur_slot", 1),
     (try_end),
     (try_begin),
       (store_random_in_range, ":random_no", 0, 100),
       (lt, ":random_no", 50),
       (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_kradus"),
       (val_add, ":cur_slot", 1),
     (try_end),

     (try_for_range, ":cur_troop", quick_battle_troops_begin, quick_battle_troops_end),
       (store_random_in_range, ":random_no", 0, 100),
       (lt, ":random_no", 70),
       (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":cur_troop"),
       (val_add, ":cur_slot", 1),
     (try_end),

     (assign, ":begin_slot", ":cur_slot"),
     (try_for_range, ":cur_slot", ":begin_slot", 64),
       (store_random_in_range, ":random_no", 0, 6),
       (try_begin),
         (eq, ":random_no", 0),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_regular_fighter"),
       (else_try),
         (eq, ":random_no", 1),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_veteran_fighter"),
       (else_try),
         (eq, ":random_no", 2),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_champion_fighter"),
       (else_try),
         (eq, ":random_no", 3),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_sword_sister"),
       (else_try),
         (eq, ":random_no", 4),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_merc_infantryt5"),
       (else_try),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_merc_infantryt4"),
       (try_end),
     (try_end),
     ]),

  # script_get_num_tournament_participants
  # Input: none
  # Output: reg0 = num_participants
  ("get_num_tournament_participants",
    [(assign, ":num_participants", 0),
     (try_for_range, ":cur_slot", 0, 64),
       (troop_slot_ge, "trp_tournament_participants", ":cur_slot", 0),
       (val_add, ":num_participants", 1),
     (try_end),
     (assign, reg0, ":num_participants"),
     ]),

  # script_get_random_tournament_participant
  # Input: none
  # Output: reg0 = troop_no
  ("get_random_tournament_participant",
    [(call_script, "script_get_num_tournament_participants"),
     (assign, ":num_participants", reg0),
     (store_random_in_range, ":random_troop", 0, ":num_participants"),
     (assign, ":continue", 1),
     (try_for_range, ":cur_slot", 0, 64),
       (eq, ":continue", 1),
       (troop_slot_ge, "trp_tournament_participants", ":cur_slot", 0),
       (val_sub, ":random_troop", 1),
       (lt, ":random_troop", 0),
       (assign, ":continue", 0),
       (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
       (troop_set_slot, "trp_tournament_participants", ":cur_slot", -1),
     (try_end),
     (assign, reg0, ":troop_no"),
     ]),

  # script_add_tournament_participant
  # Input: arg1 = troop_no
  # Output: none
  ("add_tournament_participant",
    [(store_script_param, ":troop_no", 1),
     (assign, ":continue", 1),
     (try_for_range, ":cur_slot", 0, 64),
       (eq, ":continue", 1),
       (troop_slot_eq, "trp_tournament_participants", ":cur_slot", -1),
       (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":troop_no"),
       (assign, ":continue", 0),
     (try_end),
     ]),

  # script_get_random_tournament_team_amount_and_size
  # Input: none
  # Output: reg0 = number_of_teams, reg1 = team_size
  ("get_random_tournament_team_amount_and_size",
    [
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (party_get_slot, ":town_max_teams", "$current_town", "slot_town_tournament_max_teams"),
        (val_add, ":town_max_teams", 1),
        (party_get_slot, ":town_max_team_size", "$current_town", "slot_town_tournament_max_team_size"),
        (val_add, ":town_max_team_size", 1),
        (assign, ":max_teams", ":num_participants"),
        (val_min, ":max_teams", ":town_max_teams"),
        (assign, ":max_size", ":num_participants"),
        (val_min, ":max_size", ":town_max_team_size"),
        (assign, ":min_size", 1),
        (try_begin),
          (ge, ":num_participants", 32),
          (assign, ":min_size", 2),
          (val_min, ":min_size", ":town_max_team_size"),
        (try_end),
        (assign, ":end_cond", 500),
        (try_for_range, ":unused", 0, ":end_cond"),
          (store_random_in_range, ":random_teams", 2, ":max_teams"),
          (store_random_in_range, ":random_size", ":min_size", ":max_size"),
          (store_mul, ":total_men", ":random_teams", ":random_size"),
          (le, ":total_men", ":num_participants"),
          (store_sub, ":left_men", ":num_participants", ":total_men"),
          (neq, ":left_men", 1),
          (assign, ":end_cond", 0),
        (try_end),
        (try_begin),
          (gt, ":end_cond", 0),
          (assign, ":random_teams", 2),
          (assign, ":random_size", 1),
        (try_end),
        (assign, reg0, ":random_teams"),
        (assign, reg1, ":random_size"),
     ]),

  # script_get_troop_priority_point_for_tournament
  # Input: arg1 = troop_no
  # Output: reg0 = troop_point
  ("get_troop_priority_point_for_tournament",
    [(store_script_param, ":troop_no", 1),
     (assign, ":troop_point", 0),
     (try_begin),
       (ge, ":troop_no", 0),
       (val_add, ":troop_point", 40000),
       (try_begin),
         (eq, ":troop_no", "trp_player"),
         (val_add, ":troop_point", 80000),
       (try_end),
       (try_begin),
         (troop_is_hero, ":troop_no"),
         (val_add, ":troop_point", 20000),
       (try_end),
       (try_begin),
         (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_player_companion),
         (val_add, ":troop_point", 10000),
       (else_try),
         (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
         (troop_get_slot, ":renown", ":troop_no", "slot_troop_renown"),
         (val_add, ":troop_point", ":renown"),
         (val_add, ":troop_point", 1000), #in order to make it more prior than tournament heroes with higher levels
       (else_try),
         (store_character_level, ":level", ":troop_no"),
         (val_add, ":troop_point", ":level"),
       (try_end),
     (try_end),
     (assign, reg0, ":troop_point"),
     ]),

  # script_sort_tournament_participant_troops
  # Input: none
  # Output: none (sorts trp_tournament_participants)
  ("sort_tournament_participant_troops",
    [(try_for_range, ":cur_slot", 0, 63),
       (store_add, ":cur_slot_2_begin", ":cur_slot", 1),
       (try_for_range, ":cur_slot_2", ":cur_slot_2_begin", 64),
         (troop_get_slot, ":troop_1", "trp_tournament_participants", ":cur_slot"),
         (troop_get_slot, ":troop_2", "trp_tournament_participants", ":cur_slot_2"),
         (call_script, "script_get_troop_priority_point_for_tournament", ":troop_1"),
         (assign, ":troop_1_point", reg0),
         (call_script, "script_get_troop_priority_point_for_tournament", ":troop_2"),
         (assign, ":troop_2_point", reg0),
         (gt, ":troop_2_point", ":troop_1_point"),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":troop_2"),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot_2", ":troop_1"),
       (try_end),
     (try_end),
     ]),

  # script_remove_tournament_participants_randomly
  # Input: arg1 = number_to_be_removed
  # Output: none
  ("remove_tournament_participants_randomly",
    [(store_script_param, ":number_to_be_removed", 1),
     (try_for_range, ":unused", 0, ":number_to_be_removed"),
       (assign, ":total_weight", 0),
       (try_for_range, ":cur_slot", 0, 64),
         (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
         (ge, ":troop_no", 0),
         (store_character_level, ":level", ":troop_no"),
         (val_min, ":level", 38),
         (store_sub, ":weight", 40, ":level"),
         (val_add, ":total_weight", ":weight"),
       (try_end),
       (store_random_in_range, ":random_weight", 0, ":total_weight"),
       (assign, ":continue", 1),
       (try_for_range, ":cur_slot", 0, 64),
         (eq, ":continue", 1),
         (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
         (ge, ":troop_no", 0),
         (store_character_level, ":level", ":troop_no"),
         (val_min, ":level", 38),
         (store_sub, ":weight", 40, ":level"),
         (val_sub, ":random_weight", ":weight"),
         (lt, ":random_weight", 0),
         (troop_set_slot, "trp_tournament_participants", ":cur_slot", -1),
         (assign, ":continue", 0),
       (try_end),
     (try_end),
     ]),

  # script_end_tournament_fight
  # Input: arg1 = player_team_won (1 or 0)
  # Output: none
  ("end_tournament_fight",
    [(store_script_param, ":player_team_won", 1),
     (call_script, "script_get_num_tournament_participants"),
     (assign, ":num_participants", reg0),
     (store_div, ":needed_to_remove_randomly", ":num_participants", 2),
     #Must remove other participants randomly earlier than adding the winners back to participants
     (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),

     (assign, ":num_needed", "$g_tournament_num_participants_for_fight"),
     (val_div, ":num_needed", 2),
     (get_player_agent_no, ":player_agent"),
     (agent_get_team, ":player_team", ":player_agent"),
     (try_for_agents, ":agent_no"),
       (agent_is_human, ":agent_no"),
       (agent_get_troop_id, ":troop_id", ":agent_no"),
       (neg|is_between, ":troop_id", arena_masters_begin, arena_masters_end),#omit tournament master
       (agent_get_team, ":agent_team", ":agent_no"),
       (assign, ":cur_point", 0),
       (try_begin),
         (eq, ":player_team_won", 1),
         (eq, ":agent_team", ":player_team"),
         (val_add, ":cur_point", 5000000),#Make sure that team members are chosen
       (try_end),
       (agent_get_kill_count, ":kill_count", ":agent_no", 1), #everyone is knocked unconscious
       (store_mul, ":kill_point", ":kill_count", 160000),#Make sure that kill count is the second most important variable
       (val_add, ":cur_point", ":kill_point"),
       (call_script, "script_get_troop_priority_point_for_tournament", ":troop_id"),
       (val_add, ":cur_point", reg0),
       (try_begin),#reset player's point if kill count is one after the first 2 rounds, or if it is zero
         (eq, ":agent_no", ":player_agent"),
         (eq, ":player_team_won", 0),
         (assign, ":not_passed", 1),
         (try_begin),
           (ge, ":kill_count", 2),
           (assign, ":not_passed", 0),
         (else_try),
           (eq, ":kill_count", 1),
           (le, "$g_tournament_cur_tier", 1),
           (assign, ":not_passed", 0),
         (try_end),
         (eq, ":not_passed", 1),
         (assign, ":cur_point", 0),
       (try_end),
       (agent_set_slot, ":agent_no", "slot_agent_tournament_point", ":cur_point"),
     (try_end),
     (try_for_range, ":unused", 0, ":num_needed"),
       (assign, ":best_point", 0),
       (assign, ":best_agent_no", -1),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_get_slot, ":point", ":agent_no", "slot_agent_tournament_point"),
         (gt, ":point", ":best_point"),
         (assign, ":best_agent_no", ":agent_no"),
         (assign, ":best_point", ":point"),
       (try_end),
       (agent_set_slot, ":best_agent_no", "slot_agent_tournament_point", 0),#Do not select the same agent again
       (agent_get_troop_id, ":troop_id", ":best_agent_no"),
       (call_script, "script_add_tournament_participant", ":troop_id"),
     (try_end),
     (assign, "$g_tournament_player_team_won", ":player_team_won"),
     (jump_to_menu, "mnu_town_tournament"),
     ]),


  # script_get_win_amount_for_tournament_bet
  # Input: none
  # Output: reg0 = win_amount_with_100_denars
  ("get_win_amount_for_tournament_bet",
    [
        (party_get_slot, ":player_odds", "$current_town", "slot_town_player_odds"),
        (try_begin),
          (eq, "$g_tournament_cur_tier", 0),
          (assign, ":win_amount", 120),
        (else_try),
          (eq, "$g_tournament_cur_tier", 1),
          (assign, ":win_amount", 90),
        (else_try),
          (eq, "$g_tournament_cur_tier", 2),
          (assign, ":win_amount", 60),
        (else_try),
          (eq, "$g_tournament_cur_tier", 3),
          (assign, ":win_amount", 40),
        (else_try),
          (eq, "$g_tournament_cur_tier", 4),
          (assign, ":win_amount", 20),
        (else_try),
          (assign, ":win_amount", 8),
        (try_end),
        (val_mul, ":win_amount", ":player_odds"),
        (val_div, ":win_amount", 100),
        (val_add, ":win_amount", 100), #win amount when 100 denars is placed
        (assign, reg0, ":win_amount"),
     ]),

  # script_tournament_place_bet
  # Input: arg1 = bet_amount
  # Output: none
  ("tournament_place_bet",
    [
        (store_script_param, ":bet_amount", 1),
        (call_script, "script_get_win_amount_for_tournament_bet"),
        (assign, ":win_amount", reg0),
        (val_mul, ":win_amount", ":bet_amount"),
        (val_div, ":win_amount", 100),
        (val_sub, ":win_amount", ":bet_amount"),
        (val_add, "$g_tournament_bet_placed", ":bet_amount"),
        (val_add, "$g_tournament_bet_win_amount", ":win_amount"),
        (troop_remove_gold, "trp_player", ":bet_amount"),
        (assign, "$g_tournament_last_bet_tier", "$g_tournament_cur_tier"),
     ]),

# script_set_items_for_tournament
  # Input: arg1 = horse_chance, arg2 = lance_chance (with horse only), arg3 = sword_chance, arg4 = axe_chance, arg5 = bow_chance (without horse only), arg6 = javelin_chance (with horse only), arg7 = mounted_bow_chance (with horse only), arg8 = crossbow_sword_chance, arg9 = armor_item_begin, arg10 = helm_item_begin
  # Output: none (sets mt_arena_melee_fight items)
  ("set_items_for_tournament",
    [
      (store_script_param, ":horse_chance", 1),
      (store_script_param, ":lance_chance", 2),
      (store_script_param, ":sword_chance", 3),
      (store_script_param, ":axe_chance", 4),
      (store_script_param, ":bow_chance", 5),
      (store_script_param, ":javelin_chance", 6),
      (store_script_param, ":mounted_bow_chance", 7),
      (store_script_param, ":crossbow_sword_chance", 8),
      (store_script_param, ":armor_item_begin", 9),
      (store_script_param, ":helm_item_begin", 10),
      (store_add, ":total_chance", ":sword_chance", ":axe_chance"),
      (val_add, ":total_chance", ":crossbow_sword_chance"),
      (try_for_range, ":i_ep", 0, 32),
        (mission_tpl_entry_clear_override_items, "mt_arena_melee_fight", ":i_ep"),
        (assign, ":has_horse", 0),
        (store_div, ":cur_team", ":i_ep", 8),
        (try_begin),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":horse_chance"),
          (assign, ":has_horse", 1),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_javelins"), #chief cambia caballo practice_horse a daga
        (try_end),
        (try_begin),
          (eq, ":has_horse", 1),
          (store_add, ":cur_total_chance", ":total_chance", ":lance_chance"),
          (val_add, ":cur_total_chance", ":javelin_chance"),
          (val_add, ":cur_total_chance", ":mounted_bow_chance"),
        (else_try),
          (store_add, ":cur_total_chance", ":total_chance", ":bow_chance"),
        (try_end),
        (store_random_in_range, ":random_no", 0, ":cur_total_chance"),
        (store_add, ":cur_shield_item", "itm_arena_shieldred", ":cur_team"),
        (try_begin),
          (val_sub, ":random_no", ":sword_chance"),
          (lt, ":random_no", 0),
          (try_begin),
            (store_random_in_range, ":sub_random_no", 0, 100),
            (lt, ":sub_random_no", 50),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_spear"), #chief cambia tipo de espada de practice_sword
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
#            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_shield_4a"),
          (else_try),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
          (try_end),
        (else_try),
          (val_sub, ":random_no", ":axe_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_axe"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
#         (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_shield_4a"),
        (else_try),
          (val_sub, ":random_no", ":crossbow_sword_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"), #chief cambia tipo de espada de practice_sword
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"), #chief cambia
        (else_try),
          (eq, ":has_horse", 0),
          (val_sub, ":random_no", ":bow_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_seaxe"),
        (else_try),
          (eq, ":has_horse", 1), #chief cambiado torneo
          (val_sub, ":random_no", ":lance_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_spear"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
#          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_shield_4a"),
        (else_try),
          (eq, ":has_horse", 1),
          (val_sub, ":random_no", ":javelin_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_staff"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
#          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_shield_4a"),
        (else_try),
          (eq, ":has_horse", 1), #chief cambiado
          (val_sub, ":random_no", ":mounted_bow_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_seaxe"),
        (try_end),
        (try_begin),
          (ge, ":armor_item_begin", 0),
          (store_add, ":cur_armor_item", ":armor_item_begin", ":cur_team"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_armor_item"),
        (try_end),
        (try_begin),
          (ge, ":helm_item_begin", 0),
          (store_add, ":cur_helm_item", ":helm_item_begin", ":cur_team"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_helm_item"),
        (try_end),
      (try_end),
     ]),
]
