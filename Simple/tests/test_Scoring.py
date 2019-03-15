import unittest
from main.Scoring import Scoring

class ScoringTest(unittest.TestCase):
    
    def setUp(self):
        self.scoring = Scoring()

    def score_three_points(self, player):
        self.scoring.give_point(player)
        self.scoring.give_point(player)
        self.scoring.give_point(player)

    def test_give_point_to_player(self):
        self.scoring.give_point("player_one")

        points = self.scoring.get_points("player_one")
        self.assertEqual(points, 1)
    
    def test_give_love(self):
        score_description = self.scoring.get_described("player_one")
        self.assertEqual(score_description, "love")
    
    def test_give_fifteen(self):
        self.scoring.give_point("player_one")
        
        score_description = self.scoring.get_described("player_one")
        self.assertEqual(score_description, "fifteen")
    
    def test_give_thirty(self):
        self.scoring.give_point("player_one")
        self.scoring.give_point("player_one")
        
        score_description = self.scoring.get_described("player_one")
        self.assertEqual(score_description, "thirty")
    
    def test_give_forty(self):
        self.scoring.give_point("player_one")
        self.scoring.give_point("player_one")
        self.scoring.give_point("player_one")
        
        score_description = self.scoring.get_described("player_one")
        self.assertEqual(score_description, "forty")

    def test_deuce(self):
        self.score_three_points("player_one")
        self.score_three_points("player_two")

        score_description = self.scoring.get_described()
        self.assertEqual(score_description, "deuce")
    
    def test_not_deuce(self):
        self.scoring.give_point("player_one")
        self.scoring.give_point("player_one")
        
        self.score_three_points("player_two")
        
        score_description = self.scoring.get_described()
        self.assertEqual(score_description, None)
    
    def test_advantage(self):
        self.score_three_points("player_one")
        self.scoring.give_point("player_one")
        
        self.score_three_points("player_two")

        advantage = self.scoring.get_advantage()
        self.assertEqual(advantage, "player_one has the advantage")
    
    def test_advantage_less_than_three(self):
        self.scoring.give_point("player_one")
        self.scoring.give_point("player_one")
        
        self.score_three_points("player_two")

        advantage = self.scoring.get_advantage()
        self.assertEqual(advantage, None)
    
    def test_winner(self):
        self.score_three_points("player_one")
        self.scoring.give_point("player_one")
        
        self.scoring.give_point("player_two")
        self.scoring.give_point("player_two")
        
        winner = self.scoring.get_winner()
        self.assertEqual(winner, "player_one wins!")
    
    def test_winner_not_greater_than_two(self):
        self.score_three_points("player_one")
        self.scoring.give_point("player_one")
        
        self.score_three_points("player_two")

        winner = self.scoring.get_winner()
        self.assertEqual(winner, None)



if __name__ is "__main__":
    unittest.main()
