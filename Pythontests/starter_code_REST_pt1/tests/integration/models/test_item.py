from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTEst(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format('test'))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 "Not found item {}, but expected to.".format('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format('test'))
