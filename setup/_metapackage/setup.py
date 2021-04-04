import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-stock-logistics-workflow",
    description="Meta package for oca-stock-logistics-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-delivery_package_default_shipping_weight',
        'odoo13-addon-delivery_total_weight_from_packaging',
        'odoo13-addon-sale_stock_mto_as_mts_orderpoint',
        'odoo13-addon-stock_account_product_run_fifo_hook',
        'odoo13-addon-stock_lock_lot',
        'odoo13-addon-stock_lot_scrap',
        'odoo13-addon-stock_move_assign_picking_hook',
        'odoo13-addon-stock_move_line_auto_fill',
        'odoo13-addon-stock_move_line_reference_link',
        'odoo13-addon-stock_move_quick_lot',
        'odoo13-addon-stock_no_negative',
        'odoo13-addon-stock_partner_delivery_window',
        'odoo13-addon-stock_picking_auto_create_lot',
        'odoo13-addon-stock_picking_back2draft',
        'odoo13-addon-stock_picking_backorder_strategy',
        'odoo13-addon-stock_picking_batch_extended',
        'odoo13-addon-stock_picking_filter_lot',
        'odoo13-addon-stock_picking_group_by_partner_by_carrier',
        'odoo13-addon-stock_picking_group_by_partner_by_carrier_by_date',
        'odoo13-addon-stock_picking_invoice_link',
        'odoo13-addon-stock_picking_late_activity',
        'odoo13-addon-stock_picking_mass_action',
        'odoo13-addon-stock_picking_product_assortment',
        'odoo13-addon-stock_picking_purchase_order_link',
        'odoo13-addon-stock_picking_restrict_cancel_with_orig_move',
        'odoo13-addon-stock_picking_return_restricted_qty',
        'odoo13-addon-stock_picking_sale_order_link',
        'odoo13-addon-stock_picking_send_by_mail',
        'odoo13-addon-stock_picking_show_backorder',
        'odoo13-addon-stock_picking_show_return',
        'odoo13-addon-stock_picking_warn_message',
        'odoo13-addon-stock_picking_whole_scrap',
        'odoo13-addon-stock_production_lot_active',
        'odoo13-addon-stock_putaway_by_route',
        'odoo13-addon-stock_putaway_hook',
        'odoo13-addon-stock_quant_package_dimension',
        'odoo13-addon-stock_quant_package_dimension_total_weight_from_packaging',
        'odoo13-addon-stock_quant_package_product_packaging',
        'odoo13-addon-stock_return_request',
        'odoo13-addon-stock_split_picking',
        'odoo13-addon-stock_valuation_layer_usage',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
