# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...

def wp(x):
  n = 0
  r = 1 + int(x / 100)
  n |= wp_one_handed(x + random.randrange(r))
  n |= wp_two_handed(x + random.randrange(r))
  n |= wp_polearm(x + random.randrange(r))
  #n |= wp_archery(x + random.randrange(r))
  n |= wp_crossbow(x + random.randrange(r))
  n |= wp_throwing(x + random.randrange(r))
  #SW - add firearm
  n |= wp_firearm(x + random.randrange(r))
  return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
  n |= wp_one_handed(x + random.randrange(r))
  n |= wp_two_handed(x + random.randrange(r))
  n |= wp_polearm(x + random.randrange(r))
  return n

#Skills
#SW - modified knows_common
#knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_tactics_1|knows_shield_1
knows_common_2 = knows_riding_2|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_2|knows_ironflesh_2|knows_power_strike_2|knows_athletics_2|knows_tactics_1|knows_shield_2
knows_common_3 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3|knows_ironflesh_3|knows_power_strike_3|knows_athletics_3|knows_tactics_2|knows_shield_3
knows_common_4 = knows_riding_4|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_4|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4|knows_tactics_2|knows_shield_4

knows_arena_1 = knows_riding_2|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3|knows_ironflesh_2|knows_power_strike_1|knows_athletics_1|knows_tactics_1|knows_shield_2|knows_power_draw_6|knows_power_throw_5|knows_weapon_master_4
knows_arena_2 = knows_riding_2|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_4|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_tactics_3|knows_shield_3|knows_power_draw_6|knows_power_throw_5|knows_weapon_master_5
knows_arena_3 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_5|knows_ironflesh_6|knows_power_strike_5|knows_athletics_5|knows_tactics_5|knows_shield_4|knows_power_draw_6|knows_power_throw_6|knows_weapon_master_6
knows_arena_4 = knows_riding_4|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_6|knows_ironflesh_8|knows_power_strike_6|knows_athletics_7|knows_tactics_7|knows_shield_5|knows_power_draw_6|knows_power_throw_6|knows_weapon_master_6

def_attrib = str_10 | agi_8 | int_6 | cha_6
def_attrib_1 = str_12 | agi_10 | int_8 | cha_8
def_attrib_2 = str_14 | agi_12 | int_10 | cha_10
def_attrib_3 = str_16 | agi_14 | int_12 | cha_12
def_attrib_4 = str_18 | agi_16 | int_14 | cha_14

def_attrib_force_1 = str_24 | agi_18 | int_10 | cha_10
def_attrib_force_2 = str_26 | agi_22 | int_14 | cha_14
def_attrib_force_3 = str_28 | agi_26 | int_18 | cha_18
def_attrib_force_4 = str_30 | agi_30 | int_22 | cha_22

knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_horse_archery_3|knows_athletics_3|knows_weapon_master_2|knows_ironflesh_1|knows_power_strike_2|knows_riding_3|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_horse_archery_3|knows_athletics_3|knows_riding_3|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_horse_archery_3|knows_riding_3|knows_weapon_master_1|knows_athletics_3|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_30|agi_25|int_25|cha_25|level(50)

knight_attrib_1 = str_22|agi_18|int_8|cha_16|level(25)
knight_attrib_2 = str_24|agi_20|int_10|cha_18|level(30)
knight_attrib_3 = str_26|agi_22|int_12|cha_20|level(35)
knight_attrib_4 = str_28|agi_24|int_13|cha_22|level(40)
knight_attrib_5 = str_30|agi_26|int_20|cha_20|level(45)

# knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3|knows_shield_3
# knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5|knows_shield_4
# knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6|knows_shield_5
# knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7|knows_shield_6
# knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9|knows_shield_7

#SW - modified knight skills for star wars knights
starwars_knight_skills_1 = knows_riding_4|knows_ironflesh_8|knows_power_strike_6|knows_athletics_6|knows_tactics_6|knows_prisoner_management_5|knows_leadership_5|knows_power_throw_6|knows_weapon_master_1|knows_shield_6|knows_horse_archery_4|knows_trainer_4|knows_deflection_5
starwars_knight_skills_2 = knows_riding_5|knows_ironflesh_9|knows_power_strike_7|knows_athletics_7|knows_tactics_7|knows_prisoner_management_6|knows_leadership_6|knows_power_throw_7|knows_weapon_master_1|knows_shield_7|knows_horse_archery_5|knows_trainer_5|knows_deflection_6
starwars_knight_skills_3 = knows_riding_6|knows_ironflesh_10|knows_power_strike_8|knows_athletics_8|knows_tactics_8|knows_prisoner_management_7|knows_leadership_7|knows_power_throw_8|knows_weapon_master_1|knows_shield_8|knows_horse_archery_6|knows_trainer_6|knows_deflection_7
starwars_knight_skills_4 = knows_riding_7|knows_ironflesh_10|knows_power_strike_9|knows_athletics_9|knows_tactics_9|knows_prisoner_management_8|knows_leadership_8|knows_power_throw_9|knows_weapon_master_1|knows_shield_9|knows_horse_archery_7|knows_trainer_7|knows_deflection_8
starwars_knight_skills_5 = knows_riding_8|knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_tactics_10|knows_prisoner_management_9|knows_leadership_9|knows_power_throw_10|knows_weapon_master_1|knows_shield_10|knows_horse_archery_8|knows_trainer_8|knows_deflection_10

#SW - added default skills for troops
starwars_skills_1 = knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_weapon_master_1|knows_shield_2|knows_athletics_3|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_2 = knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_weapon_master_1|knows_shield_3|knows_athletics_4|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_3 = knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_1|knows_shield_4|knows_athletics_5|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_4 = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_weapon_master_1|knows_shield_5|knows_athletics_6|knows_tactics_4|knows_leadership_4|knows_trainer_2

starwars_skills_melee_1 = knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_1|knows_shield_5|knows_athletics_5|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_melee_2 = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_weapon_master_1|knows_shield_6|knows_athletics_6|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_melee_3 = knows_ironflesh_7|knows_power_strike_7|knows_power_throw_6|knows_weapon_master_1|knows_shield_7|knows_athletics_7|knows_tactics_5|knows_leadership_5|knows_trainer_3
starwars_skills_melee_4 = knows_ironflesh_8|knows_power_strike_8|knows_power_throw_7|knows_weapon_master_1|knows_shield_8|knows_athletics_8|knows_tactics_5|knows_leadership_5|knows_trainer_3

starwars_skills_mounted_1 = knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_weapon_master_1|knows_shield_2|knows_athletics_3|knows_riding_4|knows_horse_archery_4|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_mounted_2 = knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_weapon_master_1|knows_shield_3|knows_athletics_4|knows_riding_5|knows_horse_archery_5|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_mounted_3 = knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_1|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_mounted_4 = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_weapon_master_1|knows_shield_5|knows_athletics_6|knows_riding_8|knows_horse_archery_8|knows_tactics_4|knows_leadership_4|knows_trainer_2

starwars_skills_force_1 = knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_weapon_master_1|knows_shield_4|knows_athletics_7|knows_riding_3|knows_horse_archery_4|knows_tactics_4|knows_leadership_4|knows_trainer_2|knows_power_draw_4 |knows_deflection_4
starwars_skills_force_2 = knows_ironflesh_8|knows_power_strike_8|knows_power_throw_6|knows_weapon_master_1|knows_shield_5|knows_athletics_8|knows_riding_4|knows_horse_archery_4|knows_tactics_5|knows_leadership_5|knows_trainer_2|knows_power_draw_6 |knows_deflection_6
starwars_skills_force_3 = knows_ironflesh_9|knows_power_strike_9|knows_power_throw_7|knows_weapon_master_1|knows_shield_6|knows_athletics_9|knows_riding_5|knows_horse_archery_5|knows_tactics_6|knows_leadership_6|knows_trainer_3|knows_power_draw_8 |knows_deflection_8
starwars_skills_force_4 = knows_ironflesh_10|knows_power_strike_10|knows_power_throw_8|knows_weapon_master_1|knows_shield_7|knows_athletics_10|knows_riding_6|knows_horse_archery_5|knows_tactics_7|knows_leadership_7|knows_trainer_3|knows_power_draw_10 |knows_deflection_10

#droid attributes
droid_attrib_1 = str_3|int_8|cha_3  # zero agility (so they move slow)
droid_attrib_2 = str_3|int_16|cha_3 # zero agility (so they move slow)

#droid skills
droid_skills_1 = knows_ironflesh_6|knows_tactics_2|knows_leadership_2|knows_trainer_2
droid_skills_2 = knows_ironflesh_8|knows_tactics_4|knows_leadership_4|knows_trainer_4

# give outlaws lower riding skills so their ships move slower on the world map
starwars_skills_outlaws_1 = knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_weapon_master_1|knows_shield_2|knows_athletics_3|knows_riding_1|knows_horse_archery_3|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_outlaws_2 = knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_weapon_master_1|knows_shield_3|knows_athletics_4|knows_riding_1|knows_horse_archery_3|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_outlaws_3 = knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_1|knows_shield_4|knows_athletics_5|knows_riding_1|knows_horse_archery_4|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_outlaws_4 = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_weapon_master_1|knows_shield_5|knows_athletics_6|knows_riding_1|knows_horse_archery_4|knows_tactics_4|knows_leadership_4|knows_trainer_2

# default npc skills/attrib
starwars_npc_skills = knows_ironflesh_2|knows_power_strike_1|knows_power_throw_1|knows_weapon_master_1|knows_shield_1|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_tactics_1|knows_leadership_1|knows_trainer_1
starwars_npc_attrib = str_10 | agi_10 | int_8 | cha_8

# Mando - Clone Skills
clone_skills_1 = knows_ironflesh_4|knows_power_strike_6|knows_power_throw_5|knows_weapon_master_1|knows_shield_5|knows_athletics_6|knows_riding_3|knows_horse_archery_4|knows_tactics_4|knows_leadership_4|knows_trainer_2


# SW (HC) - Guarantee constants
tf_guarantee_all_armor = tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_boots

#sw_npc_jedi = sw_npc_basic|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_4|knows_tactics_4|knows_leadership_4
#sw_npc_warrior = sw_npc_basic|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_4|knows_tactics_2|knows_leadership_2
#sw_npc_tracker = sw_npc_basic|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_4|knows_tactics_2|knows_leadership_2
#sw_npc_merchant

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

#SW - face codes

#@> // Swyter's Face codes //

#Male
swc_brunette_m_hero = 0x000000003d0090562d5ab4a56d918acb0000000000f5c9550000000000000000
swc_brunette_m_thug = 0x0000000dfd0080562d5ab4a56d918acb0000000000e9c9490000000000000000
swc_brunette_m_thug_2 =0x0000000dfd00c0552d5ab4a56d918acb0000000000e9c9490000000000000000

swc_blonde_m_neutral = 0x0000000ec300c1432d5a951b6d918acb0000000000e9c9490000000000000000
swc_blonde_m_neutral_2 = 0x0000000da900a0012d5a951b6d918acb0000000000e9c9490000000000000000

swc_blonde_m_good = 0x0000000f8800c0815861d13484c9c9e20000000000e9c29d0000000000000000
swc_blonde_m_good_2 = 0x0000000f8800c0815861d13484c9c9e20000000000e9c29d0000000000000000

#Female
# swc_brunette_f_neutral =
# swc_brunette_f_neutral_2 =
# swc_blonde_f_neutral =
# swc_blonde_f_neutral_2 =

#Weequay
swc_weequay = 0x0000000d8a0160002793b35442a9bd230000000000f9272d0000000000000000
swc_weequay_2 = 0x0000000d8a01500027bbb35bc0a9bd230000000000fd2f280000000000000000


sw_player_face = 0x000000003f00c00136db6db6db6db6db0000000000e936db0000000000000000
#sw_player_face = 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000    #original code from native
#sw_player_face =   # NEW   
sw_woman_face_1    = 0x00000001be00000336db6db6db6db6db00000000001db6db0000000000000000
#sw_woman_face_1    = 0x0000000000000001249249480029249200000000001d24920000000000000000
sw_woman_face_2    = 0x0000000cff00700849246e480092492400000000001e49240000000000000000
#sw_woman_face_2    = 0x0000000cff00700849246e480092492400000000001e49240000000000000000
sw_woman_face_3   = 0x000000018b000006361b8db6db6dbefb00000000001db6db0000000000000000
## cute woman code:
## 0x0000000035004003472269c4ddb0a6da00000000001f35a90000000000000000

sw_slave_dancer_face1 = 0x0000000000000001249249249249249200000000001d24920000000000000000
sw_slave_dancer_face2 = 0x000000003f0060085b65b6b6dbb6db6d00000000001e49240000000000000000
sw_man_face_1 = 0x0000000000000001249249249249249200000000001c924b0000000000000000
sw_man_face_2 = 0x0000000fff006287492492491c924b6d00000000001edb230000000000000000
sw_rebel_face_1 = 0x0000000000000001249249249249249200000000001d24930000000000000000
sw_rebel_face_2 = 0x0000000fff006287492492491c924b6d00000000001edb230000000000000000
sw_imperial_face_1 = 0x000000003f000001249249249249249200000000001c924b0000000000000000
sw_imperial_face_2 = 0x0000000fff005005492492491392492400000000001e49230000000000000000
sw_hutt_face_1 = 0x0000000000000001249249249249249200000000001d24930000000000000000
sw_hutt_face_2 = 0x0000000fff01034e492492491c924b6d00000000001edb230000000000000000
sw_bandit_face_1  = sw_hutt_face_1
sw_bandit_face_2  = sw_hutt_face_2
sw_sith_face_1 = 0x0000000000011000249249249249249200000000001d24530000000000000000
sw_sith_face_2 = 0x0000000fff011000492492491c92492400000000001e49230000000000000000
#alien face textures
wookiee_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
wookiee_face2 = 0x0000000fff001000000000000000000000000000000000000000000000000000
mandalorian_face1 = 0x0000000fc0007001249249249249249200000000001d24930000000000000000
mandalorian_face2 = 0x0000000fff00c185492492491c92492400000000001e49230000000000000000
twilek_female_face1 = 0x0000000000000000124924929244949200000000001c92490000000000000000
twilek_female_face2 = 0x0000000d00002000492492491b92492400000000001e49240000000000000000
twilek_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
twilek_face2 = 0x0000000aab003000000000000000000000000000000000000000000000000000
rodian_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
rodian_face2 = 0x0000000fff002000000000000000000000000000000000000000000000000000
chiss_face1 = 0x0000000000014001249249249249249200000000001d24530000000000000000
chiss_face2 = 0x0000000fff014005492492491c92492400000000001e49230000000000000000
chiss_female_face1 = 0x000000003500a003472269c4ddb0a6da00000000001f35a90000000000000000
chiss_female_face2 = 0x000000003700a0011c6b7293a4484b6400000000001ca76b0000000000000000
weequay_face1 = 0x000000000001500c249249249249249200000000001d24930000000000000000
weequay_face2 = 0x0000000fff01600c492492491c92492400000000001e49230000000000000000
#clone_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
#clone_face2 = 0x0000000fff001000000000000000000000000000000000000000000000000000
bothan_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
bothan_face2 = 0x0000000fff000003000000000000000000000000000000000000000000000000
sw_zabrak_face_1 = 0x000000018000119735c22e7f632a053f0000000000f5b1c70000000000000000
sw_zabrak_face_2 = 0x000000018000415735c22e7f632a053f0000000000f5b1c70000000000000000

#single face texture only
trandoshan_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
trandoshan_face2 = 0x0000000fff001000000000000000000000000000000000000000000000000000
gamorrean_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
gamorrean_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
hutt_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
hutt_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
moncal_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
moncal_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
droid_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
droid_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
tusken_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
tusken_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
jawa_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
jawa_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
sullustan_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
sullustan_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
geonosian_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
geonosian_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
nemoidian_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
nemoidian_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000


#NAMES:
#



troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
  #SW BSG integration
  #["player","Player","Player",tf_hero|tf_unmoveable_in_party_window|tf_inactive,no_scene,reserved,fac_player_faction,
   #to release
[],
    str_6|agi_6|int_6|cha_6,wp_one_handed(30)|wp_two_handed(30)|wp_polearm(30)|wp_crossbow(35)|wp_throwing(30)|wp_firearm(45),0,swc_brunette_m_hero],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_laser_bolts_red_pistol,itm_dh17],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],
####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_trandoshan|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_durasteel_mace],
   str_6|agi_6|level(1),wp(50),knows_common, trandoshan_face1, trandoshan_face2],
  ["tutorial_archer","Marksman","Marksman",tf_rodian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_dl44a_training,itm_laser_bolts_training_pistol,itm_arena_tunic_green],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4, rodian_face1, rodian_face2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_lightsaber_red,itm_arena_tunic_red],
   str_6|agi_6|level(5),wp(80),knows_common, sw_sith_face_1, sw_sith_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_moncal|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_ind_clothes_outfsmuggler_green],
   str_14|agi_9|level(9),wp(100)|wp_archery(100),knows_arena_1,moncal_face1, moncal_face2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_twilek|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_ind_clothes_outfsmuggler_green],
   str_14|agi_11|level(14),wp(125)|wp_archery(125),knows_arena_2,twilek_face1, twilek_face2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_trandoshan|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,0,fac_commoners,
   [],
   str_14|agi_14|level(19),wp(150)|wp_archery(150),knows_arena_3,trandoshan_face1, trandoshan_face2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_ind_clothes_outfsmuggler_green],
   str_16|agi_16|level(23),wp(175)|wp_archery(175),knows_arena_4,mandalorian_face1, mandalorian_face2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arena_tunic_white],
   str_14|agi_9|level(9),wp(100)|wp_archery(100),knows_arena_1,sw_man_face_1, sw_man_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_twilek|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arena_tunic_white],
   str_14|agi_9|level(9),wp(100)|wp_archery(100),knows_arena_1,twilek_face1, twilek_face2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_weequay|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arena_tunic_yellow],
   str_14|agi_11|level(14),wp(125)|wp_archery(125),knows_arena_2, weequay_face1, weequay_face2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_sullustan|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arena_tunic_yellow],
   str_14|agi_11|level(14),wp(125)|wp_archery(125),knows_arena_2,sullustan_face1, sullustan_face2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_moncal|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arena_tunic_yellow],
   str_14|agi_11|level(14),wp(125)|wp_archery(125),knows_arena_2,moncal_face1, moncal_face2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_chiss|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arena_tunic_green],
   str_14|agi_14|level(19),wp(150)|wp_archery(150),knows_arena_3,chiss_face1, chiss_face2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_rodian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arena_tunic_green],
   str_14|agi_14|level(19),wp(150)|wp_archery(150),knows_arena_3,rodian_face1, rodian_face2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_bothan|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arena_tunic_green],
   str_14|agi_14|level(19),wp(150)|wp_archery(150),knows_arena_3,bothan_face1, bothan_face2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_trandoshan|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [],
   str_16|agi_16|level(23),wp(175)|wp_archery(175),knows_arena_4,trandoshan_face1, trandoshan_face2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arena_tunic_red],
   str_16|agi_16|level(23),wp(175)|wp_archery(175),knows_arena_4,mandalorian_face1, mandalorian_face2],

   #SW - modified cattle to nerfs and have tf_mounted flag and higher riding skill so they travel faster on the world map
  ["cattle","Nerf","Nerf Herd",tf_mounted,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),knows_common|knows_riding_8,sw_man_face_1, sw_man_face_2],


   #####################################################################################################
   #  add wp_firearm(X) to some troops?
   #SW - added Star Wars mercs

#SW - NOTE - wookiee is the troop marked as soldiers_begin   
   
#wookiee mercs (removed tf_guarantee_ranged from wookiee berserker/bacca so they will be part of the infantry group and can be given separate battle commands)
["wookiee","Wookiee","Wookiees",
  tf_wookiee|tf_guarantee_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ itm_wookiee_bowcaster,
    itm_wookiee_bowcaster,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_melee_punch,
    itm_wookiee_shield_small,
    itm_wookiee_shield_small,
    itm_wookiee_fur
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_1,
  wookiee_face1, wookiee_face2
],
["wookiee_warrior","Wookiee Warrior","Wookiee Warriors",
  tf_wookiee|tf_guarantee_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ itm_wookiee_bowcaster,
    itm_wookiee_bowcaster,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_vibro_blade1,
    itm_vibro_blade3,
    #itm_wookiee_armor1,
    #itm_wookiee_armor2,
    #itm_ryyk_kerarthorr,
    itm_ryyk_kerarthorr,
    itm_ryyk_kerarthorr_shield,
    itm_ryyk_kerarthorr_shield,   
    itm_wookiee_shield_small,
    itm_wookiee_shield_small,
    itm_wookiee_fur
  ],
  def_attrib_2|level(16),
  wp(110)|wp_crossbow(125),
  starwars_skills_2,
  wookiee_face1, wookiee_face2
],
["wookiee_marksman","Wookiee Marksman","Wookiee Marksmen",
  tf_wookiee|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ itm_vibro_blade1,
    itm_vibro_blade3,
    itm_wookiee_bowcaster,
    itm_wookiee_bowcaster,
    #itm_wookiee_armor2,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_wookiee_shield_small,
    itm_wookiee_shield_small,
    itm_wookiee_fur
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  wookiee_face1, wookiee_face2
],
["wookiee_berserker","Wookiee Berserker","Wookiee Berserkers",
  tf_wookiee|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ itm_ryyk_blade,
    itm_ryyk_blade,
    itm_ryyk_kerarthorr,
    #itm_ryyk_kerarthorr,
    itm_wookiee_shield_large,
    itm_wookiee_shield_large,
    #itm_ryyk_kerarthorr_shield,
    itm_ryyk_kerarthorr_shield,
    itm_westar,
    #itm_westar,
    itm_ddc_defender,
    #itm_ddc_defender,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_wookiee_fur
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(140),
  starwars_skills_melee_3,
  wookiee_face1, wookiee_face2
],
["wookiee_sharpshooter","Wookiee Sharpshooter","Wookiee Sharpshooters",
  tf_wookiee|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ itm_vibro_blade1,
    itm_vibro_blade3,
    itm_wookiee_bowcaster,
    itm_wookiee_bowcaster,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_wookiee_shield_small,
    itm_wookiee_shield_small,
    itm_wookiee_fur
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  wookiee_face1,wookiee_face2
],
["bacca_warrior","Warrior of Bacca","Warriors of Bacca",
  tf_wookiee|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ itm_ryyk_blade,
    itm_ryyk_blade,
    itm_ryyk_blade_chieftain,
    itm_ryyk_blade_chieftain,
    itm_wookiee_shield_large,
    itm_wookiee_shield_large,
    itm_ryyk_blade_shield,
    itm_ryyk_blade_shield,
    itm_westar,
    itm_ddc_defender,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_transparent_helmet,
    itm_wookiee_fur
  ],
  def_attrib_4|level(30),
  wp(150)|wp_firearm(160),
  starwars_skills_melee_4,
  wookiee_face1, wookiee_face2
],
   
