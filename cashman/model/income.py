from marshmallow import post_load

from cashman.model.transaction import Transaction, TransactionSchema
from cashman.model.transaction_type import TransactionType


class Income(Transaction):
    def __init__(self, description, amount):
        super().__init__(description, amount, TransactionType.INCOME)

    def __repr__(self):
        return f'<Income(name={self.description!r})>'


class IncomeSchema(TransactionSchema):
    @post_load
    def make_income(self, data, **kwargs):
        return Income(**data)

instance_1 = Income("bleee","100")

print(instance_1)
