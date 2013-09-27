import urllib2
from urllib2 import urlopen
from cookielib import CookieJar

from BeautifulSoup import BeautifulSoup

log_file = open('welseal_log.txt', 'w')

site_url = 'http://intl.wetseal.com'
site = 'wetseal'

womens_categories = {
    'Tops': {
        'Casual': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=101&subCategoryId=115',
        'Dressy': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=101&subCategoryId=113',
        'Graphic Tees': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=101&subCategoryId=215',
        'Camis & Tanks': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=101&subCategoryId=1177',
        'Basic Tees': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=101&subCategoryId=185',
        'Sweaters': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=101&subCategoryId=110'
    },
    'Tees & Tanks': {
         'Camis': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=176&subCategoryId=183',
         'Tanks': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=176&subCategoryId=184',
         'Basic Tees': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=176&subCategoryId=185',
         'Graphic Tees': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=176&subCategoryId=215'
    },
    'Bottoms': {
        'Skirts': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=102&subCategoryId=117',
        'Pants': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=102&subCategoryId=118',
        'Shorts': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=102&subCategoryId=116',
        'Leggings': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=102&subCategoryId=121'
    },
    'Accessories': {
        'Jewelry': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=106&subCategoryId=545',
        'Hair': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=106&subCategoryId=803',
        'Sunglasses': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=106&subCategoryId=197',
        'Hats': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=106&subCategoryId=131',
        'Belts': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=106&subCategoryId=130',
        'Scarves': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=106&subCategoryId=129',
        'Hosiery': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=106&subCategoryId=198',
        'Handbags': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=106&subCategoryId=126'
    },
    'Shoes': {
        'Sandals': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=109&subCategoryId=208',
        'Flats': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=109&subCategoryId=207',
        'Pumps': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=109&subCategoryId=132',
        'Boots': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=109&subCategoryId=206'
    },
    'Intimates': {
         'Thongs': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=107&subCategoryId=209',
         'Boyshorts': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=107&subCategoryId=210',
         'Bras': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=107&subCategoryId=211',
         'Loungewear': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=107&subCategoryId=212',
         'Novelty': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=107&subCategoryId=257'
    },
    'Jackets': {
        'Hoodies': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=451&subCategoryId=452'
    },
    'Dresses': {
        'Homecoming': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=104&subCategoryId=586',
        'Rompers & Jumpsuits': 'http://intl.wetseal.com/catalog/thumbnail.jsp?categoryId=104&subCategoryId=1009'
    }
}

# CookieJar
cj = CookieJar()

def read_page(url):
    data = ''
    try:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US;" + \
            "rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1"
        opener.addheaders.append(('User-Agent', user_agent))
        response = opener.open(url)
        data = response.read()
        response.close()
    except Exception, e:
        print e
    return data

def save_item(item):
    # Save item in db

    print item

def scrape_item(category, subcategory, gender, link ):
    item_page = read_page(link)
    soup = BeautifulSoup(item_page)

    try:
        title = soup.find('span', {'id': 'product-detail-name'}).contents[0]
    except:
        title = ''
    price = soup.find('span', {'id': 'product-detail-name'}).contents[0].strip().replace('$', '')
    description = ''
    desc_div = soup.find('div', {'class': 'product-description'}).contents
    for d in desc_div:
        description += str(d)

    color_links = []
    color_links = soup.find('table', {'id': 'color-info-table'}).findAll('a')
    index = 0
    colors = []
    while index < len(color_links):
        color_link = color_links[index]
        color_name = color_link.find('img')['name']
        color_url = site_url + color_link.find('img')['src']
        if index > 0:
            color_page = read_page(site_url + color_link['href'])
            color_soup = BeautifulSoup(color_page)
        else:
            color_soup = soup
        
        sizes = []
        try:
            size_select = color_soup.find('select', {'id': 'size'})
            options = size_select.findAll('option')[1:]
            for op in options:
                sizes.append( { 'size': op['value'], 'price': price, 'regPrice': price } )
        except Exception, e:
            size_table = color_soup.find('table', {'id': 'size-quantity-table'})
            sizes = [ { 'price': price, 'regPrice': price, 'size': size_table.find('input', {'name': 'size'})['value'] } ]

        views = []
        try:
            images = color_soup.find('table', {'id': 'alt-images-table'}).findAll('img')
            viewId = 1
            for img in images:
                views.append( { 'viewId': viewId,
                        'viewUrl': site_url + img['src'].replace('.jpg', 'zm.jpg')
                })
                viewId += 1
        except Exception, e:
            log_file.writelines([str(e), link])

        color = {
            'colorName': color_name,
            'colorValue' : {
                "blue" : '',
                "green" : '',
                "red" : ''
            },
            'colorUrl' : color_url,
            'colorId': '',
            'sizes': sizes,
            'views': views
        }

        colors.append( color )
        index += 1

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


def scrape_page(category, subcategory, gender, link, is_first=True):
    page = read_page(link)
    soup = BeautifulSoup(page)
    
    all_items = []
    try:
        all_items = soup.findAll('div', {'class': 'product-display'})
    except Exception, e:
        log_file.writelines([str(e) , link])
    
    for item in all_items:
        item_a = item.find('a')
        url = site_url + item_a['href']
        try:
            scrape_item(category, subcategory, gender, url)
        except Exception, e:
            log_file.writelines([str(e), url ])

    if is_first:
        try:
            pagination = soup.find('div', {'class': 'pagnation'})
            if pagination:
                links = pagination.findAll('a')[:-2]
                for link in links:
                    url = site_url  + link['href']
                    scrape_page(category, subcategory, gender, url, False)
        except:
            pass

def scrape(cats, gender=''):
    """
    Scrape all items
    """
    for key in cats.keys():
        log_file.write(key)
        if type(cats[key]) == type({}):
            for sub_key in cats[key]:
                log_file.write(sub_key)
                scrape_page(key, sub_key, gender, cats[key][sub_key])
        else:
            for link in cats[key]:
                scrape_page(key, '', gender, link)

if __name__ == '__main__':
    url = 'http://www.wetseal.com/home.jsp'
    read_page(url)
    pipeline_session_id = ''
    for c in cj:
        if c.name == 'PIPELINE_SESSION_ID':
            pipeline_session_id = c.value
            break
    url = 'http://www.wetseal.com/home.jsp?pipeline_session_id=' + pipeline_session_id
    read_page(url)

    scrape(womens_categories, 'women')