# mandalorian mercs - keep tf_guarantee_ranged so they fall into the 'archery' group and can be given separate battle commands
["mandalorian","Mandalorian","Mandalorians",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_shield,
  no_scene,reserved,fac_commoners,
  [ 
    itm_mand_arm_dummy,
    itm_mand_helm_dummy,
    itm_grey_gloves,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_ddc_defender,
    itm_ddc_defender,   
    itm_westar,
    itm_westar,
    itm_westar_shield,
    itm_westar_shield,
    itm_energy_shield_red_small,
    itm_energy_shield_yellow_small
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_1,
  mandalorian_face1, mandalorian_face2
],
["mandalorian_soldier","Mandalorian Soldier","Mandalorian Soldiers",
  tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_mand_arm_dummy,
    itm_mand_helm_dummy,
    itm_grey_gloves,
    itm_grey_gloves,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_westar,
    itm_westar,
    itm_westar_shield,
    itm_westar_shield
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_2,
  mandalorian_face1, mandalorian_face2
],
["mandalorian_commando","Mandalorian Commando","Mandalorian Commandos",
  tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_mand_arm_dummy,
    itm_mand_helm_dummy,
    itm_grey_gloves,
    itm_grey_gloves,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_a295,
    itm_a295_crouch,
    itm_mandalorian_heavy_blaster,
    itm_mandalorian_heavy_blaster,
    itm_mandalorian_heavy_blaster,
    itm_westar_shield,
    itm_westar_shield
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  mandalorian_face1, mandalorian_face2
],
["mandalorian_sniper","Mandalorian Sniper","Mandalorian Snipers",
  tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_mand_arm_dummy,
    itm_mand_helm_dummy,
    itm_grey_gloves,
    itm_grey_gloves,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_dlt19,
    itm_dlt20a,
    itm_kisteer_1284,
    itm_dlt19_scope,
    itm_westar_shield,
    itm_westar_shield
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  mandalorian_face1, mandalorian_face2
],
["mandalorian_crusader","Mandalorian Crusader","Mandalorian Crusaders",
  tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_mand_arm_dummy,
    itm_mand_helm_dummy,
    itm_grey_gloves,
    itm_grey_gloves,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_a295,
    itm_a295_crouch,
    itm_mandalorian_heavy_blaster,
    itm_mandalorian_heavy_blaster,
    itm_mandalorian_heavy_blaster,
    itm_westar_shield,
    itm_westar_shield
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  mandalorian_face1, mandalorian_face2
],
["mandalorian_deadeye","Mandalorian Deadeye","Mandalorian Deadeyes",
  tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_mand_arm_dummy,
    itm_mand_helm_dummy,
    itm_grey_gloves,
    itm_grey_gloves,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle,
    itm_dlt19,
    itm_dlt20a,
    itm_kisteer_1284,
    itm_dlt19_scope,
    itm_westar_shield,
    itm_westar_shield
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  mandalorian_face1, mandalorian_face2
],

#gamorrean mercs - used starwars_skills_melee_# so they have better melee fighting ability, thicker skin (ie. higher ironflesh), etc
#                -  removed tf_guarantee_ranged so they fall into the 'infantry' group and can be given separate battle command
["gamorrean","Gamorrean","Gamorreans",
  tf_gamorrean,
  no_scene,reserved,fac_commoners,
  [ 
    #itm_gamorrean_armor,
    itm_gamorrean_axe_1h,
    itm_gamorrean_axe_1h,
    itm_gamorrean_axe_2h,
    itm_gamorrean_axe_2h,
    #itm_dl18,
    #itm_dl18,
    itm_throwing_axes,
    itm_throwing_axes,
    itm_gamorrean_helmet,
    itm_transparent_helmet
    #itm_laser_bolts_orange_pistol,
    #itm_laser_bolts_orange_pistol
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_melee_1,
  gamorrean_face1, gamorrean_face2
],
["gamorrean_warrior","Gamorrean Warrior","Gamorrean Warriors",
  tf_gamorrean,
  no_scene,reserved,fac_commoners,
  [ 
    itm_gamorrean_armor,
    itm_gamorrean_axe_1h,
    itm_gamorrean_axe_1h,
    itm_gamorrean_axe_2h,
    itm_gamorrean_axe_2h,
    #itm_dl18,
    #itm_dl18,
    itm_throwing_axes,
    itm_throwing_axes,    
    itm_gamorrean_helmet,
    itm_transparent_helmet
    #itm_laser_bolts_orange_pistol,
    #itm_laser_bolts_orange_pistol
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_melee_2,
  gamorrean_face1, gamorrean_face2
],
["gamorrean_guard","Gamorrean Guard","Gamorrean Guards",
  tf_gamorrean|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ itm_gamorrean_armor,
    itm_durasteel_shield_small,
    itm_durasteel_shield_small_2,
    itm_vibro_axe_medium_1h,
    itm_vibro_axe_medium_1h,
    itm_dl18,
    itm_dl18,
    itm_transparent_helmet,
    #itm_gamorrean_helmet,    
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(140),
  starwars_skills_melee_3,
  gamorrean_face1, gamorrean_face2
],
["gamorrean_palace_guard","Gamorrean Palace Guard","Gamorrean Palace Guards",
  tf_gamorrean|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ itm_gamorrean_armor,
    itm_durasteel_shield_small,
    itm_durasteel_shield_small_2,
    itm_vibro_axe_medium_1h,
    itm_vibro_axe_medium_1h,
    itm_dl18,
    itm_dl18,
    itm_transparent_helmet,   
    #itm_gamorrean_helmet,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol
  ],
  def_attrib_4|level(30),
  wp(150)|wp_firearm(160),
  starwars_skills_melee_4,
  gamorrean_face1, gamorrean_face2
],

#twilek female
["twilek_female1","Twi'lek Female","Twilek Females",
  tf_twilek_female|tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_ranged,
  0,0,fac_commoners,
  [ 
    #itm_lady_gloves,
    #itm_lady_gloves,
    itm_transparent_head,
    itm_transparent_feet,
    itm_transparent_hands,
    itm_twilek_slave_a,
    itm_twilek_slave_b,
    itm_twilek_slave_c,
    itm_twilek_slave_d,
    itm_twilek_dagger,
    itm_twilek_dagger,
    itm_twilek_dagger_throwing,
    itm_twilek_dagger_throwing,
    itm_dl44a,
    itm_wpn_blaster_cycler_rifle
    # itm_dl44a,
    # itm_q2,
    # itm_ddc_defender,
    # itm_laser_bolts_orange,
    # itm_laser_bolts_orange
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_melee_1,
  twilek_female_face1, twilek_female_face2
],
["twilek_female2","Twi'lek Dancer","Twilek Dancers",
  tf_twilek_female|tf_guarantee_all_armor|tf_guarantee_ranged,
  0,0,fac_commoners,
  [
    #itm_twilek_female_helmet,
    #itm_twilek_female_helmet,
    itm_twilek_dagger,
    itm_twilek_dagger,
    itm_transparent_head,
    itm_transparent_feet,
    itm_transparent_hands,
    itm_twilek_slave_a,
    itm_twilek_slave_b,
    itm_twilek_slave_c,
    itm_twilek_slave_d,
    #itm_twilek_dagger_throwing,    
    itm_dl44a,
    itm_wpn_blaster_cycler_rifle,
    itm_q2,
    itm_ddc_defender,       
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_melee_2,
  twilek_female_face1, twilek_female_face2
],
["twilek_female3","Twi'lek Entertainer","Twilek Entertainers",
  tf_twilek_female|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_helmet,
  0,0,fac_commoners,
  [
    itm_twilek_dagger,
    itm_twilek_dagger,
    itm_dl44a,
    itm_ddc_defender,
    itm_wpn_blaster_cycler_rifle,
    #itm_transparent_helmet_armor,
    itm_transparent_helmet_armor,
    itm_ind_clothes_tightcoverall_blue,
    itm_ind_clothes_tightcoverall_red,
    itm_ind_clothes_tightcoverall_green,
    itm_ind_clothes_tightcoverall_wred,
    itm_ind_clothes_tightcoverall_wblue,
    #itm_twilek_female_helmet_armor,
    #itm_twilek_female_helmet_armor,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_energy_shield_yellow_small,
    itm_energy_shield_yellow_small
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(140),
  starwars_skills_melee_3,
  twilek_female_face1, twilek_female_face2
],

#twilek   
["twilek","Twi'lek","Twi'leks",
  tf_twilek|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    itm_twilek_dagger,
    itm_twilek_dagger,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_wpn_blaster_cycler_rifle,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_melee_1,
  twilek_face1, twilek_face2
],
["twilek_warrior","Twi'lek Warrior","Twi'lek Warriors",
  tf_twilek|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    itm_twilek_dagger,
    itm_twilek_dagger,    
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_ee3,
    itm_ee3,
    itm_wpn_blaster_cycler_rifle,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_2|level(16),
  wp(110)|wp_crossbow(125),
  starwars_skills_melee_2,
  twilek_face1, twilek_face2
],
["twilek_soldier","Twi'lek Soldier","Twi'lek Soldiers",
  tf_twilek|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [
    itm_vibro_axe_long_2h,
    itm_vibro_axe_long_1h,
    itm_vibro_sword3_gold,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_a295,
    itm_a295_crouch,
    itm_wpn_blaster_cycler_rifle,
    itm_transparent_helmet,
    itm_energy_shield_yellow_small,
    itm_energy_shield_yellow_small,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_melee_3,
  twilek_face1, twilek_face2
],
["twilek_commando","Twi'lek Commando","Twi'lek Commandos",
  tf_twilek|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [
    itm_vibro_axe_long_2h,
    itm_vibro_axe_long_1h,
    itm_vibro_sword3_gold,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_a295,
    itm_a295_crouch,
    itm_wpn_blaster_cycler_rifle,
    itm_transparent_helmet,
    itm_energy_shield_yellow_medium,
    itm_energy_shield_yellow_medium,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_melee_4,
  twilek_face1, twilek_face2
],

#Rodian
["rodian","Rodian","Rodians",
  tf_rodian|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ 
    #itm_leather_gloves,
    #itm_leather_gloves,
    itm_melee_punch,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_dl18,
    itm_ddc_defender,
    itm_dl44a,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_1,
  rodian_face1, rodian_face2
],
["rodian_warrior","Rodian Warrior","Rodian Warriors",
  tf_rodian|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    #itm_black_gloves,
    #itm_black_gloves,
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_ee3,
    itm_ee3,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_2|level(16),
  wp(110)|wp_crossbow(125),
  starwars_skills_2,
  rodian_face1, rodian_face2
],
["rodian_hunter","Rodian Hunter","Rodian Hunters",
  tf_rodian|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [
    #itm_black_gloves,
    #itm_black_gloves,
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_rodian_ventilator,
    itm_rodian_ventilator_red,
    itm_rodian_ventilator_black,
    itm_energy_shield_green_small,
    itm_energy_shield_green_small,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  rodian_face1, rodian_face2
],
["rodian_bounty_hunter","Rodian Bounty Hunter","Rodian Bounty Hunters",
  tf_rodian|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [
    itm_black_gloves,
    itm_black_gloves,
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_a295,
    itm_a295_crouch,
    itm_dlt19,
    itm_dlt20a,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_rodian_ventilator,    
    itm_rodian_ventilator_red,
    itm_rodian_ventilator_black,
    itm_energy_shield_green_medium,
    itm_energy_shield_green_medium,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  rodian_face1, rodian_face2
],

#Trandoshan
["trandoshan","Trandoshan","Trandoshans",
  tf_trandoshan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ 
    itm_melee_punch,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_trandoshan_supressor,
    itm_trandoshan_supressor,
    itm_trandoshan_skin
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_1,
  trandoshan_face1, trandoshan_face2
],
["trandoshan_warrior","Trandoshan Warrior","Trandoshan Warriors",
  tf_trandoshan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ 
    itm_trandoshan_blade,
    itm_trandoshan_blade,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_trandoshan_supressor,
    itm_trandoshan_supressor,
    itm_trandoshan_skin
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_2,
  trandoshan_face1, trandoshan_face2
],
["trandoshan_hunter","Trandoshan Hunter","Trandoshan Hunters",
  tf_trandoshan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ 
    itm_trandoshan_blade,
    itm_trandoshan_blade,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_trandoshan_acp_array_gun,
    itm_trandoshan_acp_array_gun,
    itm_trandoshan_stun_gun,
    itm_trandoshan_stun_gun,
    itm_energy_shield_yellow_small,
    itm_energy_shield_yellow_small,
    itm_trandoshan_skin
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  trandoshan_face1, trandoshan_face2
],
["trandoshan_bounty_hunter","Trandoshan Bounty Hunter","Trandoshan Bounty Hunters",
  tf_trandoshan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ 
    itm_trandoshan_blade,
    itm_trandoshan_blade,   
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_trandoshan_acp_array_gun,
    itm_trandoshan_acp_array_gun,
    itm_energy_shield_yellow_medium,
    itm_energy_shield_yellow_medium,
    itm_trandoshan_skin
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  trandoshan_face1, trandoshan_face2
],

#moncal
["moncal_1","Mon Calamarian","Mon Calamarians",
  tf_moncal|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_1,
  moncal_face1, moncal_face2
],
["moncal_2","Mon Calamari Warrior","Mon Calamari Warriors",
  tf_moncal|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_2,
  moncal_face1, moncal_face2
],
["moncal_3","Mon Calamari Soldier","Mon Calamari Soldiers",
  tf_moncal|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield,
  no_scene,reserved,fac_commoners,
  [ itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_ee3,
    itm_ee3,
    itm_energy_shield_green_small,
    itm_energy_shield_blue_small,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  moncal_face1, moncal_face2
],
["moncal_4","Mon Calamari Knight","Mon Calamari Knights",
  tf_moncal|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield,
  no_scene,reserved,fac_commoners,
  [ itm_black_gloves,
    itm_black_gloves,   
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_energy_shield_green_medium,
    itm_energy_shield_blue_medium,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  moncal_face1, moncal_face2
],

#chiss
["chiss_1","Chiss","Chiss",
  tf_chiss|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_red_pistol,
    itm_laser_bolts_red_pistol,
    itm_ddc_defender,
    #itm_ddc_defender,
    #itm_dl44a,
    itm_dl44a,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_1,
  chiss_face1, chiss_face2
],
["chiss_2","Chiss Soldier","Chiss Soldiers",
  tf_chiss|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle,
    itm_ee3,
    itm_ee3,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_2|level(16),
  wp(110)|wp_crossbow(125),
  starwars_skills_2,
  chiss_face1, chiss_face2
],
["chiss_3","Chiss Officer","Chiss Officer",
  tf_chiss|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_a295,
    itm_a295_crouch,
    itm_energy_shield_red_small,
    itm_energy_shield_red_small,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  chiss_face1, chiss_face2
],
["chiss_4","Chiss Commander","Chiss Commanders",
  tf_chiss|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield,
  no_scene,reserved,fac_commoners,
  [
    itm_black_gloves,
    itm_black_gloves,
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_a295,
    itm_a295_crouch,
    itm_dlt19,
    itm_dlt20a,
    itm_transparent_helmet,
    itm_energy_shield_red_small,
    itm_energy_shield_red_medium,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  chiss_face1, chiss_face2
],

#geonosian #TAS updated
["geonosian_1","Geonosian","Geonosians",
  tf_geonosian|tf_guarantee_all_armor|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    itm_geonosian_sonic_pistol,
    itm_geonosian_sonic_pistol,
    itm_sonic_beam_pistol,
    itm_sonic_beam_pistol,
    itm_geonosian_static_pike,
    itm_geonosian_static_pike
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_1,
  geonosian_face1, geonosian_face2
],
["geonosian_2","Geonosian Drone","Geonosian Drones",
  tf_geonosian|tf_guarantee_all_armor|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    itm_geonosian_sonic_pistol,
    itm_geonosian_sonic_pistol,
    itm_sonic_beam_pistol,
    itm_sonic_beam_pistol,    
    itm_geonosian_static_pike,
    itm_geonosian_static_pike
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_2,
  geonosian_face1, geonosian_face2
],
["geonosian_3","Geonosian Warrior","Geonosian Warrior",
  tf_geonosian|tf_guarantee_all_armor|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    itm_geonosian_sonic_rifle,
    itm_geonosian_sonic_rifle,
    itm_sonic_beam_rifle,
    itm_sonic_beam_rifle,       
    itm_geonosian_static_pike,
    itm_geonosian_static_pike
    #itm_energy_shield_yellow_medium,
    #itm_energy_shield_yellow_medium
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  geonosian_face1, geonosian_face2
],
["geonosian_4","Veteran Geonosian Warrior","Veteran Geonosian Warrior",
  tf_geonosian|tf_guarantee_all_armor|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    itm_geonosian_sonic_rifle,
    itm_geonosian_sonic_rifle,
    itm_sonic_beam_rifle,
    itm_sonic_beam_rifle,   
    itm_geonosian_static_pike,    
    itm_geonosian_static_pike
    #itm_energy_shield_yellow_medium,
    #itm_energy_shield_yellow_medium
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  geonosian_face1, geonosian_face2
],

#sullustan
["sullustan_1","Sullustan","Sullustans",
  tf_sullustan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ 
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_ddc_defender,
    itm_ddc_defender,
    #itm_dl44a,
    itm_dl44a,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_1,
  sullustan_face1, sullustan_face2
],
["sullustan_2","Sullustan Navigator","Sullustan Navigators",
  tf_sullustan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ 
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_2,
  sullustan_face1, sullustan_face2
],
["sullustan_3","Sullustan Pilot","Sullustan Pilots",
  tf_sullustan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ 
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_quicksnap_36t,
    itm_quicksnap_36t,
    itm_transparent_helmet,
    itm_energy_shield_green_small,
    itm_energy_shield_blue_small,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  sullustan_face1, sullustan_face2
],
["sullustan_4","Sullustan Captain","Sullustan Captains",
  tf_sullustan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ 
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_quicksnap_36t,
    itm_quicksnap_36t,
    itm_transparent_helmet,
    itm_energy_shield_green_medium,
    itm_energy_shield_blue_medium,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  sullustan_face1, sullustan_face2
],

#bothan
["bothan","Bothan","Bothans",
  tf_bothan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ 
    #itm_leather_gloves,
    #itm_leather_gloves,
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_melee_1,
  bothan_face1, bothan_face2
],
["bothan_militia","Bothan Militia","Bothan Militia",
  tf_bothan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ 
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_melee_2,
  bothan_face1, bothan_face2
],
["bothan_agent","Bothan Agent","Bothan Agents",
  tf_bothan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [ 
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_melee_2,
  bothan_face1, bothan_face2
],
["bothan_infantry","Bothan Infantry","Bothan Infantry",
  tf_bothan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ 
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_bothan_bola_carabine,
    itm_bothan_bola_carabine,
    itm_transparent_helmet,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_3,
  bothan_face1, bothan_face2
],
["bothan_spy","Bothan Spy","Bothan Spies",
  tf_bothan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ 
    itm_vibro_sword3_gold,
    itm_vibro_sword3_red,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,   
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_transparent_helmet,
    itm_energy_shield_green_small,
    itm_energy_shield_blue_small,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(140),
  starwars_skills_melee_3,
  bothan_face1, bothan_face2
],
["bothan_infiltrator","Bothan Infiltrator","Bothan Infiltrators",
  tf_bothan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ 
    itm_vibro_sword3_gold,
    itm_vibro_sword3_red,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_bothan_bola_carabine,
    itm_bothan_bola_carabine,
    itm_transparent_helmet,
    itm_energy_shield_green_medium,
    itm_energy_shield_blue_medium,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_melee_4,
  bothan_face1, bothan_face2
],
["kaminoan","Kaminoan","Kaminoans",
  tf_bothan|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,reserved,fac_commoners,
  [ 
    itm_transparent_hands,
    itm_kaminoan_female_head,
    itm_kaminoan_female_body,
    itm_transparent_feet,
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_melee_4,
  bothan_face1, bothan_face2
],
#ig88 droid merc
["ig88","IG-86 Sentinel Droid","IG-86 Sentinel Droids",
  tf_droid|tf_guarantee_all_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_ig88_attack,
    #itm_ig86_head,
    itm_ig86_body,
    #itm_ig86_hand,
    itm_transparent_droid_feet,
    itm_transparent_droid_head,
    itm_ig86_e5_shield,
    itm_ig86_e5_pistol,               #gave 2x so ther eis a chance the player could find it in the loot after a battle
    itm_laser_bolts_orange_pistol,  #have to give pistol ammo since itm_ig88_dlt20a is a pistol so it can be carried 1-handed
    itm_laser_bolts_orange_pistol   #have to give pistol ammo since itm_ig88_dlt20a is a pistol so it can be carried 1-handed
  ],
  str_16|int_12|level(35),
  wp(175)|wp_crossbow(200),
  knows_ironflesh_8|knows_power_strike_6|knows_weapon_master_8|knows_shield_6|knows_tactics_5|knows_leadership_5|knows_trainer_2,
  droid_face1, droid_face2
],


#ihk droid merc
["hkseries","HK-Series Droid","HK-Series Droids",
  tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_shield,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_hk_attack,
    itm_hk_head,
    itm_hk_body,
    itm_hk_hands,
    itm_hk_feet,
    itm_a280,
    itm_a295,
    itm_dlt19,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle
  ],
  str_14|int_8|level(24),
  wp(150)|wp_crossbow(175),
  knows_ironflesh_7|knows_power_strike_5|knows_weapon_master_6|knows_shield_3|knows_tactics_4|knows_leadership_3|knows_trainer_2,
  droid_face1, droid_face2
],

#Umbaran mercs
["Umbaran_militia","Umbaran Militia","Umbaran Militia",
  tf_guarantee_all_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    #itm_umbaran_head,
    itm_umbaran_armor,
    itm_transparent_feet,
    itm_transparent_head,
    itm_transparent_helmet,
    itm_darkgrey_gloves,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_umbaran_rifle,
    itm_umbaran_rifle,
  ],
  def_attrib_2|level(10),
  starwars_skills_2,
  sw_man_face_1, sw_man_face_2
],

["Umbaran_Soldier","Umbaran Solider","Umbaran Soldiers",
  tf_guarantee_all_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    #itm_umbaran_head,
    itm_umbaran_armor,
    itm_transparent_feet,
    itm_transparent_head,
    itm_transparent_helmet,
    itm_darkgrey_gloves,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_umbaran_rifle,
    itm_umbaran_rifle,
  ],
  def_attrib_3|level(15),
  starwars_skills_3,
  sw_man_face_1, sw_man_face_2
],

["Umbaran_officer","Umbaran Officer","Umbaran Officers",
  tf_guarantee_all_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    #itm_umbaran_head,
    itm_umbaran_officer,
    itm_transparent_feet,
    itm_transparent_head,
    itm_transparent_helmet,
    itm_darkgrey_gloves,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_umbaran_rifle,
    itm_umbaran_rifle,
  ],
  def_attrib_4|level(20),
  starwars_skills_4,
  sw_man_face_1, sw_man_face_2
],

#Nighsister Mercs

["Nightsister","Nightsister","Nightsisters",
  tf_female|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_nightsister_heada,
    itm_nightsister_headb,
    itm_nightsister_clothes,
    itm_nightsister_clothes_armored,
    itm_nightsister_gloves,
    itm_ns_bow,
    itm_ns_bow,
    itm_energy_arrows,
    itm_energy_arrows,
    itm_nightsister_sword,
    itm_nightsister_sword,
  ],
  def_attrib_force_2|level(10),
  starwars_skills_force_2,
  wp(100)|wp_archery(120),
  knows_power_strike_3,
  sw_imperial_face_1, sw_imperial_face_1
],

["Nightsister_assassin","Nightsister Assassin","Nightsister Assassins",
  tf_female|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_nightsister_headb,
    itm_nightsister_headc,
    itm_nightsister_clothes,
    itm_nightsister_clothes_armored,
    itm_nightsister_gloves,
    itm_ns_bow,
    itm_ns_bow,
    itm_energy_arrows,
    itm_energy_arrows,
    itm_nightsister_sword,
    itm_nightsister_sword,
  ],
  def_attrib_force_2|level(10),
  starwars_skills_force_3,
  wp(126)|wp_archery(140),
  knows_power_strike_4,
  sw_imperial_face_1, sw_imperial_face_1
],

["Nightsister_reaper","Nightsister Reaper","Nightsister Reapers",
  tf_female|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_nightsister_headc,
    itm_nightsister_headd,
    itm_nightsister_clothes,
    itm_nightsister_clothes_armored,
    itm_nightsister_gloves,
    itm_ns_bow,
    itm_ns_bow,
    itm_energy_arrows,
    itm_energy_arrows,
    itm_nightsister_sword,
    itm_nightsister_sword,
  ],
  def_attrib_force_2|level(10),
  starwars_skills_force_4,
  wp(100)|wp_archery(120),
  knows_power_strike_6,
  sw_imperial_face_1, sw_imperial_face_1
],

#Deathwatch Mandos


#human merc upgrade paths

  ["farmer","Farmer","Farmers",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [
     itm_baton,
     itm_baton,
     itm_pipe1,
     itm_pipe2,
     itm_melee_punch,
     itm_melee_punch,
     itm_q2,
     itm_ddc_defender,
     itm_dl44a,
     itm_laser_bolts_orange_pistol,
     itm_laser_bolts_yellow_pistol,
     itm_vibro_blade1,
     itm_durasteel_staff,
     itm_quarter_staff,
     itm_vibro_blade2,
     itm_vibro_blade3,
     itm_club,
     itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
     ],
   def_attrib|level(6),wp(60),knows_common,sw_man_face_1, sw_man_face_2],

  ["townsman","Colonist","Colonists",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [
     itm_pipe1,
     itm_pipe2,
     itm_melee_punch,
     itm_q2,
     itm_ddc_defender,
     itm_dl44a,
     itm_laser_bolts_orange_pistol,
     itm_laser_bolts_yellow_pistol,
     itm_vibro_blade1,
     itm_durasteel_staff,
     itm_quarter_staff,
     itm_vibro_blade2,
     itm_vibro_blade3,
     itm_club,
     itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
     ],
   def_attrib|level(6),wp(60),knows_common,sw_man_face_1, sw_man_face_2],

  ["civilian","Civilian","Civilians",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
  [
    itm_baton,
    itm_pipe1,
    itm_pipe2,
    itm_melee_punch,
    itm_melee_punch,
    itm_q2,
    itm_ddc_defender,
    itm_dl44a,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_leather_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_1|level(10),
  wp(100)|wp_firearm(105),
  starwars_skills_1,  
  sw_man_face_1, sw_man_face_2
  ],

  ["militia","Militia","Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
  [
    itm_baton,
    itm_baton,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_2,
   sw_man_face_1, sw_man_face_2
  ],

  ["security_guard","Security Guard","Security Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
  [
    itm_baton,
    itm_baton,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_energy_shield_yellow_small,
    itm_energy_shield_yellow_small,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(140),
  starwars_skills_melee_3,
   sw_man_face_1, sw_man_face_2
  ],   

  ["soldier","Soldier","Soldiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
  [
    itm_baton,
    itm_baton,
    itm_a280,
    itm_a280_crouch,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(140),
  starwars_skills_3,
   sw_man_face_1, sw_man_face_2
  ],     

  ["bodyguard","Bodyguard","Bodyguards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
  [
    itm_vibro_sword3_gold,
    itm_vibro_sword3_gold,
    itm_a280,
    itm_a280_crouch,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_yellow_rifle,   
    itm_energy_shield_yellow_medium,
    itm_energy_shield_yellow_medium,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_firearm(160),
  starwars_skills_melee_4,
   sw_man_face_1, sw_man_face_2
  ],   

  ["commando","Commando","Commandos",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
  [
    itm_baton,
    itm_baton,
    itm_a280,
    itm_a280_crouch,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_firearm(160),
  starwars_skills_4,
   sw_man_face_1, sw_man_face_2
  ],     

  ["pilot","Pilot","Pilots",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,no_scene,reserved,fac_commoners,
  [
    itm_speeder,
    itm_speeder,
    itm_speeder_hutt,
    itm_speeder_hutt,
    itm_speeder_dagger,
    itm_speeder_dagger,
    #itm_swoop_bike,
    #itm_pod_racer,     
    itm_vibro_sword3_gold,
    itm_vibro_sword3_gold,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_firearm(160),
  starwars_skills_mounted_4,
   sw_man_face_1, sw_man_face_2
  ],     
  
  ["thug","Thug","Thugs",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
  [
    itm_baton,
    itm_durasteel_mace,
    itm_durasteel_bat,
    itm_vibro_blade1,
    itm_vibro_blade2,
    itm_vibro_knuckler,
    itm_combat_knife,   
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_leather_gloves,
    itm_leather_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_2|level(16),
  wp(110)|wp_firearm(125),
  starwars_skills_melee_2,
   sw_man_face_1, sw_man_face_2
 ],

  ["goon","Goon","Goons",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
  [
    itm_baton,
    itm_durasteel_mace,
    itm_durasteel_bat,
    itm_vibro_blade1,
    itm_vibro_blade2,
    itm_vibro_knuckler,
    itm_combat_knife,   
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,
    itm_leather_gloves,
    itm_leather_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(140),
  starwars_skills_melee_3,
   sw_man_face_1, sw_man_face_2
 ], 

  ["biker","Biker","Bikers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,no_scene,reserved,fac_commoners,
  [
    itm_speeder,
    itm_speeder,
    itm_speeder_hutt,
    itm_speeder_hutt,
    itm_speeder_dagger,
    itm_speeder_dagger,
    #itm_swoop_bike,
    #itm_pod_racer,   
    itm_durasteel_mace,
    itm_durasteel_bat,
    itm_vibro_sword3_gold,
    itm_vibro_sword3_gold,
    itm_ddc_defender,
    itm_ddc_defender,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_dl44a,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,   
    itm_leather_gloves,
    itm_leather_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(140),
  starwars_skills_mounted_3,
   sw_man_face_1, sw_man_face_2
 ],  
 
  ["assassin","Assassin","Assassins",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
  [
    #itm_transparent_helmet,
    #itm_transparent_helmet,  
    itm_glasses_black,
    itm_glasses_yellow,
    itm_eyepiece_tactics,
    itm_eyepiece_leadership,
    itm_black_gloves,
    itm_black_gloves,       
    itm_vibro_sword3_gold,
    itm_vibro_sword3_gold,
    itm_energy_shield_yellow_medium,
    itm_energy_shield_yellow_medium,
    itm_a295,
    itm_a295_crouch,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_firearm(160),
  starwars_skills_melee_4,
   sw_man_face_1, sw_man_face_2
 ], 

  ["biker_scout","Biker Scout","Biker Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,no_scene,reserved,fac_commoners,
  [
    itm_speeder,
    itm_speeder,
    itm_speeder_hutt,
    itm_speeder_hutt,
    itm_speeder_dagger,
    itm_speeder_dagger,
    #itm_swoop_bike,
    #itm_pod_racer,   
    itm_vibro_sword3_gold,
    itm_vibro_sword3_gold,
    itm_energy_shield_yellow_small,
    itm_energy_shield_yellow_small,   
    itm_a280,
    itm_a280_crouch,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_yellow_rifle,   
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_glasses_black,
    itm_glasses_yellow,   
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,
    itm_leather_gloves,
    itm_leather_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown
  ],
  def_attrib_4|level(30),
  wp(150)|wp_firearm(160),
  starwars_skills_mounted_4,
   sw_man_face_1, sw_man_face_2
 ], 
 
 
 
# ["hired_guard","Security Guard","Security Guards",
  # tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
  # no_scene,0,fac_commoners,
  # [ 
  # ],
  # def_attrib_2|level(16),
  # wp(110)|wp_firearm(125),
  # starwars_skills_2,
  # sw_man_face_1, sw_man_face_2
# ],
# ["hired_guardian","Security Officer","Security Officers",
  # tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet,
  # no_scene,0,fac_commoners,
  # [ 
  # ],
  # def_attrib_3|level(24),
  # wp(135)|wp_crossbow(140),
  # starwars_skills_3,
  # sw_man_face_1, sw_man_face_2
# ],
   
#####################################################################################################
["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners, [], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
#####################################################################################################

#specialized mercs, must build village improvement to recruit

#oom_series droid
["oom_series_security","OOM Security Battle Droid","OOM Security Battle Droids",
  tf_battledroid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_battle_droid_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    itm_oomseries_body,
    itm_e5,
    itm_e5,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle
  ],
  str_6|int_3|cha_3|agi_3|level(1),
  wp(60)|wp_crossbow(80),
  knows_ironflesh_3|knows_tactics_2|knows_leadership_2|knows_trainer_2,
  droid_face1, droid_face2
],

["oom_series_marine","OOM Marine Battle Droid","OOM Marine Battle Droids",
  tf_battledroid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_battle_droid_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    itm_oomseries_marine_body,
    itm_e5,
    itm_e5,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle
  ],
  str_10|int_6|cha_3|agi_6|level(12),
  wp(140)|wp_crossbow(160),
  knows_ironflesh_6|knows_tactics_4|knows_leadership_4|knows_trainer_4,
  droid_face1, droid_face2
],

["oom_series_pilot","OOM Pilot Battle Droid","OOM Pilot Battle Droids",
  tf_battledroid|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_vibro_sword3_blue,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    itm_oomseries_pilot_body,
    itm_e5,
    itm_e5,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle,
    itm_horus_winged_cruiser,
    itm_horus_winged_cruiser
  ],
  str_10|int_6|cha_3|agi_6|level(12),
  wp(140)|wp_crossbow(160),
  knows_ironflesh_6|knows_tactics_4|knows_leadership_4|knows_trainer_4|knows_riding_5|knows_horse_archery_5,
  droid_face1, droid_face2
],

["oom_series_command","OOM Command Battle Droid","OOM Command Battle Droid",
  tf_battledroid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_battle_droid_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    itm_oomseries_command_body,
    itm_e5,
    itm_e5,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle
  ],
  str_16|int_9|cha_3|agi_9|level(24),
  wp(160)|wp_crossbow(180),
  knows_ironflesh_9|knows_tactics_6|knows_leadership_6|knows_trainer_6,
  droid_face1, droid_face2
],

# b1series droid
["b1series","B1-Series Battle Droid","B1-Series Battle Droids",
  tf_battledroid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_battle_droid_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    itm_b1series_body,
    itm_e5,
    itm_e5,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle
  ],
  str_5|int_3|cha_3|agi_3|level(5),
  wp(30)|wp_crossbow(75),
  knows_ironflesh_3|knows_tactics_2|knows_leadership_1|knows_trainer_1,
  droid_face1, droid_face2
],

["b1series_assassin","B1-Series Droid Assassin","B1-Series Droid Assassins",
  tf_battledroid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_battle_droid_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    itm_b1series_body,
    itm_e5s,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle
  ],
  str_5|int_3|cha_3|agi_5|level(15),
  wp(65)|wp_crossbow(180),
  knows_ironflesh_4|knows_tactics_4|knows_leadership_2|knows_trainer_2,
  droid_face1, droid_face2
],

["bxseries_commando","BX-Series Droid Commando","BX-Series Droid Commandos",
  tf_battledroid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    itm_bxseries_body,
    itm_e5,
    itm_e5,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle,
    itm_droid_sword,
    itm_droid_sword,
    itm_droid_blast_shield,
  ],
  str_18|int_10|cha_6|agi_18|level(24),
  wp(160)|wp_crossbow(220)|wp_one_handed(200),
  knows_ironflesh_4|knows_power_strike_6|knows_athletics_6|knows_tactics_6|knows_leadership_6|knows_trainer_5,
  droid_face1, droid_face2
],

 ["b2series","B2-Series Battle Droid","B2-Series Battle Droids",
   tf_sbd|tf_guarantee_all_armor|tf_guarantee_ranged,
   no_scene,0,fac_commoners,
   [
     itm_droid_parts,
     itm_b2series_attack,
     itm_transparent_droid_head,
     itm_transparent_droid_hands,
     itm_transparent_droid_feet,    
     itm_b2series_body,
     itm_b2series_blaster,
     itm_b2series_blaster,
     itm_laser_bolts_red_pistol,
     itm_laser_bolts_red_pistol
   ],
   str_26|agi_5|int_6|cha_6|level(18),
   wp(90)|wp_firearm(125),
   knows_ironflesh_3|knows_power_strike_7|knows_tactics_4|knows_leadership_3|knows_trainer_2,
   droid_face1, droid_face2
 ],
 
 ["b2series_enhanced","C-B3 Cortosis Battle Droid","C-B3 Cortosis Battle Droids",
   tf_sbd|tf_guarantee_all_armor|tf_guarantee_ranged,
   no_scene,0,fac_commoners,
   [
    itm_droid_parts,
    itm_b2series_attack, 
      itm_b2series_body_enhanced,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    itm_b2series_body_enhanced,
    itm_b2series_blaster,
    itm_b2series_blaster,
    itm_laser_bolts_red_pistol,
    itm_laser_bolts_red_pistol
   ],
   str_28|agi_7|int_8|cha_12|level(26),
   wp(90)|wp_firearm(125),
   knows_ironflesh_3|knows_power_strike_7|knows_athletics_1|knows_tactics_4|knows_leadership_4|knows_trainer_2,
   droid_face1, droid_face2
 ],
 
#clone troopers
["clone_trooper_1","501st Legion ARC Trooper","501ST Legion ARC Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [
    itm_phase_ii_armor_fives,
    itm_phase_ii_helmet_rex,
    itm_clone_trooper_gloves_white,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15s,
    itm_dc15s,
    itm_dc15a_hip
  ],
  str_18|str_18|str_20|cha_18|level(28),
  wp(420)|wp_firearm(420),
  starwars_skills_4,
  mandalorian_face1, mandalorian_face2
],
["clone_trooper_2","212th ARC Trooper","212th Siege ARC Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_phase_ii_arc_kama,
    itm_phase_ii_helmet_212,
    itm_phase_ii_armor_212, 
    itm_clone_trooper_gloves_white,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a,
    itm_dc15a_hip
  ],
  str_18|str_18|str_18|cha_16|level(34),
  wp(420)|wp_firearm(420),
  starwars_skills_4,
  mandalorian_face1, mandalorian_face2
],
["arc_trooper_2","Wolfpack Battalion ARC Trooper","Wolfpack Battalion ARC Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_phase_ii_arc_kama,
    itm_phase_ii_helmet_wolf,
    itm_phase_ii_armor_wolf,  
    itm_clone_trooper_gloves_white,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a,
    itm_dc15a_hip
  ],
  str_20|str_20|str_18|cha_18|level(34),
  wp(420)|wp_crossbow(420),
  starwars_skills_4,
  mandalorian_face1, mandalorian_face2
],
["clone_trooper_3","Riot Trooper","Riot Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_shield,
  no_scene,reserved,fac_commoners,
  [   
    itm_phase_ii_armor_shock,
      itm_phase_ii_armor_fox,
    itm_phase_ii_helmet_shock,
    itm_clone_trooper_gloves_red,
    itm_baton2,
      itm_republic_shield,
    itm_laser_bolts_blue_pistol,
    itm_dc17sa,
    itm_westar35,
  ],
  str_20|agi_18|int_14|cha_14|level(20),
  wp(220),#|wp_crossbow(165),
  starwars_skills_4,
  mandalorian_face1, mandalorian_face2
],
["arc_trooper_3","Clone Pilot","Clone Pilots",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_commoners,
  [   
    itm_phase_ii_armor_clean,
    itm_rep_helm_phase2scout,
    itm_black_gloves,
    itm_black_gloves_long,
    itm_speeder_imperial,
    itm_dc15s,
      itm_dc15a_hip,
    itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
  ],
  def_attrib_2|level(20),
  wp(165)|wp_firearm(165),
  starwars_skills_mounted_2,
  mandalorian_face1, mandalorian_face2
],
["clone_trooper_4","Galactic Marine","Galactic Marines",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_rep_arm_galacticmarine,
    itm_black_gloves,
    itm_phase_ii_clonepack,
    itm_dc15a_hip,
    itm_dc15a,
    itm_vibro_blade1,
    itm_dc15a_hip,
    itm_dlt20a,
    itm_dlt19,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
  ],
  str_20|str_18|int_18|cha_16|level(28),
  wp(275)|wp_crossbow(350),
  starwars_skills_4|knows_ironflesh_7,
  mandalorian_face1, mandalorian_face2
],
["arc_trooper_4","Elite Clone Lancer","Elite Clone Lancer",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_rep_helm_phase2arf,
    itm_phase_ii_armor_worn,
    itm_black_gloves,
    itm_phase_ii_arc_kama,
    itm_lance,
    itm_lance,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
      itm_energy_shield_blue_small,
    itm_dc17sa,
    itm_westar35,
    itm_dc15a_hip
  ],
  def_attrib_4|level(28),
  wp(250),#|wp_crossbow(160),
  starwars_skills_mounted_4,
  mandalorian_face1, mandalorian_face2
],
["clone_trooper_5","Clone Trooper Commander","Clone Trooper Commanders",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_clone_trooper_gloves_yellow,
    itm_rep_arm_phase1_yellow,
    itm_rep_helm_phase1_yellow,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15a,
    itm_dc15a_hip,
    itm_dc15a_hip
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  mandalorian_face1, mandalorian_face2
],
["arc_trooper_5","Arc Trooper Commander","Arc Trooper Commanders",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_commoners,
  [   
    itm_clone_trooper_gloves_yellow,
    itm_rep_arm_phase1_yellow,
    itm_rep_arm_phase1arc_yellow,
    itm_rep_helm_phase1_yellow,
    itm_combat_knife,
    itm_combat_knife,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15a,
    itm_dc15a_hip,
    itm_dc15a_hip
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(160),
  starwars_skills_4,
  mandalorian_face1, mandalorian_face2
],

# rancor
["rancor","Baby Rancor","Baby Rancors",
  tf_gamorrean|tf_guarantee_all_armor,    # used tf_gamorrean sounds  since we have a limit of races in module_skins.py
  no_scene,0,fac_commoners,
  [
    itm_rancor_body_a,
    itm_rancor_body_a,
    itm_rancor_body_a,
    itm_rancor_body_b,
    itm_rancor_body_b,    
    itm_transparent_head,
    itm_transparent_hands,
    itm_transparent_feet,
    itm_rancor_attack
  ],
  str_16|int_3|cha_3|level(35),
  wp(175),
  knows_ironflesh_8|knows_power_strike_8|knows_weapon_master_8|knows_shield_2|knows_tactics_2|knows_leadership_2,
  sw_man_face_1, sw_man_face_2
],

["rancor_mutant","Mutant Baby Rancor","Mutant Baby Rancors",
  tf_gamorrean|tf_guarantee_all_armor,    # used tf_gamorrean sounds  since we have a limit of races in module_skins.py
  no_scene,0,fac_commoners,
  [ 
    itm_rancor_body_c,
    itm_transparent_head,
    itm_transparent_hands,
    itm_transparent_feet,
    itm_rancor_attack
  ],
  str_29|int_4|cha_5|level(40),
  wp(200),
  knows_ironflesh_10|knows_power_strike_10|knows_weapon_master_10|knows_shield_4|knows_tactics_4|knows_leadership_4,
  sw_man_face_1, sw_man_face_2
],


#Special unit specifically for minning vessels
["asteroid_miner","Asteroid Miner","Asteroid Miners",tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
  [
  itm_mining_helmet,
  itm_mining_helmet,
  itm_pipe1,
  itm_pipe2,
  itm_ddc_defender,
  itm_ddc_defender,
  itm_dl44a,
  itm_dl44a,
  itm_dl44a,
  itm_dl44a,  
  #they come with goodies
  itm_container_ore,
  itm_container_ore,
  itm_container_ore,
  itm_container_ore,
  itm_container_ore,
  itm_container_ore,
  itm_container_ore,
  itm_container_food_1,
  itm_container_food_2,
  itm_container_drink_1,
  itm_container_drink_1
  ],
  def_attrib_3|level(10),
  wp(125)|wp_firearm(90),
  starwars_skills_melee_1,
   sw_man_face_1, sw_man_face_2
  ],   

######################################################################
# droids primarily used as town_walkers or prisoners

# 3poseries droid
["3poseries","3PO-Series Droid","3PO-Series Droids",
  tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_3poseries_attack,
    itm_transparent_head,
    itm_transparent_hands,
    itm_transparent_feet,   
    itm_3poseries_gold,
    itm_3poseries_gold,
    itm_3poseries_blue,
    itm_3poseries_red,
    itm_3poseries_grey,
    itm_3poseries_grey
    #itm_q2,
    #itm_q2,
    #itm_laser_bolts_orange,
    #itm_laser_bolts_orange
  ],
  droid_attrib_2|level(25),
  wp(60),
  droid_skills_2,
  droid_face1, droid_face2
],

# r2series droid
["r2series","R2-Series Droid","R2-Series Droids",
  tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_droid_weapon_no_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet, 
    itm_r2series_blue,
    itm_r2series_green,   
    itm_r2series_orange,
    #itm_r2series_purple,
    itm_r2series_blue,
    itm_r2series_green,   
    itm_r2series_orange,
    itm_r2series_purple   
  ],
  droid_attrib_2|level(25),
  wp(40),
  droid_skills_2,
  droid_face1, droid_face2
],

#power_droid
#["power_droid","EG-6 Power Droid","EG-6 Power Droids",
["power_droid","EG-Series Power Droid","EG-Series Power Droids",
  tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_droid_weapon_no_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet, 
    #itm_power_droid_legs,
    itm_power_droid_tan,
    itm_power_droid_tan,
    itm_power_droid_grey,
    itm_power_droid_grey,
    itm_power_droid_snow
    #itm_power_droid_snow
  ],
  droid_attrib_2|level(24),
  wp(40),
  droid_skills_2,
  droid_face1, droid_face2
],

#power_droid
#["power_droid","EG-6 Power Droid","EG-6 Power Droids",
["fxseries_droid","FX-Series Medical Droid","FX-Series Medical Droids",
  tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_droid_weapon_no_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet, 
    itm_fxseries_droid_armor,
    itm_fxseries_droid_armor
  ],
  droid_attrib_2|level(32),
  wp(60),
  droid_skills_2,
  droid_face1, droid_face2
],

# r2series droid
["lin_droid","LIN Droid","LIN Droids",
  tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_droid_weapon_no_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet, 
    itm_lin_droid_armor,
    itm_lin_droid_armor,
    itm_lin_droid_armor_w_arm
  ],
  droid_attrib_2|level(20),
  wp(30),
  droid_skills_2,
  droid_face1, droid_face2
],

# mse6 droid
["mse6","MSE-Series Droid","MSE-Series Droids",
  tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_commoners,
  [
    itm_droid_parts,
    itm_droid_weapon_no_attack,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet, 
    itm_mse6_armor
  ],
  droid_attrib_1|level(15),
  wp(20),
  droid_skills_1,
  droid_face1, droid_face2
],

###################################################################################
#SW - special culture specific troops
#human
["human_messenger","Messenger","Messengers",
  tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
  0,0,fac_neutral,
  [itm_speeder,itm_ind_clothes_outfsmuggler_red,itm_black_gloves,itm_eyepiece_tactics,itm_a280,itm_laser_bolts_yellow_rifle,itm_westar_shield,itm_vibro_sword3_gold],
  def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,sw_man_face_1, sw_man_face_2
],
["human_deserter","Deserter","Deserters",
  tf_guarantee_boots|tf_guarantee_all_armor,
  0,0,fac_neutral,
  [itm_ind_clothes_outfsmuggler_red,itm_black_gloves,itm_dl44a,itm_laser_bolts_yellow_pistol,itm_combat_knife],
  def_attrib_2|level(16),wp(80),starwars_skills_2,sw_man_face_1, sw_man_face_2
],
#wookiee
["wookiee_messenger","Wookiee Messenger","Wookiee Messengers",
  tf_wookiee|tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
  0,0,fac_neutral,
  [itm_speeder,itm_ryyk_blade,itm_wookiee_bowcaster,itm_laser_bolts_green_rifle,itm_wookiee_shield_large,itm_wookiee_fur],
  def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,wookiee_face1, wookiee_face2
],
["wookiee_deserter","Wookiee Deserter","Wookiee Deserters",
  tf_wookiee|tf_guarantee_boots|tf_guarantee_armor,
  0,0,fac_neutral,
  [itm_ryyk_blade,itm_wookiee_bowcaster,itm_laser_bolts_green_rifle,itm_wookiee_shield_large,itm_wookiee_fur],
  def_attrib_2|level(16),wp(80),starwars_skills_2,wookiee_face1, wookiee_face2
],
#mandalorian
["mandalorian_messenger","Mandalorian Messenger","Mandalorian Messengers",
  tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_ranged,
  0,0,fac_neutral,
  [itm_speeder_hutt,itm_mand_arm_dummy,itm_mand_helm_dummy,itm_grey_gloves,itm_combat_knife,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster,itm_westar_shield],
  def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,mandalorian_face1, mandalorian_face2
],
["mandalorian_deserter","Mandalorian Deserter","Mandalorian Deserters",
  tf_guarantee_boots|tf_guarantee_boots|tf_guarantee_all_armor,
  0,0,fac_neutral,
  [itm_mand_arm_dummy,itm_mand_helm_dummy,itm_grey_gloves,itm_combat_knife,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster],
  def_attrib_2|level(16),wp(80),starwars_skills_2,mandalorian_face1, mandalorian_face2
],
#clone
["clone_messenger","Clone Messenger","Clone Messengers",
  tf_tusken|tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
  0,0,fac_neutral,
  [itm_speeder,itm_rep_arm_phase1_red,itm_rep_helm_phase1_red,itm_black_gloves,itm_combat_knife,itm_laser_bolts_blue_rifle,itm_dc15a],
  def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,mandalorian_face1, mandalorian_face2
],
["clone_deserter","Clone Deserter","Clone Deserters",
  tf_tusken|tf_guarantee_boots|tf_guarantee_all_armor,
  0,0,fac_neutral,
  [itm_rep_arm_phase1_white,itm_rep_helm_phase1_white,itm_black_gloves,itm_combat_knife,itm_laser_bolts_blue_rifle,itm_dc15s],
  def_attrib_2|level(16),wp(80),starwars_skills_2,mandalorian_face1, mandalorian_face2
],
#trandoshan
["trandoshan_messenger","Trandoshan Messenger","Trandoshan Messengers",
  tf_trandoshan|tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_ranged,
  0,0,fac_neutral,
  [itm_speeder,itm_trandoshan_blade,itm_laser_bolts_orange_rifle,itm_trandoshan_acp_array_gun,itm_trandoshan_skin],
  def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4, trandoshan_face1, trandoshan_face2
],
["trandoshan_deserter","Trandoshan Deserter","Trandoshan Deserters",
  tf_trandoshan|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_all_armor,
  0,0,fac_neutral,
  [itm_trandoshan_blade,itm_laser_bolts_orange_rifle,itm_trandoshan_acp_array_gun,itm_trandoshan_skin],
  def_attrib_2|level(16),wp(80),starwars_skills_2, trandoshan_face1, trandoshan_face2
],
###################################################################################

#SW BSG integration - player_inactive for BSG integration (nevermind, not used)
#  ["player_inactive","Player","Player",tf_hero|tf_unmoveable_in_party_window|tf_inactive,no_scene,reserved,fac_player_faction, 
#   [],str_4|agi_4|int_4|cha_4,wp(25)|wp_firearm(50)|wp_throwing(35),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  
["force_sensitive_recruit","Force-Sensitive","Force-Sensitives",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_training_lightsaber_blue_1h,
    itm_training_lightsaber_green_1h,
    itm_stun_beam_pistol,
    itm_stun_beam_pistol,
    itm_q2_stun,
    itm_q2_stun,
    itm_dl44a_stun,
    itm_dl44a
  ],
  def_attrib_force_1|level(6),
  wp(60)|wp_archery(70),
  starwars_skills_force_1,
  sw_imperial_face_1, sw_imperial_face_2
],  
  
#================================================================================================================================ 
#SW - Republic troops 
#SW - Grand Army of Republic Soldiers (removed tf_guarantee_ranged from sith apprentice/master/lord so they will be part of the infantry group and can be given separate battle commands)
["imperial_recruit","Republic Clone Cadet","Republic Clone Cadets",
  tf_tusken|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_imperial_trooper_armor,
    itm_imperial_hat_black,
    itm_melee_punch,
    itm_laser_bolts_blue_rifle,
      itm_dc15s,
  ],
  def_attrib_1|level(8),
  wp(70)|wp_firearm(95)|wp_archery(0),
  starwars_skills_1,
  sw_imperial_face_1, sw_imperial_face_2
],

