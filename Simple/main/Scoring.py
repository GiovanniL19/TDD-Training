class Scoring():
    player_one = 0
    player_two = 0

    def give_point(self, player):
        if player is "player_one":
            self.player_one += 1
        if player is "player_two":
            self.player_two += 1

    def get_points(self, player):
        if player is "player_one":
            return self.player_one
        if player is "player_two":
            return self.player_two
            
    def get_described(self, player=None):
        if player is "player_one":
            if self.player_one is 0:
                return "love"
            if self.player_one is 1:
                return "fifteen"
            if self.player_one is 2:
                return "thirty"
            if self.player_one is 3:
                return "forty"

        if player is "player_two":
            if self.player_two:
                if self.player_one is 0:
                    return "love"
                if self.player_two is 1:
                    return "fifteen"
                if self.player_two is 2:
                    return "thirty"
                if self.player_two is 3:
                    return "forty"
        
        if self.player_one >= 3 and self.player_two >= 3:
            if self.player_one is self.player_two:
                return "deuce"
        
        return None

    def get_advantage(self):
        if self.player_one >= 3 and self.player_two >= 3:        
            if self.player_one is (self.player_two + 1):
                return "player_one has the advantage"
            elif self.player_one is (self.player_two - 1):
                return "player_two has the advantage"
        return None

    def get_winner(self):
        if self.player_one >= 4:
            if self.player_one >= self.player_two:
                difference = self.player_one - self.player_two
                if difference >= 2:
                    return "player_one wins!"

        if self.player_two >= 4:
            if self.player_two >= self.player_one:
                difference = self.player_two - self.player_one
                if difference >= 2:
                    return "player_two wins!"

        return None
