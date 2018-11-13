# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from ID_items import *
from ID_quests import *
from ID_parties import *
from ID_factions import *
from ID_map_icons import *

 ##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
 ##############################################################

 ########################################################
##  ITEM SLOTS             #############################
 ########################################################

slot_item_is_checked               = 0
slot_item_food_bonus               = 1
slot_item_book_reading_progress    = 2
slot_item_book_read                = 3
slot_item_intelligence_requirement = 4
# Autoloot
slot_item_difficulty               = 5
#end Autoloot
slot_item_alternate_weapon         = 6  #SW - for the common_toggle_weapon_capabilities code
slot_item_ammo_clip                = 7  #SWY - so we can easily manage all the ammo properties frame showing stuff

 ########################################################
##  AGENT SLOTS            #############################
 ########################################################

slot_agent_target_entry_point      = 0
slot_agent_target_x_pos            = 1
slot_agent_target_y_pos            = 2
slot_agent_is_alive_before_retreat = 3
slot_agent_is_in_scripted_mode     = 4
slot_agent_is_not_reinforcement    = 5
slot_agent_tournament_point        = 6
slot_agent_arena_team_set          = 7
slot_agent_map_overlay_id          = 10
slot_agent_target_entry_point      = 11

#SW - new speeder slot
slot_agent_speeder_movement        = 12
slot_agent_hit_points              = 13

#SW - Chronicles of Talera regen rate script by Kardiophylax START
slot_agent_regen_rate = 145
#SW - Chronicles of Talera regen rate script by Kardiophylax END


 ########################################################
##  FACTION SLOTS          #############################
 ########################################################
slot_faction_ai_state                 = 4
slot_faction_ai_object                = 5
slot_faction_ai_last_offensive_time   = 6
slot_faction_marshall                 = 7
slot_faction_ai_offensive_max_followers = 8

slot_faction_culture              = 9
slot_faction_leader               = 10
##slot_faction_vassal_of          = 11

slot_faction_number_of_parties    = 20
slot_faction_state                = 21

slot_faction_player_alarm         = 30
slot_faction_last_mercenary_offer_time = 31

slot_faction_tier_1_troop         = 41
slot_faction_tier_2_troop         = 42
slot_faction_tier_3_troop         = 43
slot_faction_tier_4_troop         = 44
slot_faction_tier_5_troop         = 45
slot_faction_deserter_troop       = 48
slot_faction_guard_troop          = 49
slot_faction_messenger_troop      = 50
slot_faction_prison_guard_troop   = 51
slot_faction_spacestation_guard_troop   = 52

slot_faction_has_rebellion_chance = 60


#Rebellion changes
#slot_faction_rebellion_target                = 65
#slot_faction_inactive_leader_location        = 66
#slot_faction_support_base                    = 67
#Rebellion changes



#slot_faction_deserter_party_template       = 62

slot_faction_reinforcements_a        = 77
slot_faction_reinforcements_b        = 78
slot_faction_reinforcements_c        = 79

slot_faction_num_armies              = 80
slot_faction_num_castles             = 81
slot_faction_num_towns               = 82

#SW faction slots
slot_faction_patrol_unit_1      = 83
slot_faction_patrol_unit_2      = 84
slot_faction_patrol_unit_3      = 85

#SW bank slots
slot_faction_bank_debt         = 86
slot_faction_bank_deposit      = 87
slot_faction_debt_interest     = 88
slot_faction_deposit_interest  = 89
slot_faction_debt_expires      = 90

 ########################################################
##  PARTY SLOTS            #############################
 ########################################################
slot_party_type                = 0  #spt_caravan, spt_mainplanet, spt_castle

slot_party_retreat_flag        = 2
slot_party_ignore_player_until = 3
slot_party_ai_state            = 4
slot_party_ai_object           = 5

slot_mainplanet_belongs_to_faction  = 6
slot_mainplanet_lord                = 7
slot_party_ai_substate              = 8
slot_mainplanet_claimed_by_player   = 9

slot_cattle_driven_by_player = slot_mainplanet_lord #hack

slot_mainplanet_center        = 10
slot_mainplanet_castle        = 11
slot_mainplanet_prison        = 12
slot_mainplanet_cantina       = 13
slot_mainplanet_store         = 14
slot_mainplanet_arena         = 16
slot_mainplanet_alley         = 17
slot_mainplanet_walls         = 18
slot_center_culture           = 19

slot_mainplanet_bartender     = 20
slot_mainplanet_weaponsmith   = 21
slot_mainplanet_armorer       = 22
slot_mainplanet_merchant      = 23
slot_mainplanet_horse_merchant= 24
slot_mainplanet_elder         = 25
slot_center_player_relation = 26

slot_center_siege_with_belfry = 27
slot_center_last_taken_by_troop = 28

# party will follow this party if set:
slot_party_commander_party = 30 #default -1
slot_party_following_player    = 31
slot_party_follow_player_until_time = 32
slot_party_dont_follow_player_until_time = 33

slot_minorplanet_raided_by        = 34
slot_minorplanet_state            = 35 #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
slot_minorplanet_raid_progress    = 36
slot_minorplanet_recover_progress = 37
slot_minorplanet_smoke_added      = 38

slot_minorplanet_infested_by_bandits   = 39

slot_center_last_player_alarm_hour = 42

slot_minorplanet_land_quality          = 44
slot_minorplanet_number_of_cattle      = 45
slot_minorplanet_player_can_not_steal_cattle = 46

slot_center_accumulated_rents      = 47
slot_center_accumulated_tariffs    = 48
slot_mainplanet_wealth        = 49
slot_mainplanet_prosperity    = 50
slot_mainplanet_player_odds   = 51


slot_party_last_toll_paid_hours = 52
slot_party_food_store           = 53 #used for sieges
slot_center_is_besieged_by      = 54 #used for sieges
slot_center_last_spotted_enemy  = 55

slot_party_cached_strength      = 56
slot_party_nearby_friend_strength = 57
slot_party_nearby_enemy_strength = 58
slot_party_follower_strength = 59

slot_mainplanet_reinforcement_party_template = 60
slot_center_original_faction      = 61
slot_center_ex_faction            = 62

slot_party_follow_me              = 63
slot_center_siege_begin_hours     = 64 #used for sieges
slot_center_siege_hardness        = 65

#Tavern recruitment START
slot_mainplanet_mercs = 66
#Tavern recruitment END

slot_spacestation_exterior    = slot_mainplanet_center

# Freelancer Extra
slot_party_last_in_combat              = 68 #used for AI 
# Freelancer Extra END

#slot_mainplanet_rebellion_contact   = 76
#trs_not_yet_approached  = 0
#trs_approached_before   = 1
#trs_approached_recently = 2

argument_none    = 0
argument_claim   = 1
argument_ruler   = 2
argument_benefit = 3
argument_victory = 4

slot_mainplanet_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