# ["imperial_cadet","Imperial Cadet","Imperial Cadets",
  # tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  # no_scene,reserved,fac_neutral,
  # [
    # itm_imperial_trooper_armor,
    # itm_imperial_trooper_armor,
    # itm_imperial_hat_black,
    # itm_imperial_hat_black,
    # itm_melee_punch,
    # itm_laser_bolts_red,
    # itm_laser_bolts_red,
    # itm_q2,
    # itm_q2,
    # itm_westar,
    # itm_westar
  # ],
  # def_attrib_1|level(8),
  # wp(70)|wp_firearm(80),
  # starwars_skills_1,
  # sw_imperial_face_1, sw_imperial_face_2
# ],

#SW - Darksider troop tree
["sith_hopeful","Jedi Hopeful","Jedi Hopefuls",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_black_gloves,
    itm_jedi_clothes_robes_tan,
    itm_jedi_clothes_robes_black,
    itm_jedi_clothes_robes_grey,
    itm_jedi_clothes_robes_brown,
    itm_training_lightsaber_blue_1h,
    itm_training_lightsaber_green_1h,
    itm_laser_bolts_green_pistol,
    itm_laser_bolts_green_pistol,
    itm_q2,
    itm_q2,
    itm_dl44a,
    itm_dl44a
  ],
  def_attrib_force_1|level(10),
  wp(100)|wp_archery(120),
  starwars_skills_force_1,
  sw_rebel_face_1, sw_rebel_face_2
],
["sith_acolyte","Dark Acolyte","Dark Acolytes",
  tf_guarantee_boots|tf_guarantee_all_armor,
  no_scene,reserved,fac_neutral,
  [
    itm_black_gloves,
    itm_sith_marauder_robe_a,
    itm_sith_marauder_robe_b,
    itm_sith_marauder_robe_c,
    itm_sith_marauder_robe_d,
    itm_training_lightsaber_red_1h,
    itm_training_lightsaber_red_1h,
    itm_force_power_ds_1,
    itm_force_power_ds_1,
    itm_force_lightning_ammo,
    itm_force_lightning_ammo
  ],
  def_attrib_force_2|level(14),
  wp(130)|wp_archery(150),
  starwars_skills_force_2,
  sw_imperial_face_1, sw_imperial_face_2
],
["sith_apprentice","Dark Apprentice","Dark Apprentices",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield,
  no_scene,0,fac_neutral,
  [
    itm_black_gloves,
    itm_sith_marauder_robe_a,
    itm_sith_marauder_robe_b,
    itm_sith_marauder_robe_c,
    itm_sith_marauder_robe_d,
    itm_lightsaber_red_1h,
    itm_lightsaber_red_1h,
    itm_force_block,
    itm_force_block,
    itm_force_power_ds_2,
    itm_force_power_ds_2,
    itm_force_lightning_ammo,
    itm_force_lightning_ammo
  ],
  def_attrib_force_2|level(18),
  wp(160)|wp_archery(180),
  starwars_skills_force_2,
  sw_imperial_face_1, sw_imperial_face_2
],
["sith_knight","Dark Jedi","Dark Jedi",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [ 
    itm_black_gloves,
    itm_sith_clothes_robes_assassin,
    #itm_sith_marauder_robe_b,
    #itm_sith_marauder_robe_c,
    #itm_sith_marauder_robe_d,
    itm_lightsaber_red_1h,
    itm_lightsaber_red_1h,
    itm_lightsaber_red,
    itm_lightsaber_red,
    #itm_force_shield,
    #itm_force_shield,
    itm_lightsaber_block_red,
    itm_lightsaber_block_red,
    itm_force_power_ds_3,
    itm_force_power_ds_3,
    itm_force_lightning_ammo,
    itm_force_lightning_ammo,
    itm_force_throw_lightsaber_red,
    itm_force_throw_lightsaber_red
  ],
  def_attrib_force_3|level(22),
  wp(190)|wp_archery(210),
  starwars_skills_force_3,
  sw_imperial_face_1, sw_imperial_face_2
],
["sith_marauder","Dark Assassin","Dark Assassins",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [ 
    itm_sith_clothes_robes_assassin,
    #itm_sith_marauder_robe_b,
    #itm_sith_marauder_robe_c,
    #itm_sith_marauder_robe_d,
    itm_black_gloves,
    itm_black_gloves,
    itm_lightsaber_red,
    itm_lightsaber_red,
    #itm_force_shield,
    #itm_force_shield,
    itm_force_protect,
    itm_force_protect,
    itm_lightsaber_block_red,
    itm_lightsaber_block_red,
    itm_force_power_ds_3,
    itm_force_power_ds_3,
    itm_force_lightning_ammo,
    itm_force_lightning_ammo,
    itm_force_throw_lightsaber_red,
    itm_force_throw_lightsaber_red
  ],
  def_attrib_force_3|level(28),
  wp(220)|wp_archery(240),
  starwars_skills_force_3,
  sw_sith_face_1, sw_sith_face_2
],
["sith_master","Dark Master","Dark Masters",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [ 
    itm_sith_master_robe_unique,
    itm_sith_master_robe_unique,
    #itm_black_gloves,
    #itm_black_gloves,
    itm_lightsaber_red,
    itm_lightsaber_red,
    itm_force_protect,
    itm_force_protect,
    itm_force_power_ds_4,
    itm_force_power_ds_4,
    itm_force_lightning_ammo,
    itm_force_lightning_ammo,
    itm_force_throw_lightsaber_red,
    itm_force_throw_lightsaber_red
  ],
  def_attrib_force_4|level(35),
  wp(250)|wp_archery(270),
  starwars_skills_force_4,
  sw_sith_face_1, sw_sith_face_2
],
["sith_lord","Dark Lord","Dark Lords",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [ 
    itm_sith_master_robe_unique,
    itm_sith_master_robe_unique,
    itm_black_gloves,
    itm_black_gloves,
    itm_lightsaber_red,
    itm_lightsaber_red,
    itm_force_protect,
    itm_force_protect,
    itm_force_power_ds_4,
    itm_force_power_ds_4,
    itm_force_lightning_ammo,
    itm_force_lightning_ammo,
    itm_force_throw_lightsaber_red,
    itm_force_throw_lightsaber_red
  ],
  def_attrib_force_4|level(42),
  wp(280)|wp_archery(300),
  starwars_skills_force_4,
  sw_sith_face_1, sw_sith_face_2
],
#SW - Republic troop tree      

["imperial_navy_trooper","Clone Trooper","Clone Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_clean,
    itm_clone_trooper_gloves_white,
    itm_phase_ii_helmet_clean,
    itm_baton,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a,
  
  ],
  def_attrib_1|level(12),
  wp(100)|wp_firearm(100)|wp_crossbow(100)|wp_archery(0),
  starwars_skills_1,
  sw_imperial_face_1, sw_imperial_face_2
],

["imperial_army_trooper","Veteran Clone Trooper","Veteran Clone_Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_worn,
    itm_clone_trooper_gloves_white,
      itm_phase_ii_clonepack,
    itm_phase_ii_helmet_worn,
      itm_baton,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15a,
  
  ],
  def_attrib_1|level(14),
  wp(120)|wp_firearm(120)|wp_archery(0),
  starwars_skills_1,
  sw_imperial_face_1, sw_imperial_face_2
],

### Bugged entry, doesnt show correctly it's armor
["imperial_gunner","Republic Shocktrooper","Republic Shocktroopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_shock,
    itm_clone_trooper_gloves_red,
      itm_phase_ii_clonepack,   
    itm_phase_ii_helmet_shock,
    itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
  
  ],
  def_attrib_2|level(16),
  wp(140)|wp_firearm(140)|wp_archery(0),
  starwars_skills_1,
  sw_imperial_face_1, sw_imperial_face_2
],

["imperial_stormtrooper","Battle-hardened Clone Trooper","Battle-Hardened Clones",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
  [
    itm_phase_ii_armor_worn,
    itm_clone_trooper_gloves_white,
    itm_phase_ii_helmet_worn,
      itm_vibro_blade1,
    itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
      itm_dc15a_hip,
      itm_dc15a,
    itm_dc15s,
      itm_phase_ii_clonepack,
  
  ],
  def_attrib_2|level(18),
  wp(175)|wp_firearm(175)|wp_archery(0),
  starwars_skills_2,
  sw_imperial_face_1, sw_imperial_face_2
],
["imperial_pilot","212th Clone Trooper","212th Clone Troopers",
  tf_tusken|tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,0,fac_neutral,
  [
    itm_phase_ii_armor_212,
    itm_clone_trooper_gloves_white,
    itm_phase_ii_helmet_212,
      itm_vibro_blade1,
    itm_baton2,
      itm_phase_ii_clonepack,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a,
  
  ],
  def_attrib_2|level(22),
  wp(200)|wp_firearm(200)|wp_archery(0),
  starwars_skills_2,
  sw_imperial_face_1, sw_imperial_face_2
],
["imperial_scout_trooper","Clone Marksman","Clone Marksmans",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
  [
    itm_phase_ii_armor_worn,
    itm_rep_helm_phase2scout,
      itm_phase_ii_clonepack,
    itm_phase_ii_sniper_gear,
    itm_black_gloves_long,
    itm_clone_trooper_gloves_white,
      itm_dlt19_scope,
    itm_vibro_blade1,
    #itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
  ],
  def_attrib_2|level(20),
  wp(220)|wp_firearm(220)|wp_archery(0),
  starwars_skills_2,
  sw_imperial_face_1, sw_imperial_face_2
],
["republic_clone_clonesniper","Clone Sniper","Clone Snipers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
  [
    itm_phase_ii_armor_worn,
    itm_rep_helm_phase2arf,
      itm_phase_ii_clonepack,
    itm_phase_ii_sniper_gear,
    itm_black_gloves_long,
    itm_clone_trooper_gloves_white,
      itm_dlt19_scope,
    itm_vibro_blade1,
    #itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
  ],
  def_attrib_2|level(27),
  wp(275)|wp_firearm(275)|wp_archery(0),
  starwars_skills_2,
  sw_imperial_face_1, sw_imperial_face_2
],
["republic_clone_442clone","442nd Clone Trooper","442nd Clone Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
  [
    itm_phase_ii_armor_442,
    itm_phase_ii_helmet_442,
    itm_black_gloves_long,
    itm_clone_trooper_gloves_white,
      itm_dc15s,
    itm_dc15a,
    itm_vibro_blade1,
    #itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
  ],
  def_attrib_2|level(20),
  wp(120)|wp_firearm(160),wp_crossbow(220)|wp_archery(0),
  starwars_skills_2,
  sw_imperial_face_1, sw_imperial_face_2
],
["republic_clone_442cloneveteran","442nd Clone Trooper Veteran","442nd Clone Troopers Veterans",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
  [
    itm_phase_ii_armor_442,
    itm_phase_ii_helmet_442,
      itm_phase_ii_clonepack,
    itm_black_gloves_long,
    itm_clone_trooper_gloves_white,
      itm_dc15s,
    itm_dc15a,
    itm_vibro_blade1,
    #itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
  ],
  def_attrib_2|level(20),
  wp(120)|wp_firearm(160),wp_crossbow(220)|wp_archery(0),
  starwars_skills_2,
  sw_imperial_face_1, sw_imperial_face_2
],
["republic_clone_442clonearc","442nd ARC Trooper","442nd ARC Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
  [
    itm_phase_ii_armor_442,
    itm_phase_ii_helmet_442,
      itm_phase_ii_arc_kama,
    itm_black_gloves_long,
    itm_clone_trooper_gloves_white,
      itm_dc15s,
    itm_dc15a,
    itm_vibro_blade1,
    #itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
  ],
  def_attrib_2|level(20),
  wp(120)|wp_firearm(160),wp_crossbow(220)|wp_archery(0),
  starwars_skills_2,
  sw_imperial_face_1, sw_imperial_face_2
],
["imperial_gunner_veteran","212th Elite Trooper","212th Elite Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_212,
    itm_clone_trooper_gloves_white,
    itm_phase_ii_helmet_212,
    itm_vibro_blade1,
      itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a,
  
  ],
  def_attrib_4|level(25),
  wp(235)|wp_firearm(235)|wp_archery(0),
  starwars_skills_4,
  sw_imperial_face_1, sw_imperial_face_2
],
["imperial_stormtrooper_veteran","Elite Clone Trooper","Elite Clone Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_worn,
    itm_clone_trooper_gloves_white,
      itm_phase_ii_clonepack,
    itm_phase_ii_helmet_worn,
    itm_baton,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15a_hip,
    itm_dc15a,
      itm_dlt20a,
  
  ],
  def_attrib_3|level(24),
  wp(200)|wp_firearm(200)|wp_archery(0),
  starwars_skills_4,
  sw_imperial_face_1, sw_imperial_face_2
],
["incinerator_trooper","Republic Senate Commando","Republic Senate Commandos",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [ 
    itm_senate_guard_gloves,
    itm_senate_commando_armor,
    itm_senate_commando_helm,
    itm_senate_commando_helm1,
    itm_baton2,
    #itm_baton,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_storm_rifle,
    itm_dlt19,
    itm_dlt20a,
    itm_dc15a,
    itm_dc15s,
  ],
  def_attrib_3|level(34),
  wp(365)|wp_firearm(365)|wp_archery(0),
  starwars_skills_3,
  sw_imperial_face_1, sw_imperial_face_2
],
["novatrooper","501st Legion Clone Trooper","501st Legion Clone Trooper",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_white,
      itm_phase_ii_clonepack,
    itm_phase_ii_helmet_501,
      itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a,
      itm_dc15a_hip,
  
  ],
  def_attrib_4|level(28),
  wp(265)|wp_firearm(265)|wp_archery(0),
  starwars_skills_3,
  sw_imperial_face_1, sw_imperial_face_2
],
["imperial_pilot_veteran","Clone Lancer","Clone Lancers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_worn,
    itm_clone_trooper_gloves_white,
      itm_phase_ii_helmet_worn,
    itm_lance,
      itm_lance,
      itm_force_pike,
      itm_dc17sa,
    itm_laser_bolts_blue_pistol,
    itm_energy_shield_blue_small,
    itm_speeder_dagger,
  
  ],
  def_attrib_3|level(24),
  wp(200)|wp_polearm(250)|wp_archery(0),
  starwars_skills_mounted_4,
  sw_imperial_face_1, sw_imperial_face_2
],
["imperial_scout_trooper_veteran","Wolfpack Battalion Clone Trooper","Wolfpack Battalion Clone Troopers",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_wolf,
    itm_clone_trooper_gloves_white,
      itm_phase_ii_clonepack,
    itm_phase_ii_helmet_wolf,
      itm_vibro_blade1,
    itm_vibro_blade1,
      itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a,
  ],
  def_attrib_4|level(24),
  wp(265)|wp_firearm(265)|wp_archery(0),
  starwars_skills_3,
  sw_imperial_face_1, sw_imperial_face_2
],
["imperial_scout_trooper_marksman","Elite 501st Legion Clone","Elite 501st Legion Clones",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_501,
      itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_white,
      itm_phase_ii_arc_kama,
    itm_phase_ii_helmet_501,
    itm_dc15s,
      itm_laser_bolts_blue_rifle,
    itm_dc15a,
      itm_laser_bolts_blue_rifle,
      itm_baton2,
      itm_energy_shield_oval,
  
  ],
  str_18|agi_18|int_20|cha_15|level(30),
  wp(325)|wp_firearm(325)|wp_archery(0),
  starwars_skills_4,
  sw_imperial_face_1, sw_imperial_face_2
],

["imperial_scout_trooper_captain","Elite Wolfpack Battalion Clone","Elite Wolfpack Battalion Clones",
  tf_tusken|tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_wolf,
    itm_clone_trooper_gloves_white,
    itm_phase_ii_helmet_wolf,
      itm_vibro_blade1,
      itm_vibro_blade1,
      itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a,
  
  ],
  str_20|agi_19|int_20|cha_15|level(30),
  wp(325)|wp_firearm(325)|wp_archery(0),
  starwars_skills_4,
  sw_imperial_face_1, sw_imperial_face_2
],

["imperial_scout_trooper_sniper","Republic Clone Commando","Republic Clone Commandos",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_clone_commando_armor,
    itm_clone_commando_armor,
    itm_clone_commando_helmet,
    itm_clone_commando_helmet,
    itm_clone_trooper_gloves_white,
    itm_clone_trooper_gloves_white,
      itm_dc17m,
      itm_dc17m,
      itm_vibro_knuckler,
    itm_laser_bolts_blue_rifle,
  ],
  str_18|agi_18|int_18|cha_14|level(33),
  wp(325)|wp_firearm(325)|wp_archery(0),
  starwars_skills_4,
  sw_imperial_face_1, sw_imperial_face_2
],

# ["imperial_darktrooper","Imperial Dark Trooper","Imperial Dark Troopers",
  # tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,
  # no_scene,reserved,fac_neutral,
  # [

    # itm_black_gloves,
    # itm_black_gloves,
    # itm_vibro_sword3_gold,
    # itm_vibro_sword3_gold,
    # itm_laser_bolts_red,
    # itm_laser_bolts_red,
    # itm_dlt19,
    # itm_dlt19,
    # itm_e11,
    # itm_e11
  # ],
  # def_attrib_4|level(30),
  # wp(150)|wp_firearm(170),
  # starwars_skills_4,
  # sw_imperial_face_1, sw_imperial_face_2
# ],

["imperial_stormtrooper_officer","Veteran Republic Clone Commando","Veteran Republic Commandos",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_clone_commando_armor,
    itm_clone_commando_armor,
    itm_clone_commando_helmet,
    itm_clone_commando_helmet,
    itm_clone_trooper_gloves_white,
    itm_clone_trooper_gloves_white,
    itm_dc17m,
      itm_dc17m,
      itm_vibro_blade1,
      itm_energy_shield_blue_small,
      itm_disruptor_ammo_rifle,

  ],
  str_20|agi_18|int_20|cha_14|level(36),
  wp(390)|wp_firearm(390)|wp_archery(0),
  starwars_skills_4,
  sw_imperial_face_1, sw_imperial_face_2
],

# ["imperial_shadow_stormtrooper","Imperial Shadow Stormtrooper","Imperial Shadow Stormtrooper",
  # tf_guarantee_all_armor|tf_guarantee_ranged,
  # no_scene,reserved,fac_neutral,
  # [ 
  # ],
  # def_attrib_4|level(30),
  # wp(150)|wp_firearm(170),
  # starwars_skills_4,
  # sw_imperial_face_1, sw_imperial_face_2
# ],

["imperial_royal_guard","Republic Senate Guard","Republic Senate Guards",
  tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_force_pike,
    itm_force_pike,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle,
    itm_dlt19,
    itm_dlt19,
  ],
  def_attrib_4|level(30),
  wp(160)|wp_crossbow(170)|wp_archery(0),
  starwars_skills_4,
  sw_imperial_face_1, sw_imperial_face_2
],

# ["imperial_shadow_scout_trooper","Imperial Shadow Scout Trooper","Imperial Shadow Scout Trooper",
  # tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
  # no_scene,reserved,fac_neutral,
  # [
    # itm_black_gloves_long,
    # itm_black_gloves_long,
    # itm_vibro_sword3_gold,
    # itm_vibro_sword3_gold,
    # itm_laser_bolts_red,
    # itm_laser_bolts_red,
    # itm_dlt19,
    # itm_dlt20a
  # ],
  # def_attrib_4|level(35),
  # wp(175)|wp_firearm(200),
  # starwars_skills_mounted_4,
  # sw_imperial_face_1, sw_imperial_face_2
# ],

["imperial_messenger","Imperial Messenger","Imperial Messengers",
  tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
  0,0,fac_neutral,
  [itm_black_gloves,itm_speeder_imperial,itm_imperial_scout_trooper_armor,itm_imperial_scout_trooper_helmet],#itm_imperial_scout_trooper_boots,itm_black_gloves,itm_laser_bolts_red_pistol,itm_scout_trooper_pistol,itm_baton],
  def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,sw_imperial_face_1, sw_imperial_face_2
],
["imperial_deserter","Imperial Deserter","Imperial Deserters",
  tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,
  0,0,fac_deserters,
  [itm_black_gloves,itm_imperial_scout_trooper_armor,itm_laser_bolts_red_pistol,itm_laser_bolts_red_pistol,itm_q2,itm_dl44a,itm_melee_punch],
  def_attrib_2|level(16),wp(80),starwars_skills_2,sw_imperial_face_1, sw_imperial_face_2
],

#================================================================================================================================
#SW - rebelalliance troops
#SW - rebel alliance soldiers (removed tf_guarantee_ranged from jedi padawan/knight/master so they will be part of the infantry group and can be given separate battle commands)
["rebel_recruit","Factory New B1 Battledroid","Factory New B1 Battledroids",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
    [
    itm_b1series_body,
    itm_transparent_droid_feet,
      itm_transparent_droid_head,
      itm_transparent_droid_hands,
    itm_melee_punch,
      itm_e5,
    itm_laser_bolts_red_rifle,
  ],
  def_attrib_1|level(5),
  wp(30)|wp_firearm(70),
  starwars_skills_1,
  sw_rebel_face_1, sw_rebel_face_2
],
#SW - jedi upgrade tree
["jedi_hopeful","Darksider","Darksiders",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_black_gloves,
    itm_sith_marauder_robe_a,
    itm_sith_marauder_robe_b,
    itm_sith_marauder_robe_c,
    itm_sith_marauder_robe_d,
    itm_training_lightsaber_red_1h,
    itm_training_lightsaber_red_1h,
    itm_laser_bolts_red_pistol,
    itm_laser_bolts_red_pistol,
    itm_q2,
    itm_q2,
    itm_dl44a,
    itm_dl44a
  ],
  def_attrib_force_1|level(10),
  wp(100)|wp_archery(120),
  starwars_skills_force_1,
  sw_imperial_face_1, sw_imperial_face_2
],
["jedi_initiate","Jedi Initiate","Jedi Initiates",
  tf_guarantee_boots|tf_guarantee_all_armor,
  no_scene,reserved,fac_neutral,
  [
    itm_black_gloves,
    itm_jedi_clothes_robes_tan,
    itm_jedi_clothes_robes_black,
    itm_jedi_clothes_robes_grey,
    itm_jedi_clothes_robes_brown,
    itm_training_lightsaber_blue_1h,
    itm_training_lightsaber_green_1h,
    itm_force_power_ls_1,
    itm_force_power_ls_1,
    itm_force_push_ammo,
    itm_force_push_ammo
  ],
  def_attrib_force_2|level(14),
  wp(130)|wp_archery(150),
  starwars_skills_force_2,
  sw_rebel_face_1, sw_rebel_face_2
],
["jedi_padawan","Jedi Padawan","Jedi Padawans",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield,
  no_scene,0,fac_neutral,
  [
    itm_black_gloves,
    itm_jedi_clothes_robes_tan,
    itm_jedi_clothes_robes_black,
    itm_jedi_clothes_robes_grey,
    itm_jedi_clothes_robes_brown,
    itm_lightsaber_blue_1h,
    itm_lightsaber_green_1h,
    itm_force_block,
    itm_force_block,    
    itm_force_power_ls_2,
    itm_force_power_ls_2,
    itm_force_push_ammo,
    itm_force_push_ammo
  ],
  def_attrib_force_2|level(18),
  wp(160)|wp_archery(180),
  starwars_skills_force_2,
  sw_rebel_face_1, sw_rebel_face_2
],
["jedi_guardian","Jedi Guardian","Jedi Guardians",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [ 
    itm_black_gloves,
    itm_jedi_clothes_robes_tan,
    itm_jedi_clothes_robes_black,
    itm_jedi_clothes_robes_grey,
    itm_jedi_clothes_robes_brown,
    itm_lightsaber_blue,
    itm_lightsaber_blue,    
    itm_force_block,
    itm_force_block,    
    itm_lightsaber_block_blue,
    itm_lightsaber_block_blue,    
    itm_force_throw_lightsaber_blue,
    itm_force_throw_lightsaber_blue
  ],
  def_attrib_force_3|level(22),
  wp(190)|wp_archery(210),
  starwars_skills_force_3,
  sw_rebel_face_1, sw_rebel_face_2
],
["jedi_consular","Jedi Consular","Jedi Consulars",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [
    itm_black_gloves,
    itm_jedi_clothes_robes_tan,
    itm_jedi_clothes_robes_black,
    itm_jedi_clothes_robes_grey,
    itm_jedi_clothes_robes_brown,
    itm_lightsaber_green,
    itm_lightsaber_green,       
    itm_force_power_ls_3, #give 3x to increase the chance they get a ranged attack since guarantee_ranged will make them fall into the archer group
    itm_force_power_ls_3,
    itm_force_power_ls_3,
    itm_force_push_ammo,
    itm_force_push_ammo,
    itm_force_push_ammo
  ],
  def_attrib_force_3|level(22),
  wp(190)|wp_archery(210),
  starwars_skills_force_3,
  sw_rebel_face_1, sw_rebel_face_2
],
["jedi_warrior_master","Jedi Warrior Master","Jedi Warrior Masters",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [ 
    itm_black_gloves,
    itm_jedi_clothes_robesmaster_tan,
    itm_jedi_clothes_robesmaster_black,
    itm_jedi_clothes_robesmaster_grey,
    itm_jedi_clothes_robesmaster_brown,
    itm_lightsaber_blue,
    itm_lightsaber_blue,
    itm_lightsaber_block_blue,
    itm_lightsaber_block_blue,
    itm_force_throw_lightsaber_blue,
    itm_force_throw_lightsaber_blue
  ],
  def_attrib_force_3|level(28),
  wp(220)|wp_archery(240),
  starwars_skills_force_3,
  sw_rebel_face_1, sw_rebel_face_2
],
["jedi_sage_master","Jedi Sage Master","Jedi Sage Masters",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [ 
    itm_black_gloves,
    itm_jedi_clothes_robesmaster_tan,
    itm_jedi_clothes_robesmaster_black,
    itm_jedi_clothes_robesmaster_grey,
    itm_jedi_clothes_robesmaster_brown,
    itm_lightsaber_green,
    itm_lightsaber_green,   
    itm_force_protect,
    itm_force_protect,    
    itm_force_power_ls_3, #give 3x to increase the chance they get a ranged attack since guarantee_ranged will make them fall into the archer group
    itm_force_power_ls_3,
    itm_force_power_ls_3,
    itm_force_push_ammo,
    itm_force_push_ammo,
    itm_force_push_ammo
  ],
  def_attrib_force_3|level(28),
  wp(220)|wp_archery(240),
  starwars_skills_force_3,
  sw_rebel_face_1, sw_rebel_face_2
],
["jedi_councilor","Jedi Councilor","Jedi Councilors",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [ 
    itm_black_gloves,
    itm_jedi_clothes_robesmaster_tan,
    itm_jedi_clothes_robesmaster_black,
    itm_jedi_clothes_robesmaster_grey,
    itm_jedi_clothes_robesmaster_brown,
    itm_lightsaber_blue,
    itm_lightsaber_green,
    itm_lightsaber_purple,
    itm_force_protect,
    itm_force_protect,
    itm_force_power_ls_4,
    itm_force_power_ls_4,   
    itm_force_push_ammo,
    itm_force_push_ammo,    
    itm_force_throw_lightsaber_blue,
    itm_force_throw_lightsaber_green,
    itm_force_throw_lightsaber_purple
  ],
  def_attrib_force_4|level(35),
  wp(250)|wp_archery(270),
  starwars_skills_force_4,
  sw_rebel_face_1, sw_rebel_face_2
],
["jedi_grand_master","Jedi Grand Master","Jedi Grand Masters",
  tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_shield|tf_guarantee_helmet,
  no_scene,0,fac_neutral,
  [ 
    itm_black_gloves,
    itm_jedi_clothes_robesmaster_tan,
    itm_jedi_clothes_robesmaster_black,
    itm_jedi_clothes_robesmaster_grey,
    itm_jedi_clothes_robesmaster_brown,
    itm_lightsaber_blue,
    itm_lightsaber_green,
    itm_lightsaber_purple,
    itm_force_protect,
    itm_force_protect,
    itm_force_power_ls_4,
    itm_force_power_ls_4,   
    itm_force_push_ammo,
    itm_force_push_ammo,
    itm_force_throw_lightsaber_blue,
    itm_force_throw_lightsaber_green,
    itm_force_throw_lightsaber_purple
  ],
  def_attrib_force_4|level(42),
  wp(280)|wp_archery(300),
  starwars_skills_force_4,
  sw_rebel_face_1, sw_rebel_face_2
],
#SW - rebel upgrade tree
["rebel_cadet","Field Tested B1 Battledroid","Field Tested B1 Battledroid",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
    [
      itm_b1series_body,
      itm_transparent_droid_feet,
      itm_transparent_droid_head,
      itm_transparent_droid_hands,
      itm_melee_punch,
      itm_e5,
      itm_laser_bolts_red_rifle,
  ],
    def_attrib_1|level(10),
  wp(45)|wp_firearm(90),
  starwars_skills_1,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_trooper","Enhanced B1 Battledroid","Enhanced B1 Battledroid",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
    [
      itm_b1series_body,
      itm_transparent_droid_feet,
      itm_transparent_droid_head,
      itm_transparent_droid_hands,
      itm_baton,
      itm_e5,
      itm_laser_bolts_red_rifle,
  ],
    def_attrib_2|level(15),
  wp(65)|wp_firearm(115),
  starwars_skills_2,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_scout","BX Sniper","Rebel Scouts",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
    [
      itm_droid_parts,
      itm_droid_parts,
      itm_bxseries_body,
      itm_transparent_droid_feet,
      itm_transparent_droid_head,
      itm_transparent_droid_hands,
      itm_e5s,
      itm_vibro_blade1,
      itm_vibro_blade3,
      itm_laser_bolts_red_rifle,
  ],
    str_16|agi_18|int_14|cha_8|level(24),
  wp(180)|wp_crossbow(250),
  starwars_skills_4|knows_ironflesh_4,
  sw_rebel_face_1, sw_rebel_face_2
],

