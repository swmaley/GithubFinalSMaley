import r6sapi as R6Api


class RainbowSixSiegeService:
    def __init__(self, ubisoft_email, ubisoft_password):
        self.api = R6Api(ubisoft_email, ubisoft_password)

    def get_player_stats(self, username):
        player = self.api.get_player(username, platform='uplay')
        return player