slot_mainplanet_arena_melee_mission_tpl = 78
slot_mainplanet_arena_torny_mission_tpl = 79
slot_mainplanet_arena_melee_1_num_teams = 80
slot_mainplanet_arena_melee_1_team_size = 81
slot_mainplanet_arena_melee_2_num_teams = 82
slot_mainplanet_arena_melee_2_team_size = 83
slot_mainplanet_arena_melee_3_num_teams = 84
slot_mainplanet_arena_melee_3_team_size = 85
slot_mainplanet_arena_melee_cur_tier    = 86
##slot_mainplanet_arena_template        = 87

slot_center_npc_volunteer_troop_type   = 90
slot_center_npc_volunteer_troop_amount = 91
slot_center_mercenary_troop_type  = 90
slot_center_mercenary_troop_amount= 91
slot_center_volunteer_troop_type  = 92
slot_center_volunteer_troop_amount= 93

#slot_center_companion_candidate  = 94
slot_center_ransom_broker         = 95
slot_center_tavern_traveler       = 96
slot_center_traveler_info_faction = 97
slot_center_tavern_bookseller     = 98
slot_center_tavern_minstrel       = 99

num_party_loot_slots    = 5
slot_party_next_looted_item_slot  = 109
slot_party_looted_item_1          = 110
slot_party_looted_item_2          = 111
slot_party_looted_item_3          = 112
slot_party_looted_item_4          = 113
slot_party_looted_item_5          = 114
slot_party_looted_item_1_modifier = 115
slot_party_looted_item_2_modifier = 116
slot_party_looted_item_3_modifier = 117
slot_party_looted_item_4_modifier = 118
slot_party_looted_item_5_modifier = 119

slot_minorplanet_bound_center         = 120
slot_minorplanet_market_town          = 121
slot_minorplanet_farmer_party         = 122

slot_party_home_center            = 123

slot_center_current_improvement   = 124
slot_center_improvement_end_hour  = 125

slot_center_has_manor             = 130 #village
slot_center_has_fish_pond         = 131 #village
slot_center_has_watch_tower       = 132 #village
slot_center_has_school            = 133 #village
slot_center_has_messenger_post    = 134 #town, castle, village
# inserted by obi 2009-04-28 --> recruit clones, droids, force sensitives
slot_center_has_clone_chambers    = 135
slot_center_has_temple            = 136
slot_center_has_droid_foundry     = 137
slot_center_has_rancor_pit        = 138
# end of insert
#slot_center_has_prisoner_tower   = 135 #town, castle
slot_center_has_prisoner_tower    = 139 #town, castle



minorplanet_improvements_begin      = slot_center_has_manor
minorplanet_improvements_end        = slot_center_has_prisoner_tower

walled_center_improvements_begin    = slot_center_has_messenger_post
#walled_center_improvements_end              = 136
walled_center_improvements_end               = 139

slot_center_has_bandits                      = 149
slot_mainplanet_has_tournament               = 150
slot_mainplanet_tournament_max_teams         = 151
slot_mainplanet_tournament_max_team_size     = 152

slot_center_faction_when_oath_renounced      = 155

slot_center_walker_0_troop                   = 160
slot_center_walker_1_troop                   = 161
slot_center_walker_2_troop                   = 162
slot_center_walker_3_troop                   = 163
slot_center_walker_4_troop                   = 164
slot_center_walker_5_troop                   = 165
slot_center_walker_6_troop                   = 166
slot_center_walker_7_troop                   = 167
slot_center_walker_8_troop                   = 168
slot_center_walker_9_troop                   = 169

slot_center_walker_0_dna                     = 170
slot_center_walker_1_dna                     = 171
slot_center_walker_2_dna                     = 172
slot_center_walker_3_dna                     = 173
slot_center_walker_4_dna                     = 174
slot_center_walker_5_dna                     = 175
slot_center_walker_6_dna                     = 176
slot_center_walker_7_dna                     = 177
slot_center_walker_8_dna                     = 178
slot_center_walker_9_dna                     = 179

slot_center_walker_0_type                    = 180
slot_center_walker_1_type                    = 181
slot_center_walker_2_type                    = 182
slot_center_walker_3_type                    = 183
slot_center_walker_4_type                    = 184
slot_center_walker_5_type                    = 185
slot_center_walker_6_type                    = 186
slot_center_walker_7_type                    = 187
slot_center_walker_8_type                    = 188
slot_center_walker_9_type                    = 189

slot_mainplanet_trade_route_1           = 190
slot_mainplanet_trade_route_2           = 191
slot_mainplanet_trade_route_3           = 192
slot_mainplanet_trade_route_4           = 193
slot_mainplanet_trade_route_5           = 194
slot_mainplanet_trade_route_6           = 195
slot_mainplanet_trade_route_7           = 196
slot_mainplanet_trade_route_8           = 197
slot_mainplanet_trade_route_9           = 198
slot_mainplanet_trade_route_10          = 199
slot_mainplanet_trade_route_11          = 200
slot_mainplanet_trade_route_12          = 201
slot_mainplanet_trade_route_13          = 202
slot_mainplanet_trade_route_14          = 203
slot_mainplanet_trade_route_15          = 204
slot_mainplanet_trade_routes_begin = slot_mainplanet_trade_route_1
slot_mainplanet_trade_routes_end = slot_mainplanet_trade_route_15 + 1


num_trade_goods = itm_siege_supply - itm_smoked_fish
slot_mainplanet_trade_good_productions_begin       = 205
slot_mainplanet_trade_good_prices_begin            = slot_mainplanet_trade_good_productions_begin + num_trade_goods + 1

#SW MF - extra slots for battle stations test - these are party slots
slot_center_turrets        = 206
slot_center_has_shields    = 207  #0 for no, else it is the shield lvl which decides max shields
slot_center_shields        = 208
slot_party_fighters        = 209
slot_party_bombers         = 210
slot_center_has_patrol     = 800  #0 for no, else it is the patrol lvl which decides unit str
slot_center_recruit_ai     = 212  # set to -1 to stop patrol auto reinforcing from your base
slot_center_has_scanner    = 213  # set to 0 for none, 1,2,3 for lvl

slot_center_has_bank       = 214
slot_center_has_slave_market  = 215

slot_center_patrol_party    = 216 #The party which is used to hold the patrol units for reinforcement

#SW - HokieBT
slot_spaceship_name                   = 250
slot_spaceship_price                  = 251
slot_spaceship_desc                   = 252
slot_spaceship_icon                   = 253
#slot_spaceship_starting_upgrades     = 254      #no longer used
slot_spaceship_base_speed             = 255
slot_spaceship_drive_min              = 256
slot_spaceship_drive_max              = 257
slot_spaceship_scanner_min            = 258
slot_spaceship_scanner_max            = 259
slot_spaceship_combat_computer_min    = 260
slot_spaceship_combat_computer_max    = 261
slot_spaceship_troop_capacity_min     = 262
slot_spaceship_troop_capacity_max     = 263
slot_spaceship_medical_bay_min        = 264
slot_spaceship_medical_bay_max        = 265
slot_spaceship_prisoner_capacity_min  = 266
slot_spaceship_prisoner_capacity_max  = 267
slot_spaceship_trade_computer_min     = 268
slot_spaceship_trade_computer_max     = 269
slot_spaceship_cargo_capacity_min     = 270
slot_spaceship_cargo_capacity_max     = 271


