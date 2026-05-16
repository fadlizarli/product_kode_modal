{
    'name': 'Kode Modal Generator',
    'version': '17.0.1.0.1',
    'category': 'Inventory',
    'summary': 'Generator kode modal produk dengan cipher MOBILSEDAN dan ABCDEFGHIL',
    'depends': ['product', 'point_of_sale'],
    'data': [
        'views/product_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'kode_modal_generator/static/src/xml/product_info_popup.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
}
