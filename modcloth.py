import urllib2
from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup


site_url = 'http://www.modcloth.com'
site = 'ModCloth'

log_file = open('modcloth.txt', 'w')

def read_page(url):
    data = ''
    try:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US;" + \
            "rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1"
        headers = { 'User-Agent': user_agent }
        request = urllib2.Request(url, headers=headers)
        response = opener.open(request)
        data = response.read()
        response.close()
    except Exception, e:
        log_file.writelines([str(e), url])
    return data


categories = {

    'Dresses': {
        'Party': 'http://www.modcloth.com/store/ModCloth/Womens/Dresses/Party',
        'Floral': 'http://www.modcloth.com/store/ModCloth/Womens/Dresses/Floral',
        'Tiered': 'http://www.modcloth.com/store/ModCloth/Womens/Dresses/Tiered',
        'Twofer': 'http://www.modcloth.com/store/ModCloth/Womens/Dresses/Twofer',
        'Ruffle': 'http://www.modcloth.com/store/ModCloth/Womens/Dresses/Ruffle'
    },

    'Tops': {
        'Long Sleeve Shirts': 'http://www.modcloth.com/store/ModCloth/Womens/Tops/Long+Sleeve+',
        'Short Sleeve Shirts': 'http://www.modcloth.com/store/ModCloth/Womens/Tops/Short+Sleeve+',
        'Sweaters': 'http://www.modcloth.com/store/ModCloth/Womens/Tops/Sweaters',
        'Vests': 'http://www.modcloth.com/store/ModCloth/Womens/Tops/Vests',
        'T-Shirts': 'http://www.modcloth.com/store/ModCloth/Womens/Tops/T+Shirts'

    },

    'Bottoms': {
        'Pants': 'http://www.modcloth.com/store/ModCloth/Womens/Bottoms/Pants',
        'Skirts': 'http://www.modcloth.com/store/ModCloth/Womens/Bottoms/Skirts',
        'Shorts': 'http://www.modcloth.com/store/ModCloth/Womens/Bottoms/Shorts',
        'Rompers': 'http://www.modcloth.com/store/ModCloth/Womens/Bottoms/Rompers'
    },

    'Swimwear': [
        'http://www.modcloth.com/store/ModCloth/Womens/Swimwear'
    ],

    'Outerwear': {
        'Coats': 'http://www.modcloth.com/store/ModCloth/Womens/Outerwear/Coats',
        'Jackets': 'http://www.modcloth.com/store/ModCloth/Womens/Outerwear/Jackets'

    },

    'Accessories': {
        'Cosmetics': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Cosmetics',
        'Bags': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Bags',
        'Necklaces': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Necklaces',
        'Earrings & Rings': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Earrings+Rings',
        'Eyewear': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Eyewear',
        'Socks & Tights': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Socks+Tights',
        'Hair Accessories': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Hair%20Accessories',
        'Hats & Scarves': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Hats+Scarves',
        'Bracelets & Watches': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Bracelets+Watches',
        'Wallets': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Wallets',
        'Belts': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Belts',
        'Umbrellas': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Umbrellas',
        'Gloves': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Gloves',
        'Pins & Keychains': 'http://www.modcloth.com/store/ModCloth/Womens/Accessories/Pins+Keychains'
    },
    
    'Shoes': {
        'Flats': 'http://www.modcloth.com/store/ModCloth/Womens/Shoes/Flats',
        'Heels': 'http://www.modcloth.com/store/ModCloth/Womens/Shoes/Heels',
        'Boots': 'http://www.modcloth.com/store/ModCloth/Womens/Shoes/Boots',
        'Wedges': 'http://www.modcloth.com/store/ModCloth/Womens/Shoes/Wedges',
        'Sandals': 'http://www.modcloth.com/store/ModCloth/Womens/Shoes/Sandals'
    }
    
}

def save_item(item):
    # Save item in db
    print item

def scrape_item(category, subcategory, gender, link):
    """
    Scrape individual item.
    """
    print link
    item_page = read_page(link)
    soup = BeautifulSoup(item_page)

    title = soup.find('h1', {'id': 'product-name'}).contents[0]
    description_contents = soup.find('body').find('div', {'id': 'desc'}).find('p').contents
    description = ''
    for c in description_contents:
        description += str(c)
    price = soup.find('div', {'id': 'product-price'}).find('span').contents[0]
    sizes = []
    try:
        size_ths = soup.find('table', {'class': 'measurements-data'}).findAll('th')[1:]
        if size_ths:
            for s in size_ths:
                sizes.append({ 'size': s.contents[0], 'price': price, 'regPrice': '' })
    except:
        pass

    #print sizes
    views = []
    try:
        spans = soup.find('ul', {'id': 'product-image-thumbnails'}).findAll('span', {'style': 'display:none'})
        index = 1
        while index <= len(spans):
            views.append( { 'viewId': index, 'viewUrl': site_url + spans[index-1].contents[0] } )
            index += 1
    except Exception, e:
        print 'Error: ', e

    #print views
    colors = [{
        'colorName': '',
        'colorId': '',
        'colorUrl': '',
        'colorValue': {'blue': '', 'red': '', 'green': ''},
        'sizes': sizes,
        'views': views
    }]
    
    item = {}
    item['title']= title
    item['description']= description
    item['category']= category
    item['subcategory']= subcategory
    item['gender'] = gender
    item['productId'] = ''
    item['colors'] = colors
    item['site'] = site

    save_item(item)

def scrape_page(category, subcategory, gender, link):
    #print link
    page = read_page(link)
    soup = BeautifulSoup(page)
    all_items = soup.findAll('div', {'class': 'product_cat_view'})
    for item in all_items:
        item_a = item.find('a')
        try:
            scrape_item(category, subcategory, gender, site_url + item_a['href'])
        except Exception, e:
            log_file.writelines([str(e), site_url + item_a['href']])
    next_page = soup.find('a', {'class': 'next_page'})
    if next_page:
        scrape_page(category, subcategory, gender, site_url + next_page['href'])


def scrape(cats, gender=''):
    """
    Scrape all items
    """
    for key in cats.keys():
        if type(cats[key]) == type({}):
            for sub_key in cats[key]:
                scrape_page(key, sub_key, gender, cats[key][sub_key])
        else:
            for link in cats[key]:
                scrape_page(key, '', gender, link)

if __name__ == '__main__':
    scrape(categories, 'women')
    log_file.close()


