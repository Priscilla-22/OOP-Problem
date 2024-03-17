class Player:
    def __init__(self, name, chicken_wings, hamburgers, hot_dogs):
        self.name = name
        self.score = (chicken_wings * 5) + (hamburgers * 3) + (hot_dogs * 2)


def scoreboard(players):
    scores = []

    for player_info in players:
        player = Player(player_info['name'], player_info['chicken_wings'],
                        player_info['hamburgers'], player_info['hot_dogs'])
        scores.append({"name": player.name, "score": player.score})

    scores.sort(key=lambda x: (-x["score"], x["name"]))

    return scores


