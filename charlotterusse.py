import urllib2
from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup


site_url = 'http://www.charlotterusse.com'
site = 'charlotterusse'

log_file = open('charlotterusse.txt', 'w')

categories = {
    'Tops': {
        'Dressy': 'http://www.charlotterusse.com/family/index.jsp?categoryId=10965642',
        'Going Out': 'http://www.charlotterusse.com/family/index.jsp?categoryId=11254408',
        'Casual': 'http://www.charlotterusse.com/family/index.jsp?categoryId=10965643',
        'Cargigans & Cover UPS': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4238860',
        'Sweaters': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4238859',
        'Layering Camis': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4238887'
    },
    'Denim': {
        'Leggings': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4359701',
        'Skinny': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4335678',
        'Bootcut': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4335680',
        'Flare': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4359702',
        'Shorts & Crops': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4335683'
    },

    'Bottoms': {
        'Pants': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4238870',
        'Skirts': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4238872',
        'Shorts': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4238873',
        'Leggings': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4238874'
    },

    'Dresses': {
        'Night': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4234500',
        'Day': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4234473'
    },
    'Wear to Work': ['http://www.charlotterusse.com/family/index.jsp?categoryId=4335463'],

    'Jackets And Outerwear': {
        'Jackets': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4238896',
        'Blazers & Vests': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4238879'
    },

    'Sleep & Lounge': {
        'Cookies & Cream': 'http://www.charlotterusse.com/family/index.jsp?categoryId=11202642',
        'Layering Camis': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4238887'
    },
    
    'Intimates': {
        'Bras': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4187634',
        'Perfect Fit Bras': 'http://www.charlotterusse.com/family/index.jsp?categoryId=10896350',
        'Panties': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4187627'
    },

    'Shoes': {
        'Sandals & Wedges': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4192333',
        'Boots & Booties': 'http://www.charlotterusse.com/category/index.jsp?categoryId=10965636',
        'Pumps': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4238907',
        'Flats': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4238909',
        'Evening': 'http://www.charlotterusse.com/family/index.jsp?categoryId=4446601',
        'Online Exclusives': 'http://www.charlotterusse.com/family/index.jsp?categoryId=11156003',
        'Shoe Essentials': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4427724'
    },

    'Accessories': {
        'Jewelry': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4192366',
        'Bags': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4240804',
        'Belts': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4240807',
        'Hosiery': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4240809',
        'Hats, Hair & Scarves': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4192363',
        'Sunglasses': 'http://www.charlotterusse.com/category/index.jsp?categoryId=4240806',
        'Trinkets': 'http://www.charlotterusse.com/category/index.jsp?categoryId=10980692'
    }
}

def read_page(url):
    data = ''
    proxies = ['http://www.google.com/']
    try:
        #opener = urllib2.build_opener(urllib2.ProxyHandler({'http' : proxies[0]}))
        #user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US;" + \
        #    "rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1"
        #headers = { 'User-Agent': user_agent }
        #request = urllib2.Request(url, headers=headers)
        #response = opener.open(request)
        #data = response.read()
        #response.close()
        data = urllib2.urlopen(url).read()
    except Exception, e:
        raise e
    return data

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
    
    product_details = soup.find('div', {'id': 'product-detail'})
    title = product_details.find('h1').contents[0]
    price = ''
    try:
        price = product_details.find('dd', {'class': 'pricing'}).findAll('span')[0].contents[0].strip('$')
    except:
        pass
    reg_price = ''
    try:
        reg_price = product_details.find('span', {'class': 'price-list'}).contents[0].split('$')[-1].strip()
    except:
        pass

    description = ''
    try:
        desc_div = product_details.find('div', {'class': 'descrip'})
        description = desc_div.contents[0]

    except:
        pass

    sizes = []
    size_options = soup.find('ul', {'id': 'productsize'}).findAll('a')
    for size in size_options:
        s = {
            "size" : size.contents[0],
            "price" : price,
            "regPrice" : reg_price
        }
        sizes.append( s )

    colors = []
    color_container = soup.find('ul', {'id': 'main-product-swatches', 'class': 'swatches'})
    
    colors_links = color_container.findAll('a')
    index = 0
    while index < len(colors_links):
        c = colors_links[index]
        swatch_url = c.find('img')['src']
        color_id = ''
        color = {
            'colorName': c['title'],
            'colorValue' : {
                "blue" : '',
                "green" : '',
                "red" : ''
            },
            'colorUrl' : swatch_url,
            'colorId': color_id,
            'sizes': sizes

        }

        view_links = []
        try:
            root_url = swatch_url.split('_pattern_')[0]
            view_links = [
                root_url + 'enh-z6.jpg',
                root_url + '_alternate1_enh-z6.jpg'
            ]
        except:
            pass
        
        # Create views
        views = []
        count = 0
        while count < len(view_links):
            view_link = view_links[count]
            v = { 'viewId': count + 1 }
            v['viewUrl'] = view_link
            views.append(v)
            count += 1
        color['views'] = views
        colors.append( color )
        index += 1

    productId = ''
    item = {}
    item['title']= title
    item['description']= description
    item['category']= category
    item['subcategory']= subcategory
    item['gender'] = gender
    item['productId'] = productId
    item['colors'] = colors
    item['site'] = site

    save_item(item)
    

def scrape_page(category, subcategory, gender, link):
    page = read_page(link)
    soup = BeautifulSoup(page)
    all_items = soup.findAll('dl', {'class': 'product'})
    for item in all_items:
        url = item.find('dt', {'class': 'title'}).find('a')['href']
        try:
            scrape_item(category, subcategory, gender, site_url + url)
        except Exception, e:
            log_file.writelines([str(e), site_url + url])

    div_paging = soup.find('div', {'class': 'paging'})
    if div_paging:
        next_page = div_paging.find('a', {'title': 'Next'})
        if next_page:
            scrape_page(category, subcategory, gender, site_url + next_page['href'])

def scrape(cats, gender=''):
    """
    Scrape all items
    """
    for key in cats.keys():
        print key
        if type(cats[key]) == type({}):
            for sub_key in cats[key]:
                print sub_key
                scrape_page(key, sub_key, gender, cats[key][sub_key])
        else:
            for link in cats[key]:
                scrape_page(key, '', gender, link)

if __name__ == '__main__':
    scrape(categories, 'women')
    log_file.close()
    #scrape_item('', '', '', 'http://www.charlotterusse.com/product/index.jsp?productId=10795203&cp=4078198.11025267')


