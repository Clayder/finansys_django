# from datetime import datetime
# from unittest import TestCase
#
# from accounts.models import Account
#
#
# class AccountModelTest(TestCase):
#
#     def setUp(self):
#         self.account = Account.objects.create(
#             # updated_at=datetime.strptime('2021-09-15 13:00:00', '%Y-%m-%d %H:%M:%S'),
#             # created_at=datetime.strptime('2021-09-15 13:00:00', '%Y-%m-%d %H:%M:%S'),
#             # deleted_at=None,
#             type=Account.DEBIT,
#             balance=1000.00,
#             due_day=10,
#             close_day=3
#         )
#
#     def test_create(self):
#         self.assertTrue(Account.objects.exists())