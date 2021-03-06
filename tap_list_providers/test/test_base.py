from unittest import TestCase

from tap_list_providers.base import fix_urls, BaseTapListProvider
from beers.test.factories import ManufacturerFactory
from beers.models import Manufacturer, ManufacturerAlternateName


class URLFixTestCase(TestCase):

    def test_fix_urls(self):
        bad_data = {
            'beer_advocate_url': "http://www.ratebeer.com/beer/ace-pear-cider/3004/",
        }
        fix_urls(bad_data)
        self.assertEqual(
            bad_data,
            {
                'rate_beer_url': "http://www.ratebeer.com/beer/ace-pear-cider/3004/",
            }
        )


class ManufacturerTestCase(TestCase):

    def test_manufacturer_lookup(self):
        mfg = ManufacturerFactory(name='Stone')
        provider = BaseTapListProvider()
        for name in [
                'Stone Brewing Company', 'Stone Brewing', 'Stone',
                'Stone Beer Co.',
        ]:
            looked_up = provider.get_manufacturer(name)
            self.assertEqual(
                mfg, looked_up, f'{looked_up.name} does not match {name}',
            )
            self.assertEqual(Manufacturer.objects.count(), 1, name)

    def test_mfg_duplicate_alt_name(self):
        mfg = ManufacturerFactory(name='Founders')
        ManufacturerAlternateName.objects.create(
            name=mfg.name, manufacturer=mfg)
        ManufacturerAlternateName.objects.create(
            name='Founders Brewing Co.', manufacturer=mfg,
        )
        provider = BaseTapListProvider()
        looked_up = provider.get_manufacturer(name=mfg.name)
        self.assertEqual(looked_up, mfg)
