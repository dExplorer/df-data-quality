class DQRule:
    def __init__(self, rule_id, dataset_id, column_name, exp_id, rule_fail_action):
        self.rule_id = rule_id
        self.dataset_id = dataset_id
        self.column_name = column_name
        self.exp_id = exp_id
        self.rule_fail_action = rule_fail_action