# Library of Overwatch Characters

from random import shuffle
from random import choice


class CharacterBase:
    def __init__(self):
        self.name = "default"
        self.action = []
        pass

    def get_name(self):
        return self.name

    def get_mixed_up_name(self):
        word = list(self.name)
        shuffle(word)
        return ''.join(word)

    def get_random_action(self):
        if len(self.action) == 0:
            print('empty action')
            return 0
        else:
            return choice(self.action)

    def generate_message(self):
        return "Here's today's question!\n" \
               "Action: {}\n" \
               "Hint: {}".format(self.get_random_action(),self.get_mixed_up_name())


class Genji(CharacterBase):
    def __init__(self):
        super(Genji, self).__init__()
        self.name = "Genji"
        self.action = [
            "Deflect",
            "Swift Strike"
        ]


class McCree(CharacterBase):
    def __init__(self):
        super(McCree, self).__init__()
        self.name = "McCree"
        self.action = [
            "Combat Roll",
            "Flashbang"
        ]


class Pharah(CharacterBase):
    def __init__(self):
        super(Pharah, self).__init__()
        self.name = "Pharah"
        self.action = [
            "Concussive Blast",
            "Jump Jet"
        ]


class Reaper(CharacterBase):
    def __init__(self):
        super(Reaper, self).__init__()
        self.name = "Reaper"
        self.action = [
            "Wraith Form",
            "Shadow Step"
        ]


class Soldier76(CharacterBase):
    def __init__(self):
        super(Soldier76, self).__init__()
        self.name = "Soldier 76"
        self.action = [
            "Helix Rockets",
            "Sprint",
            "Biotic Field"
        ]


class Tracer(CharacterBase):
    def __init__(self):
        super(Tracer, self).__init__()
        self.name = "Tracer"
        self.action = [
            "Blink",
            "Recall"
        ]


class Bastion(CharacterBase):
    def __init__(self):
        super(Bastion, self).__init__()
        self.name = "Bastion"
        self.action = [
            "Reconfigure",
            "Self-repair"
        ]


class Hanzo(CharacterBase):
    def __init__(self):
        super(Hanzo, self).__init__()
        self.name = "Hanzo"
        self.action = [
            "Sonic Arrow",
            "Scatter Arrow"
        ]


class Junkrat(CharacterBase):
    def __init__(self):
        super(Junkrat, self).__init__()
        self.name = "Junkrat"
        self.action = [
            "Concussion Mine",
            "Steel Trap"
        ]


class Mei(CharacterBase):
    def __init__(self):
        super(Mei, self).__init__()
        self.name = "Mei"
        self.action = [
            "Cryo-Freeze",
            "Ice Wall"
        ]


class Torbjorn(CharacterBase):
    def __init__(self):
        super(Torbjorn, self).__init__()
        self.name = "Torbjorn"
        self.action = [
            "Build Turret",
            "Armor Pack"
        ]


class Widowmaker(CharacterBase):
    def __init__(self):
        super(Widowmaker, self).__init__()
        self.name = "Widowmaker"
        self.action = [
            "Grappling Hook",
            "Venom Mine"
        ]


class DVa(CharacterBase):
    def __init__(self):
        super(DVa, self).__init__()
        self.name = "D.Va"
        self.action = [
            "Boosters",
            "Defense Matrix"
        ]


class Reinhardt(CharacterBase):
    def __init__(self):
        super(Reinhardt, self).__init__()
        self.name = "Reinhardt"
        self.action = [
            "Barrier Field",
            "Charge"
        ]


class Roadhog(CharacterBase):
    def __init__(self):
        super(Roadhog, self).__init__()
        self.name = "Roadhog"
        self.action = [
            "Take a Breather",
            "Chain Hook"
        ]


class Winston(CharacterBase):
    def __init__(self):
        super(Winston, self).__init__()
        self.name = "Winston"
        self.action = [
            "Jump Pack",
            "Barrier Protection"
        ]


class Zarya(CharacterBase):
    def __init__(self):
        super(Zarya, self).__init__()
        self.name = "Zarya"
        self.action = [
            "Particle Barrier",
            "Projected Barrier"
        ]


class Ana(CharacterBase):
    def __init__(self):
        super(Ana, self).__init__()
        self.name = "Ana"
        self.action = [
            "Sleep Dart",
            "Biotic Grenade"
        ]


class Lucio(CharacterBase):
    def __init__(self):
        super(Lucio, self).__init__()
        self.name = "Lucio"
        self.action = [
            "Crossfade",
            "Amp It Up"
        ]


class Mercy(CharacterBase):
    def __init__(self):
        super(Mercy, self).__init__()
        self.name = "Mercy"
        self.action = [
            "Guardian Angel",
            "Angelic Descent"
        ]


class Symmetra(CharacterBase):
    def __init__(self):
        super(Symmetra, self).__init__()
        self.name = "Symmetra"
        self.action = [
            "Sentry Turret",
            "Photon Shield"
        ]


class Zenyatta(CharacterBase):
    def __init__(self):
        super(Zenyatta, self).__init__()
        self.name = "Zenyatta"
        self.action = [
            "Orb of Harmony",
            "Orb of Discord"
        ]


class Roster:
    def __init__(self):
        self.character_roster = [
            Genji(),
            McCree(),
            Pharah(),
            Reaper(),
            Soldier76(),
            Tracer(),
            Bastion(),
            Hanzo(),
            Junkrat(),
            Mei(),
            Torbjorn(),
            Widowmaker(),
            DVa(),
            Reinhardt(),
            Roadhog(),
            Winston(),
            Zarya(),
            Ana(),
            Lucio(),
            Mercy(),
            Symmetra(),
            Zenyatta()
        ]
        
    def get_message(self):
        chosen_character = choice(self.character_roster)
        assert isinstance(chosen_character, CharacterBase)
        return chosen_character.generate_message()
        
        
if __name__ == '__main__':
    overwatch_roster = Roster()
    print(overwatch_roster.get_message())