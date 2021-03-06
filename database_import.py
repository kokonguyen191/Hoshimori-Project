import csv
import re

from hoshimori.models import *


###########################################################
# Utils

def extract_number(str):
    return re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", str)


def return_number_or_none(str):
    if str.isdigit():
        return str
    else:
        return None


###########################################################
# Student

def character_import_data():
    with open('database\characters.csv') as f:
        reader = csv.reader(f)
        id = 0
        for row in reader:
            if row[0] != 'name':  # ignore header row
                _, created = Student.objects.get_or_create(
                    name=row[0],
                    japanese_name=row[1],
                    unlock=row[2],
                    description=row[3],
                    i_school_year=row[4],
                    birthday=row[5],
                    i_star_sign=row[6],
                    i_blood_type=row[7],
                    extra_activity=row[8],
                    catchphrase_1=row[9],
                    catchphrase_2=row[10],
                    height=return_number_or_none(row[11]),
                    weight=return_number_or_none(row[12]),
                    bust=return_number_or_none(row[13]),
                    waist=return_number_or_none(row[14]),
                    hip=return_number_or_none(row[15]),
                    hobby_1=row[16],
                    hobby_2=row[17],
                    hobby_3=row[18],
                    food_likes=row[19],
                    food_dislikes=row[20],
                    family=row[21],
                    dream=row[22],
                    ideal_1=row[23],
                    ideal_2=row[24],
                    ideal_3=row[25],
                    pastime=row[26],
                    destress=row[27],
                    fav_memory=row[28],
                    fav_phrase=row[29],
                    secret=row[30],
                    CV=row[31],
                    romaji_CV=row[32],
                    image=row[33],
                    full_image=row[34],
                    signature=row[35],
                    phrase_1=row[36],
                    phrase_2=row[37],
                    introduction_1=row[38],
                    introduction_2=row[39],
                    owner_id=1,
                    id=row[41],
                    mini_body=row[42],
                    mini_icon=row[43],
                )


character_import_data()


###########################################################
# Irous

def irous_species_import_data():
    with open('database\irous_species.csv') as f:
        reader = csv.reader(f)
        id = 0
        for row in reader:
            if row[0] != 'name':  # ignore header row
                id += 1
                _, created = Irous.objects.get_or_create(
                    id=id,
                    name=row[0],
                    weak=row[1],
                    strong=row[2],
                    guard=row[3],
                )


irous_species_import_data()


def irous_import_data():
    with open('database\irous.csv') as f:
        reader = csv.reader(f)
        id = 0
        for row in reader:
            if row[0] != 'species':  # ignore header row
                _, created = IrousVariation.objects.get_or_create(
                    id=row[5],
                    species_id=row[0],
                    japanese_name=row[1],
                    name=row[2],
                    image=row[3],
                    is_large_irous=True if row[4] == "1" else False,
                )


irous_import_data()


###########################################################
# Stage

def stage_import_data():
    with open('database/outputStages.csv') as f:
        reader = csv.reader(f)
        id = 0
        for row in reader:
            if row[0] != 'stage_name':  # ignore header row
                id += 1
                # Add stage if not added
                if Stage.objects.filter(name=row[0]).__len__() == 0:
                    _, created = Stage.objects.get_or_create(
                        id=id,
                        owner_id=1,
                        name=row[0],
                        episode=row[1],
                        number=row[2],
                        part=row[3],
                        chapter=row[4],
                    )

                    # Add Irouss
                    small_irous = row[5]
                    large_irous = row[6]

                    # Split 'em up and add small irouss
                    for irous in small_irous.split(','):
                        if irous != "":
                            _, created = Stage.small_irous.through.objects.get_or_create(
                                stage_id=id,
                                irousvariation_id=irous,
                            )

                    # Split 'em up and add big irouss
                    for irous in large_irous.split(','):
                        if irous != "":
                            _, created = Stage.large_irous.through.objects.get_or_create(
                                stage_id=id,
                                irousvariation_id=irous,
                            )


stage_import_data()


###########################################################
# StageDifficulty

def stage_difficulties_import_data():
    with open('database/outputDifficulties.csv') as f:
        reader = csv.reader(f)
        id = 0
        for row in reader:
            if row[0] != 'episode':  # ignore header row
                id += 1
                # Add difficulty if not added
                filtered = StageDifficulty.objects.filter(stage__episode=row[0], stage__number=row[1],
                                                          difficulty=row[3])
                if filtered.__len__() == 0:  # if not added
                    _, created = StageDifficulty.objects.get_or_create(
                        id=id,
                        stage_id=Stage.objects.filter(episode=row[0], number=row[1])[0].id,
                        difficulty=row[3],
                        level=row[4],
                        exp=row[5],
                        coins=row[6],
                        cheerpoints=row[7],
                        drops=row[8],
                        objectives=row[9],
                    )


stage_difficulties_import_data()


###########################################################
# Card

def card_import_data():
    with open('database/revamped_card_database.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'id':  # ignore header row
                if Card.objects.filter(name=row[3]).__len__() == 0:  # If card is not added
                    _, created = Card.objects.get_or_create(
                        id=row[0],
                        owner_id=row[1],
                        i_card_type=row[3],
                        name=row[4],
                        japanese_name=row[5],
                        student_id=row[7],
                        i_rarity=row[9],
                        i_weapon=row[11],
                        obtain_method=row[12],
                        image=row[13],
                        special_icon=row[14],
                        art=row[15],
                        special_front=row[16],
                        front_top=row[17],
                        front_bottom=row[18],
                        front_name=row[19],
                        front_rarity=row[20],
                        front_weapon=row[21],
                        transparent=row[22],
                        subcard_effect=True if row[23] == "true" else False,
                        hp_1=row[24],
                        sp_1=row[25],
                        atk_1=row[26],
                        def_1=row[27],
                        hp_50=row[28],
                        sp_50=row[29],
                        atk_50=row[30],
                        def_50=row[31],
                        hp_70=return_number_or_none(row[32]),
                        sp_70=return_number_or_none(row[33]),
                        atk_70=return_number_or_none(row[34]),
                        def_70=return_number_or_none(row[35]),
                        skill_name=row[36],
                        japanese_skill_name=row[37],
                        skill_SP=return_number_or_none(row[38]),
                        skill_range=row[39],
                        i_skill_affinity=row[41],
                        action_skill_effects=row[42],
                        skill_comment=row[43],
                        skill_preview=row[44],
                        action_skill_combo=return_number_or_none(row[45]),
                        evolved_action_skill_combo=return_number_or_none(row[46]),
                        action_skill_damage=row[47],
                        evolved_action_skill_damage=row[48],
                        nakayoshi_title=row[49],
                        japanese_nakayoshi_title=row[50],
                        nakayoshi_skill_requirement=row[51],
                        nakayoshi_skill_effect=row[52],
                        nakayoshi_skill_target=row[53],
                        evolved_nakayoshi_skill_requirement=row[54],
                        evolved_nakayoshi_skill_effect=row[55],
                        evolved_nakayoshi_skill_target=row[56],
                        charge_comment=row[57],
                        charge_damage=row[58],
                        charge_hit=row[59],
                        charge_name=row[60],
                        charge_range=row[61],
                    )


card_import_data()
