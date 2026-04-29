{
    'name': 'Product Kode Modal',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Tambah field Kode Modal di master produk dan POS',
    'depends': ['product', 'point_of_sale'],
    'data': [
        'views/product_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'product_kode_modal/static/src/xml/product_info_popup.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
}
