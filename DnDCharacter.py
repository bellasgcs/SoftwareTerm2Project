from DnDData import *

# v This matches the first letter of the user's input to its corresponding race to allow shortcuts
# it also converts all letters to lowercase
def convert_to_dnd_race(race):
    if isinstance(race, DnDRace):
        return race
    elif isinstance(race, int) and race in DnDRace._value2member_map_:
        return DnDRace(race)
    elif isinstance(race, str) and race.title() in DnDRace._member_names_:
        return DnDRace[race.title()]

    if race in DnDRace._member_names_:
        return DnDRace[race]
    else:
        race = race.lower()
        match race[0]:
            case 'd':
                match race[1]:
                    case 'w':
                        return DnDRace.Dwarf

                    case 'r':
                        return DnDRace.Dragonborn

            case 'e':
                return DnDRace.Elf
                # ^ for this one, if the user enters the letter 'e', it will assume that the user was typing 'elf'
                # as that is the only race starting with 'e'
                # all other races work in the same way

            case 'h':
                if 'i' in race:
                    return DnDRace.Halfling

                elif 'o' in race:
                    return DnDRace.Half_Orc

                elif 'e' in race:
                    return DnDRace.Half_Elf

            case't':
                return DnDRace.Tiefling

    return None

# v This matches the first letter of the user's input to its corresponding class to allow shortcuts
# it also converts all letters to lowercase
# it works the exact same as the previous function

def convert_to_dnd_class(classtype):
    if isinstance(classtype, DnDClass):
        return classtype
    elif isinstance(classtype, int) and classtype in DnDClass._value2member_map_:
        return DnDClass(classtype)
    elif isinstance(classtype, str) and classtype.title() in DnDClass._member_names_:
        return DnDClass[classtype.title()]

    if classtype in DnDClass._member_names_:
        return DnDClass[classtype]
    else:
        classtype = classtype.lower()
        match classtype[0]:
            case 'a':
                return DnDClass.Artificer

            case 'c':
                return DnDClass.Cleric

            case 'd':
                return DnDClass.Druid

            case 'f':
                return DnDClass.Fighter

            case 'm':
                return DnDClass.Monk

            case 'p':
                return DnDClass.Paladin

            case 's':
                return DnDClass.Sorcerer

            case 'w':
                if classtype[1] == 'i':
                    return DnDClass.Wizard
                else:
                    return DnDClass.Warlock

            case 'r':
                 match classtype[1]:
                     case 'a':
                         return DnDClass.Ranger

                     case 'o':
                         return DnDClass.Rogue
            case 'b':
                match classtype[1]:
                    case 'b':
                        return DnDClass.Barbarian
                    case 'd':
                        return DnDClass.Bard


    return None

# This matches the first letter of the user's input to the corresponding background to allow shortcuts
# it also converts all letters to lowercase
# it also functions the exact same way as the last two functions
def convert_to_dnd_background(background):
    if isinstance(background, DnDBackground):
        return background
    elif isinstance(background, int) and background in DnDBackground._value2member_map_:
        return DnDBackground(background)
    elif isinstance(background, str) and background.title().replace(" ", "_") in DnDBackground._member_names_:
        return DnDBackground[background.title().replace(" ", "_")]

    if background in DnDBackground._member_names_:
        return DnDBackground[background]
    else:
        background = background.lower()
        match background[0]:
            case 'a':
                return DnDBackground.Acolyte

            case 'c':
                match background[1]:
                    case 'h':
                        return DnDBackground.Charlatan

                    case 'r':
                        return DnDBackground.Criminal

            case 'e':
                return DnDBackground.Entertainer

            case 'f':
                return DnDBackground.Folk_Hero

            case 'g':
                return DnDBackground.Guild_Artisan

            case 'h':
                return DnDBackground.Hermit

            case 'n':
                return DnDBackground.Noble

            case 'o':
                return DnDBackground.Outlander

            case 's':
                if background[1] == 'a':
                    return DnDBackground.Sage
                else:
                    match background[2]:
                        case 'i':
                            return DnDBackground.Sailor

                        case 'l':
                            return DnDBackground.Soldier

            case 'u':
                return DnDBackground.Urchin

    return None

# This converts all input letters to lowercase
def convert_to_dnd_martialweapons(weapons):
    weapons = weapons.lower()
    weapons = weapons[0].upper()
    return weapons

