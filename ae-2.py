import urllib2
from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup


site_url = 'http://www.ae.com'
site = 'American Eagle'

mens_categories = {
    'Tops': 'http://www.ae.com/web/browse/category.jsp?catId=cat10025',
    #'Bottoms': 'http://www.ae.com/web/browse/category.jsp?catId=cat10027',
    #'Accessories': 'http://www.ae.com/web/browse/category.jsp?catId=cat570002',
    #'Footwear': 'http://www.ae.com/web/browse/category.jsp?catId=cat10030',
    #'Underwear': 'http://www.ae.com/web/browse/category.jsp?catId=cat10032'
}

def read_page(url):
    data = ''
    try:
        data = urlopen(url).read()
    except Exception, e:
        print e
    return data

def save_item(item):
    # Save item in db
    print item

def scrape_item(category, gender, link, subcategory):
    if link.find('http://') < 0:
        link = site_url + link

    page = read_page(link)
    soup = BeautifulSoup(page)
    overview = soup.find('div', {'id': 'overviewtab'})
    if not overview:
        overview = soup.find('div', {'id': 'equity_table'})
    if not overview:
        overview = soup.find('div', {'id': 'equity_table_wrap'})
    if not overview:
        overview = soup
    
    title = overview.find('h2', {'id': 'prod_equity'}).contents[0]
    description_div = overview.find('div', {'id': 'product_description'})
    description = ''
    for c in description_div.contents:
        description += str(c)
    product_id = overview.find('form', {'id': 'productid_form'})['name']
    try:
        reg_price = overview.find('a', {'id': 'maxprice_33'}).contents[0]
        reg_price = '$' + reg_price.split('$')[-1].strip()
        price = reg_price
    except:
        reg_price = overview.find('a', {'id': 'maxprice'}).contents[0]
        reg_price = '$' + reg_price.split('$')[-1].strip()
        price = overview.find('div', {'id': 'product_price'}).find('span', {'class': 'newprice'}).contents[0]
        price = '$' + price.split('$')[-1].strip()
    # Get Sizes
    sizes = []
    size_options = overview.find('select', {'id': 'size'}).findAll('option')
    for size in size_options:
        s = {
            "size" : size.contents[0],
            "price" : price,
            "regPrice" : reg_price
        }
        sizes.append( s )
    color_container = overview.find('div', {'id': 'swatch_td', 'class': 'swatchesContainer'})
    colors_links = color_container.find('div', {'class': 'color_swatch_container'}).findAll('a')
    colors = []
    index = 0
    while index < len(colors_links):
        c = colors_links[index]
        swatch_url = c['style'].split(')')[0].split('(')[-1].strip('"').strip()
        swatch_url = 'http:' + swatch_url
        color_id = c['id'].split('-')[-1].strip()
        color = { 'colorName': c.contents[0],
                  'colorValue' : {
                                "blue" : '',
                                "green" : '',
                                "red" : ''
                        },
                  'colorUrl' : swatch_url,
                  'colorId': color_id,
                  'sizes': sizes

        }
        if index == 0:
            view_links = soup.find('div', {'id': 'laydown'}).find('div', {'id': 'imageNav'}).find('div', {'class': 'views'}).findAll('a')
        else:
            link = 'http://www.ae.com/web/browse/' + c['href'].strip()
            color_page = read_page(link)
            color_soup = BeautifulSoup(color_page)
            view_links = color_soup.find('div', {'id': 'laydown'}).find('div', {'id': 'imageNav'}).find('div', {'class': 'views'}).findAll('a')
        # Create views
        views = []
        count = 0
        while count < len(view_links):
            a_tag = view_links[count]
            v = { 'viewId': count + 1 }
            v['viewUrl'] = 'http:' + a_tag.find('img')['src'].split('?')[0]
            views.append(v)
            count += 1
        color['views'] = views
        colors.append( color )
        index += 1

    item = {}
    item['title']= title
    item['description']= description
    item['category']= category
    item['subcategory']= subcategory
    item['gender'] = gender
    item['productId'] = product_id
    item['colors'] = colors
    item['site'] = site

    save_item(item)
    
def scrape_data(cats, gender=''):
    for category in cats.keys():
        main_page = read_page(cats[category])
        soup = BeautifulSoup(main_page)
        content_div = soup.findAll('div', {'id': 'contentInnerMost'})
        if not content_div:
            continue
        content_div = content_div[0]
        tables = content_div.findAll('table')
        count = len(tables)
        index = 0
        while index <= count - 2:
            table_head = tables[index]
            table_content = tables[index + 1]
            subcategory = table_head.find('h3').contents[0]
            product_links = table_content.findAll('a', {'class': 'section_prodlink'})
            for link in product_links:
                print site_url + link['href']
                scrape_item(category, gender, link['href'], subcategory)
            index += 2
            break
        break

if __name__ == '__main__':
    scrape_data(mens_categories)