#slot_party_type values
##spt_caravan          = 1
spt_castle             = 2
spt_mainplanet         = 3
spt_minorplanet        = 4
##spt_forager          = 5
##spt_war_party        = 6
# #SW - un-commented Faction Patrols
# #http://forums.taleworlds.com/index.php/topic,8652.msg2331555.html#msg2331555
# spt_patrol           = 7
##spt_messenger        = 8
##spt_raider           = 9
##spt_scout            = 10
spt_faction_caravan    = 11
##spt_prisoner_train   = 12
spt_faction_hero_party = 13
##spt_merchant_caravan = 14
spt_minorplanet_farmer = 15
spt_ship               = 16
spt_cattle_herd        = 17
#spt_deserter          = 20

faction_party_types_begin = spt_faction_caravan
faction_party_types_end = spt_faction_hero_party + 1

#slot_faction_state values
sfs_active                     = 0
sfs_defeated                   = 1
sfs_inactive                   = 2
sfs_inactive_rebellion         = 3
sfs_beginning_rebellion        = 4


#slot_faction_ai_state values
sfai_default                   = 0
sfai_gathering_army            = 1
sfai_attacking_center          = 2
sfai_raiding_village           = 3
sfai_attacking_enemy_army      = 4
sfai_attacking_enemies_around_center = 5
#Rebellion system changes begin
sfai_nascent_rebellion          = 6
#Rebellion system changes end

#slot_party_ai_state values
spai_undefined                  = -1
spai_besieging_center           = 1
spai_patrolling_around_center   = 4
spai_raiding_around_center      = 5
##spai_raiding_village          = 6
spai_holding_center             = 7
##spai_helping_town_against_siege = 9
spai_engaging_army              = 10
spai_accompanying_army          = 11
spai_trading_with_town          = 13
spai_retreating_to_center       = 14
##spai_trading_within_faction   = 15
spai_recruiting_troops          = 16

#slot_minorplanet_state values
svs_normal                      = 0
svs_being_raided                = 1
svs_looted                      = 2
svs_recovering                  = 3
svs_deserted                    = 4
svs_under_siege                 = 5

#$g_player_icon_state values
pis_normal                      = 0
pis_camping                     = 1
pis_ship                        = 2


 ########################################################
##  SCENE SLOTS            #############################
 ########################################################
slot_scene_visited              = 0
slot_scene_belfry_props_begin   = 10


 ########################################################
##  TROOP SLOTS            #############################
 ########################################################
#slot_troop_role         = 0  # 10=Faction Lord

slot_troop_occupation           = 2  # 0 = free, 1 = merchant
#slot_troop_duty                = 3  # Faction duty, 0 = free
slot_troop_state                = 3
slot_troop_last_talk_time       = 4
slot_troop_met                  = 5
slot_troop_party_template       = 6
#slot_troop_faction_rank        = 7

slot_troop_renown               = 7

##slot_troop_is_prisoner        = 8  # important for heroes only
slot_troop_prisoner_of_party    = 8  # important for heroes only
#slot_troop_is_player_companion = 9  # important for heroes only:::USE  slot_troop_occupation = slto_player_companion

slot_troop_leaded_party         = 10 # important for faction heroes only
slot_troop_wealth               = 11 # important for faction heroes only
slot_troop_cur_center           = 12 # important for royal family members only (non-faction heroes)

slot_troop_banner_scene_prop    = 13 # important for faction heroes and player only

slot_troop_original_faction     = 14 # for pretenders
slot_troop_loyalty              = 15
slot_troop_player_order_state   = 16
slot_troop_player_order_object  = 17

#slot_troop_present_at_event    = 19 #defined below

slot_troop_does_not_give_quest  = 20
slot_troop_player_debt          = 21
slot_troop_player_relation      = 22
#slot_troop_player_favor        = 23
slot_troop_last_quest           = 24
slot_troop_last_quest_betrayed  = 25
slot_troop_last_persuasion_time = 26
slot_troop_last_comment_time    = 27
slot_troop_spawned_before       = 28

#Post 0907 changes begin
slot_troop_last_comment_slot    = 29
slot_troop_present_at_event     = 19
#Post 0907 changes end

slot_troop_spouse               = 30
slot_troop_father               = 31
slot_troop_mother               = 32
slot_troop_daughter             = 33
slot_troop_son                  = 34
slot_troop_sibling              = 35
slot_troop_lover                = 36

slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36
slot_troop_trainer_training_fight_won        = 37


slot_troop_family_begin        = 30
slot_troop_family_end          = 36

slot_troop_enemy_1             = 40
slot_troop_enemy_2             = 41
slot_troop_enemy_3             = 42
slot_troop_enemy_4             = 43
slot_troop_enemy_5             = 44

slot_troop_enemies_begin       = 40
slot_troop_enemies_end         = 45

slot_troop_honorable           = 50
#slot_troop_merciful           = 51

#SW BSG integration
slot_troop_damage              = 60
slot_troop_craft_no            = 61
slot_troop_craft_type          = 62
slot_troop_ai                  = 63
slot_troop_status              = 64
slot_troop_ai_target           = 65
slot_troop_ai_target_troop     = 66

slot_lord_reputation_type      = 52

slot_troop_change_to_faction          = 55
slot_troop_readiness_to_join_army     = 57
slot_troop_readiness_to_follow_orders = 58

# NPC-related constants

#NPC companion changes begin
slot_troop_first_encountered     = 59
slot_troop_home                  = 60

slot_troop_morality_state        = 61
tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

slot_troop_morality_type = 62
tmt_aristocratic = 1
tmt_egalitarian  = 2
tmt_humanitarian = 3
tmt_honest       = 4
tmt_pious        = 5

slot_troop_morality_value = 63

slot_troop_2ary_morality_type  = 64
slot_troop_2ary_morality_state = 65
slot_troop_2ary_morality_value = 66

slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts


slot_troop_personalityclash_object     = 71
#(0 - they have no problem, 1 - they have a problem)
slot_troop_personalityclash_state    = 72 #1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3
#(a string)
slot_troop_personalityclash2_object   = 73
slot_troop_personalityclash2_state    = 74

slot_troop_personalitymatch_object    = 75
slot_troop_personalitymatch_state     = 76

slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered = 78

#NPC history slots

slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4

slot_troop_playerparty_history_string   = 83
slot_troop_return_renown        = 84

