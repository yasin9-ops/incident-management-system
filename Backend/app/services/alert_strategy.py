class AlertStrategy:
    def send(self, component_id):
        pass


class P0Strategy(AlertStrategy):
    def send(self, component_id):
        print(f"🚨 CRITICAL ALERT: {component_id}")


class P2Strategy(AlertStrategy):
    def send(self, component_id):
        print(f"⚠️ Warning Alert: {component_id}")


def get_strategy(severity):
    if severity == "P0":
        return P0Strategy()
    return P2Strategy()