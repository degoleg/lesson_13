from player import Player

class TestPlayer:
    def test_change_name(self):
        player = Player('Oleg')
        player.change_name('Vasya')
        assert player.name == 'Vasya', "Ошибка в имени"

    def test_add_points(self):
        player = Player(2)
        player.add_points(2)
        assert player.points == 2, "Ошибка в числе"

    def test_get_points(self):
        player = Player('Oleg')
        assert player.get_points() == 0, "Ошибка в очках"