slot_troop_custom_banner_bg_color_1      = 85
slot_troop_custom_banner_bg_color_2      = 86
slot_troop_custom_banner_charge_color_1  = 87
slot_troop_custom_banner_charge_color_2  = 88
slot_troop_custom_banner_charge_color_3  = 89
slot_troop_custom_banner_charge_color_4  = 90
slot_troop_custom_banner_bg_type         = 91
slot_troop_custom_banner_charge_type_1   = 92
slot_troop_custom_banner_charge_type_2   = 93
slot_troop_custom_banner_charge_type_3   = 94
slot_troop_custom_banner_charge_type_4   = 95
slot_troop_custom_banner_flag_type       = 96
slot_troop_custom_banner_num_charges     = 97
slot_troop_custom_banner_positioning     = 98
slot_troop_custom_banner_map_flag_type   = 99

#conversation strings -- must be in this order!
slot_troop_intro = 101

slot_troop_intro_response_1 = 102
slot_troop_intro_response_2 = 103

slot_troop_backstory_a = 104
slot_troop_backstory_b = 105
slot_troop_backstory_c = 106

slot_troop_backstory_delayed = 107

slot_troop_backstory_response_1 = 108
slot_troop_backstory_response_2 = 109

slot_troop_signup   = 110
slot_troop_signup_2 = 111

slot_troop_signup_response_1 = 112
slot_troop_signup_response_2 = 113

slot_troop_mentions_payment           = 114 #Not actually used
slot_troop_payment_response           = 115 #Not actually used
slot_troop_morality_speech            = 116
slot_troop_2ary_morality_speech       = 117
slot_troop_personalityclash_speech    = 118
slot_troop_personalityclash_speech_b  = 119
slot_troop_personalityclash2_speech   = 120
slot_troop_personalityclash2_speech_b = 121
slot_troop_personalitymatch_speech    = 122
slot_troop_personalitymatch_speech_b  = 123
slot_troop_retirement_speech          = 124
slot_troop_rehire_speech              = 125
slot_troop_home_intro                 = 126
slot_troop_home_description           = 127
slot_troop_home_description_2         = 128
slot_troop_home_recap                 = 129
slot_troop_honorific                  = 130
slot_troop_strings_end                = 131
slot_troop_payment_request            = 132

#Rebellion changes begin
slot_troop_discussed_rebellion = 140
slot_troop_support_base = 141

 ###################################################################################
# AutoLoot: Modified Constants
 ###################################################################################
num_loot_management_menu_heroes = 4

slot_upgrade_armor = 153
slot_upgrade_horse = 154
slot_upgrade_wpn_0 = 157
slot_upgrade_wpn_1 = 158
slot_upgrade_wpn_2 = 159
slot_upgrade_wpn_3 = 160

 ###################################################################################
# End Autoloot
 ###################################################################################


#SW troop slot for spaceship
slot_troop_has_spaceship        = 300  # 0 is no, 1,2, etc is type

slot_ship_troop_capacity        = 301
slot_ship_troop_capacity_max    = 302
slot_ship_prisoner_capacity     = 303
slot_ship_prisoner_capacity_max = 304
slot_ship_cargo_capacity        = 305
slot_ship_cargo_capacity_max    = 306
slot_ship_medical_bay           = 307
slot_ship_medical_bay_max       = 308
slot_ship_combat_computer       = 309
slot_ship_combat_computer_max   = 310
slot_ship_trade_computer        = 311
slot_ship_trade_computer_max    = 312
slot_ship_scanner               = 313
slot_ship_scanner_max           = 314
slot_ship_drive                 = 315
slot_ship_drive_max             = 316

#Rebellion changes end

# Freelancer Extra
slot_troop_days_on_mission		        = 317
slot_troop_current_mission			    = 318
# Freelance Extra END
# character backgrounds

#SW - new constants
cb0_ambassador      = 1
cb0_merchant        = 2
cb0_soldier         = 3
cb0_smuggler        = 4
cb0_hunter          = 5
cb0_forcesensitive  = 6

cb0_empire          = 1
cb0_rebel           = 2
cb0_hutt            = 3
cb0_independent     = 4

cb_noble            = 1
cb_merchant         = 2
cb_guard            = 3
cb_forester         = 4
cb_nomad            = 5
cb_thief            = 6
cb_priest           = 7

cb2_page            = 0
cb2_apprentice      = 1
cb2_urchin          = 2
cb2_steppe_child    = 3
cb2_merchants_helper= 4

cb3_poacher         = 3
cb3_craftsman       = 4
cb3_peddler         = 5
cb3_troubadour      = 7
cb3_squire          = 8
cb3_lady_in_waiting = 9
cb3_student         = 10

cb4_revenge         = 1
cb4_loss            = 2
cb4_wanderlust      = 3
cb4_disown          = 5
cb4_greed           = 6

#NPC system changes end
#Encounter types
enctype_fighting_against_minorplanet_raid = 1
enctype_catched_during_minorplanet_raid   = 2


### Troop occupations slot_troop_occupation
##slto_merchant         = 1
slto_faction_hero       = 2
slto_player_companion   = 3
slto_faction_lady       = 4
slto_faction_seneschal  = 5
slto_robber_knight      = 6

stl_unassigned          = -1
stl_reserved_for_player = -2
stl_rejected_by_player  = -3

#NPC changes begin
slto_retirement         = 11
#slto_retirement_medium = 12
#slto_retirement_short  = 13
#NPC changes end

########################################################
##  QUEST SLOTS            #############################
########################################################

slot_quest_target_center            = 1
slot_quest_target_troop             = 2
slot_quest_target_faction           = 3
slot_quest_object_troop             = 4
##slot_quest_target_troop_is_prisoner = 5
slot_quest_giver_troop              = 6
slot_quest_object_center            = 7
slot_quest_target_party             = 8
slot_quest_target_party_template    = 9
slot_quest_target_amount            = 10
slot_quest_current_state            = 11
slot_quest_giver_center             = 12
slot_quest_target_dna               = 13
slot_quest_target_item              = 14
slot_quest_object_faction           = 15

slot_quest_convince_value           = 19
slot_quest_importance               = 20
slot_quest_xp_reward                = 21
slot_quest_gold_reward              = 22
slot_quest_expiration_days          = 23
slot_quest_dont_give_again_period   = 24
slot_quest_dont_give_again_remaining_days = 25


 ########################################################
##  PARTY TEMPLATE SLOTS   #############################
 ########################################################

# Ryan BEGIN
slot_party_template_num_killed   = 1
# Ryan END

########################################################
rel_enemy   = 0
rel_neutral = 1
rel_ally    = 2


