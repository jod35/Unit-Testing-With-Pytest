class Player:
    def __init__(self,name,health):
        self.name=name
        self.health=health


def create_player(name,health):
    return Player(name=name,health=health)


def test_player_hit():
    player=create_player("Jonathan",80)
    assert player.health==80

    assert player.name=="Jonathan"