#["rebel_trooper_veteran","Veteran Rebel Fleet Trooper","Veteran Rebel Fleet Troopers",
["rebel_vanguard","Rebel Vanguard","Rebel Vanguards",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
    [
    itm_black_gloves,
    itm_black_gloves,   
    itm_baton,
    itm_baton,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_a280,
    itm_a280_crouch
  ],
    def_attrib_3|level(24),
  wp(135)|wp_firearm(150),
  starwars_skills_3,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_pilot","B1 Pilotdroid","B1 Pilotdroids",
  tf_battledroid|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
    [
    itm_oomseries_pilot_body,
    itm_transparent_droid_feet,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_baton,
    itm_e5,
    itm_laser_bolts_red_rifle,
    itm_speeder_rebel
  ],
    def_attrib_2|level(20),
  wp(65)|wp_firearm(125),
  starwars_skills_mounted_2,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_commando","Enhanced B1 Pilotdroid","Enhanced B1 Pilotdroids",
  tf_battledroid|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [
    itm_oomseries_pilot_body,
    itm_transparent_droid_feet,
    itm_transparent_droid_head,
    itm_transparent_droid_hands,
    itm_baton,
    itm_e5,
    itm_laser_bolts_red_rifle,
    itm_speeder_rebel
  ],
    def_attrib_2|level(24),
  wp(80)|wp_crossbow(140),
  starwars_skills_mounted_3,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_marksman","Rebel Marksman","Rebel Marksmen",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
  no_scene,reserved,fac_neutral,
  [
    itm_leather_gloves,
    itm_leather_gloves,   
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_kisteer_1284,
    itm_dlt19_scope
  ],
    def_attrib_3|level(24),
  wp(135)|wp_crossbow(150),
  starwars_skills_3,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_honor_guard","Magnaguard","Magnaguards",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
    [
      itm_droid_parts,
      itm_droid_parts,
      itm_droid_parts,
      itm_magna_head_plain,
      itm_transparent_droid_hands,
      itm_transparent_droid_feet,   
      itm_magnaplain,
      itm_ig86_e5_pistol,
      itm_dlt19,
      itm_laser_bolts_red_rifle,
      itm_laser_bolts_red_rifle,
      itm_electro_staff_magna,
  ],
  str_20|agi_18|int_12|cha_12|level(35),
  wp(280)|wp_crossbow(170),
  starwars_skills_4,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_heavy_trooper","Enhanced BX Commando Droid","Enhanced BX Commando Droid",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
    [
      itm_droid_parts,
      itm_droid_parts,
      itm_droid_parts,
      itm_transparent_droid_head,
      itm_transparent_droid_hands,
      itm_transparent_droid_feet,   
      itm_bxseries_body,
      itm_e5,
      itm_e5s,
      itm_laser_bolts_red_rifle,
      itm_laser_bolts_red_rifle,
      itm_droid_sword,
      itm_droid_sword,
      itm_droid_blast_shield,
  ],
  str_22|agi_20|int_12|cha_10|level(30),
  wp(160)|wp_crossbow(220)|wp_one_handed(220),
  knows_ironflesh_6|knows_power_strike_6|knows_athletics_6|knows_tactics_6|knows_leadership_6|knows_trainer_5,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_pilot_veteran","IG Lancer Combat Droid","IG Lancer Combat Droid",
  tf_battledroid|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [
    itm_ig86_body,
    itm_transparent_droid_feet,
  itm_transparent_droid_head,
    itm_lance,
    itm_ig86_e5_pistol,
    itm_ig86_e5_shield,
    itm_speeder_dagger,
  ],
  def_attrib_4|level(30),
  wp(140)|wp_polearm(200)|wp_crossbow(200)|wp_firearm(220),
  starwars_skills_mounted_4,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_commando_veteran","Veteran Rebel Commando","Veteran Rebel Commandos",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
  no_scene,reserved,fac_neutral,
  [
    itm_leather_gloves,
    itm_leather_gloves,
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_a295,
    itm_a295_crouch
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(170),
  starwars_skills_4,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_sniper","Rebel Sniper","Rebel Snipers",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
  no_scene,reserved,fac_neutral,
  [
    itm_leather_gloves,
    itm_leather_gloves,   
    itm_vibro_blade1,
    itm_vibro_blade3,
    itm_laser_bolts_green_rifle,
    itm_laser_bolts_green_rifle,
    itm_kisteer_1284,
    itm_dlt19_scope
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(170),
  starwars_skills_4,
  sw_rebel_face_1, sw_rebel_face_2
],

["rebel_messenger","Rebel Messenger","Rebel Messengers",
     tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
[itm_speeder_rebel,itm_black_gloves,itm_laser_bolts_green_pistol,itm_dh17,itm_baton],
def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,sw_rebel_face_1, sw_rebel_face_2],
["rebel_deserter","Rebel Deserter","Rebel Deserters",
     tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
[itm_laser_bolts_green_pistol,itm_laser_bolts_green_pistol,itm_q2,itm_dl44a,itm_melee_punch],
def_attrib_2|level(16),wp(80),starwars_skills_2,sw_rebel_face_1, sw_rebel_face_2],  

#================================================================================================================================
#SW - huttcartel troops
#SW - Hutt Cartel soldiers
["hutt_militia","Hutt Militia","Hutt Militias",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
  [
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,
    itm_melee_punch,    
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_dl18,
    itm_dl18
  ],
  def_attrib_1|level(6),
  wp(60)|wp_firearm(70),
  starwars_skills_1,
  sw_hutt_face_1, sw_hutt_face_2
],
["hutt_mercenary","Hutt Mercenary","Hutt Mercenaries",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
  [
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,
    itm_vibro_blade1,
    itm_vibro_blade2,
    itm_melee_punch,    
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_ammo_belt_pistol,
    itm_dl18,
    itm_dl18
  ],
  def_attrib_1|level(10),
  wp(80)|wp_firearm(90),
  starwars_skills_1,
  sw_hutt_face_1, sw_hutt_face_2
],
["hutt_guard","Hutt Guard","Hutt Guards",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
  [
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_transparent_helmet,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,
    itm_vibro_blade1,
    itm_vibro_blade2,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_ammo_belt_pistol,
    itm_dl18,
    itm_dl18
  ],
  def_attrib_2|level(16),
  wp(95)|wp_firearm(110),
  starwars_skills_2,
  sw_hutt_face_1, sw_hutt_face_2
],
["hutt_marksman","Hutt Marksman","Hutt Marksmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
  no_scene,0,fac_neutral,
  [
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,
    itm_vibro_blade1,
    itm_vibro_blade2,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_ammo_belt_rifle,
    itm_a280,
    itm_a280_crouch
  ],
  def_attrib_2|level(16),
  wp(95)|wp_crossbow(110),
  starwars_skills_2,
  sw_hutt_face_1, sw_hutt_face_2
],
["hutt_bounty_hunter","Hutt Bounty Hunter","Hutt Bounty Hunters",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet,
  no_scene,reserved,fac_neutral,
  [ 
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,
    itm_vibro_blade1,
    itm_vibro_blade2,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_ammo_belt_rifle,
    itm_a280,
    itm_a280_crouch
  ],
  def_attrib_3|level(24),
  wp(135)|wp_crossbow(150),
  starwars_skills_3,
  sw_hutt_face_1, sw_hutt_face_2
],
["hutt_skiff_guard","Hutt Skiff Guard","Hutt Skiff Guards",
  tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [ 
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_transparent_helmet,
    itm_skiff_guard_helmet,
    itm_skiff_guard_helmet,
    itm_skiff_guard_helmet,   
    itm_speeder,
    itm_speeder,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,
    itm_ind_arm_lightmercenarya1,
    itm_ind_arm_lightmercenarya2,
    itm_ind_arm_lightmercenarya3,
    itm_ind_arm_lightmercenarya4,
    itm_ind_arm_lightmercenaryb1,
    itm_ind_arm_lightmercenaryb2,
    itm_ind_arm_lightmercenaryb3,
    itm_ind_arm_lightmercenaryb4,
    itm_ind_arm_lightmercenaryc1,
    itm_ind_arm_lightmercenaryc2,
    itm_ind_arm_lightmercenaryc3,
    itm_ind_arm_lightmercenaryc4,
    itm_ind_arm_lightmercenaryd1,
    itm_ind_arm_lightmercenaryd2,
    itm_ind_arm_lightmercenaryd3,
    itm_ind_arm_lightmercenaryd4,
    itm_vibro_axe_long_2h,
    itm_vibro_axe_long_2h,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_ammo_belt_pistol,
    itm_dl18,
    itm_dl18
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(150),
  starwars_skills_mounted_3,
  sw_hutt_face_1, sw_hutt_face_2
],
["hutt_palace_guard","Hutt Palace Guard","Hutt Palace Guards",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_helmet,
  no_scene,reserved,fac_neutral,
  [ 
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_arm_lightmercenarya1,
    itm_ind_arm_lightmercenarya2,
    itm_ind_arm_lightmercenarya3,
    itm_ind_arm_lightmercenarya4,
    itm_ind_arm_lightmercenaryb1,
    itm_ind_arm_lightmercenaryb2,
    itm_ind_arm_lightmercenaryb3,
    itm_ind_arm_lightmercenaryb4,
    itm_ind_arm_lightmercenaryc1,
    itm_ind_arm_lightmercenaryc2,
    itm_ind_arm_lightmercenaryc3,
    itm_ind_arm_lightmercenaryc4,
    itm_ind_arm_lightmercenaryd1,
    itm_ind_arm_lightmercenaryd2,
    itm_ind_arm_lightmercenaryd3,
    itm_ind_arm_lightmercenaryd4,
    itm_vibro_sword3_gold,
    itm_vibro_sword3_gold,
    itm_energy_shield_yellow_small,
    itm_energy_shield_red_small,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_ammo_belt_pistol,
    itm_dl18,
    itm_dl18
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(150),
  starwars_skills_melee_3,
  sw_hutt_face_1, sw_hutt_face_2
],
["hutt_commando","Hutt Commando","Hutt Commandos",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet,
  no_scene,reserved,fac_neutral,
  [
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_arm_heavyarmor_gold,
    itm_ind_arm_heavyarmor_blue,
    itm_ind_arm_heavyarmor_purple,
    itm_ind_arm_heavyarmor_green,
    itm_ind_arm_heavyarmor_silver,
    itm_ind_arm_lightmercenarya1,
    itm_ind_arm_lightmercenarya2,
    itm_ind_arm_lightmercenarya3,
    itm_ind_arm_lightmercenarya4,
    itm_ind_arm_lightmercenaryb1,
    itm_ind_arm_lightmercenaryb2,
    itm_ind_arm_lightmercenaryb3,
    itm_ind_arm_lightmercenaryb4,
    itm_ind_arm_lightmercenaryc1,
    itm_ind_arm_lightmercenaryc2,
    itm_ind_arm_lightmercenaryc3,
    itm_ind_arm_lightmercenaryc4,
    itm_ind_arm_lightmercenaryd1,
    itm_ind_arm_lightmercenaryd2,
    itm_ind_arm_lightmercenaryd3,
    itm_ind_arm_lightmercenaryd4,   
    itm_vibro_blade1,
    itm_vibro_blade2,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_ammo_belt_rifle,
    itm_a280,
    itm_a280_crouch
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(170),
  starwars_skills_4,
  sw_hutt_face_1, sw_hutt_face_2
],
["hutt_skiff_guard_captain","Hutt Skiff Guard Captain","Hutt Skiff Guard Captains",
  tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [ 
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_skiff_guard_helmet,
    itm_skiff_guard_helmet,
    itm_skiff_guard_helmet,
    itm_speeder_hutt,
    itm_speeder_hutt,
    itm_ind_helm_heavyhelmet_gold,
    itm_ind_helm_heavyhelmet_blue,
    itm_ind_helm_heavyhelmet_purple,
    itm_ind_helm_heavyhelmet_green,
    itm_ind_helm_heavyhelmet_silver,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_arm_lightmercenarya1,
    itm_ind_arm_lightmercenarya2,
    itm_ind_arm_lightmercenarya3,
    itm_ind_arm_lightmercenarya4,
    itm_ind_arm_lightmercenaryb1,
    itm_ind_arm_lightmercenaryb2,
    itm_ind_arm_lightmercenaryb3,
    itm_ind_arm_lightmercenaryb4,
    itm_ind_arm_lightmercenaryc1,
    itm_ind_arm_lightmercenaryc2,
    itm_ind_arm_lightmercenaryc3,
    itm_ind_arm_lightmercenaryc4,
    itm_ind_arm_lightmercenaryd1,
    itm_ind_arm_lightmercenaryd2,
    itm_ind_arm_lightmercenaryd3,
    itm_ind_arm_lightmercenaryd4,
    itm_ind_arm_heavyarmor_gold,
    itm_ind_arm_heavyarmor_blue,
    itm_ind_arm_heavyarmor_purple,
    itm_ind_arm_heavyarmor_green,
    itm_ind_arm_heavyarmor_silver,
    itm_vibro_axe_long_2h,
    itm_vibro_axe_long_2h,
    itm_laser_bolts_orange_rifle,
    itm_laser_bolts_orange_rifle,
    itm_ammo_belt_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_a295,
    itm_a295_crouch
  ],
  def_attrib_4|level(30),
  wp(150)|wp_crossbow(170),
  starwars_skills_mounted_4,
  sw_hutt_face_1, sw_hutt_face_2
],
["hutt_palace_guard_captain","Hutt Palace Guard Captain","Hutt Palace Guard Captains",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet,
  no_scene,reserved,fac_neutral,
  [
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,
    itm_ind_helm_heavyhelmet_gold,
    itm_ind_helm_heavyhelmet_blue,
    itm_ind_helm_heavyhelmet_purple,
    itm_ind_helm_heavyhelmet_green,
    itm_ind_helm_heavyhelmet_silver,
    itm_ind_arm_heavyarmor_gold,
    itm_ind_arm_heavyarmor_blue,
    itm_ind_arm_heavyarmor_purple,
    itm_ind_arm_heavyarmor_green,
    itm_ind_arm_heavyarmor_silver,
    itm_vibro_sword3_gold,
    itm_vibro_sword3_gold,
    itm_energy_shield_yellow_medium,
    itm_energy_shield_yellow_medium,
    itm_energy_shield_red_medium,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_ammo_belt_pistol,
    itm_dl44a,
    itm_dl44a
  ],
  def_attrib_4|level(30),
  wp(150)|wp_firearm(170),
  starwars_skills_melee_4,
  sw_hutt_face_1, sw_hutt_face_2
],

["hutt_messenger","Hutt Messenger","Hutt Messengers",
     tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
[
  itm_skiff_guard_helmet,
  itm_speeder_hutt,
  itm_ind_rep_guardarmor1,
  itm_ind_rep_guardarmor2,
  itm_ind_rep_guardarmor3,
  itm_ind_rep_guardarmor_black,
  itm_ind_clothes_outfitvest_red,
  itm_ind_clothes_outfitvest_green,
  itm_ind_clothes_outfsmuggler_red,
  itm_ind_clothes_outfsmuggler_green,
  itm_ind_clothes_outfsmuggleralter1_red,
  itm_ind_clothes_outfsmuggleralter1_green,
  itm_ind_clothes_outfsmuggleralter2_red,
  itm_ind_clothes_outfsmuggleralter2_green,
  itm_ind_clothes_securityguarda1,
  itm_ind_clothes_securityguarda2,
  itm_ind_clothes_securityguarda3,
  itm_ind_clothes_securityguarda4,
  itm_ind_clothes_securityguarda5,
  itm_ind_clothes_hutttunic_red,
  itm_ind_clothes_hutttunic_grey,
  itm_ind_clothes_hutttunic_brown,
  itm_ind_clothes_hutttuniccape_red,
  itm_ind_clothes_hutttuniccape_grey,
  itm_ind_clothes_hutttuniccape_brown,
  itm_laser_bolts_orange_pistol,
  itm_dl18,
  itm_vibro_axe_long_2h],
def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,sw_hutt_face_1, sw_hutt_face_2],
["hutt_deserter","Hutt Deserter","Hutt Deserters",
     tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_deserters,
[
  itm_weequay_head_helmet_a,
  itm_weequay_head_helmet_b,
  itm_klatooinian_head_helmet_a,
  itm_leather_gloves,
  itm_black_gloves,
  itm_transparent_helmet,
  itm_mining_helmet,
  itm_pipe_helmet,
  itm_fang_helmet,
  itm_beak_helmet,
  itm_gas_mask,
  itm_skiff_guard_helmet,
  itm_ind_rep_guardarmor1,
  itm_ind_rep_guardarmor2,
  itm_ind_rep_guardarmor3,
  itm_ind_rep_guardarmor_black,
  itm_ind_clothes_outfitvest_red,
  itm_ind_clothes_outfitvest_green,
  itm_ind_clothes_outfsmuggler_red,
  itm_ind_clothes_outfsmuggler_green,
  itm_ind_clothes_outfsmuggleralter1_red,
  itm_ind_clothes_outfsmuggleralter1_green,
  itm_ind_clothes_outfsmuggleralter2_red,
  itm_ind_clothes_outfsmuggleralter2_green,
  itm_ind_clothes_securityguarda1,
  itm_ind_clothes_securityguarda2,
  itm_ind_clothes_securityguarda3,
  itm_ind_clothes_securityguarda4,
  itm_ind_clothes_securityguarda5,
  itm_ind_clothes_hutttunic_red,
  itm_ind_clothes_hutttunic_grey,
  itm_ind_clothes_hutttunic_brown,
  itm_ind_clothes_hutttuniccape_red,
  itm_ind_clothes_hutttuniccape_grey,
  itm_ind_clothes_hutttuniccape_brown,
  itm_laser_bolts_orange_pistol,
  itm_laser_bolts_orange_pistol,
  itm_q2,
  itm_dl44a,
  itm_vibro_blade1,
  itm_vibro_blade2
  ],
def_attrib_4|level(16),wp(80),starwars_skills_2,sw_hutt_face_1, sw_hutt_face_2],

#================================================================================================================================   

["jawa","Jawa","Jawas",
  tf_jawa|tf_guarantee_all_armor,
  0,0,fac_outlaws,
  [
    itm_jawa_hood,
    itm_jawa_robe,
    itm_jawa_boots,
    itm_leather_gloves,
    itm_leather_gloves,   
    itm_melee_punch,
    itm_ion_beam_pistol,
    itm_ion_beam_pistol,    
    itm_ion_pistol,
    itm_ion_pistol
  ],
  def_attrib|level(8),
  wp(80),
  starwars_skills_outlaws_1,
  jawa_face1, jawa_face2
],
["jawa_2","Jawa Scavenger","Jawa Scavengers",
  tf_jawa|tf_guarantee_all_armor,
  0,0,fac_outlaws,
  [
    itm_jawa_hood,
    itm_jawa_robe,
    itm_jawa_boots,
    itm_leather_gloves,
    itm_leather_gloves,
    itm_melee_punch,
    itm_melee_punch,    
    itm_pipe1,
    itm_pipe2,
    itm_ion_beam_pistol,
    itm_ion_beam_pistol,
    itm_ion_pistol,
    itm_ion_pistol
  ],
  def_attrib|level(11),
  wp(100),
  starwars_skills_outlaws_2,
  jawa_face1, jawa_face2
],
["jawa_3","Jawa Scout","Jawa Scouts",
  tf_jawa|tf_guarantee_all_armor|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [
    itm_jawa_hood,
    itm_jawa_robe,
    itm_jawa_boots,
    itm_leather_gloves,
    itm_leather_gloves,
    itm_pipe1,
    itm_pipe2,
    itm_ion_beam_rifle,
    itm_ion_beam_rifle,
    itm_ion_blaster,
    itm_ion_blaster
  ],
  def_attrib|level(14),
  wp(120),
  starwars_skills_outlaws_2,
  jawa_face1, jawa_face2
],

#SW - modified names of bandit, brigand, mountain, forest, sea, steppe outlaws
["bandit","Bandit","Bandits",
  tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,
    itm_glasses_black,
    itm_glasses_yellow,
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,  
    itm_laser_bolts_yellow_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_ammo_belt_pistol,
    itm_dl18,
    itm_dl18,
    itm_q2,
    itm_dl44a,
    itm_melee_punch,
    itm_melee_punch,
    itm_vibro_knuckler,
    itm_combat_knife,
    itm_vibro_blade2,
    itm_vibro_blade4
  ],
  def_attrib|level(10),
  wp(90),
  starwars_skills_outlaws_2,
  sw_bandit_face_1, sw_bandit_face_2
],
["brigand","Brigand","Brigands",
  tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [ 
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask,
    itm_glasses_black,
    itm_glasses_yellow,
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,  
    itm_laser_bolts_yellow_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_ammo_belt_pistol,
    itm_dl18,
    itm_dl18,   
    itm_q2,
    itm_dl44a,
    itm_melee_punch,
    itm_melee_punch,
    itm_vibro_knuckler,
    itm_combat_knife,   
    itm_vibro_blade2,
    itm_vibro_blade4
  ],
  def_attrib|level(11),
  wp(100),
  starwars_skills_outlaws_2,
  sw_bandit_face_1, sw_bandit_face_2
],

["black_sun_pirate_1","Black Sun Thug","Black Sun Thugs",
  tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves,
  0,0,fac_outlaws,
  [ 
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,  
    itm_laser_bolts_yellow_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_ammo_belt_pistol,
    itm_dl18,
    itm_dl18,
    itm_ddc_defender,
    itm_dl44a,
    itm_melee_punch,
    itm_pipe1,
    itm_pipe1
  ],
  def_attrib|level(6),
  wp(60),
  starwars_skills_outlaws_1,
  sw_bandit_face_1, sw_bandit_face_2
],

["black_sun_pirate_2","Black Sun Smuggler","Black Sun Smugglers",
  tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [ 
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_glasses_black,
    itm_glasses_yellow,
    itm_eyepiece_tactics,
    itm_eyepiece_leadership,
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,  
    itm_laser_bolts_yellow_pistol,
    itm_laser_bolts_yellow_pistol,
    itm_ammo_belt_pistol,
    itm_dl44a,
    itm_dl44a,    
    itm_dl18,
    itm_dl18,   
    itm_dl44a,
    itm_melee_punch,    
    itm_combat_knife,
    itm_vibro_knuckler,
    itm_vibro_blade2,
    itm_vibro_blade4
  ],
  def_attrib|level(10),
  wp(100),
  starwars_skills_outlaws_2,
  sw_bandit_face_1, sw_bandit_face_2
],

["black_sun_pirate_3","Black Sun Pirate","Black Sun Pirates",
  tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [ 
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask, 
    itm_glasses_black,
    itm_glasses_yellow,
    itm_eyepiece_tactics,
    itm_eyepiece_leadership,
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,      
    itm_energy_shield_red_small,
    itm_energy_shield_yellow_small,
    itm_energy_shield_blue_small,
    itm_laser_bolts_yellow_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_ammo_belt_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_ee3,
    itm_ee3,    
    itm_kisteer_1284,
    itm_corellian_destroyer_blaster,
    itm_vibro_axe_long_1h,
    itm_combat_knife,
    itm_vibro_knuckler,
    itm_vibro_blade2,
    itm_vibro_blade4
  ],
  def_attrib|level(16),
  wp(125),
  starwars_skills_outlaws_3,
  sw_bandit_face_1, sw_bandit_face_2
],

["black_sun_pirate_4","Black Sun Elite","Black Sun Elites",
  tf_guarantee_all_armor|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [ 
    itm_ind_arm_heavyarmor_silver,
    itm_ind_helm_heavyhelmet_silver,
    itm_black_gloves,
    itm_energy_shield_red_small,
    itm_energy_shield_yellow_small,
    itm_energy_shield_blue_small,
    itm_laser_bolts_yellow_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_a295,
    itm_a295_crouch,
    itm_corellian_destroyer_blaster,
    itm_corellian_destroyer_blaster,
    itm_mandalorian_heavy_blaster,
    itm_mandalorian_heavy_blaster,
    itm_vibro_knuckler,
    itm_vibro_blade2,
    itm_vibro_blade4
  ],
  def_attrib|level(24),
  wp(150),
  starwars_skills_outlaws_4,
  sw_bandit_face_1, sw_bandit_face_2
],

["blazing_claw_pirate","Blazing Claw Pirate","Blazing Claw Pirates",
  tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask, 
    itm_glasses_black,
    itm_glasses_yellow,
    itm_eyepiece_tactics,
    itm_eyepiece_leadership,
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,  
    itm_energy_shield_red_small,
    itm_energy_shield_yellow_small,
    itm_energy_shield_blue_small,
    itm_laser_bolts_yellow_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_ammo_belt_rifle,
    itm_ee3,
    itm_ee3,
    itm_dc15s,
    itm_kisteer_1284,
    itm_corellian_destroyer_blaster,
    itm_melee_punch,
    itm_vibro_axe_long_1h,
    itm_vibro_knuckler,
    itm_combat_knife,
    itm_vibro_blade2,
    itm_vibro_blade4
  ],
  def_attrib|level(11),
  wp(100),
  starwars_skills_outlaws_2,
  sw_bandit_face_1, sw_bandit_face_2
],
["blazing_claw_pirate_female","Blazing Claw Pirate","Blazing Claw Pirates",
  tf_female|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [
    itm_black_gloves,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_tightcoverall_blue,
    itm_ind_clothes_tightcoverall_green,
    itm_ind_clothes_tightcoverall_red,
    itm_ind_clothes_tightcoverall_wblue,
    itm_ind_clothes_tightcoverall_wred,
    itm_energy_shield_red_small,
    itm_energy_shield_yellow_small,
    itm_energy_shield_blue_small,
    itm_laser_bolts_yellow_pistol,
    itm_laser_bolts_yellow_pistol,
    #itm_ammo_belt_pistol,
    itm_dl44a,
    itm_dl44a,
    itm_q2,
    itm_dl18,
    itm_dl18,
    itm_dl44a,
    itm_melee_punch,
    itm_vibro_knuckler,
    itm_combat_knife,
    itm_vibro_blade2,
    itm_vibro_blade4
  ],
  def_attrib|level(11),
  wp(100),
  starwars_skills_outlaws_2,
  sw_woman_face_1, sw_woman_face_2
],
["steppe_bandit","Night Fangs Pirate","Night Fangs Pirates",
  tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_transparent_helmet,
    itm_mining_helmet,
    itm_pipe_helmet,
    itm_fang_helmet,
    itm_beak_helmet,
    itm_gas_mask, 
    itm_glasses_black,
    itm_glasses_yellow,
    itm_eyepiece_tactics,
    itm_eyepiece_leadership,  
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves,
    itm_ind_rep_guardarmor1,
    itm_ind_rep_guardarmor2,
    itm_ind_rep_guardarmor3,
    itm_ind_rep_guardarmor_black,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,  
    itm_energy_shield_yellow_small,
    itm_energy_shield_red_small,
    itm_energy_shield_blue_small,
    itm_laser_bolts_yellow_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_ammo_belt_rifle,
    itm_a280,
    itm_a280_crouch,
    itm_ee3,
    itm_ee3,    
    itm_mg15,
    itm_kisteer_1284,
    itm_corellian_destroyer_blaster,
    itm_melee_punch,
    itm_vibro_axe_long_1h,    
    itm_vibro_knuckler,
    itm_combat_knife,
    itm_vibro_blade2,
    itm_vibro_blade4
  ],
  def_attrib|level(12),
  wp(110),
  starwars_skills_outlaws_2,
  sw_bandit_face_1, sw_bandit_face_2
],
["steppe_bandit_female","Night Fangs Pirate","Night Fangs Pirates",
  tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [
    itm_black_gloves,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_tightcoverall_blue,
    itm_ind_clothes_tightcoverall_green,
    itm_ind_clothes_tightcoverall_red,
    itm_ind_clothes_tightcoverall_wblue,
    itm_ind_clothes_tightcoverall_wred,
    itm_energy_shield_red_small,
    itm_energy_shield_yellow_small,
    itm_energy_shield_blue_small,
    itm_laser_bolts_yellow_pistol,
    itm_laser_bolts_yellow_pistol,
    #itm_ammo_belt_pistol,
    itm_dl44a,
    itm_dl44a,
    itm_q2,
    itm_dl18,
    itm_dl18,
    itm_dl44a,
    itm_melee_punch,
    itm_vibro_knuckler,
    itm_combat_knife,
    itm_vibro_blade2,
    itm_vibro_blade4
  ],
  def_attrib|level(12),
  wp(110),
  starwars_skills_outlaws_2,
  sw_woman_face_3, sw_woman_face_2
],
#SW - TUSKEN RAIDERS
["tusken_1","Tusken Warrior","Tusken Warriors",
  tf_tusken|tf_guarantee_all_armor,
  0,0,fac_outlaws,
  [   
    itm_tusken_helmet,
    itm_tusken_helmet,
    itm_tusken_armor,
    itm_tusken_armor,
    itm_leather_gloves,
    itm_leather_gloves,
    itm_tusken_rifle,
    #itm_tusken_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_laser_bolts_yellow_rifle,   
    itm_tusken_gaffi_stick,
    itm_tusken_gaffi_stick,
    itm_tusken_gaffi_staff,
    itm_tusken_gaffi_staff
  ],
  def_attrib|level(11),
  wp(100),
  starwars_skills_outlaws_2,
  tusken_face1, tusken_face2
],
["tusken_2","Tusken Raider","Tusken Raiders",
  tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
  0,0,fac_outlaws,
  [
    itm_tusken_helmet,
    itm_tusken_helmet,
    itm_tusken_armor,
    itm_tusken_armor,
    itm_leather_gloves,
    itm_leather_gloves, 
    itm_tusken_rifle,
    itm_tusken_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_laser_bolts_yellow_rifle,
    itm_tusken_gaffi_stick,
    itm_tusken_gaffi_stick,
    itm_tusken_gaffi_staff,
    itm_tusken_gaffi_staff
  ],
  def_attrib|level(18),
  wp(150),
  starwars_skills_outlaws_3,
  tusken_face1, tusken_face2
],
#SITH EMPIRE TROOPS
["Sith_strooper_lancer","Sith Trooper Lancer","Sith Lancers",
  tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [ 
    itm_weequay_head_helmet_a,
    itm_weequay_head_helmet_b,
    itm_klatooinian_head_helmet_a,
    itm_klatooinian_head_helmet_a,
    itm_nikto_head_helmet_a,
    itm_nikto_head_helmet_b,
    itm_nikto_head_helmet_c,
    itm_leather_gloves,
    itm_black_gloves, 
    itm_transparent_helmet,
    itm_skiff_guard_helmet,
    itm_skiff_guard_helmet,
    itm_skiff_guard_helmet,   
    itm_speeder,
    itm_speeder,
    itm_vibro_axe_long_2h,
    itm_vibro_axe_long_2h,
    itm_laser_bolts_orange_pistol,
    itm_laser_bolts_orange_pistol,
    itm_ammo_belt_pistol,
    itm_dl18,
    itm_dl18
  ],
  def_attrib_3|level(24),
  wp(135)|wp_firearm(150),
  starwars_skills_mounted_4,
  sw_imperial_face_1, sw_imperial_face_2
],

#SW - switched to Bounty Hunters - use rodian's and trandoshan's for bountyhunter party?
#["bountyhunter","Bounty Hunter","Bounty Hunters",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_mounted,0,0,fac_bountyhunters, [], def_attrib|level(10),wp(70),starwars_skills_2,sw_bandit_face_1, sw_bandit_face_2],
["bountyhunter","Trandoshan Slaver","Trandoshan Slavers",tf_trandoshan|tf_guarantee_all_armor|tf_guarantee_ranged,0,0,fac_bountyhunters, [itm_baton,itm_baton,itm_trandoshan_skin,itm_a280_stun,itm_ee3_stun,itm_trandoshan_stun_gun,itm_trandoshan_stun_gun,itm_durasteel_mace,itm_durasteel_bat,itm_energy_shield_yellow_small,itm_energy_shield_yellow_small,itm_electro_staff_medium,itm_electro_staff_long], def_attrib|level(16),wp(100),starwars_skills_3,trandoshan_face1, trandoshan_face2],
#["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,[],def_attrib|level(12),wp(60),knows_common,sw_bandit_face_1, sw_bandit_face_2],

#fac_slavers
#["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor,0,0,fac_slavers,[],def_attrib|level(10),wp(60),knows_common,sw_bandit_face_1, sw_bandit_face_2],
#SW - commented out, no longer used
#["slave_driver","Slave Driver","Slave Drivers",tf_guarantee_armor|tf_guarantee_boots|tf_mounted,0,0,fac_slavers, [], def_attrib|level(14),wp(80),starwars_skills_1,sw_bandit_face_1, sw_bandit_face_2],
#["slave_hunter","Slave Hunter","Slave Hunters",tf_guarantee_armor|tf_guarantee_boots|tf_mounted,0,0,fac_slavers, [], def_attrib|level(18),wp(90),starwars_skills_2,sw_bandit_face_1, sw_bandit_face_2],
#["slave_crusher","Slave Crusher","Slave Crushers",tf_guarantee_armor|tf_guarantee_boots|tf_mounted,0,0,fac_slavers, [], def_attrib|level(22),wp(110),starwars_skills_2,sw_bandit_face_1, sw_bandit_face_2],
#["slaver_chief","Slaver Chief","Slaver Chiefs",tf_guarantee_armor|tf_guarantee_boots|tf_mounted,0,0,fac_slavers, [], def_attrib|level(26),wp(130),starwars_skills_3,sw_bandit_face_1, sw_bandit_face_2],

#Rhodok tribal, Hunter, warrior, veteran, warchief

#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,[],def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,[],def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,[],def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,[], def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,[],def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],

#SW commented out follower_woman, hunter_woman, fighter_woman, sword_sister, refugee
#["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor|tf_guarantee_ranged|tf_mounted,0,0,fac_commoners,[],def_attrib|level(5),wp(70),starwars_skills_1,sw_woman_face_1,sw_woman_face_2],
#["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor|tf_guarantee_ranged|tf_mounted,0,0,fac_commoners,[],def_attrib|level(10),wp(85),starwars_skills_1,sw_woman_face_1,sw_woman_face_2],
#["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_mounted,0,0,fac_commoners,[],def_attrib|level(16),wp(100),starwars_skills_2,sw_woman_face_1,sw_woman_face_2],
#["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged|tf_mounted,0,0,fac_commoners,[],def_attrib|level(22),wp(140),starwars_skills_2,sw_woman_face_1,sw_woman_face_2],
#["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,[],def_attrib|level(1),wp(45),starwars_skills_1,sw_woman_face_1,sw_woman_face_2],
["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_all_armor,0,0,fac_commoners,[itm_q2,itm_dl44a,itm_laser_bolts_orange_pistol,itm_laser_bolts_yellow_pistol,itm_knife,itm_hatchet,itm_club,itm_quarter_staff,itm_vibro_blade2,itm_vibro_blade3,itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_tightcoverall_blue,itm_ind_clothes_tightcoverall_green,itm_ind_clothes_tightcoverall_red,itm_ind_clothes_tightcoverall_wblue,itm_ind_clothes_tightcoverall_wred,],def_attrib|level(1),wp(40),starwars_skills_1,sw_woman_face_1,sw_woman_face_2],

# renamed caravan master
["caravan_master","Freighter Captain","Freighter Captains",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,[itm_dl44a,itm_dl44a,itm_laser_bolts_green_pistol,itm_laser_bolts_red_pistol,itm_laser_bolts_yellow_pistol],def_attrib|level(9),wp(100),starwars_skills_3,sw_man_face_1, sw_man_face_2],
["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_female|tf_randomize_face|tf_unmoveable_in_party_window,0,reserved,fac_commoners,[],def_attrib|level(2),wp(50),starwars_skills_1,sw_woman_face_1, sw_woman_face_2],
#This troop is the troop marked as soldiers_end
#TAS updated
["mainplanet_walker_1","Colonist","Colonists",tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_walker_2","Colonist","Colonists",tf_female|tf_guarantee_boots|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_tightcoverall_blue,itm_ind_clothes_tightcoverall_green,itm_ind_clothes_tightcoverall_red,itm_ind_clothes_tightcoverall_wblue,itm_ind_clothes_tightcoverall_wred,], def_attrib|level(2),wp(40),knows_common,sw_woman_face_1, sw_woman_face_2],
#TAS updated
["mainplanet_walker_twilek","Twilek","Twileks",tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,twilek_face1,twilek_face2],

["mainplanet_walker_twilek_female","Twilek Female","Twilek Females",tf_twilek_female|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_transparent_head,itm_transparent_feet,itm_transparent_hands,itm_twilek_slave_a,itm_twilek_slave_b,itm_twilek_slave_c,itm_twilek_slave_d], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],
["mainplanet_walker_twilek_female_slave","Twilek Slave Dancer","Twilek Slave Dancers",tf_twilek_female|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_transparent_head,itm_transparent_feet,itm_transparent_hands,itm_twilek_slave_a,itm_twilek_slave_b,itm_twilek_slave_c,itm_twilek_slave_d], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],

["mainplanet_walker_slave_dancer","Slave Dancer","Slave Dancers",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_transparent_helmet,itm_slave_neck_chain], def_attrib|level(2),wp(40),knows_common,sw_slave_dancer_face1, sw_slave_dancer_face2],
#TAS updated
["mainplanet_walker_chiss","Chiss","Chiss",tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,chiss_face1,chiss_face2],
["mainplanet_walker_chiss_female","Chiss Female","Chiss Female",tf_female|tf_guarantee_all_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_tightcoverall_blue,itm_ind_clothes_tightcoverall_green,itm_ind_clothes_tightcoverall_red,itm_ind_clothes_tightcoverall_wblue,itm_ind_clothes_tightcoverall_wred,], def_attrib|level(4),wp(60),knows_common,chiss_female_face1,chiss_female_face2],

["mainplanet_walker_mandalorian","Mandalorian","Mandalorians",tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_mand_arm_dummy,itm_mand_helm_dummy,itm_grey_gloves,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster], def_attrib|level(20),wp(180),knows_common,mandalorian_face1,mandalorian_face2],
#TAS updated
["mainplanet_walker_trandoshan","Trandoshan","Trandoshans",tf_trandoshan|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_trandoshan_blade,itm_trandoshan_supressor,itm_trandoshan_stun_gun,itm_trandoshan_acp_array_gun,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,trandoshan_face1,trandoshan_face2],
#TAS updated
["mainplanet_walker_rodian","Rodian","Rodians",tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_transparent_helmet,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,rodian_face1,rodian_face2],

