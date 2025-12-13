class DataPoint:
    def __init__(self, a, b, actual):
        self.season_record = a
        self.num_races = b
        self.personal_record = actual
    
    def get_season_record(self):
        return self.season_record
    
    def get_num_races(self):
        return self.num_races
    
    def get_personal_record(self):
        return self.personal_record