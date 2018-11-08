import unittest
from order import create_quick_order, QuickOrder, delivered, StandardOrder, create_standard_order

class TestOrder(unittest.TestCase):
    def test_create_quick_order(self):
        create_quick_order('Bag', 21, 50000)
        order = delivered[-1]
        self.assertIsInstance(order, QuickOrder)
        self.assertEqual(order.product_name, 'Bag')
        self.assertLess(order.deadline, 24)

    def test_create_quick_order_with_wrong_deadline(self):
        with self.assertRaises(ValueError):
            create_quick_order('Bag', 45, 50000)
            order = delivered[-1]
            self.assertIsInstance(order, QuickOrder)

    def test_create_standard_order(self):
        create_standard_order('maize', 52)
        order = delivered[-1]
        self.assertIsInstance(order, StandardOrder)
        self.assertEqual(order.product_name, 'maize')
        self.assertEqual(order.deadline, 52)
        
    
    def test_create_quick_order_with_little_extra_dime(self):
        # wrong input
        pass
    
    def test_create_quick_order_with_exceeded_deadline(self):
        pass
    
    def test_create_quick_order_with_amount_in_words(self):
        # wrong input
        pass

    def test_create_quick_order_with_deadline_in_words(self):
        # wrong input
        pass