#Talk contexts
tc_town_talk                  = 0
tc_court_talk                 = 1
tc_party_encounter            = 2
tc_spacestation_gate          = 3
tc_siege_commander            = 4
tc_join_battle_ally           = 5
tc_join_battle_enemy          = 6
tc_spacestation_commander     = 7
tc_hero_freed                 = 8
tc_hero_defeated              = 9
tc_entering_center_quest_talk = 10
tc_back_alley                 = 11
tc_siege_won_seneschal        = 12
tc_ally_thanks                = 13
tc_tavern_talk                = 14
tc_rebel_thanks               = 15

#Freelancer Extra
tc_garden            		  = 16
tc_courtship            	  = 16
tc_after_duel            	  = 17
tc_prison_break               = 18
tc_escape               	  = 19
tc_give_center_to_fief        = 20
tc_merchants_house            = 21
#Freelancer Extra END

#Troop Commentaries begin
#Log entry types
#civilian
logent_minorplanet_raided        = 1
logent_minorplanet_extorted      = 2
logent_caravan_accosted          = 3
logent_helped_peasants           = 4

logent_spacestation_captured_by_player        = 10
logent_lord_defeated_by_player                = 11
logent_lord_captured_by_player                = 12
logent_lord_defeated_but_let_go_by_player     = 13
logent_player_defeated_by_lord                = 14
logent_player_retreated_from_lord             = 15
logent_player_retreated_from_lord_cowardly    = 16
logent_lord_helped_by_player                  = 17
logent_player_participated_in_siege           = 18
logent_player_participated_in_major_battle    = 19

logent_pledged_allegiance        = 21
logent_fief_granted_village      = 22
logent_renounced_allegiance      = 23

logent_game_start                           = 31
logent_poem_composed                        = 32 ##Not added
logent_tournament_distinguished             = 33 ##Not added
logent_tournament_won                       = 34 ##Not added


#lord reputation type, for commentaries
#"Martial" will be twice as common as the other types
lrep_none          = 0
lrep_martial       = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome   = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, Shakespeare's Richard III
lrep_selfrighteous = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he borders on upstanding)
lrep_cunning       = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched     = 5 #spiteful, amoral, sadistic, - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured   = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein, poss Ranjit Singh (although roguish), Humayun
lrep_upstanding    = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Sher Shah Suri

#Troop Commentaries end

#Walker types:
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
#SW - increased num_town_walkers (nevermind, I would have to add extra entry points in town scenes...)
num_town_walkers = 8
#num_town_walkers = 12
town_walker_entries_start = 32

reinforcement_cost            = 400

merchant_toll_duration        = 72 #Tolls are valid for 72 hours

#SW - modified hero_escape_after_defeat_chance to be 50%
#hero_escape_after_defeat_chance = 80
hero_escape_after_defeat_chance  = 50

raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end   = "str_surnames_end"
names_begin = "str_name_1"
names_end   = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end   = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end   = countersigns_begin

factions_begin = "fac_player_supporters_faction"
factions_end   = fac_huttcartel + 1
#factions_end = "fac_factions_end"

#Kham
kingdoms_begin = factions_begin
kingdoms_end = factions_end
#Kham - End


#SW - modified faction_ladies_begin to start with faction_ladies_end
#faction_ladies_begin = "trp_knight_1_1_wife"
faction_ladies_begin = "trp_heroes_end"
faction_ladies_end   = "trp_heroes_end"

kings_begin = "trp_galacticempire_lord"
kings_end   = "trp_knight_1_1"

faction_heroes_begin = "trp_galacticempire_lord"
faction_heroes_end   = faction_ladies_begin

reserved_knight_begin = "trp_reserved_knight_1"
reserved_knight_end   = "trp_heroes_end"

heroes_begin = faction_heroes_begin
heroes_end   = faction_ladies_end

companions_begin = "trp_npc1"
companions_end   = "trp_faction_heroes_including_player_begin"

soldiers_begin = "trp_wookiee"
soldiers_end   = "trp_mainplanet_walker_1"

#Rebellion changes

##rebel_factions_begin = "fac_galacticempire_rebels"
##rebel_factions_end   = "fac_factions_end"

#SW - modified  pretenders_begin to start at pretenders_end
#pretenders_begin = "trp_galacticempire_pretender"
pretenders_begin = faction_heroes_end
pretenders_end = faction_heroes_end
#Rebellion changes

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   =  companions_begin

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   =  tavern_minstrels_begin

tavern_fs_trainer_begin = "trp_tavern_bookseller_5"
tavern_fs_trainer_end   = "trp_tavern_bookseller_7"

tavern_ce_merchant_begin = "trp_tavern_bookseller_7"
tavern_ce_merchant_end   = "trp_tavern_bookseller_9"

tavern_iw_merchant_begin = "trp_tavern_bookseller_9"
tavern_iw_merchant_end   = "trp_tavern_bookseller_11"

tavern_dp_merchant_begin = "trp_tavern_bookseller_11"
tavern_dp_merchant_end   = "trp_tavern_bookseller_13"

tavern_ps_merchant_begin = "trp_tavern_bookseller_13"
tavern_ps_merchant_end   = "trp_tavern_bookseller_15"

tavern_fs_merchant_begin = "trp_tavern_bookseller_15"
tavern_fs_merchant_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

#SW - switched mercenaries to start with star wars characters
#mercenary_troops_begin = "trp_watchman"
mercenary_troops_begin = "trp_wookiee"
mercenary_troops_end   = "trp_mercenaries_end"

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

minorplanet_elder_quests_begin = "qst_deliver_grain"
minorplanet_elder_quests_end   = "qst_eliminate_bandits_infesting_village"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = minorplanet_elder_quests_begin

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin


all_quests_begin  = 0
all_quests_end    = "qst_quests_end"

mainplanets_begin = "p_mandalore"

castles_begin     = "p_spacestation_2" # "p_spacestation_1"
minorplanet_begin = "p_minorplanet_1"

mainplanets_end   = castles_begin
castles_end       = minorplanet_begin
minorplanet_end   = p_minorplanet_90 + 1

walled_centers_begin = mainplanets_begin
walled_centers_end   = castles_end

centers_begin = mainplanets_begin
centers_end   = minorplanet_end

#kham extra begin
towns_begin = mainplanets_begin
villages_begin = minorplanet_begin
towns_end = mainplanets_end
villages_end = minorplanet_end
#Kham extra end

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_sun_01"

scenes_begin         = "scn_mainplanet_mandalore_center"
scenes_end           = "scn_spacestation_2_exterior"

spawn_points_begin   = "p_shipyard_trade_federation" #"p_zendar"
spawn_points_end     = "p_spawn_points_end"

regular_troops_begin = "trp_novice_fighter"
regular_troops_end   = "trp_Ramun_the_slave_trader"

#SW
#MF - added this one to use with party speed script.
bandits_begin = "trp_jawa"
bandits_end   = "trp_bountyhunter"

#swadian_merc_parties_begin = "p_town_1_mercs"
#swadian_merc_parties_end   = "p_town_8_mercs"