# This matches the acronym to corresponding background to allow shortcuts
# it also converts all letters to lowercase
# it also functions the exact same way as the first two functions
def convert_to_dnd_alignment(alignment):
    if isinstance(alignment, DnDAlignment):
        return alignment
    elif isinstance(alignment, int) and alignment in DnDAlignment._value2member_map_:
        return DnDAlignment(alignment)
    elif isinstance(alignment, str):
        alignment = alignment.title().replace(" ", "_")
        if alignment in DnDAlignment._member_names_:
            return DnDAlignment[alignment]
        else:
            alignment = alignment.lower()
            match alignment[0]:
                case 'c':
                    match alignment[1]:
                        case 'g':
                            return DnDAlignment.Chaotic_Good
                        case 'n':
                            return DnDAlignment.Chaotic_Neutral
                        case 'e':
                            return DnDAlignment.Chaotic_Evil

                case 't':
                    if alignment[1] == 'n':
                        return DnDAlignment.True_Neutral
                    return
                case 'l':
                    match alignment[1]:
                        case 'g':
                            return DnDAlignment.Lawful_Good
                        case 'n':
                            return DnDAlignment.Lawful_Neutral
                        case 'e':
                            return DnDAlignment.Lawful_Evil
                case 'n':
                    match alignment[1]:
                        case 'g':
                            return DnDAlignment.Neutral_Good
                        case 'n':
                            return DnDAlignment.True_Neutral
                        case 'e':
                            return DnDAlignment.Neutral_Evil
    return None


