class DataPoint:
    def __init__(self, a, b, pred):
        self.a = a
        self.b = b
        self.pred = pred
    
    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
    
    def get_pred(self):
        return self.pred