#vaegir_merc_parties_begin  = "p_town_8_mercs"
#vaegir_merc_parties_end    = "p_zendar"

arena_masters_begin    = "trp_mainplanet_mandalore_arena_master"
arena_masters_end      = "trp_mainplanet_mandalore_armorer"

training_gound_trainers_begin = "trp_trainer_1"
training_gound_trainers_end   = "trp_ransom_broker_1"

town_walkers_begin = "trp_mainplanet_walker_1"
town_walkers_end   = "trp_cantina_walker_1"

slave_dancers_begin = "trp_mainplanet_walker_twilek_female_slave"
slave_dancers_end   = "trp_mainplanet_walker_chiss"

town8_walkers_begin = "trp_mainplanet_walker_geonosian"
town8_walkers_end   = "trp_mainplanet_walker_wookiee"

town9_walkers_begin = "trp_mainplanet_walker_moncal"
town9_walkers_end   = "trp_mainplanet_walker_geonosian"

town10_walkers_begin = "trp_mainplanet_walker_wookiee"
town10_walkers_end   = "trp_mainplanet_walker_gamorrean"

town12_walkers_begin = "trp_mainplanet_walker_gamorrean"
town12_walkers_end   = "trp_mainplanet_walker_empire_1"

town14_walkers_begin = "trp_mainplanet_walker_1"    #includes a jawa
town14_walkers_end   = "trp_mainplanet_walker_moncal"

town17_walkers_begin = "trp_mainplanet_walker_twilek"
town17_walkers_end   = "trp_mainplanet_walker_chiss"

#Added custom wakers by Swyter -->>
iridonia_walkers_begin = "trp_mainplanet_walker_zabrak"
iridonia_walkers_end   = "trp_mainplanet_walker_zabrak"

pzob_walkers_begin = "trp_mainplanet_walker_gamorrean"
pzob_walkers_end   = "trp_mainplanet_walker_gamorrean"

rodia_walkers_begin = "trp_mainplanet_walker_rodian"
rodia_walkers_end   = "trp_mainplanet_walker_rodian"

bothaw_moon_walkers_begin = "trp_mainplanet_walker_bothan"
bothaw_moon_walkers_end   = "trp_mainplanet_walker_bothan"
#@>SWY-->>
town_walkers_neutral_begin = town_walkers_begin
town_walkers_neutral_end   = "trp_mainplanet_walker_jawa"

town_walkers_empire_begin = "trp_mainplanet_walker_empire_1"
town_walkers_empire_end   = "trp_mainplanet_walker_rebel_1"

town_walkers_rebel_begin = "trp_mainplanet_walker_rebel_1"
town_walkers_rebel_end   = "trp_mainplanet_walker_hutt_1"

town_walkers_hutt_begin = "trp_mainplanet_walker_hutt_1"
town_walkers_hutt_end   = "trp_cantina_walker_1"

minorplanet_walkers_begin = "trp_minorplanet_walker_1"
minorplanet_walkers_end   = "trp_spy_walker_1"

assassins_begin = "trp_assassin_male"
assassins_end   = "trp_Ramun_the_slave_trader"

spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end   = "trp_assassin_male"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

#SW - new cantina_walkers
cantina_walkers_begin  = "trp_cantina_walker_1"
cantina_walkers_end    = "trp_cantina_drinker_1"

cantina_drinkers_begin = "trp_cantina_drinker_1"
cantina_drinkers_end   = "trp_minorplanet_walker_1"

armor_merchants_begin  = "trp_mainplanet_mandalore_armorer"
armor_merchants_end    = "trp_mainplanet_mandalore_weaponsmith"

weapon_merchants_begin = "trp_mainplanet_mandalore_weaponsmith"
weapon_merchants_end   = "trp_mainplanet_mandalore_bartender"

tavernkeepers_begin    = "trp_mainplanet_mandalore_bartender"
tavernkeepers_end      = "trp_mainplanet_mandalore_merchant"

goods_merchants_begin  = "trp_mainplanet_mandalore_merchant"
goods_merchants_end    = "trp_mainplanet_mandalore_horse_merchant"

horse_merchants_begin  = "trp_mainplanet_mandalore_horse_merchant"
horse_merchants_end    = "trp_mainplanet_mandalore_mayor"

mayors_begin           = "trp_mainplanet_mandalore_mayor"
mayors_end             = "trp_minorplanet_admin_1"

planet_admins_begin    = "trp_minorplanet_admin_1"
planet_admins_end      = "trp_merchants_end"


average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

minorplanet_prod_min = -5
minorplanet_prod_max = 18

trade_goods_begin            = "itm_smoked_fish"
trade_goods_end              = "itm_siege_supply"
food_begin                   = "itm_smoked_fish"
food_end                     = "itm_wine"
reference_books_begin        = "itm_book_wound_treatment_reference"
reference_books_end          =  trade_goods_begin
readable_books_begin         = "itm_book_tactics"
readable_books_end           =  reference_books_begin
books_begin                  =  readable_books_begin
books_end                    =  reference_books_end
#SW - modified horses, weapons, ranged, armors, shields begin/end
horses_begin                 = "itm_horses_begin"
horses_end                   = "itm_horses_end"
pistol_ammo_begin            = "itm_laser_bolts_green_pistol"
pistol_ammo_end              = "itm_laser_bolts_green_rifle"
rifle_ammo_begin             = "itm_laser_bolts_green_rifle"
rifle_ammo_end               = "itm_laser_bolts_training_pistol"
force_power_begin            = "itm_force_power_ls_1"
force_power_end              = "itm_force_jump"
weapons_begin                = "itm_weapons_begin"
weapons_end                  = "itm_weapons_end"
ranged_weapons_begin         = "itm_ranged_weapons_begin"
ranged_weapons_end           = "itm_ranged_weapons_end"
armors_begin                 = "itm_armors_begin"
armors_end                   = "itm_armors_end"
shields_begin                = "itm_shields_begin"
shields_end                  = "itm_shields_end"
shield_bash_begin            = "itm_shield_bash_begin"
shield_bash_end              = "itm_shield_bash_end"
shield_bash_lightsaber_begin = "itm_lightsaber_block_blue"
shield_bash_lightsaber_end   = "itm_shields_end"
#SW for special weapon noise
slot_agent_attack_sound = 230  #can be any number not already in use
lightsaber_noise_begin  = "itm_lightsaber_green_arena"
lightsaber_noise_end    = "itm_melee_punch"

