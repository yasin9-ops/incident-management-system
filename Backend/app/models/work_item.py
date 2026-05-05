from datetime import datetime

class WorkItem:
    def __init__(self, component_id):
        self.component_id = component_id
        self.status = "OPEN"
        self.signals = []
        self.start_time = datetime.now()
        self.last_signal_time = self.start_time
        self.end_time = None
        self.rca = None