["mainplanet_walker_r2series","R2-Series Droid","R2-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_r2series_blue,itm_r2series_green,itm_r2series_orange,itm_r2series_purple,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(60),droid_skills_2,droid_face1,droid_face2],
["mainplanet_walker_lin_droid","LIN Droid","LIN Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_lin_droid_armor,itm_lin_droid_armor,itm_lin_droid_armor_w_arm,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(30),droid_skills_2,droid_face1,droid_face2],
["mainplanet_walker_mse6","MSE-6 Droid","MSE-6 Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_mse6_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["mainplanet_walker_3poseries","3PO-Series Droid","3PO-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_3poseries_gold,itm_3poseries_gold,itm_3poseries_blue,itm_3poseries_red,itm_3poseries_grey,itm_3poseries_grey,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_3poseries_attack], droid_attrib_2,wp(110),droid_skills_2,droid_face1,droid_face2],
["mainplanet_walker_3poseries_naked","3PO-Series Droid","3PO-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_3poseries_attack], droid_attrib_2,wp(110),droid_skills_2,droid_face1,droid_face2],
["mainplanet_walker_power_droid","Power Droid","Power Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_power_droid_tan,itm_power_droid_tan,itm_power_droid_grey,itm_power_droid_grey,itm_power_droid_snow,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["mainplanet_walker_fxseries_droid","FX-Series Medical Droid","FX-Series Medical Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_fxseries_droid_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["mainplanet_walker_hkseries","HK-Series Droid","HK-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_hk_head,itm_hk_body,itm_hk_hands,itm_hk_feet,itm_hk_attack,itm_a280,itm_laser_bolts_orange_rifle], def_attrib_3|level(24),wp(150),starwars_skills_3,droid_face1,droid_face2],
# TAS updated
["mainplanet_walker_sullustan","Sullustan","Sullustans",tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,sullustan_face1,sullustan_face2],
# TAS updated
["mainplanet_walker_bothan","Bothan","Bothans",tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,bothan_face1,bothan_face2],
# TAS updated
["mainplanet_walker_weequay","Weequay","Weequays",tf_weequay|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,weequay_face1,weequay_face2],
# TAS updated
["mainplanet_walker_klatooinian","Klatooinian","Klatooinians",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_klatooinian_head_helmet_a,itm_leather_gloves,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common, sw_man_face_1, sw_man_face_2],

["mainplanet_walker_nikto","Nikto","Niktos",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_leather_gloves,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_walker_jawa","Jawa","Jawas",tf_jawa|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_jawa_hood,itm_jawa_robe,itm_jawa_boots,itm_leather_gloves,itm_ion_beam_pistol,itm_ion_pistol], def_attrib|level(4),wp(60),knows_common,jawa_face1,jawa_face2],
#["mainplanet_walker_tusken","Tusken","Tuskens",tf_tusken|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [], def_attrib|level(4),wp(60),knows_common,tusken_face1,tusken_face2],
#TAS updated
["mainplanet_walker_moncal","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],

["mainplanet_walker_geonosian","Geonosian","geonosians",tf_geonosian|tf_guarantee_all_armor,0,0,fac_commoners, [itm_geonosian_sonic_pistol,itm_geonosian_sonic_rifle,itm_geonosian_static_pike], def_attrib|level(4),wp(60),knows_common,geonosian_face1,geonosian_face2],
["mainplanet_walker_wookiee","Wookiee Warrior ","Wookiee Warriors",tf_wookiee|tf_guarantee_all_armor,0,0,fac_commoners, [itm_ryyk_blade,itm_melee_punch,itm_wookiee_bowcaster,itm_laser_bolts_green_rifle], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["mainplanet_walker_wookiee_female","Wookiee","Wookiees",tf_wookiee|tf_guarantee_all_armor,0,0,fac_commoners, [itm_melee_punch], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["mainplanet_walker_gamorrean","Gamorrean","Gamorreans",tf_gamorrean|tf_randomize_face,0,0,fac_commoners, [itm_vibro_axe_medium_1h,itm_throwing_axes], def_attrib|level(4),wp(60),knows_common,gamorrean_face1,gamorrean_face2],
#TAS updated
["mainplanet_walker_zabrak","Zabrak","Zabraks",tf_male|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet], def_attrib|level(4),wp(60),knows_common,sw_zabrak_face_1, sw_zabrak_face_2],

#new faction specific town walkers
#Need to switch Jedi and Siths
#The Republic
["mainplanet_walker_empire_1","Clone Trooper","Clone Troopers",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_phase_ii_armor_clean,itm_phase_ii_armor_worn,itm_clone_trooper_gloves_white,itm_laser_bolts_blue_pistol,itm_laser_bolts_blue_rifle,itm_ddc_defender,itm_dc15s], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["mainplanet_walker_empire_2","Clone Trooper","Clone Troopers",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_phase_ii_armor_clean,itm_clone_trooper_gloves_white,itm_laser_bolts_blue_pistol,itm_laser_bolts_blue_rifle,itm_ddc_defender,itm_dc15s], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["mainplanet_walker_empire_3","Clone_Trooper","Clone Troopers",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_phase_ii_armor_clean,itm_phase_ii_helmet_clean,itm_clone_trooper_gloves_white,itm_laser_bolts_blue_rifle,itm_dc15a_hip,itm_dc15s], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["mainplanet_walker_empire_4","Galactic Marine","Galactic Marines",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_rep_arm_galacticmarine,itm_clone_trooper_gloves_white,itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_pistol,itm_ddc_defender,itm_dc15a_hip], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["mainplanet_walker_empire_5","Clone Scout Trooper","Clone Scout Troopers",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_rep_helm_phase2scout,itm_imperial_scout_trooper_armor,itm_clone_trooper_gloves_white,itm_laser_bolts_blue_rifle,itm_laser_bolts_green_pistol,itm_scout_trooper_pistol,itm_dc15s,itm_dlt19_scope], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["mainplanet_walker_empire_6","Clone Officer","Clone Officers",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_imperial_hat_black,itm_laser_bolts_red_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["mainplanet_walker_empire_7","Jedi Master","Jedi Masters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_transparent_helmet,itm_jedi_robe_a_unique,itm_jedi_robe_d_unique,itm_jedi_robe_e_unique,itm_jedi_robe_f_unique,itm_leather_gloves,itm_lightsaber_blue,itm_lightsaber_green,itm_force_shield,itm_force_protect], def_attrib_force_3|level(28),wp(220)|wp_archery(240),starwars_skills_force_3,sw_rebel_face_1,sw_rebel_face_2],
#["mainplanet_walker_empire_7","Sith","Sith Marauders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [], def_attrib_force_3|level(28),wp(220)|wp_archery(240),starwars_skills_force_3,sw_sith_face_1, sw_sith_face_2],
["mainplanet_walker_empire_8","MSE-6 Droid","MSE-6 Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_mse6_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
#TAS added planet walkers
["mainplanet_walker_empire_9","Clone Tactical Officer","Clone Tactical Officers",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_imperial_trooper_armor,itm_imperial_hat_black,itm_laser_bolts_red_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["mainplanet_walker_empire_10","Clone Naval Officer","Clone Naval Officers",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_imperial_trooper_armor,itm_imperial_hat_black,itm_laser_bolts_red_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["mainplanet_walker_empire_11","Clone Naval Crew","Clone Naval Crew",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_imperial_trooper_armor,itm_imperial_hat_black,itm_laser_bolts_red_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],


#The Confederacy of Independent Systems
["mainplanet_walker_rebel_1","CIS Technician","CIS Technicians",tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_lobot_headgear,itm_umbaran_armor,itm_transparent_feet,itm_black_gloves,itm_laser_bolts_green_pistol,itm_ddc_defender,itm_umbaran_rifle], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
["mainplanet_walker_rebel_2","Battledroid","Battledroids",tf_battledroid|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_oomseries_body,itm_transparent_droid_hands,itm_transparent_droid_feet,itm_transparent_droid_head,itm_laser_bolts_red_rifle,itm_e5], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
["mainplanet_walker_rebel_3","Pilot Droid","Pilot droids",tf_droid|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_oomseries_pilot_body,itm_transparent_droid_hands,itm_transparent_droid_feet,itm_transparent_droid_head,itm_laser_bolts_red_rifle,itm_dl18], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
["mainplanet_walker_rebel_4","Mercenary","Mercenaries",tf_guarantee_all_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_black_gloves,itm_mand_arm_dummy,itm_mand_helm_dummy,itm_laser_bolts_green_rifle,itm_a280], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
["mainplanet_walker_rebel_5","Droid Commander","Droid Commanders",tf_droid|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_bxseries_body,itm_transparent_droid_head,itm_transparent_droid_head,itm_transparent_droid_hands,itm_laser_bolts_green_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
#["mainplanet_walker_rebel_6","Jedi Master","Jedi Masters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_transparent_helmet,itm_jedi_robe_a_unique,itm_jedi_robe_d_unique,itm_jedi_robe_e_unique,itm_jedi_robe_f_unique,itm_leather_gloves,itm_lightsaber_blue,itm_lightsaber_green,itm_force_shield,itm_force_protect], def_attrib_force_3|level(28),wp(220)|wp_archery(240),starwars_skills_force_3,sw_rebel_face_1,sw_rebel_face_2],
["mainplanet_walker_rebel_6","Sith","Sith Marauders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_sith_marauder_robe_unique,itm_black_gloves,itm_lightsaber_red,itm_force_shield,itm_force_protect,itm_lightsaber_block_red], def_attrib_force_3|level(28),wp(220)|wp_archery(240),starwars_skills_force_3,sw_sith_face_1, sw_sith_face_2],
["mainplanet_walker_rebel_7","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_green_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],
["mainplanet_walker_rebel_8","Wookiee","Wookiees",tf_wookiee|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ryyk_blade,itm_melee_punch,itm_wookiee_bowcaster,itm_laser_bolts_green_rifle], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["mainplanet_walker_rebel_9","R2-Series Droid","R2-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_r2series_blue,itm_r2series_green,itm_r2series_orange,itm_r2series_purple,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(60),droid_skills_2,droid_face1,droid_face2],
#Hutts
["mainplanet_walker_hutt_1","Hutt Mercenary","Hutt Mercenaries",tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_leather_gloves,itm_black_gloves,itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_klatooinian_head_helmet_a,itm_klatooinian_head_helmet_a,itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_transparent_helmet,itm_transparent_helmet,itm_mining_helmet,itm_pipe_helmet,itm_fang_helmet,itm_beak_helmet,itm_gas_mask,itm_laser_bolts_orange_pistol,itm_ddc_defender,itm_dl18,itm_dl18], def_attrib|level(4),wp(60),knows_common,sw_hutt_face_1,sw_hutt_face_2],
["mainplanet_walker_hutt_2","Hutt Skiff Guard","Hutt Skiff Guards",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_transparent_helmet,itm_skiff_guard_helmet,itm_skiff_guard_helmet,itm_transparent_feet,itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl18], def_attrib|level(4),wp(60),knows_common,sw_hutt_face_1,sw_hutt_face_2],
["mainplanet_walker_hutt_3","Gamorrean Guard","Gamorrean Guards",tf_gamorrean|tf_randomize_face,0,0,fac_commoners, [itm_vibro_axe_medium_1h,itm_throwing_axes], def_attrib|level(4),wp(60),knows_common,gamorrean_face1,gamorrean_face2],
["mainplanet_walker_hutt_4","Slave Dancer","Slave Dancers",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_female_dancer_outfit_a,itm_female_dancer_outfit_a,itm_female_dancer_outfit_a,itm_female_dancer_outfit_a_cloak,itm_female_dancer_boots], def_attrib|level(2),wp(40),knows_common,sw_slave_dancer_face1, sw_slave_dancer_face2],
#SW - added cantina_walkers - cantina_walker_1 marked as town_walker_end
#TAS updated
["cantina_walker_1","Colonist","Colonists",tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["cantina_walker_2","Colonist","Colonists",tf_female|tf_guarantee_boots|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_tightcoverall_blue,itm_ind_clothes_tightcoverall_green,itm_ind_clothes_tightcoverall_red,itm_ind_clothes_tightcoverall_wblue,itm_ind_clothes_tightcoverall_wred,], def_attrib|level(2),wp(40),knows_common,sw_woman_face_1, sw_woman_face_3],
#["cantina_walker_jawa","Jawa","Jawas",tf_jawa|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_jawa_hood,itm_jawa_robe,itm_jawa_boots,itm_leather_gloves,itm_ion_beam,itm_ion_pistol,itm_ion_blaster], def_attrib|level(4),wp(60),knows_common,jawa_face1,jawa_face2],
#TAS updated
["cantina_walker_rodian","Rodian","Rodians",tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_feet,itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,rodian_face1,rodian_face2],
#TAS updated
["cantina_walker_moncal","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],

["cantina_walker_trandoshan","Trandoshan","Trandoshans",tf_trandoshan|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_trandoshan_blade,itm_trandoshan_supressor,itm_trandoshan_stun_gun,itm_trandoshan_acp_array_gun,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,trandoshan_face1,trandoshan_face2],
["cantina_walker_mandalorian","Mandalorian","Mandalorians",tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_mand_arm_dummy,itm_mand_helm_dummy,itm_grey_gloves,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster], def_attrib|level(4),wp(60),knows_common,mandalorian_face1,mandalorian_face2],
#TAS updated
["cantina_walker_sullustan","Sullustan","Sullustans",tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,sullustan_face1,sullustan_face2],
["cantina_walker_bothan","Bothan","Bothans",tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,bothan_face1,bothan_face2],
["cantina_walker_chiss","Chiss","Chiss",tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,chiss_face1,chiss_face2],

["cantina_walker_chiss_female","Chiss Female","Chiss Female",tf_female|tf_guarantee_all_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_tightcoverall_blue,itm_ind_clothes_tightcoverall_green,itm_ind_clothes_tightcoverall_red,itm_ind_clothes_tightcoverall_wblue,itm_ind_clothes_tightcoverall_wred,], def_attrib|level(4),wp(60),knows_common,chiss_female_face1,chiss_female_face2],
#TAS updated
["cantina_walker_weequay","Weequay","Weequays",tf_weequay|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,weequay_face1,weequay_face2],
["cantina_walker_klatooinian","Klatooinian","Klatooinians",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_klatooinian_head_helmet_a,itm_leather_gloves,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common, sw_man_face_1, sw_man_face_2],
["cantina_walker_nikto","Nikto","Niktos",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_leather_gloves,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["cantina_walker_twilek","Twilek","Twileks",tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,twilek_face1,twilek_face2],

["cantina_walker_twilek_female","Twilek Female","Twilek Females",tf_twilek_female|tf_guarantee_all_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_twilek_slave_a,itm_twilek_slave_b,itm_twilek_slave_c,itm_twilek_slave_d], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],
["cantina_walker_geonosian","Geonosian","geonosians",tf_geonosian|tf_guarantee_all_armor,0,0,fac_commoners, [itm_geonosian_sonic_pistol,itm_geonosian_sonic_rifle,itm_geonosian_static_pike], def_attrib|level(4),wp(60),knows_common,geonosian_face1,geonosian_face2],
["cantina_walker_wookiee","Wookiee","Wookiees",tf_wookiee|tf_guarantee_all_armor,0,0,fac_commoners, [itm_ryyk_blade,itm_wookiee_bowcaster], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["cantina_walker_wookiee_female","Wookiee Female","Wookiee Females",tf_wookiee|tf_guarantee_all_armor,0,0,fac_commoners, [], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["cantina_walker_gamorrean","Gamorrean","Gamorreans",tf_gamorrean|tf_randomize_face,0,0,fac_commoners, [itm_vibro_axe_medium_1h], def_attrib|level(4),wp(60),knows_common,gamorrean_face1,gamorrean_face2],
#TAS updated, update trandoshans with new models
["cantina_drinker_1","Colonist","Colonists",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_laser_bolts_orange_pistol,itm_dl44a,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["cantina_drinker_rodian","Rodian","Rodians",tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_transparent_helmet,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,rodian_face1,rodian_face2],
["cantina_drinker_moncal","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],

["cantina_drinker_trandoshan","Trandoshan","Trandoshans",tf_trandoshan|tf_guarantee_all_armor|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_trandoshan_blade,itm_trandoshan_supressor,itm_trandoshan_stun_gun,itm_trandoshan_acp_array_gun,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,trandoshan_face1,trandoshan_face2],

["cantina_drinker_sullustan","Sullustan","Sullustans",tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,sullustan_face1,sullustan_face2],
["cantina_drinker_bothan","Bothan","Bothans",tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,bothan_face1,bothan_face2],
["cantina_drinker_chiss","Chiss","Chiss",tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,chiss_face1,chiss_face2],
["cantina_drinker_weequay","Weequay","Weequays",tf_weequay|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,weequay_face1,weequay_face2],
["cantina_drinker_klatooinian","Klatooinian","Klatooinians",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_klatooinian_head_helmet_a,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common, sw_man_face_1, sw_man_face_2],
["cantina_drinker_nikto","Nikto","Niktos",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["cantina_drinker_twilek","Twilek","Twileks",tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_grey_gloves_with_bottle,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,twilek_face1,twilek_face2],
#SW - renamed to colonists - minorplanet_walker_1 marked as cantina_walker_end
#TAS male updated
["minorplanet_walker_1","Colonist","Colonists",tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["minorplanet_walker_2","Colonist","Colonists",tf_female|tf_guarantee_boots|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_tightcoverall_blue,itm_ind_clothes_tightcoverall_green,itm_ind_clothes_tightcoverall_red,itm_ind_clothes_tightcoverall_wblue,itm_ind_clothes_tightcoverall_wred,], def_attrib|level(2),wp(40),knows_common,sw_woman_face_1, sw_woman_face_2],
#["minorplanet_walker_jawa","Jawa","Jawas",tf_jawa|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [], def_attrib|level(4),wp(60),knows_common,jawa_face1,jawa_face2],
#["minorplanet_walker_tusken","Tusken","Tuskens",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [], def_attrib|level(4),wp(60),knows_common,tusken_face1,tusken_face2],
["minorplanet_walker_rodian","Rodian","Rodians",tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,rodian_face1,rodian_face2],
["minorplanet_walker_moncal","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],
["minorplanet_walker_trandoshan","Trandoshan","Trandoshans",tf_trandoshan|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_trandoshan_blade,itm_trandoshan_supressor,itm_trandoshan_stun_gun,itm_trandoshan_acp_array_gun,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,trandoshan_face1,trandoshan_face2],

["minorplanet_walker_mandalorian","Mandalorian","Mandalorians",tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_mand_arm_dummy,itm_mand_helm_dummy,itm_grey_gloves,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster], def_attrib|level(4),wp(60),knows_common,mandalorian_face1,mandalorian_face2],
#TAS updated
["minorplanet_walker_sullustan","Sullustan","Sullustans",tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,sullustan_face1,sullustan_face2],
["minorplanet_walker_bothan","Bothan","Bothans",tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2], def_attrib|level(4),wp(60),knows_common,bothan_face1,bothan_face2],
# TAS male updated
["minorplanet_walker_chiss","Chiss","Chiss",tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,chiss_face1,chiss_face2],
["minorplanet_walker_chiss_female","Chiss Female","Chiss Female",tf_female|tf_guarantee_all_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_tightcoverall_blue,itm_ind_clothes_tightcoverall_green,itm_ind_clothes_tightcoverall_red,itm_ind_clothes_tightcoverall_wblue,itm_ind_clothes_tightcoverall_wred,], def_attrib|level(4),wp(60),knows_common,chiss_female_face1,chiss_female_face2],

["minorplanet_walker_weequay","Weequay","Weequays",tf_weequay|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,weequay_face1,weequay_face2],
["minorplanet_walker_klatooinian","Klatooinian","Klatooinians",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_klatooinian_head_helmet_a,itm_leather_gloves,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common, sw_man_face_1, sw_man_face_2],
["minorplanet_walker_nikto","Nikto","Niktos",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_leather_gloves,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],

["minorplanet_walker_twilek","Twilek","Twileks",tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_laser_bolts_orange_pistol,itm_dl44a,itm_ddc_defender,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,twilek_face1,twilek_face2],
["minorplanet_walker_twilek_female","Twilek Female","Twilek Females",tf_twilek_female|tf_guarantee_all_armor,0,0,fac_commoners, [itm_transparent_head,itm_transparent_feet,itm_transparent_hands,itm_twilek_slave_a,itm_twilek_slave_b,itm_twilek_slave_c,itm_twilek_slave_d], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],
["minorplanet_walker_twilek_female_slave","Twilek Slave","Twilek Slaves",tf_twilek_female|tf_guarantee_all_armor,0,0,fac_commoners, [itm_transparent_head,itm_transparent_feet,itm_transparent_hands,itm_twilek_slave_a,itm_twilek_slave_b,itm_twilek_slave_c,itm_twilek_slave_d], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],
#TAS droids and aliens bellow
["minorplanet_walker_geonosian","Geonosian","geonosians",tf_geonosian|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_geonosian_sonic_pistol,itm_geonosian_sonic_rifle,itm_geonosian_static_pike], def_attrib|level(4),wp(60),knows_common,geonosian_face1,geonosian_face2],
["minorplanet_walker_wookiee","Wookiee","Wookiees",tf_wookiee|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_ryyk_blade,itm_wookiee_bowcaster], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["minorplanet_walker_wookiee_female","Wookiee Female","Wookiee Females",tf_wookiee|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["minorplanet_walker_gamorrean","Gamorrean","Gamorreans",tf_gamorrean|tf_randomize_face,0,0,fac_commoners, [itm_vibro_axe_medium_1h], def_attrib|level(4),wp(60),knows_common,gamorrean_face1,gamorrean_face2],
["minorplanet_walker_r2series","R2-Series Droid","R2-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_r2series_blue,itm_r2series_green,itm_r2series_orange,itm_r2series_purple,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(60),droid_skills_2,droid_face1,droid_face2],
["minorplanet_walker_lin_droid","LIN Droid","LIN Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_lin_droid_armor,itm_lin_droid_armor,itm_lin_droid_armor_w_arm,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(30),droid_skills_2,droid_face1,droid_face2],
["minorplanet_walker_mse6","MSE-6 Droid","MSE-6 Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_mse6_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["minorplanet_walker_3poseries","3PO-Series Droid","3PO-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_3poseries_gold,itm_3poseries_gold,itm_3poseries_blue,itm_3poseries_red,itm_3poseries_grey,itm_3poseries_grey,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_3poseries_attack], droid_attrib_2,wp(110),droid_skills_2,droid_face1,droid_face2],
["minorplanet_walker_3poseries_naked","3PO-Series Droid","3PO-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_3poseries_attack], droid_attrib_2,wp(110),droid_skills_2,droid_face1,droid_face2],
["minorplanet_walker_power_droid","Power Droid","Power Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_power_droid_tan,itm_power_droid_tan,itm_power_droid_grey,itm_power_droid_grey,itm_power_droid_snow,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["minorplanet_walker_fxseries_droid","FX-Series Medical Droid","FX-Series Medical Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_fxseries_droid_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["minorplanet_walker_hkseries","HK-Series Droid","HK-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_hk_head,itm_hk_body,itm_hk_hands,itm_hk_feet], def_attrib_3|level(24),wp(150),starwars_skills_3,droid_face1,droid_face2],
#TAS male updated
["spy_walker_1","Colonist","Colonists",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_ind_rep_guardarmor1,itm_ind_rep_guardarmor2,itm_ind_rep_guardarmor3,itm_ind_rep_guardarmor_black,itm_ind_clothes_outfitvest_red,itm_ind_clothes_outfitvest_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggleralter1_red,itm_ind_clothes_outfsmuggleralter1_green,itm_ind_clothes_outfsmuggleralter2_red,itm_ind_clothes_outfsmuggleralter2_green,itm_ind_clothes_securityguarda1,itm_ind_clothes_securityguarda2,itm_ind_clothes_securityguarda3,itm_ind_clothes_securityguarda4,itm_ind_clothes_securityguarda5,itm_ind_clothes_hutttunic_red,itm_ind_clothes_hutttunic_grey,itm_ind_clothes_hutttunic_brown,itm_ind_clothes_hutttuniccape_red,itm_ind_clothes_hutttuniccape_grey,itm_ind_clothes_hutttuniccape_brown,itm_vibro_blade1,itm_vibro_blade2,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["spy_walker_2","Colonist","Colonists",tf_female|tf_guarantee_boots|tf_guarantee_all_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_vibro_blade1,itm_vibro_blade2,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_ind_clothes_outfsmuggler_red,itm_ind_clothes_tightcoverall_blue,itm_ind_clothes_tightcoverall_green,itm_ind_clothes_tightcoverall_red,itm_ind_clothes_tightcoverall_wblue,itm_ind_clothes_tightcoverall_wred,], def_attrib|level(2),wp(40),knows_common,sw_woman_face_1, sw_woman_face_2],
# Ryan END
["assassin_male","Assassin","Assassins",tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_laser_bolts_orange_rifle,itm_a295,itm_a295_crouch,itm_vibro_sword3_gold,itm_transparent_helmet], def_attrib_3|level(24),wp(150),starwars_skills_3,sw_man_face_1, sw_man_face_2],
["assassin_rodian","Rodian Assassin","Rodian Assassins",tf_rodian|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_laser_bolts_orange_rifle,itm_a295,itm_a295_crouch,itm_vibro_sword3_gold,itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_transparent_helmet], def_attrib_3|level(24),wp(150),starwars_skills_3,rodian_face1,rodian_face2],
["assassin_trandoshan","Trandoshan Assassin","Trandoshan Assassins",tf_trandoshan|tf_guarantee_helmet|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_laser_bolts_orange_rifle,itm_trandoshan_acp_array_gun,itm_trandoshan_blade], def_attrib_3|level(24),wp(150),starwars_skills_3,trandoshan_face1,trandoshan_face2],
["assassin_twilek","Twilek Assassin","Twilek Assassins",tf_twilek|tf_guarantee_helmet|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_vibro_axe_long_2h,itm_laser_bolts_orange_rifle,itm_a295,itm_a295_crouch,itm_transparent_helmet], def_attrib_3|level(24),wp(150),starwars_skills_3,twilek_face1,twilek_face2],
["assassin_mandalorian","Mandalorian Assassin","Mandalorian Assassins",tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_mand_arm_dummy,itm_mand_helm_dummy,itm_grey_gloves,itm_vibro_sword3_gold,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster], def_attrib_3|level(24),wp(150),starwars_skills_3,mandalorian_face1,mandalorian_face2],
["assassin_hkseries","HK-Series Assassin Droid","HK-Series Assassin Droids",tf_guarantee_all_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_droid_parts,itm_hk_attack,itm_hk_head,itm_hk_body,itm_hk_hands,itm_hk_feet,itm_a280,itm_a295,itm_dlt19,itm_laser_bolts_orange_rifle,itm_laser_bolts_orange_rifle], def_attrib_3|level(24),wp(150),starwars_skills_3,droid_face1, droid_face2],

# Zendar (next troop is marked as spy_walkers_end)
#["tournament_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_dl44a,itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
#["trainer","Trainer","Trainer",tf_hero|tf_randomize_face, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_dl44a,itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
#["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero|tf_randomize_face, scn_zendar_center|entry(5),reserved,  fac_commoners,[],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
# Ryan BEGIN
#SW - modified Ramun_the_slave_trader
#["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero|tf_randomize_face, no_scene,reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["Ramun_the_slave_trader","Slave Trader","Slave Trader",tf_hero|tf_randomize_face, no_scene,reserved, fac_commoners,[itm_ind_clothes_noble_purple],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["guide","Quick Jimmy","Quick Jimmy",tf_hero|tf_randomize_face, no_scene,0,  fac_commoners,[itm_ind_clothes_noble_purple],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1,sw_man_face_2],
# Ryan END
#["Xerina","Xerina","Xerina",tf_hero|tf_female|tf_randomize_face, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,sw_woman_face_1,sw_woman_face_2],
#["Dranton","Dranton","Dranton",tf_hero|tf_randomize_face, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,sw_man_face_1,sw_man_face_2],
#["Kradus","Kradus","Kradus",tf_hero|tf_randomize_face, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,sw_man_face_1,sw_man_face_2],
#Tutorial
["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero|tf_randomize_face, scn_training_ground|entry(2),reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_dl44a,itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
["Galeas","Galeas","Galeas",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

#Dhorak keep

["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor|tf_guarantee_boots,no_scene,reserved,fac_commoners, [itm_ind_clothes_noble_purple], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],

["trainer_1","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["trainer_2","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["trainer_3","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["trainer_4","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["trainer_5","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

# Ransom brokers.
["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_noble_purple,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_blue],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

# Tavern traveler.
["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ind_clothes_outfsmuggler_green,itm_phase_ii_clonepack],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

# Tavern traveler.
#SW - switched Book_Merchant to Treasure Hunter (holocron's and possibly other rare items that give +1 to stats?)
#SW - added tavern_bookseller_#'s
["tavern_bookseller_1","Holocron Merchant","Holocron Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_book_tactics,itm_book_persuasion,itm_book_leadership,itm_book_intelligence,itm_book_trade,itm_book_weapon_mastery,itm_book_engineering],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1,sw_man_face_2],
["tavern_bookseller_2","Holocron Merchant","Holocron Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_book_tactics,itm_book_persuasion,itm_book_leadership,itm_book_intelligence,itm_book_trade,itm_book_weapon_mastery,itm_book_engineering],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1,sw_man_face_2],
["tavern_bookseller_3","Item Merchant","Item Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_book_ironflesh_reference,itm_book_horse_archery_reference,itm_book_trade_reference,itm_book_wound_treatment_reference,itm_book_training_reference,itm_book_surgery_reference,itm_book_first_aid_reference,itm_book_tactics_reference],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_4","Item Merchant","Item Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_book_ironflesh_reference,itm_book_horse_archery_reference,itm_book_trade_reference,itm_book_wound_treatment_reference,itm_book_training_reference,itm_book_surgery_reference,itm_book_first_aid_reference,itm_book_tactics_reference],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_5","Force-Sensitive Trainer","Force-Sensitive Trainers",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_jedi_robe_d],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_6","Force-Sensitive Trainer","Force-Sensitive Trainers",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_jedi_robe_d],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_1, sw_woman_face_2],
["tavern_bookseller_7","Clone Wars Era Merchant","Clone Era Merchants",tf_tusken|tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_phase_ii_armor_442,itm_clone_trooper_gloves_red],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_8","Clone Wars Era Merchant","Clone Era Merchants",tf_tusken|tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_phase_ii_armor_442,itm_clone_trooper_gloves_red],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_9", "Illegal Weapons Merchant","Illegal Weapons Merchants",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_10","Illegal Weapons Merchant","Illegal Weapons Merchants",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_3, sw_woman_face_2],
#["tavern_bookseller_11","Droid Parts Merchant","Droid Parts Merchants",tf_hero|tf_droid|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,droid_face1, droid_face2],
#["tavern_bookseller_12","Droid Parts Merchant","Droid Parts Merchants",tf_hero|tf_droid|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,droid_face1, droid_face2],
["tavern_bookseller_11","Droid Parts Merchant","Droid Parts Merchants",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_12","Droid Parts Merchant","Droid Parts Merchants",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_1, sw_woman_face_2],
["tavern_bookseller_13","Plastic Surgeon","Plastic Surgeons",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1,sw_man_face_2],
["tavern_bookseller_14","Plastic Surgeon","Plastic Surgeons",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_1, sw_woman_face_2],
["tavern_bookseller_15","Force-Sensitive Merchant","Force-Sensitive Merchants",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_jedi_robe_e],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_16","Force-Sensitive Merchant","Force-Sensitive Merchants",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_jedi_robe_e],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_1, sw_woman_face_2],
# Tavern minstrel
["tavern_minstrel_1","Musician","Musicians",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

#NPC system changes begin
#Companions

#SW - switched NPC's to Star Wars Characters, all now start at level 1, still need to update dialogs and some items
#SW - Borcha
["npc1","Kyle Katarn","Kyle Katarn",tf_hero|tf_unmoveable_in_party_window, 0, reserved,fac_commoners,[itm_laser_bolts_yellow_pistol,itm_dl44a,itm_vibro_blade3], str_14|agi_9|int_6|cha_5|level(6),wp(100),knows_weapon_master_4|knows_ironflesh_2|knows_athletics_3|knows_trainer_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_horse_archery_1, 0x000000003f00708136db6db6db6db6db00000000001db6db0000000000000000],
#SW - Marnid
["npc2","Rahm Kota","Rahm Kota", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_lightsaber_green_1h,itm_force_power_ls_2,itm_force_push_ammo,itm_force_throw_lightsaber_green], str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4, 0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],
#SW Ymira (female)
["npc3","Kyra Moryne","Kyra Moryne",tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_laser_bolts_yellow_pistol,itm_q2,itm_force_power_ls_1,itm_force_push_ammo],  str_12|agi_8|int_6|cha_6|level(1),wp(40)|wp_archery(40),knows_ironflesh_1|knows_weapon_master_2|knows_riding_1|knows_trade_1|knows_athletics_1|knows_power_throw_4|knows_inventory_management_1|knows_power_draw_2, sw_woman_face_1,sw_woman_face_2],
#SW - Rolf
["npc4","Dav Foss","Dav Foss",tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_pistol,itm_dl44a,itm_vibro_blade3], str_7|agi_6|int_12|cha_5|level(4),wp(65),knows_weapon_master_2|knows_riding_2|knows_horse_archery_2|knows_athletics_1|knows_spotting_3|knows_pathfinding_4|knows_engineer_1|knows_leadership_1|knows_tactics_2, sw_man_face_1,sw_man_face_2],
#SW - Baheshtur
["npc5","Trec Quizan","Trec Quizan",tf_weequay|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_vibro_blade3], str_12|agi_10|int_4|cha_5|level(3),wp(50),knows_ironflesh_3|knows_power_strike_1|knows_athletics_3|knows_trade_1|knows_trainer_1|knows_inventory_management_1|knows_first_aid_1|knows_shield_1, weequay_face1, weequay_face2],
#SW - Firentis
["npc6","Gaven Iscandar","Gaven Iscandar",tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_pistol,itm_dl44a,itm_vibro_blade3], str_11|agi_9|int_6|cha_9|level(4),wp(70),knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_looting_1|knows_riding_2|knows_horse_archery_1|knows_trade_2|knows_inventory_management_1|knows_weapon_master_3, sw_man_face_1,sw_man_face_2],
#SW - Deshavi (female)
["npc7","Jade Codi","Jade Codi",tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_pistol,itm_q2,itm_vibro_blade3], str_5|agi_5|cha_13|int_10|level(2),wp(30),knows_athletics_1|knows_riding_1|knows_leadership_3|knows_weapon_master_1|knows_trade_4|knows_tactics_1, sw_woman_face_1,sw_woman_face_2],
#SW - Matheld (female)
["npc8","Dossok Snorkh","Dossok Snorkh",tf_trandoshan|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_pistol], str_5|agi_11|cha_10|int_4|level(2),wp(110),knows_ironflesh_2|knows_weapon_master_5|knows_spotting_2|knows_pathfinding_3|knows_athletics_4|knows_riding_3|knows_horse_archery_3, trandoshan_face1, trandoshan_face2],
#SW - Alayen
["npc9","Arvis Sunwright","Arvis Sunwright",tf_chiss|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_pistol,itm_dl44a,itm_vibro_blade3], str_10|agi_12|int_8|cha_6|level(3),wp(60),knows_ironflesh_1|knows_weapon_master_2|knows_athletics_3|knows_riding_4|knows_horse_archery_2|knows_first_aid_1|knows_trade_2|knows_tactics_1|knows_leadership_2, chiss_face1, chiss_face2],
#SW - Bunduk
["npc10","Nerthak Beviin","Nerthak Beviin",tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_rifle,itm_e11,itm_vibro_blade3], str_13|agi_10|int_8|cha_7|level(5),wp(110),knows_weapon_master_4|knows_engineer_2|knows_trade_1|knows_ironflesh_2|knows_power_strike_2|knows_tracking_1|knows_trainer_2|knows_pathfinding_1|knows_riding_2|knows_horse_archery_1|knows_leadership_3|knows_tactics_3, sw_man_face_1,sw_man_face_2],
#SW - Katrin (female)
["npc11","Luna Novar","Luna Novar",tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_vibro_blade3], str_7|agi_8|int_13|cha_7|level(2),wp(80),knows_ironflesh_2|knows_power_strike_3|knows_weapon_master_1|knows_surgery_4|knows_first_aid_3|knows_wound_treatment_4|knows_trade_1|knows_engineer_1, sw_woman_face_1,sw_woman_face_2],
#SW - Jeremus
["npc12","Vaian Swogg","Vaian Swogg",tf_sullustan|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_quarter_staff], str_11|agi_9|int_7|cha_6|level(1),wp(30),knows_ironflesh_3|knows_power_strike_3|knows_weapon_master_2|knows_trade_2|knows_tracking_2|knows_athletics_3|knows_inventory_management_3, sullustan_face1, sullustan_face2],
#SW - Nizar
["npc13","Tam Yarrow","Tam Yarrow",tf_rodian|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_pistol,itm_q2,itm_vibro_blade3], str_7|agi_9|int_8|cha_9|level(1),wp(50),knows_weapon_master_2|knows_inventory_management_3|knows_trade_4|knows_looting_2|knows_athletics_1|knows_riding_1|knows_shield_1, rodian_face1, rodian_face2],
#Lezalit
["npc14","Rath Varik","Rath Varik",tf_twilek|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_pistol,itm_westar,itm_vibro_blade3], str_10|agi_11|int_11|cha_5|level(6),wp(115),knows_ironflesh_2|knows_power_strike_2|knows_riding_2|knows_weapon_master_3|knows_horse_archery_1|knows_tracking_1|knows_pathfinding_1|knows_trainer_4|knows_leadership_2, twilek_face1, twilek_face2],
#SW - Artimenner
["npc15","Miriti Shoa","Miriti Shoa",tf_moncal|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_pistol,itm_q2,itm_vibro_blade3], str_9|agi_8|int_13|cha_7|level(6),wp(70),knows_ironflesh_2|knows_power_strike_2|knows_riding_1|knows_engineer_4|knows_trainer_3|knows_tracking_1|knows_spotting_1|knows_tactics_1|knows_leadership_1|knows_weapon_master_2|knows_power_throw_2|knows_looting_1, moncal_face1, moncal_face2],
#SW - Klethi (female)
["npc16","Anela Kinse","Anela Kinse",tf_twilek_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_laser_bolts_yellow_rifle,itm_kisteer_1284,itm_vibro_blade3], str_12|agi_13|int_9|cha_5|level(8),wp(115),knows_power_strike_3|knows_looting_2|knows_riding_2|knows_weapon_master_5|knows_athletics_4|knows_tracking_3|knows_spotting_2, twilek_female_face1, twilek_female_face2],
#NPC system changes end
#SW - new Droid NPC's
["npc17","B-2HO","B-2HO",tf_droid|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],  str_12|agi_4|int_6|cha_3|level(1),wp(25),knows_ironflesh_4|knows_weapon_master_4|knows_riding_1|knows_trade_2|knows_inventory_management_4, droid_face1, droid_face2],
["npc18","B-2KI","B-2KI",tf_droid|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],  str_12|agi_4|int_6|cha_3|level(1),wp(25),knows_ironflesh_4|knows_weapon_master_4|knows_riding_1|knows_trade_2|knows_inventory_management_4, droid_face1, droid_face2],

["faction_heroes_including_player_begin", "faction_heroes_including_player_begin", "faction_heroes_including_player_begin", tf_hero|tf_randomize_face,0,reserved,fac_galacticempire,[],lord_attrib,wp(220),knows_lord_1, sw_man_face_1,sw_man_face_2],

#Started renaming lords dor TAS TC08
#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
["galacticempire_lord",  "Supreme Chancellor Palpatine",  "Faction 1 Lord",  tf_hero, 0,reserved,  fac_galacticempire,[itm_jedi_clothes_robesmaster_grey,itm_lightsaber_red,itm_force_protect,itm_force_power_ds_4,itm_force_lightning_ammo],lord_attrib,wp(300)|wp_archery(300),starwars_knight_skills_5|knows_power_draw_10, 0x0000000fc000700546e189c6b34dc69b0000000000ed3a820000000000000000],
["rebelalliance_lord",  "Count Dooku",  "Faction 2 Lord",  tf_hero, 0,reserved,fac_rebelalliance,[itm_dooku_head,itm_dooku_body,itm_dookuus_lightsaber,itm_laser_bolts_green_rifle,itm_a295,itm_vibro_blade1,itm_hero_shield],lord_attrib,wp(300),starwars_knight_skills_5, 0x0000000ceb00500436db49480049b6db00000000001db6db0000000000000000],
["huttcartel_lord",  "Jabba the Hutt",  "Faction 3 Lord",  tf_hutt|tf_hero|tf_randomize_face, 0,reserved,  fac_huttcartel,[itm_jabba_speeder,itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],  lord_attrib,wp(300),starwars_knight_skills_5, hutt_face1, hutt_face2],
  
#SW - commented out faction 4 & 5 lords
#TAS preparations for the Mandalorians factions additions
#["faction_4_lord",  "Darth Maul",  "Faction 4 Lord",  tf_hero, 0,reserved,  fac_faction_4,[],            knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000, nord_face_older_2],
#["faction_5_lord",  "Satine Kryze",  "Faction 5 Lord",  tf_hero|tf_female, 0,reserved,  fac_faction_5,[],         knight_attrib_3,wp(220),knight_skills_4|knows_trainer_5, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],

#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield

#SW - Galactic Republic Knights
# don't adjust skills much because it may lead to game in-balance?
#knight skill 5 - Jedi Masters
["knight_1_1", "Jedi Master Obi-wan Kenobi", "knight_1_1", tf_hero, 0, reserved,fac_galacticempire, [itm_obi_wan_head,itm_phase_ii_armor_worn,itm_jedi_master_cloak,itm_obi_wan_lightsaber,itm_black_gloves,itm_force_protect,itm_force_power_ds_4,itm_force_lightning_ammo],knight_attrib_5,wp(400)|wp_archery(400),starwars_knight_skills_5|knows_power_draw_9, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_2", "Jedi Master Anakin Skywalker", "knight_1_2", tf_hero, 0, reserved,fac_galacticempire, [itm_anakin_head,itm_anakin_body,itm_lightsaber_blue], knight_attrib_5,wp(400),starwars_knight_skills_5, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_3", "Jedi Master Mace Windu", "knight_1_3", tf_hero, 0, reserved,fac_galacticempire, [itm_mace_head,itm_jedi_clothes_robesmasterhd_grey,itm_lightsaber_purple],knight_attrib_5,wp(400),starwars_knight_skills_5, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_4", "Jedi Master Yoda", "knight_1_4", tf_hero, 0, reserved,fac_galacticempire, [itm_yoda_armor,itm_yoda_speeder,itm_yoda_lightsaber,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_force_protect,itm_force_throw_lightsaber_green,itm_force_power_ls_4,itm_force_push_ammo], knight_attrib_5,wp(400),starwars_knight_skills_5, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_5", "Jedi Master Aayla Secura", "knight_1_5", tf_female|tf_hero, 0, reserved,fac_galacticempire, [itm_speeder_fc20,itm_aayla_head,itm_jedi_clothes_robes_grey,itm_lightsaber_purple,itm_force_protect,itm_force_power_ds_4,itm_force_lightning_ammo],knight_attrib_5,wp(400)|wp_archery(400),starwars_knight_skills_5|knows_power_draw_8, 0x000000018000500536db6d86026db6db00000000001db6db0000000000000000],
["knight_1_6", "Jedi Master Luminara Unduli", "knight_1_6", tf_female|tf_hero, 0, reserved,fac_galacticempire, [itm_speeder_fc20,itm_unduli_head,itm_undulirobes,itm_lightsaber_green,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_shield,itm_force_shield], knight_attrib_5,wp(400)|wp_archery(400),starwars_knight_skills_5|knows_power_draw_8, sw_sith_face_1, sw_sith_face_2],
["knight_1_7", "Jedi Master Ima_Gun-Di", "knight_1_7", tf_hero, 0, reserved,fac_galacticempire, [itm_nikto_head_helmet_a,itm_jedi_clothes_robesmasterhd_grey,itm_lightsaber_blue,itm_force_protect,itm_force_power_ds_4], knight_attrib_5,wp(220),starwars_knight_skills_5, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_8", "Jedi Master Bolla Ropal", "knight_1_8", tf_rodian|tf_hero, 0, reserved,fac_galacticempire, [itm_jedi_clothes_robesmaster_grey,itm_black_gloves,itm_lightsaber_blue,itm_force_protect,itm_force_power_ds_4],knight_attrib_5,wp(220),starwars_knight_skills_5, 0x0000000c3f01400436db6db6db6db6db00000000001db6db0000000000000000],
#knight skill 4 - Jedis
["knight_1_9", "Jedi Master Kit Fisto", "knight_1_8", tf_hero, 0, reserved,fac_galacticempire, [itm_nautolan_head,itm_jedi_clothes_robes_brown,itm_speeder_fc20,itm_lightsaber_blue,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_protect],knight_attrib_4,wp(200)|wp_archery(200),starwars_knight_skills_4|knows_power_draw_7, sw_sith_face_1, sw_sith_face_2],
["knight_1_10", "Jedi Master Plo Koon", "knight_1_9", tf_hero, 0, reserved,fac_galacticempire, [itm_keldorian_head,itm_jedi_clothes_robes_grey,itm_lightsaber_green],knight_attrib_4,wp(200),starwars_knight_skills_4, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_11", "Jedi Knight Nahdar Vebb", "knight_1_0", tf_moncal|tf_hero, 0, reserved,fac_galacticempire, [itm_jedi_clothes_robes_grey,itm_lightsaber_blue,itm_force_power_ds_4,itm_force_protect], knight_attrib_4,wp(200),starwars_knight_skills_4, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_12", "Jedi Knight Sora Bulq", "knight_1_1", tf_weequay|tf_hero, 0, reserved,fac_galacticempire, [itm_jedi_clothes_robes_grey,itm_lightsaber_blue,itm_force_power_ds_4,itm_force_protect], knight_attrib_4,wp(200),starwars_knight_skills_4, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_13", "Jedi Knight Hydra", "knight_1_2", tf_hero, 0, reserved,fac_galacticempire, [itm_jedi_clothes_robes_grey,itm_speeder_fc20,itm_lightsaber_blue,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_shield],knight_attrib_4,wp(200)|wp_archery(200),starwars_knight_skills_4|knows_power_draw_7, sw_sith_face_1, sw_sith_face_2],
["knight_1_14", "Admiral Wulff Yuralen", "knight_1_3", tf_hero, 0, reserved,fac_galacticempire, [itm_black_gloves],knight_attrib_4,wp(200),starwars_knight_skills_4, 0x0000000ebd0031162d5a66ca2d9186cb0000000000e9d9820000000000000000],
["knight_1_15", "Jedi Knight Moradmin Bast", "knight_1_4", tf_hero, 0, reserved,fac_galacticempire, [itm_jedi_clothes_robes_grey,itm_lightsaber_blue],knight_attrib_4,wp(200),starwars_knight_skills_4, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_16", "Jedi Knight Onel'da", "knight_1_5", tf_hero, 0, reserved,fac_galacticempire, [itm_jedi_clothes_robes_grey,itm_speeder_fc20,itm_lightsaber_yellow,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_shield], knight_attrib_4,wp(200)|wp_archery(200),starwars_knight_skills_4|knows_power_draw_7, 0x0000000d0000300036db6da44a6db6db00000000001db6db0000000000000000],
#knight skill 3 - Named Clone Commanders
["knight_1_17", "Commander Cody", "knight_1_6", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_cody,itm_phase_ii_armor_cody,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4], knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_18", "Commander Rex", "knight_1_7", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_rex,itm_phase_ii_armor_rex,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4], knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_19", "Commander Fox", "knight_1_8", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_fox,itm_phase_ii_armor_fox,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4], knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_20", "Commander Echo", "knight_1_9", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_echo,itm_phase_ii_armor_echo,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2], 
["knight_1_21", "Commander Fives", "knight_1_0", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_fives,itm_phase_ii_armor_fives,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],  
["knight_1_22", "Commander Appo", "knight_1_2", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_appo,itm_phase_ii_armor_appo,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_3,wp(160),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_23", "Commander Wollfe", "knight_1_3", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_wolffe,itm_phase_ii_armor_wolffe,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_3,wp(160),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_24", "Commander Thorn", "knight_1_4", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_thorn,itm_phase_ii_armor_thorn,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_3,wp(160),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],   
#knight skill 2 - Unnamed Clone Commanders
["knight_1_25", "Quinlan Vos", "knight_1_5", tf_hero, 0, reserved,fac_galacticempire, [itm_jedi_clothes_robes_grey,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_2,wp(400),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_26", "Aubrie Win", "knight_1_6", tf_female|tf_hero, 0, reserved,fac_galacticempire, [itm_jedi_clothes_robes_grey,itm_black_gloves,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_2,wp(400),starwars_knight_skills_2, 0x000000000a0010032d5ab4a56d918acb00000000001dc9550000000000000000],   
["knight_1_27", "Commander (Black)", "knight_1_7", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_rep_helm_phase2_black,itm_rep_arm_phase2_black,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_2,wp(400),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_28", "Commander (Camo)", "knight_1_8", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_rep_helm_phase2_camo,itm_rep_arm_phase2_camo,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_2,wp(400),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_29", "Commander (212th)", "knight_1_9", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_212,itm_phase_ii_armor_212,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_2,wp(400),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_30", "Commander (442nd)", "knight_1_0", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_442,itm_phase_ii_armor_442,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_2,wp(400),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_31", "Commander (501st)", "knight_1_1", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_501,itm_phase_ii_armor_501,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_2,wp(400),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_32", "Commander (Wolfpack)", "knight_1_2", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_phase_ii_helmet_wolf,itm_phase_ii_armor_wolf,itm_wpn_blaster_dc17m_auto,itm_laser_bolts_red_rifle,itm_vibro_blade4],knight_attrib_2,wp(400),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
#knight skill 1
["knight_1_33", "Commander Gen 1", "knight_1_3", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_34", "Commander Gen 2", "knight_1_4", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_35", "Commander Gen 3", "knight_1_5", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_36", "Commander Gen 4", "knight_1_6", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_37", "Commander Gen 5", "knight_1_7", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_38", "Commander Gen 6", "knight_1_8", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_39", "Commander Gen 7", "knight_1_9", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_40", "Commander Gen 8", "knight_1_0", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_41", "Commander Gen 9", "knight_1_1", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_42", "Commander Gen 10", "knight_1_2", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_43", "Commander Gen 11", "knight_1_3", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_44", "Commander Gen 12", "knight_1_4", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_45", "Commander Gen 13", "knight_1_5", tf_tusken|tf_hero, 0, reserved,fac_galacticempire, [itm_clone_trooper_gloves_white,itm_phase_ii_helmet_worn,itm_phase_ii_armor_worn,itm_wpn_blaster_dc17m_auto,itm_vibro_blade4],knight_attrib_1,wp(400),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   

## SWY 0.9.0.3 Added Taris Commander, an old sith
["knight_taris","Joruus C'baoth","knight_2_1",tf_hero,0,reserved,fac_galacticempire,[itm_transparent_helmet_armor,itm_force_power_ls_4,itm_sith_master_robe_unique,itm_joruus_lightsaber,itm_force_protect,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_throw_lightsaber_red],knight_attrib_5,wp(400)|wp_archery(400),starwars_knight_skills_5|knows_power_draw_9,0x0000000fff0073882f1c6c3bde0db6db00000000001dbaf80000000000000000],


# SW - switched 10 knights to be hutt cartel
# ["knight_1_46", "Officer Hasati Neldine", "knight_1_6", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_47", "Officer Elmi Nelma", "knight_1_7", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_48", "Officer Anabus Leesyn", "knight_1_8", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_49", "Officer Zalena Zarloinne", "knight_1_9", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_50", "Officer Reria Skyprin", "knight_1_0", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# added more imperial knights since they own more land then rebels3
# ["knight_1_51", "Officer Tyrkef Darkhrn", "knight_1_1", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_52", "Officer Pakric Nerprin", "knight_1_2", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_53", "Officer Ardrax Nayrus", "knight_1_3", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_54", "Officer Aeran Archran", "knight_1_4", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_55", "Officer Zalif Risik", "knight_1_5", tf_hero|tf_randomize_face, 0, reserved,fac_galacticempire, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
 
#SW - Confederation of Indepedent Systems Knights
# don't adjust skills much because it may lead to game in-balance?
#knight skill 5
["knight_2_1","Nute Gunray","knight_2_1",tf_hero,0,reserved,fac_rebelalliance,[itm_tuuk_head,itm_tuuk_body],knight_attrib_5,wp(400)|wp_archery(400),starwars_knight_skills_5,nemoidian_face1, nemoidian_face2],
["knight_2_2","Saato","knight_2_2",tf_female|tf_hero,0,reserved,fac_rebelalliance,[itm_saato_head,itm_saato_body],knight_attrib_5,wp(400)|wp_archery(400),starwars_knight_skills_5,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_3","Asajj Ventress","knight_2_3",tf_female|tf_hero,0,reserved,fac_rebelalliance,[itm_asajj_head,itm_asajj_body,itm_asajj_lightsaber],knight_attrib_5,wp(400),starwars_knight_skills_5,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_4","Scintel","knight_2_4",tf_female|tf_hero,0,reserved,fac_rebelalliance,[itm_scintel_head,itm_scintel_body],knight_attrib_5,wp(400),starwars_knight_skills_5,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_5","Mar Tuuk","knight_2_5",tf_hero,0,reserved,fac_rebelalliance,[itm_tuuk_head,itm_tuuk_body],knight_attrib_5,wp(400),starwars_knight_skills_5,nemoidian_face1, nemoidian_face2],
["knight_2_6","Jango Fett","knight_2_6",tf_tusken|tf_hero,0,reserved,fac_rebelalliance,[itm_speeder_hutt,itm_grey_gloves,itm_grey_gloves,itm_boba_fett_blaster,itm_boba_fett_blaster,itm_laser_bolts_orange_rifle,itm_laser_bolts_orange_rifle,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_7","Grievious","knight_2_7",tf_wookiee|tf_hero,0,reserved,fac_rebelalliance,[itm_grievous,itm_transparent_feet,itm_transparent_hands,itm_transparent_head,itm_lightsaber_green],knight_attrib_5,wp(400),starwars_knight_skills_5,nemoidian_face1, nemoidian_face2],
["knight_2_8","Droid General 1","knight_2_8",tf_hero,0,reserved,fac_rebelalliance,[itm_tuuk_head,itm_tuuk_body,itm_black_gloves,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_5,wp(400),starwars_knight_skills_5,nemoidian_face1, nemoidian_face2],
["knight_2_9","Droid General 2","knight_2_9",tf_hero,0,reserved,fac_rebelalliance,[itm_tuuk_head,itm_tuuk_body,itm_black_gloves,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_5,wp(400),starwars_knight_skills_5,nemoidian_face1, nemoidian_face2],
#knight skill 4 - Generic OOMs for now, need a general droid model
["knight_2_10","OOM-11","knight_2_0",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(200),starwars_knight_skills_4,droid_face1, droid_face2],
["knight_2_11","OOM-12","knight_2_1",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(200),starwars_knight_skills_4,droid_face1, droid_face2],
["knight_2_12","OOM-13","knight_2_2",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(200),starwars_knight_skills_4,droid_face1, droid_face2],
["knight_2_13","OOM-14","knight_2_3",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(200),starwars_knight_skills_4,droid_face1, droid_face2],
["knight_2_14","OOM-15","knight_2_4",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(200),starwars_knight_skills_4,droid_face1, droid_face2],
["knight_2_15","OOM-16","knight_2_5",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(200),starwars_knight_skills_4,droid_face1, droid_face2],
["knight_2_16","OOM-17","knight_2_6",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(200),starwars_knight_skills_4,droid_face1, droid_face2],
["knight_2_17","OOM-18","knight_2_7",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(200),starwars_knight_skills_4,droid_face1, droid_face2],
["knight_2_18","OOM-19","knight_2_8",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(200),starwars_knight_skills_4,droid_face1, droid_face2],
["knight_2_19","OOM-20","knight_2_8",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_4,wp(220),starwars_knight_skills_4,droid_face1, droid_face2],
#knight skill 3 - Generic OOMs for now
["knight_2_20","OOM-21","knight_2_9",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_3,wp(180),starwars_knight_skills_3,droid_face1, droid_face2],
["knight_2_21","OOM-22","knight_2_0",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_3,wp(180),starwars_knight_skills_3,droid_face1, droid_face2],
["knight_2_22","OOM-23","knight_2_1",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_3,wp(180),starwars_knight_skills_3,droid_face1, droid_face2],   
["knight_2_23","OOM-24","knight_2_2",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_3,wp(180),starwars_knight_skills_3,droid_face1, droid_face2],   
["knight_2_24","OOM-25","knight_2_3",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_3,wp(180),starwars_knight_skills_3,droid_face1, droid_face2],   
["knight_2_25","OOM-26","knight_2_4",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_3,wp(180),starwars_knight_skills_3,droid_face1, droid_face2],   
["knight_2_26","OOM-27","knight_2_5",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_3,wp(180),starwars_knight_skills_3,droid_face1, droid_face2],   
#knight skill 2 - Generic OOMs for now
["knight_2_27","OOM-28","knight_2_6",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_2,wp(160),starwars_knight_skills_2,droid_face1, droid_face2],   
["knight_2_28","OOM-29","knight_2_7",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_2,wp(160),starwars_knight_skills_2,droid_face1, droid_face2],   
["knight_2_29","OOM-30","knight_2_8",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_2,wp(160),starwars_knight_skills_2,droid_face1, droid_face2],   
["knight_2_30","OOM-31","knight_2_9",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_2,wp(160),starwars_knight_skills_2,droid_face1, droid_face2],   
["knight_2_31","OOM-32","knight_2_0",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_2,wp(160),starwars_knight_skills_2,droid_face1, droid_face2],   
#knight skill 1 - Generic OOMs for now
["knight_2_32","OOM-33","knight_2_1",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_1,wp(140),starwars_knight_skills_1,droid_face1, droid_face2],   
["knight_2_33","OOM-34","knight_2_2",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_1,wp(140),starwars_knight_skills_1,droid_face1, droid_face2],   
["knight_2_34","OOM-35","knight_2_3",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_1,wp(140),starwars_knight_skills_1,droid_face1, droid_face2],   
["knight_2_35","OOM-36","knight_2_4",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_1,wp(140),starwars_knight_skills_1,droid_face1, droid_face2],   
["knight_2_36","OOM-37","knight_2_5",tf_droid|tf_hero,0,reserved,fac_rebelalliance,[itm_oomseries_command_body,itm_transparent_droid_feet,itm_transparent_droid_hands,itm_transparent_droid_head,itm_e5,itm_laser_bolts_red_rifle],knight_attrib_1,wp(140),starwars_knight_skills_1,droid_face1, droid_face2],   

# SW - commented out since imperials should have more knights since they own more land/castles, also moved some knights to the hutt cartel
# ["knight_2_36", "Commander Mios Darkker", "knight_2_6", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_37", "Commander Wein Lorkin", "knight_2_7", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_38", "Commander Tenke Krahek", "knight_2_8", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_39", "Commander Akalla Sanlan", "knight_2_9", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_40", "Commander Marric Terrel", "knight_2_0", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_41", "Commander Karkin Lorwol", "knight_2_1", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_42", "Commander Melkef Wolfsiri", "knight_2_2", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_43", "Commander Kelcus Torilles", "knight_2_3", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_44", "Commander Marbus Krahrn", "knight_2_4", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_45", "Commander Jagent Loin", "knight_2_5", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_46", "Commander X", "knight_2_6", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_47", "Commander X", "knight_2_7", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_48", "Commander X", "knight_2_8", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_49", "Commander X", "knight_2_9", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_50", "Commander X", "knight_2_0", tf_hero|tf_randomize_face, 0, reserved,fac_rebelalliance, [],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   

#SW - Hutt Cartel Knights
# don't adjust skills much because it may lead to game in-balance?
#knight skill 5
["knight_3_1", "Boba Fett", "knight_3_1", tf_tusken|tf_hero, 0, reserved,fac_huttcartel, [itm_speeder_hutt,itm_grey_gloves,itm_mand_arm_dummy,itm_mand_helm_dummy,itm_boba_fett_blaster,itm_boba_fett_blaster,itm_laser_bolts_orange_rifle,itm_laser_bolts_orange_rifle,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, mandalorian_face1, mandalorian_face2],
["knight_3_2", "Bib Fortuna", "knight_3_2", tf_twilek|tf_hero, 0, reserved,fac_huttcartel, [itm_twilek_male_head_bib,itm_grey_gloves,itm_dl18,itm_laser_bolts_orange_pistol,itm_twilek_dagger,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, sw_hutt_face_1, sw_hutt_face_2],
["knight_3_3", "Queequeg", "knight_3_3", tf_hero|tf_weequay, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_speeder_hutt,itm_vibro_axe_long_2h,itm_laser_bolts_orange_rifle,itm_ee3,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, weequay_face1, weequay_face2], 
["knight_3_4", "Weequay", "knight_3_4", tf_hero|tf_weequay, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_speeder_hutt,itm_weequay_vibro_axe,itm_weequay_vibro_axe,itm_laser_bolts_orange_rifle,itm_ee3,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, weequay_face1, weequay_face2], 
["knight_3_5", "Bossk", "knight_3_5", tf_hero|tf_trandoshan, 0, reserved,fac_huttcartel, [itm_speeder_hutt,itm_a280,itm_laser_bolts_orange_rifle,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, trandoshan_face1, trandoshan_face2],  
["knight_3_6", "Dengar", "knight_3_6", tf_hero, 0, reserved,fac_huttcartel, [itm_speeder_hutt,itm_dengar_armor,itm_dengar_armor,itm_dengar_helmet,itm_dengar_helmet,itm_dengar_boots,itm_dengar_boots,itm_dengar_gloves,itm_dengar_gloves,itm_dlt19_scope,itm_dlt19_scope,itm_westar_shield,itm_westar_shield,itm_vibro_sword3_gold,itm_laser_bolts_orange_rifle,itm_laser_bolts_orange_rifle],knight_attrib_5,wp(220),starwars_knight_skills_5, mandalorian_face1, mandalorian_face2], 
["knight_3_7", "Zuckuss", "knight_3_7", tf_hero|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_speeder_hutt,itm_transparent_helmet,itm_a280,itm_laser_bolts_orange_rifle,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, sw_hutt_face_1, sw_hutt_face_2], 
#knight skill 4
["knight_3_8", "Barada", "knight_3_8", tf_hero|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_klatooinian_head_helmet_a,itm_leather_gloves,itm_pipe1,itm_laser_bolts_orange_rifle,itm_ee3,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4, weequay_face1, weequay_face2], 
["knight_3_9", "Greedo", "knight_3_9", tf_hero|tf_rodian|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_speeder_hutt,itm_transparent_helmet,itm_leather_gloves,itm_a280,itm_laser_bolts_orange_rifle,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4, rodian_face1, rodian_face2], 
["knight_3_10", "Sugi", "knight_3_0", tf_hero|tf_female, 0, reserved,fac_huttcartel, [itm_sugi_head,itm_sugi_body,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, gamorrean_face1, gamorrean_face2], 
["knight_3_11", "Ortugg", "knight_3_1", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, gamorrean_face1, gamorrean_face2], 
["knight_3_12", "Gartogg", "knight_3_2", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, gamorrean_face1, gamorrean_face2], 
["knight_3_13", "Jubnuk", "knight_3_3", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, sw_hutt_face_1, gamorrean_face1, gamorrean_face2], 
["knight_3_14", "Rogua", "knight_3_4", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, gamorrean_face1, gamorrean_face2], 
#knight skill 3
["knight_3_15", "Thok", "knight_3_5", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_3,wp(180),starwars_knight_skills_3, gamorrean_face1, gamorrean_face2], 
["knight_3_16", "Thug", "knight_3_6", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_3,wp(180),starwars_knight_skills_3, gamorrean_face1, gamorrean_face2], 
["knight_3_17", "Warlug", "knight_3_7", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_3,wp(180),starwars_knight_skills_3, gamorrean_face1, gamorrean_face2], 
["knight_3_18", "Tront", "knight_3_8", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_3,wp(180),starwars_knight_skills_3, gamorrean_face1, gamorrean_face2], 
["knight_3_19", "Malakili", "knight_3_9", tf_hero, 0, reserved,fac_huttcartel, [itm_rancor_keeper_armor,itm_rancor_keeper_hat,itm_dl18,itm_laser_bolts_orange_pistol,itm_tusken_gaffi_stick,itm_energy_shield_yellow_small],knight_attrib_3,wp(180),starwars_knight_skills_3, 0x0000000b6100500736db6db6db6db6db00000000001db6db0000000000000000], 
["knight_3_20", "Nizuc Bek", "knight_3_0", tf_hero|tf_randomize_face, 0, reserved,fac_huttcartel, [itm_transparent_helmet,itm_dl18,itm_laser_bolts_orange_pistol,itm_vibro_blade1,itm_hero_shield],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_hutt_face_1, sw_hutt_face_2], 
 
#knight skill 4
# etc... 
#SW - deleted faction 4 knights, for later use for Independants?
#TAS prepraration of faction 4 as Maul's mandalorians -> Maulos
#SW -deleted faction 5 knights, for later use for Smugglers Alliance?
#TAS preparation of faction 5 as Mandalorian rebels -> Mandos

#Own faction start------------------------------
  ["reserved_knight_1", "Commander Pechnak", "knight_6_1", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_2", "Commander Daynad", "knight_6_2", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,  [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_3", "Commander Joayah", "knight_6_3", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,  [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_4", "Commander Marlund", "knight_6_4", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_5", "Commander Taarl", "knight_6_5", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,   [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium], knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_6", "Commander Euscarl", "knight_6_6", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_7", "Commander Sigmar", "knight_6_7", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,  [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_8", "Commander Talesqe", "knight_6_8", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_9", "Commander Aels", "knight_6_9", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,    [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],   knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_10", "Commander Raurqe", "knight_6_0", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],  knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_11", "Commander Bragamus", "knight_6_1", tf_hero|tf_randomize_face, 0, reserved, fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_12", "Commander Ramin", "knight_6_2", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_13", "Commander Shulk", "knight_6_3", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_14", "Commander Putar", "knight_6_4", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_15", "Commander Reichad", "knight_6_5", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium], knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_16", "Commander Walcheas", "knight_6_6", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_17", "Commander Rulkh", "knight_6_7", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_18", "Commander Ramar", "knight_6_8", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_19", "Commander Caldaran", "knight_6_9", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],   knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_20", "Commander Brabas", "knight_6_0", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],  knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
#Own faction end------------------------------

#SW - commented out faction # pretenders
#  ["galacticempire_pretender",  "Lady Isolla of Suno",       "Faction 1 Lord",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_galacticempire,[],          lord_attrib,wp(220),knows_lord_1, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent
#  ["rebelalliance_pretender",  "Prince Valdym the Bastard", "Faction 2 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_rebelalliance,[],    lord_attrib,wp(220),knows_lord_1, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified
#  ["huttcartel_pretender",  "Dustum Khan",               "Faction 3 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_huttcartel,[],      lord_attrib,wp(220),knows_lord_1, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
#of the family
#  ["faction_4_pretender",  "Lethwin Far-Seeker",   "Faction 4 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_faction_4,[],            lord_attrib,wp(220),knows_lord_1, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged
#  ["faction_5_pretender",  "Lord Kastor of Veluca",  "Faction 5 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_faction_5,[],         lord_attrib,wp(220),knows_lord_1, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

##  ["galacticempire_lord_a", "Faction 1 Lord A", "Faction 1 Lord A", tf_hero, 0,reserved,  fac_galacticempire,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_b", "Faction 1 Lord B", "Faction 1 Lord B", tf_hero, 0,reserved,  fac_rebelalliance,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_c", "Faction 1 Lord C", "Faction 1 Lord C", tf_hero, 0,reserved,  fac_huttcartel,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_d", "Faction 1 Lord D", "Faction 1 Lord D", tf_hero, 0,reserved,  fac_galacticempire,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_e", "Faction 1 Lord E", "Faction 1 Lord E", tf_hero, 0,reserved,  fac_galacticempire,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_f", "Faction 1 Lord F", "Faction 1 Lord F", tf_hero, 0,reserved,  fac_galacticempire,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_g", "Faction 1 Lord G", "Faction 1 Lord G", tf_hero, 0,reserved,  fac_galacticempire,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_h", "Faction 1 Lord H", "Faction 1 Lord H", tf_hero, 0,reserved,  fac_rebelalliance,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_i", "Faction 1 Lord I", "Faction 1 Lord I", tf_hero, 0,reserved,  fac_rebelalliance,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_j", "Faction 1 Lord J", "Faction 1 Lord J", tf_hero, 0,reserved,  fac_rebelalliance,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_k", "Faction 1 Lord K", "Faction 1 Lord K", tf_hero, 0,reserved,  fac_rebelalliance,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_l", "Faction 1 Lord L", "Faction 1 Lord L", tf_hero, 0,reserved,  fac_huttcartel,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_m", "Faction 1 Lord M", "Faction 1 Lord M", tf_hero, 0,reserved,  fac_huttcartel,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["galacticempire_lord_n", "Faction 1 Lord N", "Faction 1 Lord N", tf_hero, 0,reserved,  fac_huttcartel,[],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["mainplanet_mandalore_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_mainplanet_mandalore_castle|entry(9),reserved,  fac_swadians,[],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["mainplanet_christophsis_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_mainplanet_christophsis_castle|entry(9),reserved,  fac_swadians,[],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["mainplanet_endor_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_mainplanet_endor_castle|entry(9),reserved, fac_swadians,[],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["mainplanet_corellia_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_mainplanet_corellia_castle|entry(9),reserved,  fac_swadians,[],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["mainplanet_naboo_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_mainplanet_naboo_castle|entry(9),reserved, fac_swadians,[],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["mainplanet_kessel_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_mainplanet_kessel_castle|entry(9),reserved,  fac_swadians,[],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["mainplanet_dantooine_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_mainplanet_dantooine_castle|entry(9),reserved,  fac_swadians,[],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],
 
#  ["mainplanet_geonosis_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_mainplanet_geonosis_castle|entry(9),reserved,  fac_vaegirs,[],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["mainplanet_mon_cal_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_mainplanet_mon_cal_castle|entry(9),reserved,  fac_vaegirs,[],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["mainplanet_kashyyyk_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_mainplanet_kashyyyk_castle|entry(9),reserved, fac_vaegirs,[],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["mainplanet_hoth_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_mainplanet_hoth_castle|entry(9),reserved,  fac_vaegirs,[],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["mainplanet_gamorr_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_mainplanet_gamorr_castle|entry(9),reserved,  fac_vaegirs,[],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["mainplanet_yavin_iv_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_mainplanet_yavin_iv_castle|entry(9),reserved, fac_vaegirs,[],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["mainplanet_tatooine_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_mainplanet_tatooine_castle|entry(9),reserved,  fac_vaegirs,[],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["rebelalliance_lord_a", "Faction 2 Lord A", "Faction 2 Lord A", tf_hero, 0,reserved,  fac_galacticempire0,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_b", "Faction 2 Lord B", "Faction 2 Lord B", tf_hero, 0,reserved,  fac_galacticempire1,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_c", "Faction 2 Lord C", "Faction 2 Lord C", tf_hero, 0,reserved,  fac_galacticempire2,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_d", "Faction 2 Lord D", "Faction 2 Lord D", tf_hero, 0,reserved,  fac_galacticempire0,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_e", "Faction 2 Lord E", "Faction 2 Lord E", tf_hero, 0,reserved,  fac_galacticempire0,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_f", "Faction 2 Lord F", "Faction 2 Lord F", tf_hero, 0,reserved,  fac_galacticempire0,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_g", "Faction 2 Lord G", "Faction 2 Lord G", tf_hero, 0,reserved,  fac_galacticempire0,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_h", "Faction 2 Lord H", "Faction 2 Lord H", tf_hero, 0,reserved,  fac_galacticempire1,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_i", "Faction 2 Lord I", "Faction 2 Lord I", tf_hero, 0,reserved,  fac_galacticempire1,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_j", "Faction 2 Lord J", "Faction 2 Lord J", tf_hero, 0,reserved,  fac_galacticempire1,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_k", "Faction 2 Lord K", "Faction 2 Lord K", tf_hero, 0,reserved,  fac_galacticempire0,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_l", "Faction 2 Lord L", "Faction 2 Lord L", tf_hero, 0,reserved,  fac_galacticempire2,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_m", "Faction 2 Lord M", "Faction 2 Lord M", tf_hero, 0,reserved,  fac_galacticempire2,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["rebelalliance_lord_n", "Faction 2 Lord N", "Faction 2 Lord N", tf_hero, 0,reserved,  fac_galacticempire2,[],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members
#SW - commented out faction # wives, daughters
#  ["knight_1_1_wife","Lady Anna","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_galacticempire, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
#  ["knight_2_1_wife","Lady Junitha","knight_2_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_rebelalliance, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#  ["knight_3_1_wife","Lady Borge","knight_3_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_huttcartel, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
#  ["knight_4_1_wife","Lady Jadeth","knight_4_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_faction_4, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
#  ["knight_5_1_wife","Lady Brina","knight_5_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_faction_5, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],

#  ["knight_1_2_wife","Lady Nelda","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_galacticempire, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
#   ["knight_2_2_wife","Lady Katia","knight_2_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_rebelalliance, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#  ["knight_3_2_wife","Lady Tuan","knight_3_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_huttcartel, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
#  ["knight_4_2_wife","Lady Miar","knight_4_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_faction_4, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
#  ["knight_5_2_wife","Lady Aliena","knight_5_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_faction_5, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],

#  ["knight_1_1_daughter","Lady Bela","knight_1_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_galacticempire,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
#  ["knight_2_1_daughter","Lady Seomis","knight_2_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_rebelalliance,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#  ["knight_3_1_daughter","Lady Chedina","knight_3_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_huttcartel,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
#  ["knight_4_1_daughter","Lady Dria","knight_4_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_faction_4,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
#  ["knight_5_1_daughter","Lady Aneth","knight_5_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_faction_5,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],

#  ["knight_1_2_daughter","Lady Elina","knight_1_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_galacticempire,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
#  ["knight_2_2_daughter","Lady Drina","knight_2_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_rebelalliance,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#  ["knight_3_2_daughter","Lady Ayasu","knight_3_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_huttcartel,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
#  ["knight_4_2_daughter","Lady Glunde","knight_4_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_faction_4,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
#  ["knight_5_2_daughter","Lady Reada","knight_5_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_faction_5,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],

#  ["galacticempire1_lord_daughter","galacticempire1_lord_daughter","galacticempire1_lord_daughter",tf_hero|tf_female,0,reserved,fac_galacticempire0,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["galacticempire3_lord_daughter","galacticempire3_lord_daughter","galacticempire3_lord_daughter",tf_hero|tf_female,0,reserved,fac_galacticempire0,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["galacticempire_lady_a","galacticempire_lady_a","galacticempire_lady_a",tf_hero|tf_female,0,reserved,fac_galacticempire, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["galacticempire_lady_b","galacticempire_lady_b","galacticempire_lady_b",tf_hero|tf_female,0,reserved,fac_galacticempire, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["rebelalliance_lady_a","Faction 2 Lady a","Faction 2 Lady a",tf_hero|tf_female,0,reserved,fac_rebelalliance, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["rebelalliance_lady_b","Faction 2 Lady b","Faction 2 Lady b",tf_hero|tf_female,0,reserved,fac_rebelalliance, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["huttcartel_lady_a","Faction 3 Lady a","Faction 3 Lady a",tf_hero|tf_female,0,reserved,fac_huttcartel, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["huttcartel_lady_b","Faction 3 Lady b","Faction 3 Lady b",tf_hero|tf_female,0,reserved,fac_huttcartel,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["faction_4_lady_a","Faction 4 Lady a","Faction 4 Lady a",tf_hero|tf_female,0,reserved,fac_faction_4,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["faction_4_lady_b","Faction 4 Lady b","Faction 4 Lady b",tf_hero|tf_female,0,reserved,fac_faction_4,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

["heroes_end", "heroes end", "heroes end", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_speeder],def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_galacticempire,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_rebelalliance,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_huttcartel,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_faction_4,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_faction_5,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_galacticempire,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_rebelalliance,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_huttcartel,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_faction_4,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
#SW - renamed Seneschal to Administrator ?
#SW - town_1 = Mandalore, give mandalorian armor/tunic
["mainplanet_mandalore_seneschal", "Planet Administrator", "Town 1 Administrator", tf_hero|tf_randomize_face|tf_guarantee_boots|tf_is_merchant, 0,reserved,  fac_neutral,[itm_mand_arm_dummy,itm_mand_helm_dummy,itm_grey_gloves], def_attrib|level(2),wp(20),knows_common, mandalorian_face1, mandalorian_face2],
["mainplanet_christophsis_seneschal", "Planet Administrator", "Town 2 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_endor_seneschal", "Planet Administrator", "Town 3 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_corellia_seneschal", "Planet Administrator", "Town 4 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_naboo_seneschal", "Planet Administrator", "Town 5 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_kessel_seneschal", "Planet Administrator", "Town 6 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_dantooine_seneschal", "Planet Administrator", "Town 7 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["mainplanet_geonosis_seneschal", "Planet Administrator", "Town 8 Administrator", tf_hero|tf_geonosian|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[],   def_attrib|level(2),wp(20),knows_common, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["mainplanet_mon_cal_seneschal", "Planet Administrator", "Town 9 Administrator", tf_hero|tf_moncal|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple], def_attrib|level(2),wp(20),knows_common, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["mainplanet_kashyyyk_seneschal", "Planet Administrator", "Town 10 Administrator", tf_hero|tf_randomize_face|tf_wookiee|tf_is_merchant, 0,reserved,  fac_neutral,[],     def_attrib|level(2),wp(20),knows_common, wookiee_face1, wookiee_face2],
["mainplanet_hoth_seneschal", "Planet Administrator", "Town 11 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["mainplanet_gamorr_seneschal", "Planet Administrator", "Town 12 Administrator", tf_hero|tf_randomize_face|tf_gamorrean|tf_is_merchant, 0,reserved,  fac_neutral,[], def_attrib|level(2),wp(20),knows_common, gamorrean_face1],
["mainplanet_yavin_iv_seneschal", "Planet Administrator", "Town 13 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_tatooine_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_manaan_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_coruscant_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["mainplanet_ryloth_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_twilek|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, twilek_face1, twilek_face2],
#give hutt armor
["mainplanet_nalhutta_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_hutt|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],     def_attrib|level(2),wp(20),knows_common, hutt_face1, hutt_face2],
#SW - town 19, give bothan armor
["mainplanet_bothawui_seneschal", "Planet Administrator", "Town 19 Administrator", tf_hero|tf_bothan|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, bothan_face1, bothan_face2],
["mainplanet_mustafar_seneschal", "Planet Administrator", "Town 20 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_kamino_seneschal", "Planet Administrator", "Town 21 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_taris_seneschal", "Planet Administrator", "Town 21 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_raxusprime_seneschal", "Planet Administrator", "Town 21 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_sarapin_seneschal", "Planet Administrator", "Town 21 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_hypori_seneschal", "Planet Administrator", "Town 21 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_felucia_seneschal", "Planet Administrator", "Town 21 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["mainplanet_bespin_seneschal", "Planet Administrator", "Town 21 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_noble_blue,itm_ind_clothes_noble_orange,itm_ind_clothes_noble_purple],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],

["spacestation_1_seneschal", "Spacestation Commander", "Castle 1 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_2_seneschal", "Spacestation Commander", "Castle 2 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_3_seneschal", "Spacestation Commander", "Castle 3 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_4_seneschal", "Spacestation Commander", "Castle 4 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_5_seneschal", "Spacestation Commander", "Castle 5 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_6_seneschal", "Spacestation Commander", "Castle 6 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_7_seneschal", "Spacestation Commander", "Castle 7 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_8_seneschal", "Spacestation Commander", "Castle 8 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_9_seneschal", "Spacestation Commander", "Castle 9 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_10_seneschal", "Spacestation Commander", "Castle 10 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_11_seneschal", "Spacestation Commander", "Castle 11 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_12_seneschal", "Spacestation Commander", "Castle 12 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_13_seneschal", "Spacestation Commander", "Castle 13 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_14_seneschal", "Spacestation Commander", "Castle 14 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_15_seneschal", "Spacestation Commander", "Castle 15 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_16_seneschal", "Spacestation Commander", "Castle 16 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_17_seneschal", "Spacestation Commander", "Castle 17 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_18_seneschal", "Spacestation Commander", "Castle 18 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_19_seneschal", "Spacestation Commander", "Castle 19 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_20_seneschal", "Spacestation Commander", "Castle 20 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_21_seneschal", "Spacestation Commander", "Castle 21 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_22_seneschal", "Spacestation Commander", "Castle 22 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_23_seneschal", "Spacestation Commander", "Castle 23 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_24_seneschal", "Spacestation Commander", "Castle 24 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_25_seneschal", "Spacestation Commander", "Castle 25 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_26_seneschal", "Spacestation Commander", "Castle 26 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_27_seneschal", "Spacestation Commander", "Castle 27 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_28_seneschal", "Spacestation Commander", "Castle 28 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_29_seneschal", "Spacestation Commander", "Castle 29 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_30_seneschal", "Spacestation Commander", "Castle 30 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_31_seneschal", "Spacestation Commander", "Castle 31 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_32_seneschal", "Spacestation Commander", "Castle 32 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_33_seneschal", "Spacestation Commander", "Castle 33 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_34_seneschal", "Spacestation Commander", "Castle 34 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_35_seneschal", "Spacestation Commander", "Castle 35 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_36_seneschal", "Spacestation Commander", "Castle 36 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_37_seneschal", "Spacestation Commander", "Castle 37 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_38_seneschal", "Spacestation Commander", "Castle 38 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_39_seneschal", "Spacestation Commander", "Castle 39 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_40_seneschal", "Spacestation Commander", "Castle 40 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_41_seneschal", "Spacestation Commander", "Castle 41 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["spacestation_42_seneschal", "Spacestation Commander", "Castle 42 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_ind_clothes_outfsmuggler_green],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],

#Arena Masters
#SW - town_1 = Mandalore, give mandalorian armor/tunic
["mainplanet_mandalore_arena_master", "Arena Master","Tournament Master",tf_hero|tf_guarantee_all_armor|tf_randomize_face, scn_mainplanet_mandalore_arena|entry(52),reserved,   fac_commoners,[itm_mand_arm_dummy,itm_grey_gloves],    def_attrib|level(2),wp(20),knows_common,mandalorian_face1, mandalorian_face2],
["mainplanet_christophsis_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_christophsis_arena|entry(52),reserved,   fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],   def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_endor_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_endor_arena|entry(52),reserved,   fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_corellia_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_corellia_arena|entry(52),reserved,   fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_naboo_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_naboo_arena|entry(52),reserved,   fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],   def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_kessel_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_kessel_arena|entry(52),reserved,   fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a], def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_dantooine_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_dantooine_arena|entry(52),reserved,   fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],   def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["mainplanet_geonosis_arena_master", "Arena Master","Tournament Master",tf_hero|tf_geonosian|tf_randomize_face, scn_mainplanet_geonosis_arena|entry(52),reserved,   fac_commoners,[itm_geonosian_sonic_rifle,itm_sonic_beam_rifle],    def_attrib|level(2),wp(20),knows_common,geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["mainplanet_mon_cal_arena_master", "Arena Master","Tournament Master",tf_hero|tf_moncal|tf_randomize_face, scn_mainplanet_mon_cal_arena|entry(52),reserved,   fac_commoners,[itm_ind_clothes_securityguarda5], def_attrib|level(2),wp(20),knows_common,moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["mainplanet_kashyyyk_arena_master","Arena Master","Tournament Master",tf_hero|tf_wookiee|tf_randomize_face, scn_mainplanet_kashyyyk_arena|entry(52),reserved,  fac_commoners,[itm_wookiee_armor_chest],   def_attrib|level(2),wp(20),knows_common,wookiee_face1, wookiee_face2],
["mainplanet_hoth_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_hoth_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["mainplanet_gamorr_arena_master","Arena Master","Tournament Master",tf_hero|tf_gamorrean|tf_randomize_face, scn_mainplanet_gamorr_arena|entry(52),reserved,  fac_commoners,[],    def_attrib|level(2),wp(20),knows_common, gamorrean_face1, gamorrean_face2],
["mainplanet_yavin_iv_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_yavin_iv_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],   def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_tatooine_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_tatooine_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_manaan_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_manaan_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_coruscant_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_coruscant_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["mainplanet_ryloth_arena_master","Arena Master","Tournament Master",tf_hero|tf_twilek|tf_randomize_face, scn_mainplanet_ryloth_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5],    def_attrib|level(2),wp(20),knows_common,twilek_face1, twilek_face2],
["mainplanet_nalhutta_arena_master","Arena Master","Tournament Master",tf_hero|tf_hutt|tf_randomize_face, scn_mainplanet_nalhutta_arena|entry(52),reserved,  fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],    def_attrib|level(2),wp(20),knows_common,hutt_face1, hutt_face2],
#SW - town 19, bothan
["mainplanet_bothawui_arena_master","Arena Master","Tournament Master",tf_hero|tf_bothan|tf_randomize_face, scn_mainplanet_bothawui_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common, bothan_face1, bothan_face2],
["mainplanet_mustafar_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_mustafar_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_kamino_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_kamino_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_taris_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_taris_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_raxusprime_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_raxusprime_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_sarapin_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_sarapin_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_hypori_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_hypori_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_felucia_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_felucia_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["mainplanet_bespin_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_mainplanet_bespin_arena|entry(52),reserved,  fac_commoners,[itm_ind_clothes_securityguarda5,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],

# Underground 

##  ["mainplanet_mandalore_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["mainplanet_christophsis_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["mainplanet_endor_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["mainplanet_corellia_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["mainplanet_naboo_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["mainplanet_kessel_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["mainplanet_dantooine_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["mainplanet_geonosis_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["mainplanet_mon_cal_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["mainplanet_kashyyyk_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["mainplanet_hoth_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["mainplanet_gamorr_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["mainplanet_yavin_iv_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["mainplanet_tatooine_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

#SW - town_1 = Mandalore, give mandalorian armor/tunic  
["mainplanet_mandalore_armorer","Armorer",  "Armorer",  tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_mand_arm_dummy,itm_grey_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, mandalorian_face1, mandalorian_face2],
["mainplanet_christophsis_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_endor_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_corellia_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_naboo_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_kessel_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_dantooine_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["mainplanet_geonosis_armorer","Armorer",  "Armorer",  tf_hero|tf_geonosian|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_transparent_feet,itm_transparent_hands,itm_transparent_head,itm_ind_arm_geonosian,itm_ind_arm_geonosian_wingless,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["mainplanet_mon_cal_armorer","Armorer",  "Armorer",  tf_hero|tf_moncal|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["mainplanet_kashyyyk_armorer","Armorer", "Armorer",  tf_hero|tf_wookiee|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, wookiee_face1, wookiee_face2],
["mainplanet_hoth_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["mainplanet_gamorr_armorer","Armorer", "Armorer",  tf_hero|tf_gamorrean|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, gamorrean_face1, gamorrean_face2],
["mainplanet_yavin_iv_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_tatooine_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_manaan_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_coruscant_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["mainplanet_ryloth_armorer","Armorer", "Armorer",  tf_hero|tf_twilek|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, twilek_face1, twilek_face2],
#SW - town 18 = Nal Hutta, give jabba armor
["mainplanet_nalhutta_armorer","Armorer", "Armorer",  tf_hero|tf_hutt|tf_trandoshan|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],def_attrib|level(12),wp(80),knows_inventory_management_10, hutt_face1, hutt_face2],
#SW - town 19, bothan
["mainplanet_bothawui_armorer","Armorer", "Armorer",  tf_hero|tf_bothan|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, bothan_face1, bothan_face2],
["mainplanet_mustafar_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_kamino_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_taris_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_raxusprime_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_sarapin_armorer","Armorer", "Armorer",  tf_hero|tf_trandoshan|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_hypori_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_felucia_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_bespin_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_ind_rep_guardarmor1,itm_black_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],

# Weapon merchants
#SW - town_1 = Mandalore, give mandalorian armor/tunic (also switched from female to male)
["mainplanet_mandalore_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_guarantee_all_armor|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_mand_arm_dummy,itm_grey_gloves,itm_vibro_blade1,itm_mandalorian_heavy_blaster,itm_laser_bolts_yellow_rifle],def_attrib|level(12),wp(80),knows_inventory_management_10, mandalorian_face1, mandalorian_face2],
["mainplanet_christophsis_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_endor_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_corellia_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_naboo_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_kessel_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_dantooine_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["mainplanet_geonosis_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_geonosian|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_transparent_feet,itm_transparent_hands,itm_transparent_head,itm_ind_arm_geonosian,itm_ind_arm_geonosian_wingless,itm_geonosian_sonic_rifle,itm_sonic_beam_rifle],def_attrib|level(12),wp(80),knows_inventory_management_10, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["mainplanet_mon_cal_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_moncal|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["mainplanet_kashyyyk_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_wookiee|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_wookiee_bowcaster,itm_laser_bolts_yellow_rifle,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, wookiee_face1, wookiee_face2],
["mainplanet_hoth_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["mainplanet_gamorr_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_gamorrean|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_axe_medium_1h],def_attrib|level(12),wp(80),knows_inventory_management_10, gamorrean_face1, gamorrean_face2],
["mainplanet_yavin_iv_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_tatooine_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_manaan_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_coruscant_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["mainplanet_ryloth_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_twilek|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, twilek_face1, twilek_face2],
#SW - town 18 = Nal Hutta, give jabba armor
["mainplanet_nalhutta_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_hutt|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],def_attrib|level(12),wp(80),knows_inventory_management_10, hutt_face1, hutt_face2],
#town 19, bothan
["mainplanet_bothawui_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_bothan|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, bothan_face1, bothan_face2],
["mainplanet_mustafar_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_kamino_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaminoan_female_head,itm_kaminoan_female_body,itm_transparent_feet,itm_transparent_hands],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_taris_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_raxusprime_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_sarapin_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_hypori_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_felucia_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_bespin_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],

#Tavern keepers
#SW - updated Tavern_Keeper to Bartender
#SW - town_1 = Mandalore, give mandalorian armor/tunic
["mainplanet_mandalore_bartender", "Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face,scn_mainplanet_mandalore_cantina|entry(9),0,   fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green],def_attrib|level(2),wp(20),knows_common, mandalorian_face1, mandalorian_face2],
["mainplanet_christophsis_bartender", "Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_christophsis_cantina|entry(9),0,   fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["mainplanet_endor_bartender", "Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_endor_cantina|entry(9),0,   fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_3, sw_woman_face_2],
["mainplanet_corellia_bartender", "Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_corellia_cantina|entry(9),0,   fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["mainplanet_naboo_bartender", "Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_naboo_cantina|entry(9),0,   fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_3],
["mainplanet_kessel_bartender", "Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_kessel_cantina|entry(9),0,   fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["mainplanet_dantooine_bartender", "Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_dantooine_cantina|entry(9),0,   fac_commoners,[itm_transparent_feet,itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_3],
#SW- town_8 = geonosian
["mainplanet_geonosis_bartender", "Bartender","Bartender",tf_hero|tf_geonosian|tf_randomize_face,scn_mainplanet_geonosis_cantina|entry(9),0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor (removed tf_female)
["mainplanet_mon_cal_bartender", "Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_moncal|tf_randomize_face,scn_mainplanet_mon_cal_cantina|entry(9),0,   fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green],def_attrib|level(2),wp(20),knows_common, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["mainplanet_kashyyyk_bartender","Bartender","Bartender",tf_hero|tf_wookiee|tf_randomize_face,scn_mainplanet_kashyyyk_cantina|entry(9),0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common, wookiee_face1, wookiee_face2],
["mainplanet_hoth_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_hoth_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_3],
#SW - town_12 = Gamorr, give gamorrean armor
["mainplanet_gamorr_bartender","Bartender","Bartender",tf_hero|tf_gamorrean|tf_randomize_face,scn_mainplanet_gamorr_cantina|entry(9),0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common, gamorrean_face1, gamorrean_face2],
["mainplanet_yavin_iv_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_yavin_iv_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["mainplanet_tatooine_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_tatooine_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["mainplanet_manaan_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_manaan_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_3, sw_woman_face_2],
["mainplanet_coruscant_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_coruscant_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
#SW - town 17 = Ryloth, give twilek armor
["mainplanet_ryloth_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_twilek_female,scn_mainplanet_ryloth_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green],def_attrib|level(2),wp(20),knows_common, twilek_female_face1, twilek_female_face2],
#SW - town 18 - give jaba armor
["mainplanet_nalhutta_bartender","Bartender","Bartender",tf_hero|tf_hutt|tf_randomize_face,scn_mainplanet_nalhutta_cantina|entry(9),0,  fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],def_attrib|level(2),wp(20),knows_common, hutt_face1, hutt_face2],
#SW - town 19, bothan
["mainplanet_bothawui_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_bothan|tf_randomize_face,scn_mainplanet_bothawui_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green],def_attrib|level(2),wp(20),knows_common, bothan_face1, bothan_face2],
["mainplanet_mustafar_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_mustafar_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_3],
["mainplanet_kamino_bartender","Bartender","Bartender",tf_hero|tf_randomize_face|tf_female,scn_mainplanet_kamino_cantina|entry(9),0,  fac_commoners,[itm_kaminoan_female_head,itm_kaminoan_female_body,itm_transparent_feet,itm_transparent_hands],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["mainplanet_taris_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_taris_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["mainplanet_raxusprime_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_raxusprime_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_3, sw_woman_face_2],
["mainplanet_sarapin_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_sarapin_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["mainplanet_hypori_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_hypori_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["mainplanet_felucia_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_felucia_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_3],
["mainplanet_felucia_bartender","Bartender","Bartender",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_female,scn_mainplanet_bespin_cantina|entry(9),0,  fac_commoners,[itm_black_gloves,itm_ind_clothes_outfsmuggler_green,itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_3],

#Goods Merchants
#SW - town_1 = Mandalore, give mandalorian armor/tunic
["mainplanet_mandalore_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_mandalore_store|entry(9),0, fac_commoners,     [],def_attrib|level(2),wp(20),knows_inventory_management_10, mandalorian_face1, mandalorian_face2],
["mainplanet_christophsis_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_christophsis_store|entry(9),0, fac_commoners,     [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_3],
["mainplanet_endor_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_endor_store|entry(9),0, fac_commoners,     [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["mainplanet_corellia_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_corellia_store|entry(9),0, fac_commoners,     [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["mainplanet_naboo_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_naboo_store|entry(9),0, fac_commoners,     [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_3, sw_woman_face_2],
["mainplanet_kessel_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_kessel_store|entry(9),0, fac_commoners,     [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["mainplanet_dantooine_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_dantooine_store|entry(9),0, fac_commoners,     [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_3],
#SW- town_8 = geonosian
["mainplanet_geonosis_merchant", "Merchant","Merchant",          tf_hero|tf_geonosian|tf_randomize_face|tf_is_merchant, scn_mainplanet_geonosis_store|entry(9),0, fac_commoners,     [],def_attrib|level(2),wp(20),knows_inventory_management_10, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["mainplanet_mon_cal_merchant", "Merchant","Merchant",          tf_hero|tf_moncal|tf_randomize_face|tf_is_merchant, scn_mainplanet_mon_cal_store|entry(9),0, fac_commoners,     [],def_attrib|level(2),wp(20),knows_inventory_management_10, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["mainplanet_kashyyyk_merchant","Merchant","Merchant",          tf_hero|tf_randomize_face|tf_wookiee|tf_is_merchant, scn_mainplanet_kashyyyk_store|entry(9),0, fac_commoners,    [],def_attrib|level(2),wp(20),knows_inventory_management_10, wookiee_face1, wookiee_face2],
["mainplanet_hoth_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_hoth_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_3, sw_woman_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["mainplanet_gamorr_merchant","Merchant","Merchant",tf_gamorrean|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_gamorr_store|entry(9),0, fac_commoners,    [],def_attrib|level(2),wp(20),knows_inventory_management_10, gamorrean_face1, gamorrean_face2],
["mainplanet_yavin_iv_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_yavin_iv_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["mainplanet_tatooine_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_tatooine_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["mainplanet_manaan_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_manaan_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_3, sw_woman_face_2],
["mainplanet_coruscant_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_coruscant_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
#SW - town 17 = Ryloth, give twilek armor
["mainplanet_ryloth_merchant","Merchant","Merchant",tf_twilek_female|tf_guarantee_all_armor|tf_hero|tf_is_merchant, scn_mainplanet_ryloth_store|entry(9),0, fac_commoners,    [itm_transparent_head,itm_transparent_feet,itm_transparent_hands,itm_twilek_slave_a,itm_twilek_slave_b,itm_twilek_slave_c,itm_twilek_slave_d],def_attrib|level(2),wp(20),knows_inventory_management_10, twilek_female_face1, twilek_female_face2],
#town 18, hutt
["mainplanet_nalhutta_merchant","Merchant","Merchant",          tf_hero|tf_hutt|tf_randomize_face|tf_is_merchant, scn_mainplanet_nalhutta_store|entry(9),0, fac_commoners,    [itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],def_attrib|level(2),wp(20),knows_inventory_management_10, hutt_face1, hutt_face2],
#SW - town 19, bothan
["mainplanet_bothawui_merchant","Merchant","Merchant",tf_bothan|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_bothawui_store|entry(9),0, fac_commoners,    [],def_attrib|level(2),wp(20),knows_inventory_management_10, bothan_face1, bothan_face2],
["mainplanet_mustafar_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_mustafar_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["mainplanet_kamino_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant|tf_bothan, scn_mainplanet_kamino_store|entry(9),0, fac_commoners,    [itm_kaminoan_female_head,itm_kaminoan_female_body,itm_transparent_feet,itm_transparent_hands],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_3, sw_woman_face_2],
["mainplanet_taris_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_taris_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_3],
["mainplanet_raxusprime_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_raxusprime_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["mainplanet_sarapin_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_sarapin_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_3],
["mainplanet_hypori_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_hypori_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["mainplanet_felucia_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_felucia_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_3, sw_woman_face_2],
["mainplanet_bespin_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_mainplanet_bespin_store|entry(9),0, fac_commoners,    [itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_3, sw_woman_face_2],

#["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_randomize_face|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],

# Horse Merchants
#SW - renamed to Transportation Merchant ?
#SW - town_1 = Mandalore, give mandalorian armor/tunic (also removed female flag)
["mainplanet_mandalore_horse_merchant","Transportation Merchant","Town 1 Transportation Merchant",tf_hero|tf_guarantee_all_armor|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_mand_arm_dummy,itm_mand_helm_dummy,itm_grey_gloves],   def_attrib|level(2),wp(20),knows_inventory_management_10, mandalorian_face1, mandalorian_face2],
["mainplanet_christophsis_horse_merchant","Transportation Merchant","Town 2 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                      def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_endor_horse_merchant","Transportation Merchant","Town 3 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_corellia_horse_merchant","Transportation Merchant","Town 4 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                       def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_naboo_horse_merchant","Transportation Merchant","Town 5 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],   def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_kessel_horse_merchant","Transportation Merchant","Town 6 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_dantooine_horse_merchant","Transportation Merchant","Town 7 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["mainplanet_geonosis_horse_merchant","Transportation Merchant","Town 8 Transportation Merchant",tf_hero|tf_geonosian|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_geonosian_static_pike],                        def_attrib|level(5),wp(20),knows_inventory_management_10, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["mainplanet_mon_cal_horse_merchant","Transportation Merchant","Town 9 Transportation Merchant",tf_hero|tf_moncal|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green],                       def_attrib|level(5),wp(20),knows_inventory_management_10, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["mainplanet_kashyyyk_horse_merchant","Transportation Merchant","Town 10 Transportation Merchant",tf_hero|tf_wookiee|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[],     def_attrib|level(5),wp(20),knows_inventory_management_10, wookiee_face1, wookiee_face2],
["mainplanet_hoth_horse_merchant","Transportation Merchant","Town 11 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["mainplanet_gamorr_horse_merchant","Transportation Merchant","Town 12 Transportation Merchant",tf_hero|tf_gamorrean|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[],                        def_attrib|level(5),wp(20),knows_inventory_management_10, gamorrean_face1, gamorrean_face2],
["mainplanet_yavin_iv_horse_merchant","Transportation Merchant","Town 13 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                       def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_tatooine_horse_merchant","Transportation Merchant","Town 14 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],     def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_manaan_horse_merchant","Transportation Merchant","Town 15 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_coruscant_horse_merchant","Transportation Merchant","Town 16 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["mainplanet_ryloth_horse_merchant","Transportation Merchant","Town 17 Transportation Merchant",tf_hero|tf_twilek|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green],                       def_attrib|level(5),wp(20),knows_inventory_management_10, twilek_face1, twilek_face2],
#SW - town 18, give hutt armor
["mainplanet_nalhutta_horse_merchant","Transportation Merchant","Town 18 Transportation Merchant",tf_hero|tf_hutt|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],     def_attrib|level(5),wp(20),knows_inventory_management_10, hutt_face1, hutt_face2],
#SW - town 19 - bothan
["mainplanet_bothawui_horse_merchant","Transportation Merchant","Town 19 Transportation Merchant",tf_hero|tf_bothan|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green],                        def_attrib|level(5),wp(20),knows_inventory_management_10, bothan_face1, bothan_face2],
["mainplanet_mustafar_horse_merchant","Transportation Merchant","Town 20 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_kamino_horse_merchant","Transportation Merchant","Town 21 Transportation Merchant",tf_hero|tf_bothan|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_kaminoan_female_head,itm_kaminoan_female_body,itm_transparent_feet,itm_transparent_hands],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_taris_horse_merchant","Transportation Merchant","Town 22 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_raxusprime_horse_merchant","Transportation Merchant","Town 23 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_sarapin_horse_merchant","Transportation Merchant","Town 24 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_hypori_horse_merchant","Transportation Merchant","Town 23 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_felucia_horse_merchant","Transportation Merchant","Town 24 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["mainplanet_bespin_horse_merchant","Transportation Merchant","Town 24 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,0, 0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],

#SW - town_1 = Mandalore, give mandalorian armor/tunic
["mainplanet_mandalore_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_guarantee_all_armor|tf_randomize_face, 0,reserved,  fac_neutral,[itm_mand_arm_dummy,itm_mand_helm_dummy,itm_grey_gloves], def_attrib|level(2),wp(20),knows_common, mandalorian_face1, mandalorian_face2],
["mainplanet_christophsis_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_endor_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_corellia_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear],     def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_naboo_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_kessel_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_dantooine_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["mainplanet_geonosis_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_geonosian|tf_randomize_face, 0,reserved,  fac_neutral,[itm_transparent_feet,itm_transparent_hands,itm_transparent_head,itm_ind_arm_geonosian,itm_ind_arm_geonosian_wingless,itm_geonosian_sonic_pistol,itm_sonic_beam_pistol],   def_attrib|level(2),wp(20),knows_common,  geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["mainplanet_mon_cal_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_moncal|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green], def_attrib|level(2),wp(20),knows_common,  moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["mainplanet_kashyyyk_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_wookiee|tf_randomize_face, 0,reserved,  fac_neutral,[itm_transparent_hands,itm_transparent_feet,itm_wookiee_fullbody],     def_attrib|level(2),wp(20),knows_common,  wookiee_face1, wookiee_face2],
["mainplanet_hoth_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["mainplanet_gamorr_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_gamorrean|tf_randomize_face, 0,reserved,  fac_neutral,[], def_attrib|level(2),wp(20),knows_common,  gamorrean_face1, gamorrean_face2],
["mainplanet_yavin_iv_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_tatooine_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear],     def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_manaan_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_coruscant_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["mainplanet_ryloth_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_twilek|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green],   def_attrib|level(2),wp(20),knows_common,  twilek_face1, twilek_face2],
#SW - town_18 = Nal Hutta, give jabba armor
["mainplanet_nalhutta_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_hutt|tf_randomize_face, 0,reserved,  fac_neutral,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],     def_attrib|level(2),wp(20),knows_common,  hutt_face1, hutt_face2],
#SW - town 19, bothan
["mainplanet_bothawui_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_bothan|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green], def_attrib|level(2),wp(20),knows_common,  bothan_face1, bothan_face2],
["mainplanet_mustafar_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_kamino_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_bothan|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kaminoan_female_head,itm_kaminoan_female_body,itm_transparent_feet,itm_transparent_hands], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_taris_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_raxusprime_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_sarapin_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_hypori_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_felucia_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["mainplanet_bespin_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ind_clothes_outfitvest_green,itm_lobot_headgear], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],


#Village stores
["minorplanet_admin_1", "Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_2", "Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_3", "Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Ilum
["minorplanet_admin_4", "Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Sernipadal
["minorplanet_admin_5", "Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_6", "Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_7", "Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_8", "Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Dubrilion
["minorplanet_admin_9", "Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_10","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_11","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Rakata Prime
["minorplanet_admin_12","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Mykr
["minorplanet_admin_13","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_14","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_15","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_16","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_17","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_18","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_19","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_20","Planet_Administrator", "Planet_Administrator",tf_hero|tf_moncal|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_21","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_22","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_23","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_24","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_25","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_26","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Bilbingri
["minorplanet_admin_27","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_28","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Dantooine Moon
["minorplanet_admin_29","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_30","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_31","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_32","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Muunulist
["minorplanet_admin_33","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_34","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Iridonia
["minorplanet_admin_35","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_zabrak_face_2, sw_zabrak_face_2],
["minorplanet_admin_36","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_37","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Belkadan
["minorplanet_admin_38","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Helska
["minorplanet_admin_39","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_40","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_41","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_42","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_43","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_44","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_45","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_46","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Selvaris
["minorplanet_admin_47","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_48","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_49","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_50","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Yaga Minor
["minorplanet_admin_51","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_52","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_53","Planet_Administrator", "Planet_Administrator",tf_hero|tf_gamorrean|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_durasteel_shield_small,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_throwing_axes], def_attrib_4|level(2),wp(20),starwars_skills_4, gamorrean_face1, gamorrean_face2],
["minorplanet_admin_54","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_55","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Ithor
["minorplanet_admin_56","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_57","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_58","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Bastion
["minorplanet_admin_59","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Anobis
["minorplanet_admin_60","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_61","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_62","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_63","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_64","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_65","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_66","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_67","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_68","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_69","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_70","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_71","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_72","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_73","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_74","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_75","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_76","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Ord Mantel
["minorplanet_admin_77","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_78","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Manaan Moon
["minorplanet_admin_79","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_80","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_81","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Garqi
["minorplanet_admin_82","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_83","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_84","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_85","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_86","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_87","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_88","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_89","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["minorplanet_admin_90","Planet_Administrator", "Planet_Administrator",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ind_clothes_outfitvest_green,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Place extra merchants before this point
["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

# Chests
#["zendar_chest","Zendar Chest","Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
#SW - modified tutorial_chests
["tutorial_chest_1","Melee Weapons Chest","Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_2","Ranged Weapons Chest","Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
#SW - added Star Wars items to bonus chests
# bonus_chest_1 = town_13 (Rivacheg)
["bonus_chest_1","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_darth_vader_helmet,itm_darth_vader_armor,itm_darth_vader_lightsaber,itm_obi_wan_lightsaber,itm_luke_skywalker_lightsaber,itm_chewbacca_bowcaster,itm_han_solo_blaster,itm_princess_leia_outfit,itm_boba_fett_blaster,itm_twilek_male_head_bib,itm_weequay_vibro_axe],def_attrib|level(18),wp(60),knows_common, 0],
# bonus_chest_2 = town_5 (Jelkala)
["bonus_chest_2","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_darth_vader_helmet,itm_darth_vader_armor,itm_darth_vader_lightsaber,itm_obi_wan_lightsaber,itm_luke_skywalker_lightsaber,itm_chewbacca_bowcaster,itm_han_solo_blaster,itm_princess_leia_outfit,itm_boba_fett_blaster,itm_twilek_male_head_bib,itm_weequay_vibro_axe],def_attrib|level(18),wp(60),knows_common, 0],
# bonus_chest_3 = town_2 (Tihr)
["bonus_chest_3","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_darth_vader_helmet,itm_darth_vader_armor,itm_darth_vader_lightsaber,itm_obi_wan_lightsaber,itm_luke_skywalker_lightsaber,itm_chewbacca_bowcaster,itm_han_solo_blaster,itm_princess_leia_outfit,itm_boba_fett_blaster,itm_twilek_male_head_bib,itm_weequay_vibro_axe],def_attrib|level(18),wp(60),knows_common, 0],

#town specific bonus chests
["bonus_box_mainplanet_1","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_boba_fett_blaster],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_2","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_3","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_4","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_han_solo_blaster],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_5","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_6","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_7","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_8","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_9","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_10","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_chewbacca_bowcaster,itm_chewbacca_ryyk_blade],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_11","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_12","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_13","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_princess_leia_outfit,itm_princess_leia_blaster,itm_luke_skywalker_outfit,itm_luke_skywalker_lightsaber,itm_anakin_skywalker_lightsaber],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_14","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_rancor_keeper_armor,itm_dengar_armor,itm_dengar_helmet,itm_dengar_boots,itm_dengar_gloves,itm_weequay_vibro_axe,itm_obi_wan_lightsaber],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_15","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_16","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_darth_vader_lightsaber,itm_darth_vader_helmet,itm_darth_vader_armor],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_17","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_18","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_19","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_20","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_21","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_22","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_23","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_24","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_25","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_26","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_box_mainplanet_27","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
  
# These are used as arrays in the scripts.
["temp_array_a","temp_array_a","temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["temp_array_b","temp_array_b","temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["temp_array_c","temp_array_c","temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

["stack_selection_amounts","stack_selection_amounts","stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["stack_selection_ids","stack_selection_ids","stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["notification_menu_types","notification_menu_types","notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var1","notification_menu_var1","notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var2","notification_menu_var2","notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["banner_background_color_array","banner_background_color_array","banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

#SW BSG integration
["viper_a","viper_a","viper_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_b","viper_c","viper_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_c","viper_b","viper_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_d","viper_d","viper_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_e","viper_e","viper_e",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_f","viper_f","viper_f",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_g","viper_g","viper_g",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_h","viper_h","viper_h",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_end","viper_end","viper_end",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

["cylon_a","cylon_a","cylon_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_b","cylon_c","cylon_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_c","cylon_b","cylon_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_d","cylon_d","cylon_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_e","cylon_e","cylon_e",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_f","cylon_f","cylon_f",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_g","cylon_g","cylon_g",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_h","cylon_h","cylon_h",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_end","cylon_end","cylon_end",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],  
  
##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_laser_bolts_green,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_ee3,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  

["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["tax_rebel","Rebel Colonist","Rebel Colonist",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners, [itm_q2,itm_ddc_defender,itm_dl44a,itm_laser_bolts_orange_pistol,itm_laser_bolts_yellow_pistol,itm_cleaver,itm_durasteel_staff,itm_quarter_staff,itm_vibro_blade2,itm_vibro_blade3,itm_club], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["trainee_peasant","Colonist","Colonists",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners, [itm_q2,itm_ddc_defender,itm_dl44a,itm_laser_bolts_orange_pistol,itm_laser_bolts_yellow_pistol,itm_cleaver,itm_durasteel_staff,itm_quarter_staff,itm_vibro_blade2,itm_vibro_blade3,itm_club], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners, [itm_vibro_sword3_gold,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet], def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,mandalorian_face1, mandalorian_face2],
["spy","Ordinary Colonist","Ordinary Colonists", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral, [itm_vibro_sword3_gold,itm_laser_bolts_orange_pistol,itm_dl44a,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet], def_attrib|agi_11|level(20),wp(130),knows_common,mandalorian_face1, mandalorian_face2],
["spy_partner","Unremarkable Colonist","Unremarkable Colonists", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral, [itm_vibro_sword3_gold,itm_laser_bolts_orange_pistol,itm_dl44a,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet], def_attrib|agi_11|level(10),wp(130),knows_common,mandalorian_face1, mandalorian_face2],
["bounty_target_1a","CIS Officer","CIS Officers",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_black_gloves,itm_vibro_sword3_gold,itm_energy_shield_yellow_small,itm_laser_bolts_yellow_rifle,itm_a295], def_attrib_3|level(26),wp(180),starwars_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["bounty_target_1b","CIS Officer","CIS Officers",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_black_gloves,itm_vibro_sword3_gold,itm_energy_shield_yellow_small,itm_laser_bolts_yellow_rifle,itm_a295], def_attrib_3|level(26),wp(180),starwars_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["bounty_target_2a","Farmer","Farmers",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_vibro_blade1,itm_q2,itm_ddc_defender,itm_laser_bolts_yellow_pistol,itm_leather_gloves], def_attrib_2|level(20),wp(150),starwars_skills_2 ,sw_man_face_1, sw_man_face_2],
["bounty_target_2b","Farmer","Farmers",tf_twilek|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_vibro_blade1,itm_q2,itm_ddc_defender,itm_laser_bolts_yellow_pistol,itm_leather_gloves], def_attrib_2|level(20),wp(150),starwars_skills_2 ,twilek_face1, twilek_face2],
["bounty_target_3a","Target","Targets",tf_bothan|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_vibro_sword3_red,itm_laser_bolts_green_rifle,itm_bothan_bola_carabine,itm_energy_shield_green_medium], def_attrib_4|level(30),wp(220),starwars_skills_4, bothan_face1, bothan_face2],
["bounty_target_3b","Target","Targets",tf_gamorrean|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_durasteel_shield_small,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_throwing_axes], def_attrib_4|level(30),wp(220),starwars_skills_4, gamorrean_face1, gamorrean_face2],
["bounty_target_3c","Target","Targets",tf_chiss|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_vibro_sword3_gold,itm_energy_shield_red_medium,itm_laser_bolts_red_rifle,itm_a295], def_attrib_4|level(30),wp(220),starwars_skills_4, chiss_face1, chiss_face2],
["bounty_target_3d","Target","Targets",tf_moncal|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_a295,itm_laser_bolts_green_rifle,itm_vibro_sword3_gold,itm_energy_shield_green_medium], def_attrib_4|level(30),wp(220),starwars_skills_4, moncal_face1, moncal_face1],
["bounty_target_4a","Pirate","Pirates",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_laser_bolts_yellow_rifle,itm_a295,itm_vibro_sword3_gold,itm_westar_shield,itm_energy_shield_yellow_small], def_attrib_3|level(26),wp(180),starwars_skills_3, mandalorian_face1, mandalorian_face2],
["bounty_target_4b","Pirate","Pirates",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_laser_bolts_yellow_rifle,itm_a295,itm_vibro_sword3_gold,itm_westar_shield,itm_energy_shield_yellow_small], def_attrib_3|level(26),wp(180),starwars_skills_3, sw_rebel_face_1, sw_rebel_face_2],
["bounty_target_5a","Bountyhunter","Bountyhunters",tf_randomize_face|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_mand_arm_dummy,itm_mand_helm_dummy,itm_transparent_feet,itm_grey_gloves,itm_vibro_sword3_gold,itm_laser_bolts_red_rifle,itm_mandalorian_heavy_blaster,itm_westar_shield], def_attrib_4|level(30),wp(220),starwars_skills_4, mandalorian_face1, mandalorian_face2],
["bounty_target_5b","Bountyhunter","Bountyhunters",tf_trandoshan|tf_guarantee_all_armor|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_feet,itm_transparent_hands,itm_trandoshan_fullbody_1,itm_trandoshan_fullbody_2,itm_trandoshan_blade,itm_laser_bolts_orange_rifle,itm_trandoshan_acp_array_gun,itm_energy_shield_yellow_medium,itm_westar_shield], def_attrib_4|level(30),wp(220),starwars_skills_4, trandoshan_face1, trandoshan_face2],
["bounty_target_5c","Bountyhunter","Bountyhunters",tf_rodian|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_black_gloves,itm_vibro_sword3_gold,itm_laser_bolts_orange_rifle,itm_a295,itm_transparent_helmet_armor,itm_energy_shield_green_medium,itm_westar_shield], def_attrib_4|level(30),wp(220),starwars_skills_4, rodian_face1, rodian_face2],
["bounty_target_6a","Smuggler","Smugglers",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_vibro_blade1,itm_dl44a,itm_laser_bolts_green_pistol,itm_westar_shield,itm_energy_shield_yellow_small,itm_transparent_helmet_armor], def_attrib_3|level(26),wp(180),starwars_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["bounty_target_6b","Smuggler","Smugglers",tf_wookiee|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_feet,itm_transparent_hands,itm_wookiee_fullbody,itm_ryyk_blade,itm_ryyk_blade_chieftain,itm_wookiee_shield_small,itm_wookiee_bowcaster,itm_laser_bolts_green_rifle], def_attrib|str_24|agi_25|level(26),wp(180), def_attrib_3|level(26),wp(180),starwars_skills_3, wookiee_face1, wookiee_face2],
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [],
##   def_attrib|agi_11|level(10),wp(130),knows_common,sw_man_face_1, sw_man_face_2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [],
##   def_attrib|agi_11|level(10),wp(130),knows_common,sw_man_face_1, sw_man_face_2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [],
##   def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [],
##   def_attrib|level(3),wp(45),knows_common,sw_woman_face_1,sw_woman_face_2],


#SW - modified quick_battle_6_player which is then used in the Quick Battle (this is also bounty_targets_end)
["quick_battle_player", "Player", "Player", tf_hero, 0, reserved,  fac_player_faction, 
  [
    itm_transparent_helmet,
    #itm_transparent_feet,
    #itm_ind_clothes_hutttuniccape_red,
    #itm_quick_battle_armor,
    itm_sith_clothes_robes_skirt,
    itm_anakin_head,
    itm_leather_gloves,
    itm_lightsaber_blue,
    itm_wpn_blaster_dc17m_auto, 
    itm_stun_beam_rifle,
    #itm_energy_shield_yellow_medium
  ],    knight_attrib_5,wp(250),starwars_knight_skills_5, sw_player_face],
["quick_battle_player_mounted", "Player", "Player", tf_hero, 0, reserved,  fac_player_faction, [itm_transparent_helmet,itm_quick_battle_armor, itm_leather_gloves, itm_lightsaber_yellow, itm_a280,  itm_stun_beam_rifle, itm_energy_shield_yellow_medium, itm_practice_speeder],knight_attrib_5,wp(250),starwars_knight_skills_5, sw_player_face],
["quick_battle_farmer","Farmer","Farmers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
    [
      itm_baton,
      itm_baton,
      itm_pipe1,
      itm_pipe2,
      itm_melee_punch,
      itm_melee_punch,
      itm_vibro_blade1,
      itm_vibro_blade2,
      itm_q2,
      itm_q2,
      itm_dl44a,
      itm_ddc_defender,
      itm_dl44a,
      itm_laser_bolts_yellow_pistol,
      itm_leather_gloves,
    itm_ind_clothes_outfitvest_red,
    itm_ind_clothes_outfitvest_green,
    itm_ind_clothes_outfsmuggler_red,
    itm_ind_clothes_outfsmuggler_green,
    itm_ind_clothes_outfsmuggleralter1_red,
    itm_ind_clothes_outfsmuggleralter1_green,
    itm_ind_clothes_outfsmuggleralter2_red,
    itm_ind_clothes_outfsmuggleralter2_green,
    itm_ind_clothes_hutttunic_red,
    itm_ind_clothes_hutttunic_grey,
    itm_ind_clothes_hutttunic_brown,
    itm_ind_clothes_hutttuniccape_red,
    itm_ind_clothes_hutttuniccape_grey,
    itm_ind_clothes_hutttuniccape_brown,
    itm_ind_clothes_securityguarda1,
    itm_ind_clothes_securityguarda2,
    itm_ind_clothes_securityguarda3,
    itm_ind_clothes_securityguarda4,
    itm_ind_clothes_securityguarda5
     ],
   def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],

# START OF CUSTOM BATTLE TROOPS  
#########################################
# Custom Battle Troops
#########################################

["custom_battle_fac_store","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_1_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_2_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_3_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_4_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_5_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_6_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_spawn_store","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],   

# END OF CUSTOM BATTLE TROOPS

#Player history array
["log_array_entry_type",            "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_entry_time",            "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_actor",                 "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_center_object",         "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_center_object_lord",    "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_center_object_faction", "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_troop_object",          "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_troop_object_faction",  "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_faction_object",        "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],

#Highlander begin--------------------------------------
  #particle arrays
  ["pjct_active",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_x",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_y",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_z",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_x_velocity",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_y_velocity",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_z_velocity",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_emit_time",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],

  ["pjct_source_agent",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_damage",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_bounce_effect",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explosive",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explosion_countdown",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explosion_area",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explosion_damage",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explode_on_ground_hit",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_particle_system",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_particle_system_magnitude",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],

  ["pjct_attach_scene_prop",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],

  ["pjct_check_collision",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  #instance arrays
  ["instance_attached_to",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
#Highlander end--------------------------------------

##@> Swyter's Gate.sys array
["gate_sys_array","Mr Gate Array[Internal]","Mr Gate Array[Internal]",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["gate_sys_counter","Mr Gate Array[Internal]","Mr Gate Array[Internal]",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],

["gate_sys_array2","Mr Gate Array[Internal]","Mr Gate Array[Internal]",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["gate_sys_counter2","Mr Gate Array[Internal]","Mr Gate Array[Internal]",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],


##@> new droid culture troops for the player faction
["droid_messenger","Droid Messenger","Droid Messengers", # oom_series_pilot
  tf_battledroid|tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
  0,0,fac_neutral,
  [itm_horus_winged_cruiser, itm_vibro_sword3_blue, itm_droid_parts, itm_transparent_droid_head, itm_transparent_droid_hands, itm_transparent_droid_feet, itm_oomseries_pilot_body, itm_e5, itm_laser_bolts_red_rifle],
  def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4, droid_face1, droid_face2
],
["droid_deserter","Droid Deserter","Droid Deserters", # b1series
  tf_battledroid|tf_guarantee_boots|tf_guarantee_all_armor,
  0,0,fac_neutral,
  [itm_droid_parts, itm_battle_droid_attack, itm_transparent_droid_head, itm_transparent_droid_hands, itm_transparent_droid_feet, itm_e5, itm_laser_bolts_red_rifle],
  def_attrib_2|level(16),wp(80),starwars_skills_2, droid_face1, droid_face2
],



#########################################################################################################################################
#########################################################################################################################################

#New Troops from CWC

["cloaked_magna","Magnaguard","Magnaguards",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
    [
    itm_droid_parts,
    itm_droid_parts,
    itm_droid_parts,
    itm_magna_head_cloak,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    itm_magnapaint,
    itm_e5,
    itm_dlt19,
    itm_laser_bolts_red_rifle,
    itm_laser_bolts_red_rifle,
    itm_electro_staff_magna,
  ],
  str_20|agi_20|int_12|cha_14|level(37),
  wp(300)|wp_crossbow(170),
  starwars_skills_melee_4,
  sw_rebel_face_1, sw_rebel_face_2
],

["aseries_assassin","A-series Polux Assassin Droid","A-series Polux Assassin Droids",
  tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  no_scene,reserved,fac_neutral,
    [
    itm_droid_parts,
    itm_droid_parts,
    itm_droid_parts,
    itm_transparent_head,
    itm_transparent_droid_hands,
    itm_transparent_droid_feet,   
    #itm_aseries,
    itm_wrist_blaster,
    itm_laser_bolts_red_pistol,
    itm_laser_bolts_red_pistol,
    itm_vibro_knuckler,
  ],
  str_20|agi_18|int_12|cha_14|level(24),
  wp(200)|wp_crossbow(240)|wp_firearm(240),
  starwars_skills_melee_2,
  sw_rebel_face_1, sw_rebel_face_2
],

# ["aseries_assassin2","A-series Polux Assassin Droid","A-series Polux Assassin Droids",
#   tf_battledroid|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
#   no_scene,reserved,fac_neutral,
#     [
#     itm_droid_parts,
#     itm_droid_parts,
#     itm_droid_parts,
#     itm_transparent_head,
#     itm_transparent_droid_hands,
#     itm_transparent_droid_feet,   
#     itm_aseries,
#     itm_wrist_blaster,
#     itm_laser_bolts_red_pistol,
#     itm_laser_bolts_red_pistol,
#     itm_vibro_knuckler,
#   ],
#   str_18|agi_14|int_12|cha_10|level(24),
#   wp(150)|wp_crossbow(170),
#   starwars_skills_4,
#   sw_rebel_face_1, sw_rebel_face_2
# ],


["442nd_siege_trooper","442nd_Siege Clone Trooper","442nd_Siege Clone Trooper",
  tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_wolf,
    itm_clone_trooper_gloves_green,
    itm_phase_ii_clonepack,
    itm_phase_ii_helmet_wolf,
    itm_vibro_blade1,
    itm_vibro_blade1,
    itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a,
    itm_dc17sa,
    itm_dc17_shield,
    itm_energy_shield_oval,
  
  ],
  str_18|agi_16|int_15|cha_12|level(24),
  wp(220)|wp_crossbow(270)|wp_archery(0),
  starwars_skills_3,
  sw_imperial_face_1, sw_imperial_face_2
],
["442nd_elite_trooper","442nd Elite Clone Trooper","442nd Elite Clone Trooper",
  tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_442,
    itm_clone_trooper_gloves_green,
    itm_phase_ii_clonepack,
    itm_phase_ii_clonepack,
    itm_phase_ii_arc_kama,
    #itm_phase_ii_arc_equipment_appo,
    itm_phase_ii_helmet_442,
    itm_vibro_blade1,
    itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a_hip,
    itm_dc17sa,
    itm_energy_shield_oval,
  
  ],
  str_20|agi_19|int_18|cha_15|level(28),
  wp(240)|wp_crossbow(285)|wp_archery(0),
  starwars_skills_4,
  sw_imperial_face_1, sw_imperial_face_2
],

["arf_trooper","ARF Trooper","ARF Trooper",
  tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged,#|tf_guarantee_horse,
  no_scene,reserved,fac_neutral,
  [
    itm_phase_ii_armor_worn,
    itm_black_gloves,
    itm_phase_ii_clonepack,
    #itm_phase_ii_arc_equipment_appo,
    itm_phase_ii_arc_kama,
    itm_phase_ii_helmet_442,
    itm_vibro_blade1,
    itm_baton2,
    itm_laser_bolts_blue_rifle,
    itm_laser_bolts_blue_rifle,
    itm_dc15s,
    itm_dc15a_hip,
    itm_dc17sa,
    itm_energy_shield_oval,
    itm_speeder_shadow,
  
  ],
  str_18|agi_18|int_16|cha_15|level(28),
  wp(245)|wp_crossbow(285)|wp_archery(0),
  starwars_skills_mounted_3,
  sw_imperial_face_1, sw_imperial_face_2
],





###########################################################################################

## Mando - Legion specific Clones  ##

["501stl_ct","501st_Clone_Trooper","501st_Clone_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,
    itm_baton,itm_vibro_knuckler,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_18|int_14|cha_12|level(20),wp(175)|wp_archery(200),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_3|knows_inventory_management_2|knows_leadership_3|knows_shield_3|knows_trainer_3|knows_athletics_5|knows_tracking_1|knows_tactics_3|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["501stl_vet","501st_Clone_Veteran","501st_Clone_Veterans", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    itm_phase_ii_clonepack,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_18|agi_20|int_16|cha_14|level(25),wp(225)|wp_archery(0)|wp_crossbow(250),
 knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_4|knows_trainer_5|knows_athletics_6|knows_tracking_1|knows_tactics_5|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["501stl_cc","501st_Clone_Captain","501st_Clone_Captains", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_20|agi_18|int_20|cha_20|level(30),wp(250)|wp_archery(0)|wp_crossbow(300),
 knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_7|knows_inventory_management_2|knows_leadership_7|knows_shield_5|knows_trainer_7|knows_athletics_6|knows_tracking_1|knows_tactics_7|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["501stl_cs","501st_Clone_Sniper","501st_Clone_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
  str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
  knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["501stl_so","501st_SpecialOps_Trooper","501st_Clone_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["501stl_barc","501st_BARC_Trooper","501st_BARC_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    itm_phase_ii_helmet_501,
    itm_baton,itm_melee_punch,itm_vibro_blade1,
    itm_disruptor_ammo_rifle,itm_laser_bolts_blue_rifle,
    itm_dc15s,itm_dc15a_hip,itm_dlt20a,
    itm_speeder_dagger,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_6|knows_inventory_management_4|knows_leadership_7|knows_shield_2|knows_trainer_6|knows_athletics_6|knows_tracking_3|knows_tactics_6|knows_power_draw_6|knows_horse_archery_10,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["clancer","Clone_Lancer","Clone_Lancers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    itm_phase_ii_helmet_501,
    itm_baton,itm_melee_punch,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
    itm_dc15s,itm_dc15a_hip,itm_dlt20a,
    itm_speeder_dagger,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4|knows_horse_archery_10,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["501stl_sp","501st_Clone_Specialist","501st_Clone_Specialists", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["501stl_st","501st_Support_Trooper","501st_Support_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["501stl_fm","501st_Field_Medic","501st_Field_Medics", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["501stl_as","501st_Advanced_Support","501st_Advanced_Support", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],


["7thsc_ct","7th_SkyCorps_Trooper","7th_Sky_Corps_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_212,
    itm_clone_trooper_gloves_yellow,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,
    itm_baton,itm_vibro_knuckler,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],str_16|agi_18|int_14|cha_12|level(20),wp(175)|wp_archery(0)|wp_crossbow(200),
 knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_weapon_master_3|knows_inventory_management_2|knows_leadership_3|knows_shield_3|knows_trainer_3|knows_athletics_6|knows_tracking_1|knows_tactics_3|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["7thsc_vet","7th_SkyCorps_Veteran","7th_Sky_Corps_Veterans", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_baton,itm_vibro_knuckler,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],str_18|agi_20|int_16|cha_14|level(25),wp(225)|wp_archery(0)|wp_crossbow(250),
 knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_4|knows_trainer_5|knows_athletics_6|knows_tracking_1|knows_tactics_5|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["7thsc_pt","7th_SkyCorps_Para_Trooper","7th_Sky_Corps_Para_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["7thsc_et","7th_SkyCorps_Elite","7th_Sky_Corps_Elites", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["7thsc_ss","7th_SkyCorps_Sharp_Shooter","7th_SkyCorps_Sharp_Shooters", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["7thsc_cc","7th_SkyCorps_Captain","7th_SkyCorps_Captains", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_212,
    itm_phase_ii_armor_212,
    itm_phase_ii_armor_cody,
    itm_clone_trooper_gloves_yellow,
    #itm_phase_ii_arc_equipment_cody,
    #itm_phase_ii_arc_equipment_appo,
    itm_phase_ii_arc_kama,
    itm_phase_ii_helmet_212,
    #itm_phase_ii_helmet_para_blue,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_20|agi_20|int_20|cha_20|level(30),wp(250)|wp_archery(0)|wp_crossbow(300),
 knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_7|knows_inventory_management_2|knows_leadership_7|knows_shield_5|knows_trainer_7|knows_athletics_6|knows_tracking_1|knows_tactics_7|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["7th_cg","7th_SkyCorps_Gunner","7th_SkyCorps_Guners", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["cshadow","Clone_Shadow_Trooper","Clone_Shadow_Troopers", tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_rep_arm_phase2_black,
    itm_black_gloves,
    itm_rep_helm_phase2_black,
    itm_dc15s,
  itm_dc15a,
    itm_baton2,
    itm_laser_bolts_blue_rifle,
  itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(32),wp(335)|wp_archery(335),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["7th_st","7th_SkyCorps_Support_Trooper","7th_SkyCorps_Support_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["7th_fm","7th_SkyCorps_Field_Medic","7th_SkyCorps_Field_Medics", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["7th_as","7th_SkyCorps_Advanced_Support","7th_SkyCorps_Advanced_Supports", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],


["gm_ct","Galactic_Marine","Galactic_Marines", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_black_gloves,
    itm_rep_arm_galacticmarine,
    itm_phase_ii_clonepack,
    itm_dc15a,itm_dc15a_hip,
    itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_18|int_14|cha_12|level(20),wp(175)|wp_archery(0)|wp_crossbow(200),
 knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_weapon_master_3|knows_inventory_management_2|knows_leadership_3|knows_shield_3|knows_trainer_3|knows_athletics_5|knows_tracking_1|knows_tactics_3|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["gm_vet","Veteran Galactic Marine","Veteran Galactic Marines", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_black_gloves,
    itm_rep_arm_galacticmarine,
    itm_phase_ii_clonepack,
    itm_dc15a_hip,itm_dc15a,itm_dlt19,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_18|agi_20|int_16|cha_16|level(25),wp(225)|wp_archery(0)|wp_crossbow(250),
 knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_4|knows_trainer_5|knows_athletics_6|knows_tracking_1|knows_tactics_5|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["gm_cs","21st_NovaCorps_Sniper","21st_NovaCorps_Snipers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["gm_arc","21st_NovaCorps_ARC","21st_NovaCorps_ARC", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["gm_ph","21st_NovaCorpsAerial_Trooper","21st_Clone_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["gm_cc","Galactic_Marine_Captain","Galactic_Marine_Captains", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_black_gloves,
    itm_rep_arm_galacticmarine,
    itm_phase_ii_clonepack,
    itm_phase_ii_clonepack,
    itm_dc15a_hip,itm_dc15a,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_20|agi_20|int_20|cha_20|level(30),wp(250)|wp_archery(0)|wp_crossbow(300),
 knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_7|knows_inventory_management_2|knows_leadership_7|knows_shield_5|knows_trainer_7|knows_athletics_6|knows_tracking_1|knows_tactics_7|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["gm_st","21st_NovaCorps_Support_Trooper","21st_NovaCorps_Support_Troopes", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["gm_fm","21st_NovaCorps_Field_Medic","21st_NovaCorps_Field_Medics", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["gm_as","21st_NovaCorps_Advanced_Support","21st_NovaCorps_Advanced_Supports", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["cov_ops","Covert_Ops_Clone_Trooper","Covert_Ops_Clone_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],


["442ndsb_ct","442nd_Siege_Clone_Trooper","442nd_Siege_Clone_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_442,
    itm_clone_trooper_gloves_green,
    itm_phase_ii_helmet_442,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,
    itm_baton,itm_vibro_knuckler,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_18|int_14|cha_12|level(20),wp(175)|wp_archery(0)|wp_crossbow(200),
 knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_weapon_master_3|knows_inventory_management_2|knows_leadership_3|knows_shield_4|knows_trainer_3|knows_athletics_5|knows_tracking_1|knows_tactics_3|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["442ndsb_vet","442nd_Siege_Clone_Veteran","442nd_Siege_Clone_Veterans", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_442,
    itm_clone_trooper_gloves_green,
    itm_phase_ii_clonepack,
    itm_phase_ii_helmet_442,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_18|agi_20|int_16|cha_16|level(25),wp(225)|wp_archery(0)|wp_crossbow(250),
 knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_4|knows_trainer_5|knows_athletics_6|knows_tracking_1|knows_tactics_5|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["442ndsb_ce","442nd_Siege_Clone_Elite","442nd_Siege_Clone_Elites", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["442ndsb_cc","442nd_Siege_Clone_Captain","442nd_Siege_Clone_Captains", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_442,
    itm_clone_trooper_gloves_green,
    #itm_phase_ii_arc_equipment_appo,
    itm_phase_ii_arc_kama,
    #itm_phase_ii_arc_equipment_cody,
    itm_phase_ii_sniper_gear,
    itm_phase_ii_helmet_442,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_20|agi_20|int_20|cha_20|level(30),wp(250)|wp_archery(0)|wp_crossbow(300),
 knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_7|knows_inventory_management_2|knows_leadership_7|knows_shield_5|knows_trainer_7|knows_athletics_6|knows_tracking_1|knows_tactics_7|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["442ndsb_ss","442nd_Siege_Sharp_Shooter","442nd_Siege_Sharp_Shooter", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

#["442ndsb_vet","442nd_Siege_Clone_Elite","442nd_Siege_Clone_Elites", tf_hero|tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[], str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4, 0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],
######################
["442ndsb_vg","442nd_Siege_Vanguard","442nd_Siege_Vanguards", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["442ndsb_cb","442nd_Siege_Clone_Biker","442nd_Siege_Clone_Biker",  tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["cstrooper","Clone_Shock_Trooper","Shock_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_shock,
    itm_clone_trooper_gloves_red,
    itm_phase_ii_helmet_shock,
    itm_dc15s,
    itm_baton,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_18|int_14|cha_12|level(20),wp(175)|wp_archery(0)|wp_crossbow(200),
 knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_weapon_master_3|knows_inventory_management_2|knows_leadership_3|knows_shield_4|knows_trainer_3|knows_athletics_5|knows_tracking_1|knows_tactics_3|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],
["cstguard","Shock_Trooper_Guard","Shock_Trooper_Guards", tf_tusken|tf_guarantee_shield|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_shock,
    itm_clone_trooper_gloves_red,
    itm_phase_ii_helmet_shock,
    itm_dc15s,itm_dc17sa,
    itm_republic_shield,
    itm_baton2,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_18|agi_20|int_16|cha_16|level(25),wp(225)|wp_archery(0)|wp_crossbow(250),
 knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_6|knows_trainer_5|knows_athletics_6|knows_tracking_1|knows_tactics_5|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],
["cstcaptain","Shock_Trooper_Captain","Shock_Trooper_Captains", tf_tusken|tf_guarantee_shield|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_shock,
    #itm_phase_ii_armor_thorn,
    itm_clone_trooper_gloves_red,
    #itm_phase_ii_arc_equipment_thorn,
    itm_phase_ii_helmet_shock,
    itm_dc15s,itm_dc15a_hip,itm_dlt20a,itm_dc17sa,
    itm_dc17_shield,
    itm_republic_shield,
    itm_baton2,
    itm_laser_bolts_blue_pistol,itm_laser_bolts_blue_pistol,
  ],
 str_20|agi_20|int_20|cha_20|level(30),wp(250)|wp_archery(0)|wp_crossbow(300),
 knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_7|knows_inventory_management_2|knows_leadership_7|knows_shield_6|knows_trainer_7|knows_athletics_6|knows_tracking_1|knows_tactics_7|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],
["cstheavy","Heavy_Shock_Trooper","Shock_Trooper_Captains", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],
["cstbiker","Biker_Shock_Trooper","Biker_Shock_Trooper", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],
#["cstord","Biker_Shock_Trooper","Biker_Shock_Trooper", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[], str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4, 0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

#["cstord","Biker_Shock_Trooper","Biker_Shock_Trooper", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[], str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4, 0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],



["104thb_ct","104th_Battalion_Trooper","104th_Battalion_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_wolf,
    itm_phase_ii_armor_worn,
    itm_black_gloves,
    itm_phase_ii_helmet_wolf,
    itm_phase_ii_helmet_worn,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,
    itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_18|int_14|cha_12|level(20),wp(175)|wp_archery(0)|wp_crossbow(200),
 knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_weapon_master_3|knows_inventory_management_2|knows_leadership_3|knows_shield_5|knows_trainer_3|knows_athletics_5|knows_tracking_1|knows_tactics_3|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["104thb_vet","104th_Battalion_Veteran","104th_Battalion_Veterans", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_wolf,
    itm_black_gloves,
    itm_phase_ii_clonepack,
    itm_phase_ii_helmet_wolf,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_18|agi_20|int_16|cha_16|level(25),wp(225)|wp_archery(0)|wp_crossbow(250),
 knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_5|knows_trainer_5|knows_athletics_6|knows_tracking_1|knows_tactics_5|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["104thb_ct","104th_Battalion_Recon_Trooper","104th_Battalion_Recon_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_wolf,
    itm_black_gloves,
    #itm_phase_ii_arc_equipment_wolffe,
    itm_phase_ii_helmet_wolf,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_20|agi_20|int_20|cha_20|level(30),wp(275)|wp_archery(0)|wp_crossbow(300),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["104thb_at","104th_Battalion_Assault_Trooper","104th_Battalion_Recon_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["wolf_ect","Wolfpack_Elite_Clone_Trooper","Wolfpack_Elite_Clone_Troopers", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_501,
    itm_phase_ii_armor_rex,
    itm_phase_ii_armor_501,
    itm_clone_trooper_gloves_blue,
    #itm_phase_ii_arc_equipment_appo,
    #itm_phase_ii_arc_equipment_rex,
    itm_phase_ii_helmet_501,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),
 knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

["wolf_cc","Wolfpack_Clone_Captain","Wolfpack_Clone_Captains", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [ itm_phase_ii_armor_wolf,
    itm_black_gloves,
    #itm_phase_ii_arc_equipment_wolffe,
    itm_phase_ii_helmet_wolf,
    itm_dc15s,itm_dc15a,itm_dc15a_hip,itm_dlt20a,itm_dlt19,itm_dc17sa,
    itm_dc17_shield,
    itm_baton2,itm_vibro_blade1,
    itm_laser_bolts_blue_rifle,itm_laser_bolts_blue_rifle,
  ],
 str_20|agi_20|int_20|cha_20|level(30),wp(250)|wp_archery(0)|wp_crossbow(300),
 knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_7|knows_inventory_management_2|knows_leadership_7|knows_shield_5|knows_trainer_7|knows_athletics_6|knows_tracking_1|knows_tactics_7|knows_power_draw_4,
  0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],
#["wolf_cc","Wolfpack_Clone_Captain","Wolfpack_Clone_Captains", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[], str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4, 0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],



#["cstbikerl","Biker_Shock_Trooper","Biker_Shock_Trooper", tf_tusken|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[], str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4, 0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],

######################

######################

######################


]



#Troop upgrade declarations
#TAS Troop Upgrade Paths:

## Human mercs:
upgrade(troops,"farmer", "civilian")
upgrade(troops,"townsman","civilian")
upgrade2(troops,"civilian","militia","thug")
upgrade2(troops,"militia","security_guard","soldier")
upgrade(troops,"security_guard", "bodyguard")
upgrade2(troops,"soldier","commando","pilot")
upgrade2(troops,"thug","goon","biker")
upgrade(troops,"goon", "assassin")
upgrade(troops,"biker", "biker_scout")

## Force_sensitive:
upgrade2(troops,"force_sensitive_recruit","sith_hopeful","jedi_hopeful")
### TAS Sith:
upgrade(troops,"jedi_hopeful","sith_acolyte")
upgrade(troops,"sith_acolyte","sith_apprentice")
upgrade(troops,"sith_apprentice","sith_knight")
upgrade(troops,"sith_knight","sith_marauder")
upgrade(troops,"sith_marauder","sith_master")
upgrade(troops,"sith_master","sith_lord")
### TAS Jedi:
upgrade(troops,"sith_hopeful","jedi_initiate")
upgrade(troops,"jedi_initiate","jedi_padawan")
upgrade(troops,"jedi_padawan","jedi_guardian")
upgrade(troops,"jedi_guardian","jedi_consular")
upgrade(troops,"jedi_consular","jedi_warrior_master")
upgrade(troops,"jedi_warrior_master","jedi_sage_master")
upgrade(troops,"jedi_sage_master","jedi_councilor")
upgrade(troops,"jedi_councilor","jedi_grand_master")





#TAS Republic Troop Tree
#Tier 1
upgrade(troops,"imperial_recruit","imperial_navy_trooper") #Imperial Recruit (Republic Clone Cadet) -> Imperial Navy Trooper (Clone Trooper)
#Tier 2
upgrade2(troops,"imperial_navy_trooper","imperial_army_trooper","imperial_gunner")  #Imperial Navy Trooper (Clone Trooper) -> Imperial Army trooper (Veteran Clone Trooper) & Imperial Gunner(Republic Shocktrooper)
#Tier 3
upgrade2(troops,"imperial_army_trooper","imperial_stormtrooper","imperial_scout_trooper") #Veteran CT -> Battle-Hardened CT & Clone Marksman
upgrade2(troops,"imperial_gunner","clone_trooper_3","arc_trooper_3") #Shocktrooper -> Riot trooper & Clone Pilot
#Tier 4
upgrade2(troops,"imperial_stormtrooper","imperial_stormtrooper_veteran","imperial_pilot") #Battle-Hardened CT -> Elite CT & 212th CT
upgrade(troops,"arc_trooper_3","imperial_pilot_veteran") #Clone Pilot -> Clone Lancer
upgrade2(troops,"imperial_scout_trooper","republic_clone_clonesniper","imperial_scout_trooper_sniper") #Clone Marksman -> Clone Sniper & Clone Commando
#Tier 5
upgrade2(troops,"imperial_pilot","imperial_gunner_veteran","imperial_scout_trooper_veteran") #212th CT -> 212th CT Elite & Wolfpack CT
upgrade(troops,"republic_clone_clonesniper","cshadow") #Clone Sniper -> Clone Shadow
upgrade2(troops,"imperial_scout_trooper_sniper","incinerator_trooper","imperial_stormtrooper_officer") #Clone Commando -> Senate Commando & Veteran Clone Commando
upgrade(troops,"imperial_stormtrooper_veteran","novatrooper") #Elite CT -> 501st CT
upgrade(troops,"clone_trooper_3","clone_trooper_4") #Riot Trooper -> GalMarine
#Tier 6
upgrade(troops,"imperial_gunner_veteran","clone_trooper_2") #212th CT Elite -> 212th ARC
upgrade(troops,"imperial_scout_trooper_veteran","imperial_scout_trooper_captain") #Wolfpack CT -> Wolfpack CT Elite
upgrade(troops,"novatrooper","imperial_scout_trooper_marksman") #501st CT -> 501st CT Elite
#upgrade(troops,"republic_clone_442clone","republic_clone_442cloneveteran") #442nd CT -> 442nd CT Elite
#Tier 7
upgrade(troops,"imperial_scout_trooper_captain","arc_trooper_2") #Wolfpack CT Elite -> Wolfpack ARC
upgrade(troops,"imperial_scout_trooper_marksman","clone_trooper_1") #501st CT Elite -> 501st ARC
#upgrade(troops,"republic_clone_442cloneveteran","republic_clone_442clonearc") #422nd CT elite -> 422nd ARC

#Republic CC - imperial_recruit
#CT - imperial_navy_trooper
#CT Veteran - imperial_army_trooper
#Shocktrooper - imperial_gunner
#Riot - clone_trooper_3
#Clone Pilot - arc_trooper_3
#Clone Lancer - imperial_pilot_veteran
#Galactic Marine - clone_trooper_4
#Clone Marksman - imperial_scout_trooper
#Clone Sniper - republic_clone_clonesniper
#Clone Commando - imperial_scout_trooper_sniper
#Clone Commando Veteran - imperial_stormtrooper_officer
#Clone Commando Senate - incinerator_trooper
#212th CT - imperial_pilot
#212th CT Elite - imperial_gunner_veteran
#212th ARC -  clone_trooper_2
#Wolfpack CT - imperial_scout_trooper_veteran
#Wolfpack CT Elite - imperial_scout_trooper_captain
#Wolfpack ARC - arc_trooper_2

# upgrade(troops,"imperial_gunner","imperial_gunner_veteran")
# upgrade2(troops,"imperial_army_trooper","imperial_stormtrooper","imperial_scout_trooper")
# upgrade2(troops,"imperial_scout_trooper","imperial_scout_trooper_veteran","imperial_scout_trooper_marksman")
# upgrade(troops,"imperial_scout_trooper_marksman","imperial_scout_trooper_sniper")
# upgrade(troops,"imperial_scout_trooper_veteran","imperial_scout_trooper_captain")

#upgrade tree:
#clone trooper - veterean or scout
##veteran - shock or hardened
#### hardened - 
##scout - biker scout or arf
####biker - lancer or barc
####arf - 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# rebel
# #upgrade2(troops,"rebel_recruit","rebel_cadet","jedi_hopeful")
# upgrade(troops,"rebel_recruit","rebel_cadet")
# upgrade2(troops,"rebel_cadet","rebel_trooper","rebel_scout")
# upgrade2(troops,"rebel_trooper","rebel_vanguard","rebel_pilot")
# upgrade(troops,"rebel_pilot","rebel_pilot_veteran")
# upgrade2(troops,"rebel_vanguard","rebel_heavy_trooper","rebel_honor_guard")
# upgrade2(troops,"rebel_scout","rebel_commando","rebel_marksman")
# upgrade(troops,"rebel_commando","rebel_commando_veteran")
# upgrade(troops,"rebel_marksman","rebel_sniper")
# upgrade(troops,"jedi_hopeful","jedi_initiate")
# upgrade(troops,"jedi_initiate","jedi_padawan")
# upgrade2(troops,"jedi_padawan","jedi_guardian","jedi_consular")
# upgrade(troops,"jedi_guardian","jedi_warrior_master")
# upgrade(troops,"jedi_consular","jedi_sage_master")
# upgrade(troops,"jedi_warrior_master","jedi_councilor")
# upgrade(troops,"jedi_sage_master","jedi_councilor")
# upgrade(troops,"jedi_councilor","jedi_grand_master")

#New CIS troop tree from CWC
upgrade(troops,"rebel_recruit","rebel_cadet")
upgrade2(troops,"rebel_cadet","rebel_trooper","b2series")
upgrade2(troops,"rebel_trooper","b1series_assassin","rebel_pilot")
upgrade(troops,"rebel_pilot","rebel_commando")
upgrade(troops,"rebel_commando","rebel_pilot_veteran")
upgrade(troops,"b1series_assassin","bxseries_commando")
upgrade2(troops,"bxseries_commando","rebel_scout","rebel_heavy_trooper")
upgrade(troops,"rebel_heavy_trooper","rebel_honor_guard")
upgrade(troops,"rebel_honor_guard","cloaked_magna")
upgrade2(troops,"b2series","b2series_enhanced","aseries_assassin")

#hutt
upgrade(troops,"hutt_militia","hutt_mercenary")
upgrade2(troops,"hutt_mercenary","hutt_marksman","hutt_guard")
upgrade(troops,"hutt_marksman","hutt_bounty_hunter")
upgrade(troops,"hutt_bounty_hunter","hutt_commando")
upgrade2(troops,"hutt_guard","hutt_skiff_guard","hutt_palace_guard")
upgrade(troops,"hutt_skiff_guard","hutt_skiff_guard_captain")
upgrade(troops,"hutt_palace_guard","hutt_palace_guard_captain")

#wookiee mercs
upgrade(troops,"wookiee","wookiee_warrior")
upgrade2(troops,"wookiee_warrior","wookiee_marksman","wookiee_berserker")
upgrade(troops,"wookiee_marksman","wookiee_sharpshooter")
upgrade(troops,"wookiee_berserker","bacca_warrior")
#mandalorian mercs
upgrade(troops,"mandalorian","mandalorian_soldier")
upgrade2(troops,"mandalorian_soldier","mandalorian_commando","mandalorian_sniper")
upgrade(troops,"mandalorian_commando","mandalorian_crusader")
upgrade(troops,"mandalorian_sniper","mandalorian_deadeye")
#twilek female
upgrade(troops,"twilek_female1","twilek_female2")
upgrade(troops,"twilek_female2","twilek_female3")
#sullustan male
upgrade(troops,"chiss_1","chiss_2")
upgrade(troops,"chiss_2","chiss_3")
upgrade(troops,"chiss_3","chiss_4")
#sullustan male
upgrade(troops,"sullustan_1","sullustan_2")
upgrade(troops,"sullustan_2","sullustan_3")
upgrade(troops,"sullustan_3","sullustan_4")
#geonosian male
upgrade(troops,"geonosian_1","geonosian_2")
upgrade(troops,"geonosian_2","geonosian_3")
upgrade(troops,"geonosian_3","geonosian_4")
#twilek male
upgrade(troops,"twilek","twilek_warrior")
upgrade(troops,"twilek_warrior","twilek_soldier")
upgrade(troops,"twilek_soldier","twilek_commando")
#rodian
upgrade(troops,"rodian","rodian_warrior")
upgrade(troops,"rodian_warrior","rodian_hunter")
upgrade(troops,"rodian_hunter","rodian_bounty_hunter")
#trandoshan
upgrade(troops,"trandoshan","trandoshan_warrior")
upgrade(troops,"trandoshan_warrior","trandoshan_hunter")
upgrade(troops,"trandoshan_hunter","trandoshan_bounty_hunter")
#mon cal
upgrade(troops,"moncal_1","moncal_2")
upgrade(troops,"moncal_2","moncal_3")
upgrade(troops,"moncal_3","moncal_4")
#bothan
upgrade2(troops,"bothan","bothan_agent","bothan_militia")
upgrade(troops,"bothan_militia","bothan_infantry")
upgrade(troops,"bothan_agent","bothan_spy")
upgrade(troops,"bothan_spy","bothan_infiltrator")
#gamorrean
upgrade(troops,"gamorrean","gamorrean_warrior")
upgrade(troops,"gamorrean_warrior","gamorrean_guard")
upgrade(troops,"gamorrean_guard","gamorrean_palace_guard")
#black sun
upgrade(troops,"black_sun_pirate_1","black_sun_pirate_2")
upgrade(troops,"black_sun_pirate_2","black_sun_pirate_3")
upgrade(troops,"black_sun_pirate_3","black_sun_pirate_4")
#jawa
upgrade(troops,"jawa","jawa_2")
upgrade(troops,"jawa_2","jawa_3")

#SW - tusken upgrade path
upgrade(troops,"tusken_1","tusken_2")

# SW - upgrade doesn't make sense, possible defect?
#upgrade2(troops,"bandit","brigand","mercenary_swordsman")
upgrade(troops,"bandit","brigand")

#droids
#b1series
upgrade(troops,"b1series","b1series_assassin")
upgrade(troops,"b1series_assassin","bxseries_commando")
#oom_series
upgrade2(troops,"oom_series_security","oom_series_marine","oom_series_pilot")
upgrade(troops,"oom_series_marine","oom_series_command")

#SWY B2 series + CB3 Upgrade to Cortosis shield
upgrade(troops,"b2series","b2series_enhanced")

#SWY - Fixed Rancors with new skin and upgrades
upgrade(troops,"rancor","rancor_mutant")


#SW - bountyhunter switched to trandoshan slavers, currently with no upgrade path
#upgrade(troops,"bountyhunter","slave_driver")
#upgrade(troops,"slave_driver","slave_hunter")
#upgrade(troops,"slave_hunter","slave_crusher")
#upgrade(troops,"slave_crusher","slaver_chief")

#upgrade(troops,"blazing_claw_pirate","mercenary_crossbowman")

#upgrade(troops,"refugee","follower_woman")
#upgrade(troops,"peasant_woman","follower_woman")

#upgrade(troops,"follower_woman","hunter_woman")
#upgrade(troops,"hunter_woman","fighter_woman")
#upgrade(troops,"fighter_woman","sword_sister")

#Umbarans
upgrade(troops,"Umbaran_militia","Umbaran_Soldier")
upgrade(troops,"Umbaran_Soldier","Umbaran_officer")

#Nightsisters
upgrade(troops,"Nightsister","Nightsister_assassin")
upgrade(troops,"Nightsister_assassin","Nightsister_reaper")


#upgrade2(troops,"imperial_recruit","imperial_cadet","sith_hopeful")
#upgrade(troops,"imperial_recruit","imperial_cadet")
upgrade2(troops,"501stl_ct","501stl_vet","imperial_army_trooper")
upgrade2(troops,"501stl_vet","501stl_cc","501stl_barc")
upgrade(troops,"501stl_st","501stl_fm")
upgrade(troops,"501stl_fm","501stl_as")
upgrade2(troops,"501stl_sp","501stl_cs","clancer")
#upgrade2(troops,"imperial_scout_trooper","imperial_scout_trooper_veteran","imperial_scout_trooper_marksman")
#upgrade(troops,"imperial_scout_trooper_marksman","imperial_scout_trooper_sniper")
#upgrade(troops,"imperial_scout_trooper_veteran","imperial_scout_trooper_captain")

#upgrade2(troops,"imperial_stormtrooper","imperial_stormtrooper_veteran","imperial_stormtrooper_officer")
#upgrade2(troops,"imperial_stormtrooper_veteran","novatrooper","incinerator_trooper")
#upgrade(troops,"imperial_stormtrooper_officer","imperial_royal_guard")