#SW for spaceship
spaceship_empire_begin       = "p_spaceship_tie_fighter"
spaceship_empire_end         = "p_spaceship_a_wing"
spaceship_rebel_corel_begin  = "p_spaceship_corellian_gunship"
spaceship_rebel_corel_end    = "p_spaceship_hutt_patrol"
spaceship_rebel_moncal_begin = "p_spaceship_moncal_cruiser"
spaceship_rebel_moncal_end   = "p_spaceship_rebel_transport"
spaceship_rebel_begin        = "p_spaceship_a_wing"
spaceship_rebel_end          = "p_spaceship_hutt_patrol"
spaceship_hutt_begin         = "p_spaceship_hutt_patrol"
spaceship_hutt_end           = "p_spaceship_z95"
spaceship_other_begin        = "p_spaceship_z95"
spaceship_other_end          = "p_spaceship_end"
spaceship_hutt_other_begin   =  spaceship_hutt_begin
spaceship_hutt_other_end     =  spaceship_other_end
spaceship_all_begin          =  spaceship_empire_begin
spaceship_all_end            =  spaceship_other_end

# Banner constants
banner_meshes_begin                  = "mesh_banner_a01"
#SW - modified banner_meshes_end_minus_one so only a few banners are displayed for the banner selection
#banner_meshes_end_minus_one         = "mesh_banner_f21"
banner_meshes_end_minus_one          = "mesh_banner_c01"

arms_meshes_begin                    = "mesh_arms_a01"
arms_meshes_end_minus_one            = "mesh_arms_cu"
#@>SWY arms_meshes_end_minus_one     = "mesh_arms_f21"

faction_meshes_begin                 = "mesh_pic_arms_swadian"
faction_meshes_end_minus_one         = "mesh_pic_arms_nord"

custom_banner_charges_begin          = "mesh_custom_banner_charge_01"
custom_banner_charges_end            = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin      = "mesh_custom_banner_bg"
custom_banner_backgrounds_end        =  custom_banner_charges_begin

custom_banner_flag_types_begin       = "mesh_custom_banner_01"
custom_banner_flag_types_end         =  custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin   = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end     =  custom_banner_flag_types_begin

custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
custom_banner_flag_scene_props_end   = "spr_banner_a"

custom_banner_map_icons_begin        = "icon_custom_banner_01"
custom_banner_map_icons_end          = "icon_banner_01"

banner_map_icons_begin               = "icon_banner_01"
banner_map_icons_end_minus_one       = icon_banner_42+1

banner_scene_props_begin             = "spr_banner_a"
banner_scene_props_end_minus_one     = "spr_banner_cu"
#banner_scene_props_end_minus_one    = "spr_banner_f21"

khergit_banners_begin_offset = 63
khergit_banners_end_offset   = 84

# Some constants for merchant invenotries
#SW - increased merchant_inventory_space
#merchant_inventory_space = 30
merchant_inventory_space  = 60
num_merchandise_goods     = 40

num_max_river_pirates            = 25
num_max_zendar_peasants          = 25
num_max_zendar_bountyhunters     = 10

num_max_dp_bandits               = 10
num_max_refugees                 = 10
num_max_deserters                = 10

num_max_militia_bands            = 15
num_max_armed_bands              = 12

num_max_vaegir_punishing_parties = 20
num_max_rebel_peasants           = 25

num_max_frightened_farmers       = 50
num_max_undead_messengers        = 20

num_blazing_claw_pirate_spawn_points = 3
num_black_sun_pirate_spawn_points    = 3
num_night_fang_pirate_spawn_points   = 3
#num_black_khergit_spawn_points      = 1
num_tusken_raider_spawn_points       = 3

#SW - modified peak constants
#peak_prisoner_trains    = 4
#peak_faction_caravans   = 12
#peak_faction_messengers = 3
peak_prisoner_trains     = 10
#SW - peak_faction_caravans does not appear to be used, I also modified this value in create_faction_party_if_below_limit in module_scripts.py
peak_faction_caravans    = 24
peak_faction_messengers  = 10


# Note positions
note_troop_location = 3

#battle tactics
btactic_hold          = 1
btactic_follow_leader = 2
btactic_charge        = 3
btactic_stand_ground  = 4

#default right mouse menu orders
cmenu_follow = -6
cmenu_move   = -7

# Town center modes
tcm_default   = 0
tcm_disguised = 1

# Arena battle modes
#abm_fight     = 0
abm_training   = 1
abm_visit      = 2
abm_tournament = 3

# Camp training modes
ctm_melee    = 1
ctm_ranged   = 2
ctm_mounted  = 3
ctm_training = 4

# Village bandits attack modes
vba_normal          = 1
vba_after_training  = 2

#SW - increased prizes (previously were 5, 10, 25, 60, 250)
arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 25
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 50
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 100
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 200
arena_grand_prize = 500

#Tavern recruitment and ale
merc_parties_begin = "p_town_merc_1"
merc_parties_end   = "p_spacestation_2" #"p_spacestation_1"

########################################################
##  COLOR CODES             ############################
########################################################
# HC - Add in color codes
color_great_news             = 0x00FF00
color_good_news              = 0x50FF50
color_terrible_news          = 0xFF2222
color_bad_news               = 0xFF5050
color_neutral_news           = 0xFFCC66
color_quest_and_faction_news = 0x66CCFF
color_hero_news              = 0xFFFF00

 ########################################################
##  NEWS TYPES              ############################
 ########################################################
# HC - Just an enumeration of news types to be used as a script parameter
news_lord_defeated             = 1
news_lord_captured             = 2
news_lord_freed                = 3
news_lord_escaped              = 4
news_minorplanet_looted        = 5
news_center_captured           = 6
news_center_under_siege        = 7
news_center_siege_lifted       = 8
news_center_prosperity_changed = 9

# Duel Mod Troop Slots
slot_troop_duel_won          = 142      #duel mod - how many duels player won against this troop
slot_troop_duel_lost         = 143      #duel mod - how many duels player lost against this troop
slot_troop_duel_started      = 144      #duel mod - if player started dueling with this troop

#Rubik's Easy regulars upgrading kit -- http://forums.taleworlds.com/index.php/topic,8652.msg1689787.html#msg1689787
slot_root_troop = 166

# Duel mod constants
#king_renown_for_duel = 150      # Minimum renown needed to challenge a king to a friendly duel
king_renown_for_duel  =   0      # Minimum renown needed to challenge a king to a friendly duel
#lord_renown_for_duel =  50      # Minimum renown needed to challenge a king to a friendly duel
lord_renown_for_duel  =   0      # Minimum renown needed to challenge a king to a friendly duel

#SW - new music modes
music_mode_map     = 0
music_mode_town    = 1
music_mode_cantina = 2
music_mode_arena   = 3

#SW - signs
sw_all_sign_begin      = "spr_sw_sign_a"
sw_all_sign_end        = "spr_sw_poster_random_all_1"
sw_empire_sign_begin   = "spr_sw_sign_a"
sw_empire_sign_end     = "spr_sw_sign_b"
sw_rebel_sign_begin    = "spr_sw_sign_b"
sw_rebel_sign_end      = "spr_sw_sign_e"
sw_generic_sign_begin  = "spr_sw_sign_e"
sw_generic_sign_end    = "spr_sw_poster_random_all_1"
#SW - posters
sw_all_poster_begin    = "spr_sw_poster_a"
sw_all_poster_end      = "spr_sw_ship_bed"
sw_empire_poster_begin = "spr_sw_poster_a"
sw_empire_poster_end   = "spr_sw_poster_b"
sw_rebel_poster_begin  = "spr_sw_poster_b"
sw_rebel_poster_end    = "spr_sw_poster_e"
sw_generic_poster_begin= "spr_sw_poster_e"
sw_generic_poster_end  = "spr_sw_ship_bed"

