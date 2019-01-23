from moto import mock_dynamodb2

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class UserModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = 'dynamodb-user'
    email = UnicodeAttribute(hash_key=True)
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()


@mock_dynamodb2
def test():
    UserModel.create_table(
        read_capacity_units=1, write_capacity_units=1, wait=True)
    user = UserModel(
        'test@example.com', first_name='Samuel', last_name='Adams')
    user.save()
    print(UserModel.count())


test()
