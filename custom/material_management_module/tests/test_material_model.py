# -*- coding: utf-8 -*-
from odoo.tests import common, tagged


@tagged('-at_install', 'post_install')
class TestMaterialModel(common.TransactionCase):

    def test_create(self):

        # Create a new project with the test
        test_material = self.env['materials.material'].create({
            'name': 'MaterialName',
            'buy_price': 120,
            'supplier': 1,
            'type': 'fabric'
        })

        self.assertEqual(test_material.name, 'MaterialName')
        self.assertEqual(test_material.supplier.id, 1)
        self.assertEqual(test_material.type, 'fabric')
        self.assertEqual(test_material.buy_price, 120)
        print("Create data test success!")

    def test_create_buy_price_below_100(self):

        # Create a new project with the test
        try:
            self.env['materials.material'].create({
                'name': 'TestProject',
                'buy_price': 10,
                'supplier': 1,
                'type': 'fabric'
            })
        except Exception as e:
            self.assertEqual(str(e), 'Buy price should beyond 100')
            print("Validation for buy price is success")

    def test_unlink_data(self):

        # Create a new project with the test
        record = self.env['materials.material'].create({
            'name': 'test',
            'buy_price': 200,
            'supplier': 1,
            'type': 'fabric'
        })

        search = self.env['materials.material'].search([('name', '=', 'test')])
        self.assertEqual(1, len(search))
        for s in search:
            s.unlink()

        search = self.env['materials.material'].search([('name', '=', 'test')])
        self.assertEqual(0, len(search))
        for s in search:
            print(s)

        print("Test for unlink data from model success")

    def test_update_data(self):

        # Create a new project with the test
        record = self.env['materials.material'].create({
            'name': 'test',
            'buy_price': 200,
            'supplier': 1,
            'type': 'fabric'
        })

        search = self.env['materials.material'].search([('name', '=', 'test')])
        self.assertEqual(record.name, "test")
        self.assertEqual(1, len(search))
        for s in search:
            s.write({
                'name': 'updated_test'
            })

        search = self.env['materials.material'].search([('name', '=', 'test')])
        for s in search:
            self.assertEqual(s.name, 'updated_test')
            print("Test for updating data success")