# v This defines what a 'DnDCharacter' is and the different parts of it such as its race and level
class DnDCharacter:
    def __init__(
        self, name: str, race: DnDRace, classtype: DnDClass, background, align: DnDAlignment
    ):
        self.name = name
        self.race = race
        self.level = 1
        self.HP = 1
        self.languages = []
        self.proficiencies = []
        self.inventory = []
        self.weapons = []
        self.classtype = None
        self.set_class(classtype)
        self.background = background
        self.align = align
        self.set_race(race)

    # This makes it so that if the user resets their character,
    # all features will display 'N/A' if they try to view their character without making one
    def reset(self):
        self.race = "N/A"
        self.classtype = "N/A"
        self.name = "N/A"
        self.level = "N/A"
        self.HP = "N/A"
        self.background = "N/A"
        self.align = "N/A"
        self.size = "N/A"
        self.speed = "N/A"
        self.languages = "N/A"
        self.proficiencies = "N/A"
        self.inventory = "N/A"
        self.weapons = "N/A"

    # This function contains a bunch of conditions for each class
    # it sets the characters HP, proficiency bonus, and proficiencies based on the character's class
    def set_class(self, classtype: DnDClass):
        if not isinstance(classtype, DnDClass):
            raise ValueError("Class is not a DnDClass")
        if self.classtype is not None:
            raise ValueError("Can only set class once")
        self.classtype = classtype
        match classtype:

            #For example, if the user chooses 'barbarian', the HP is set to 12, the proficiency bonus is set to 2,
            #and the character receives all the barbarian proficiencies
            case DnDClass.Barbarian:
                self.HP = 12
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDMediumArmour.Hide_armour, DnDMediumArmour.Spiked_armour, DnDMediumArmour.Scale_mail_armour, DnDMediumArmour.Halfplate, DnDMediumArmour.Breastplate, DnDMediumArmour.Chain_shirt, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDMartialWeapons.Battleaxe, DnDMartialWeapons.Flail, DnDMartialWeapons.Glaive, DnDMartialWeapons.Greataxe, DnDMartialWeapons.Greatsword, DnDMartialWeapons.Halberd, DnDMartialWeapons.Lance, DnDMartialWeapons.Longsword, DnDMartialWeapons.Maul, DnDMartialWeapons.Morningstar, DnDMartialWeapons.Pike, DnDMartialWeapons.Rapier, DnDMartialWeapons.Scimitar, DnDMartialWeapons.Shortsword, DnDMartialWeapons.Trident, DnDMartialWeapons.War_pick, DnDMartialWeapons.Warhammer, DnDMartialWeapons.Whip, DnDAttributes.Strength, DnDAttributes.Constitution, DnDShields.Shield]


            #Bard Conditions
            case DnDClass.Bard:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDMartialRangedWeapons.Hand_crossbow, DnDMartialWeapons.Longsword,DnDMartialWeapons.Rapier,DnDMartialWeapons.Shortsword, DnDAttributes.Dexterity, DnDAttributes.Charisma]
                #3 musical instruments of your choice
                #any 3 skills

            #Cleric Conditions
            case DnDClass.Cleric:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDMediumArmour.Hide_armour, DnDMediumArmour.Spiked_armour, DnDMediumArmour.Scale_mail_armour, DnDMediumArmour.Halfplate, DnDMediumArmour.Breastplate, DnDMediumArmour.Chain_shirt, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDAttributes.Wisdom, DnDAttributes.Charisma, DnDShields.Shield]
                #2 skills from list

            #Druid Conditions
            case DnDClass.Druid:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDMediumArmour.Hide_armour, DnDMediumArmour.Spiked_armour, DnDMediumArmour.Scale_mail_armour, DnDMediumArmour.Halfplate, DnDMediumArmour.Breastplate, DnDMediumArmour.Chain_shirt, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleRangedWeapons.Dart, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDMartialWeapons.Scimitar, DnDSimpleWeapons.Sickle, DnDSimpleRangedWeapons.Sling, DnDSimpleWeapons.Spear, DnDMiscTools.Herbalism_kit, DnDAttributes.Intelligence, DnDAttributes.Wisdom, DnDShields.Shield]
                #2 skills from list

            #Monk Conditions
            case DnDClass.Monk:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += [DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDMartialWeapons.Shortsword, DnDAttributes.Strength, DnDAttributes.Dexterity]
                #1 artisan tool or musical instrument
                #2 skills from list

            #Rogue Conditions
            case DnDClass.Rogue:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDMartialRangedWeapons.Hand_crossbow, DnDMartialWeapons.Longsword, DnDMartialWeapons.Rapier, DnDMartialWeapons.Shortsword, DnDMiscTools.Thieves_tools, DnDAttributes.Dexterity, DnDAttributes.Intelligence]
                #4 skills from list

            #Warlock Conditions
            case DnDClass.Warlock:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDAttributes.Wisdom, DnDAttributes.Charisma]
                #2 skills from list

            #Artificer Conditions
            case DnDClass.Artificer:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDMediumArmour.Hide_armour, DnDMediumArmour.Spiked_armour, DnDMediumArmour.Scale_mail_armour, DnDMediumArmour.Halfplate, DnDMediumArmour.Breastplate, DnDMediumArmour.Chain_shirt, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDMiscTools.Thieves_tools, DnDArtisanTools.Tinkers_tools, DnDAttributes.Constitution, DnDAttributes.Intelligence, DnDShields.Shield]
                #One type of artisan tool
                #Choose 2 skills from list

            #Fighter Conditions
            case DnDClass.Fighter:
                self.HP = 10
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDMediumArmour.Hide_armour, DnDMediumArmour.Spiked_armour, DnDMediumArmour.Scale_mail_armour, DnDMediumArmour.Halfplate, DnDMediumArmour.Breastplate, DnDMediumArmour.Chain_shirt, DnDHeavyArmour.Chain_mail_armour, DnDHeavyArmour.Ring_mail_armour, DnDHeavyArmour.Plate_armour, DnDHeavyArmour.Splint_armour, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDMartialWeapons.Battleaxe, DnDMartialWeapons.Flail, DnDMartialWeapons.Glaive, DnDMartialWeapons.Greataxe, DnDMartialWeapons.Greatsword, DnDMartialWeapons.Halberd, DnDMartialWeapons.Lance, DnDMartialWeapons.Longsword, DnDMartialWeapons.Maul, DnDMartialWeapons.Morningstar, DnDMartialWeapons.Pike, DnDMartialWeapons.Rapier, DnDMartialWeapons.Scimitar, DnDMartialWeapons.Shortsword, DnDMartialWeapons.Trident, DnDMartialWeapons.War_pick, DnDMartialWeapons.Warhammer, DnDMartialWeapons.Whip, DnDAttributes.Strength, DnDAttributes.Constitution, DnDShields.Shield]
                #2 skills from list

            #Paladin Conditions
            case DnDClass.Paladin:
                self.HP = 10
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDMediumArmour.Hide_armour, DnDMediumArmour.Spiked_armour, DnDMediumArmour.Scale_mail_armour, DnDMediumArmour.Halfplate, DnDMediumArmour.Breastplate, DnDMediumArmour.Chain_shirt, DnDHeavyArmour.Chain_mail_armour, DnDHeavyArmour.Ring_mail_armour, DnDHeavyArmour.Plate_armour, DnDHeavyArmour.Splint_armour, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDMartialWeapons.Battleaxe, DnDMartialWeapons.Flail, DnDMartialWeapons.Glaive, DnDMartialWeapons.Greataxe, DnDMartialWeapons.Greatsword, DnDMartialWeapons.Halberd, DnDMartialWeapons.Lance, DnDMartialWeapons.Longsword, DnDMartialWeapons.Maul, DnDMartialWeapons.Morningstar, DnDMartialWeapons.Pike, DnDMartialWeapons.Rapier, DnDMartialWeapons.Scimitar, DnDMartialWeapons.Shortsword, DnDMartialWeapons.Trident, DnDMartialWeapons.War_pick, DnDMartialWeapons.Warhammer, DnDMartialWeapons.Whip, DnDAttributes.Wisdom, DnDAttributes.Charisma, DnDShields.Shield]
                #2 skills from list

            #Ranger Conditions
            case DnDClass.Ranger:
                self.HP = 10
                self.prof_bonus = 2
                self.proficiencies += [DnDLightArmour.Padded_armour, DnDLightArmour.Leather_armour, DnDLightArmour.Studded_leather_armour, DnDMediumArmour.Hide_armour, DnDMediumArmour.Spiked_armour, DnDMediumArmour.Scale_mail_armour, DnDMediumArmour.Halfplate, DnDMediumArmour.Breastplate, DnDMediumArmour.Chain_shirt, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear, DnDMartialWeapons.Battleaxe, DnDMartialWeapons.Flail, DnDMartialWeapons.Glaive, DnDMartialWeapons.Greataxe, DnDMartialWeapons.Greatsword, DnDMartialWeapons.Halberd, DnDMartialWeapons.Lance, DnDMartialWeapons.Longsword, DnDMartialWeapons.Maul, DnDMartialWeapons.Morningstar, DnDMartialWeapons.Pike, DnDMartialWeapons.Rapier, DnDMartialWeapons.Scimitar, DnDMartialWeapons.Shortsword, DnDMartialWeapons.Trident, DnDMartialWeapons.War_pick, DnDMartialWeapons.Warhammer, DnDMartialWeapons.Whip, DnDAttributes.Strength, DnDAttributes.Dexterity, DnDShields.Shield]
                #3 skills from list

            #Sorcerer Conditions
            case DnDClass.Sorcerer:
                self.HP = 6
                self.prof_bonus = 2
                self.proficiencies += [DnDSimpleWeapons.Dagger, DnDSimpleRangedWeapons.Dart, DnDSimpleRangedWeapons.Sling, DnDSimpleWeapons.Quarterstaff, DnDSimpleRangedWeapons.Light_crossbow, DnDAttributes.Constitution, DnDAttributes.Charisma]
                #2 skills from list

            #Wizard Conditions
            case DnDClass.Wizard:
                self.HP = 6
                self.prof_bonus = 2
                self.proficiencies += [DnDSimpleWeapons.Dagger, DnDSimpleRangedWeapons.Dart, DnDSimpleRangedWeapons.Sling, DnDSimpleWeapons.Quarterstaff, DnDSimpleRangedWeapons.Light_crossbow, DnDAttributes.Intelligence, DnDAttributes.Wisdom]

    # This function contains a bunch of conditions for each race, like the last function
    # it sets the characters speed, size, and languages they know, based on their race
    # it works like the last function
    def set_race(self, race: DnDRace):
        match race:

            #Tiefling Conditions
            case DnDRace.Tiefling:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages += [DnDLanguages.Common, DnDLanguages.Infernal]

            #For example, if the user selects 'half orc', there character has a speed of 30ft, a size of medium,
            #and can speak common and orc
            case DnDRace.Half_Orc:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages += [DnDLanguages.Common, DnDLanguages.Orc]

            #Half Elf Conditions
            case DnDRace.Half_Elf:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages += [DnDLanguages.Common, DnDLanguages.Elvish]

            #Dragonborn Conditions
            case DnDRace.Dragonborn:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages += [DnDLanguages.Common, DnDLanguages.Draconic]

            #Dwarf Conditions
            case DnDRace.Dwarf:
                self.speed = '25ft'
                self.size = 'Medium'
                self.languages += [DnDLanguages.Common, DnDLanguages.Dwarvish]

            #Elf Conditions
            case DnDRace.Elf:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages += [DnDLanguages.Common, DnDLanguages.Elvish]

            #Gnome Conditions
            case DnDRace.Gnome:
                self.speed = '25ft'
                self.size = 'Small'
                self.languages += [DnDLanguages.Common, DnDLanguages.Gnomish]

            #Halfling Conditions
            case DnDRace.Halfling:
                self.speed = '25ft'
                self.size = 'Small'
                self.languages += [DnDLanguages.Common, DnDLanguages.Halfling]

            #Human Conditions
            case DnDRace.Human:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages += [DnDLanguages.Common]
