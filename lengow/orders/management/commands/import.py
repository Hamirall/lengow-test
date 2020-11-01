from django.core.management.base import BaseCommand, CommandError
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from orders.models import Order

class Command(BaseCommand):
    help = 'Import data form an XML file'
    
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        with urlopen('http://test.lengow.io/orders-test.xml') as f:
            tree = ET.parse(f)
            root = tree.getroot()
            for _id in root[1].findall('order'):
                marketplace = _id.find('marketplace').text
                id_flux = _id.find('idFlux').text
                order_purchase_date = _id.find('order_purchase_date').text
                order_amount = _id.find('order_amount').text

                order = Order.objects.create(
                    marketplace = marketplace,
                    id_flux = id_flux,
                    order_purchase_date = order_purchase_date,
                    order_amount = order_amount
                )