#SW - Bounty Hunting Begin - http://forums.taleworlds.com/index.php/topic,59300.0.html
bounties_begin = "qst_bounty_1"
bounties_end   = "qst_kill_local_merchant"

bounty_1_targets_begin = "trp_bounty_target_1a"
bounty_1_targets_end   = "trp_bounty_target_2a"
bounty_2_targets_begin = "trp_bounty_target_2a"
bounty_2_targets_end   = "trp_bounty_target_3a"
bounty_3_targets_begin = "trp_bounty_target_3a"
bounty_3_targets_end   = "trp_bounty_target_4a"
bounty_4_targets_begin = "trp_bounty_target_4a"
bounty_4_targets_end   = "trp_bounty_target_5a"
bounty_5_targets_begin = "trp_bounty_target_5a"
bounty_5_targets_end   = "trp_bounty_target_6a"
bounty_6_targets_begin = "trp_bounty_target_6a"
bounty_6_targets_end   = "trp_quick_battle_player"



#--> Human Bone Mapping by Swyter
hb_abdomen   = 0
hb_thigh_l   = 1
hb_calf_l    = 2
hb_foot_l    = 3
hb_thigh_r   = 4
hb_calf_r    = 5
hb_foot_r    = 6
hb_spine     = 7
hb_thorax    = 8
hb_head      = 9
hb_shoulder_l= 10
hb_upperarm_l= 11
hb_forearm_l = 12
hb_hand_l    = 13
hb_item_l    = 14
hb_shoulder_r= 15
hb_upperarm_r= 16
hb_forearm_r = 17
hb_hand_r    = 18
hb_item_r    = 19
# <-

#--> Horse Bone Mapping by Swyter
hrsb_pelvis      = 0
hrsb_spine_1     = 1
hrsb_spine_2     = 2
hrsb_spine_3     = 3
hrsb_neck_1      = 4
hrsb_neck_2      = 5
hrsb_neck_3      = 6
hrsb_head        = 7
hrsb_l_clavicle  = 8
hrsb_l_upper_arm = 9
hrsb_l_forearm   = 10
hrsb_l_hand      = 11
hrsb_l_front_hoof= 12
hrsb_r_clavicle  = 13
hrsb_r_upper_arm = 14
hrsb_r_forearm   = 15
hrsb_r_hand      = 16
hrsb_r_front_hoof= 17
hrsb_l_thigh     = 18
hrsb_l_calf      = 19
hrsb_l_foot      = 20
hrsb_l_back_hoof = 21
hrsb_r_thigh     = 22
hrsb_r_calf      = 23
hrsb_r_foot      = 24
hrsb_r_back_hoof = 25
hrsb_tail_1      = 26
hrsb_tail_2      = 27
# <-

#Speech aliases
speech_death    = 3
speech_victory  = 2
speech_deployed = 1



#autofire begin
slot_agent_firearm_wander = 30
slot_agent_autofire_ready = 31
#autofire end

#autofire begin
slot_item_accuracy = 62
slot_item_shoot_speed = 63
slot_item_speed_rating = 64
slot_item_sound = 65
#autofire end

slot_item_auto_fire_capability = 15

#Kham Added Constants

# VC Presentantion Constants
font_title = 2400
font_small = 800
font_normal = 1200

# shows mouse coordinates on presentations (set 0 for production)
debug_show_presentation_coordinates = 0

#VC Troop Tree Presentation
#Presentations Constants Moto chief
Screen_Border_Width = 24
Screen_Width = 1024-Screen_Border_Width
Screen_Height = 768-Screen_Border_Width
Screen_Text_Height = 35
Screen_Checkbox_Height_Adj = 4
Screen_Numberbox_Width = 64
Screen_Title_Height = Screen_Height-Screen_Border_Width-Screen_Text_Height
Screen_Check_Box_Dimension = 20
Screen_Undistort_Width_Num = 7  #distortion midway between 1024x768 and 1366x768 -- things will appear a little narrow on thin screens and vice versa
Screen_Undistort_Width_Den = 8
Troop_Tree_Num_Levels = 6
Troop_Tree_Max_Per_Level = 5  #2^(Troop_Tree_Num_Levels-1) opt for counting most upgrade2 over all factions
Troop_Tree_Area_Height = Screen_Title_Height-4*Screen_Text_Height
Troop_Tree_Area_Width = Screen_Width-2*Screen_Border_Width
Troop_Tree_Line_Color = 0x000000
Troop_Tree_Tableau_Height = 800
Troop_Tree_Tableau_Width = Troop_Tree_Tableau_Height*Screen_Undistort_Width_Num/Screen_Undistort_Width_Den

#+FREELANCER start
freelancer_version = 13
freelancer_can_use_item  = "script_troop_can_use_item" 

#Party Slots
slot_party_orig_morale = 280
slot_freelancer_equip_start = 100 #only used for freelancer_party_backup
slot_freelancer_version     = slot_freelancer_equip_start - 2 #only used for freelancer_party_backup

#Faction Slot
slot_faction_freelancer_troop = 101 #should be unused
slot_faction_freelancer_captain = 163 #Kham - To Check if Player is Sarge/Captain (1 or 2)

slot_faction_tier_1_archer        = 164

#Troop Slots
slot_troop_freelancer_start_xp   =  slot_troop_signup   #110 -only used for player
slot_troop_freelancer_start_date =  slot_troop_signup_2 #111 -only used for player

plyr_mission_vacation = 1
slot_freelancer_mission = 162

tc_vacation_over = 22
slot_freelancer_rank = 113 #track how many upgrades the player has had in their faction.
tc_freelancer_infantry_captain = 114 #To Reward Player as an Infantry Sarge / Captain
tc_freelancer_ranged_captain = 115 #To Reward Player as an Ranged Sarge / Captain

#+Freelancer end

message_positive = 0x33FF33
message_negative = 0xFF3333
message_neutral = 0xFFFF33

#Deflection AI - Kham
slot_agent_deflection_max = 45

# Auto Fire Weapon slot

# Racial Restrictions

slot_troop_helm_type = 164
slot_troop_armor_type = 165
slot_troop_boots_type = 166
slot_troop_horse_type = 167

slot_item_race = 66

slot_agent_is_running_away = 48
skirmish_min_distance = 1500 #Min distance you wish maintained, in cm. Where agent will retreat
skirmish_max_distance = 2000 #Max distance to maintain, in cm. Where agent will stop retreating