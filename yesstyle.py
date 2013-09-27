import urllib2
from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup


site_url = 'http://www.yesstyle.com'
site = 'yesstyle'

log_file = open('yesstyle_log.txt', 'w')

mens_categories = {

    'Tees/T-Shirts': {
        'Print/Logo T-Shirts': 'http://www.yesstyle.com/en/men-print-logo-t-shirts/list.html/bcc.11792_bpt.46',
        'Crewneck': 'http://www.yesstyle.com/en/men-crewneck/list.html/bcc.11793_bpt.46',
        'Short Sleeves': 'http://www.yesstyle.com/en/men-short-sleeves/list.html/bcc.11796_bpt.46',
        'Long Sleeves': 'http://www.yesstyle.com/en/men-long-sleeves/list.html/bcc.11795_bpt.46',
        '3/4 Sleeves': 'http://www.yesstyle.com/en/men-3-4-sleeves/list.html/bcc.11794_bpt.46',
        'Polo Shirts': 'http://www.yesstyle.com/en/men-polo-shirts/list.html/bcc.11797_bpt.46',
        'V-Neck': 'http://www.yesstyle.com/en/men-v-neck/list.html/bcc.11798_bpt.46',
        'Other Necklines': 'http://www.yesstyle.com/en/men-other-necklines/list.html/bcc.11799_bpt.46'
    },
    'Casual Tops': ['http://www.yesstyle.com/en/men-casual-tops/list.html/bcc.11279_bpt.46'],
    'Shirts': {
        'Casual Shirts': 'http://www.yesstyle.com/en/men-casual-shirts/list.html/bcc.11969_bpt.46',
        'Dress Shirts': 'http://www.yesstyle.com/en/men-dress-shirts/list.html/bcc.11968_bpt.46'
    },
    'Denims & Jeans': {
        'Straight-Cut / Regular Fit': 'http://www.yesstyle.com/en/men-straight-cut-regular-fit/list.html/bcc.11752_bpt.46',
        'Slim-Fit / Skinny Jeans': 'http://www.yesstyle.com/en/men-slim-fit-skinny-jeans/list.html/bcc.11753_bpt.46',
        'Washed Jeans': 'http://www.yesstyle.com/en/men-washed-jeans/list.html/bcc.11754_bpt.46',
        'Wide-Leg Jeans': 'http://www.yesstyle.com/en/men-wide-leg-jeans/list.html/bcc.11755_bpt.46',
        'Boot-cut Jeans': 'http://www.yesstyle.com/en/men-boot-cut-jeans/list.html/bcc.11756_bpt.46'
    },
    'Pants': {
        'Cotton Pants': 'http://www.yesstyle.com/en/men-cotton-pants/list.html/bcc.11790_bpt.46',
        'Dress Pants': 'http://www.yesstyle.com/en/men-dress-pants/list.html/bcc.11784_bpt.46',
        'Slim-Fit / Skinny': 'http://www.yesstyle.com/en/men-slim-fit-skinny/list.html/bcc.11785_bpt.46',
        'Wide-Leg Pants': 'http://www.yesstyle.com/en/men-wide-leg-pants/list.html/bcc.11786_bpt.46',
        'Cropped Pants': 'http://www.yesstyle.com/en/men-cropped-pants/list.html/bcc.11788_bpt.46',
        'Flat-front Pants': 'http://www.yesstyle.com/en/men-flat-front-pants/list.html/bcc.11789_bpt.46',
        'Wool Pants': 'http://www.yesstyle.com/en/men-wool-pants/list.html/bcc.11791_bpt.46',
        'Cargo Pants': 'http://www.yesstyle.com/en/men-cargo-pants/list.html/bcc.11783_bpt.46',
        'Training Pants / Sweatpants' : 'http://www.yesstyle.com/en/men-training-pants-sweatpants/list.html/bcc.11787_bpt.46'
    },
    'Shorts': ['http://www.yesstyle.com/en/men-shorts/list.html/bcc.11782_bpt.46'],
    'Sets': ['http://www.yesstyle.com/en/men-sets/list.html/bcc.11288_bpt.46'],
    'Sweaters': {
        'Pullovers / Sweatshirts': 'http://www.yesstyle.com/en/men-pullovers-sweatshirts/list.html/bcc.11801_bpt.46',
        'Hoodies': 'http://www.yesstyle.com/en/men-hoodies/list.html/bcc.11802_bpt.46',
        'Turtlenecks': 'http://www.yesstyle.com/en/men-turtlenecks/list.html/bcc.11803_bpt.46',
        'Cardigan': 'http://www.yesstyle.com/en/men-cardigan/list.html/bcc.11804_bpt.46'
    },
    'Hoodies': ['http://www.yesstyle.com/en/men-hoodies/list.html/bcc.11805_bpt.46'],
    'Knits': ['http://www.yesstyle.com/en/men-knits/list.html/bcc.11283_bpt.46'],
    'Jackets': ['http://www.yesstyle.com/en/men-all-jackets/list.html/bcc.11763_bpt.46'],
    'Blazers': ['http://www.yesstyle.com/en/men-all-blazers/list.html/bcc.11764_bpt.46'],
    'Outerwear': {
        'Double-Breasted Coats' : 'http://www.yesstyle.com/en/men-double-breasted-coats/list.html/bcc.11771_bpt.46',
        'Single-Breasted Coats': 'http://www.yesstyle.com/en/men-single-breasted-coats/list.html/bcc.11772_bpt.46',
        'Down / Padded Jackets': 'http://www.yesstyle.com/en/men-down-padded-jackets/list.html/bcc.11773_bpt.46',
        'Fleece': 'http://www.yesstyle.com/en/men-fleece/list.html/bcc.11774_bpt.46',
        'Trench Coats': 'http://www.yesstyle.com/en/men-trench-coats/list.html/bcc.11775_bpt.46',
        'Wool & Cashmere': 'http://www.yesstyle.com/en/men-wool-cashmere/list.html/bcc.11776_bpt.46'

    },
    'Ties': {
        'Silk Ties': 'http://www.yesstyle.com/en/men-silk-ties/list.html/bcc.11780_bpt.46',
        'Pattern Ties': 'http://www.yesstyle.com/en/men-pattern-ties/list.html/bcc.11781_bpt.46',
        'Slim / Narrow Ties': 'http://www.yesstyle.com/en/men-slim-narrow-ties/list.html/bcc.11779_bpt.46',
        'Bow Ties': 'http://www.yesstyle.com/en/men-bow-ties/list.html/bcc.11778_bpt.46'
    },
    'Belts': {
        'Fabric Belts': 'http://www.yesstyle.com/en/men-fabric-belts/list.html/bcc.11742_bpt.46',
        'Faux Leather Belts': 'http://www.yesstyle.com/en/men-faux-leather-belts/list.html/bcc.11743_bpt.46',
        'Genuine Leather Belts': 'http://www.yesstyle.com/en/men-genuine-leather-belts/list.html/bcc.11744_bpt.46',
        'Slim Belts': 'http://www.yesstyle.com/en/men-slim-belts/list.html/bcc.11745_bpt.46',
        'Buckled Belts': 'http://www.yesstyle.com/en/men-buckled-belts/list.html/bcc.11746_bpt.46',
        'Stitched Belts': 'http://www.yesstyle.com/en/men-stitched-belts/list.html/bcc.11747_bpt.46',
        'Studded Belts': 'http://www.yesstyle.com/en/men-studded-belts/list.html/bcc.11748_bpt.46'
    },
    'Hats & Scarves': {
        'Beanies': 'http://www.yesstyle.com/en/men-beanies/list.html/bcc.11757_bpt.46',
        'Caps': 'http://www.yesstyle.com/en/men-caps/list.html/bcc.11758_bpt.46',
        'Hats': 'http://www.yesstyle.com/en/men-hats/list.html/bcc.11759_bpt.46',
        'Gloves': 'http://www.yesstyle.com/en/men-gloves/list.html/bcc.11761_bpt.46',
        'Scarves': 'http://www.yesstyle.com/en/men-scarves/list.html/bcc.11762_bpt.46'
    },
    'Underwear & Socks': ['http://www.yesstyle.com/en/men-underwear-socks/list.html/bcc.11934_bpt.46'],
    'Accessories': ['http://www.yesstyle.com/en/accessories-mens-accessories/list.html/bcc.11989_bpt.46'],
    'Bags': {
        'Backpacks': 'http://www.yesstyle.com/en/bags-backpacks/list.html/bcc.11945_bpt.46',
        'Shoulder Bags': 'http://www.yesstyle.com/en/bags-shoulder-bags/list.html/bcc.11554_bpt.46',
        'Messenger Bags': 'http://www.yesstyle.com/en/bags-messenger-bags/list.html/bcc.11555_bpt.46',
        'Clutches': 'http://www.yesstyle.com/en/bags-clutches/list.html/bcc.11556_bpt.46',
        'Wallets & Coin Purses': 'http://www.yesstyle.com/en/bags-wallets-coin-purses/list.html/bcc.11733_bpt.46',
        'Carryalls': 'http://www.yesstyle.com/en/bags-carryalls/list.html/bcc.11557_bpt.46',
        'Business Bags': 'http://www.yesstyle.com/en/bags-business-bags/list.html/bcc.11558_bpt.46',
        'Others': 'http://www.yesstyle.com/en/bags-others/list.html/bcc.11559_bpt.46'
    },
    'Shoes': {
        'Dress Shoes': 'http://www.yesstyle.com/en/shoes-dress-shoes/list.html/bcc.11539_bpt.46',
        'Sandals': 'http://www.yesstyle.com/en/shoes-sandals/list.html/bcc.11540_bpt.46',
        'Boots': 'http://www.yesstyle.com/en/shoes-boots/list.html/bcc.11538_bpt.46',
        'Sneakers': 'http://www.yesstyle.com/en/shoes-sneakers/list.html/bcc.11541_bpt.46',
        'Slip-Ons': 'http://www.yesstyle.com/en/shoes-slip-ons/list.html/bcc.11956_bpt.46',
        'Others': 'http://www.yesstyle.com/en/shoes-others/list.html/bcc.11543_bpt.46'
    }
}

# WOMENS
womens_categories = {
    'Tees / T-Shirts': {
        'Print / Logo T-Shirts': 'http://www.yesstyle.com/en/women-print-logo-t-shirts/list.html/bcc.11902_bpt.46',
        'Crewneck': 'http://www.yesstyle.com/en/women-crewneck/list.html/bcc.11903_bpt.46',
        'Short Sleeves': 'http://www.yesstyle.com/en/women-short-sleeves/list.html/bcc.11905_bpt.46',
        'Long Sleeves': 'http://www.yesstyle.com/en/women-long-sleeves/list.html/bcc.11906_bpt.46',
        '3/4 Sleeves': 'http://www.yesstyle.com/en/women-3-4-sleeves/list.html/bcc.11904_bpt.46',
        'Polo Shirts': 'http://www.yesstyle.com/en/women-polo-shirts/list.html/bcc.11907_bpt.46',
        'V-Neck Tees': 'http://www.yesstyle.com/en/women-v-neck-tees/list.html/bcc.11908_bpt.46',
        'Other Necklines': 'http://www.yesstyle.com/en/women-other-necklines/list.html/bcc.11909_bpt.46'

    },

    'Casual Tops': {
        'Short Sleeves': 'http://www.yesstyle.com/en/women-short-sleeves/list.html/bcc.11832_bpt.46',
        '3/4 Sleeves': 'http://www.yesstyle.com/en/women-3-4-sleeves/list.html/bcc.11841_bpt.46',
        'Off-Shoulder': 'http://www.yesstyle.com/en/women-off-shoulder/list.html/bcc.11842_bpt.46',
        'Sleeveless': 'http://www.yesstyle.com/en/women-sleeveless/list.html/bcc.11833_bpt.46',
        'Tank Tops': 'http://www.yesstyle.com/en/women-tank-tops/list.html/bcc.11834_bpt.46',
        'Halters': 'http://www.yesstyle.com/en/women-halters/list.html/bcc.11840_bpt.46',
        'Camisoles': 'http://www.yesstyle.com/en/women-camisoles/list.html/bcc.11839_bpt.46',
        'Tube Tops': 'http://www.yesstyle.com/en/women-tube-tops/list.html/bcc.11838_bpt.46',
        'Long Shirts': 'http://www.yesstyle.com/en/women-long-shirts/list.html/bcc.11830_bpt.46',
        'Tunics': 'http://www.yesstyle.com/en/women-tunics/list.html/bcc.11835_bpt.46',
        'Turtlenecks': 'http://www.yesstyle.com/en/women-turtlenecks/list.html/bcc.11836_bpt.46',
        'Cardigans': 'http://www.yesstyle.com/en/women-cardigans/list.html/bcc.11829_bpt.46',
        'Vests': 'http://www.yesstyle.com/en/women-vests/list.html/bcc.11837_bpt.46',
        'Sets': 'http://www.yesstyle.com/en/women-sets/list.html/bcc.11843_bpt.46'

    },
    
    'Blouses & Shirts' : {
        'Casual Shirts': 'http://www.yesstyle.com/en/women-casual-shirts/list.html/bcc.11957_bpt.46',
        'Chiffon / Satin Blouses': 'http://www.yesstyle.com/en/women-chiffon-satin-blouses/list.html/bcc.11958_bpt.46',
        'Long Shirts': 'http://www.yesstyle.com/en/women-long-shirts/list.html/bcc.11960_bpt.46',
        'Smart / Work Blouses': 'http://www.yesstyle.com/en/women-smart-work-blouses/list.html/bcc.11959_bpt.46'

    },
    'Dresses': {
        'Sleeveless': 'http://www.yesstyle.com/en/women-sleeveless/list.html/bcc.11815_bpt.46',
        'Chiffon / Satin Dresses': 'http://www.yesstyle.com/en/women-chiffon-satin-dresses/list.html/bcc.11808_bpt.46',
        'Cocktail & Party Dresses': 'http://www.yesstyle.com/en/women-cocktail-party-dresses/list.html/bcc.11811_bpt.46',
        'Tunics': 'http://www.yesstyle.com/en/women-tunics/list.html/bcc.11817_bpt.46',
        'Sundresses & Maxi Dresses': 'http://www.yesstyle.com/en/women-sundresses-maxi-dresses/list.html/bcc.11963_bpt.46',
        'Knits': 'http://www.yesstyle.com/en/women-knits/list.html/bcc.11806_bpt.46',
        'Shirt Dresses': 'http://www.yesstyle.com/en/women-shirt-dresses/list.html/bcc.11807_bpt.46',
        'T-Shirt Dresses': 'http://www.yesstyle.com/en/women-t-shirt-dresses/list.html/bcc.11819_bpt.46',
        'Jumper Dresses': 'http://www.yesstyle.com/en/women-jumper-dresses/list.html/bcc.11813_bpt.46',
        'Hooded Dresses': 'http://www.yesstyle.com/en/women-hooded-dresses/list.html/bcc.11814_bpt.46',
        'Turtleneck Dresses': 'http://www.yesstyle.com/en/women-turtleneck-dresses/list.html/bcc.11809_bpt.46',
        'Sweater Dresses': 'http://www.yesstyle.com/en/women-sweater-dresses/list.html/bcc.11810_bpt.46',
        'Coatdresses': 'http://www.yesstyle.com/en/women-coatdresses/list.html/bcc.11812_bpt.46',
        'Wool': 'http://www.yesstyle.com/en/women-wool/list.html/bcc.11818_bpt.46'
    },
    'Knits': {
        'Cardigans': 'http://www.yesstyle.com/en/women-cardigans/list.html/bcc.11820_bpt.46',
        'Sweaters': 'http://www.yesstyle.com/en/women-sweaters/list.html/bcc.11821_bpt.46',
        'Vests & Coats': 'http://www.yesstyle.com/en/women-vests-coats/list.html/bcc.11822_bpt.46',
        'Knit Dresses': 'http://www.yesstyle.com/en/women-knit-scarves/list.html/bcc.11824_bpt.46',
        'Knit Scarves': 'http://www.yesstyle.com/en/women-knit-turtlenecks/list.html/bcc.11825_bpt.46',
        'Knit Turtlenecks': 'http://www.yesstyle.com/en/women-knit-turtlenecks/list.html/bcc.11825_bpt.46',
        'Sets': 'http://www.yesstyle.com/en/women-sets/list.html/bcc.11826_bpt.46'
    },

    'Denims & Jeans': {
        'Straight-Cut / Regular Fit': 'http://www.yesstyle.com/en/women-straight-cut-regular-fit/list.html/bcc.11863_bpt.46',
        'Slim-Fit / Skinny Jeans': 'http://www.yesstyle.com/en/women-slim-fit-skinny-jeans/list.html/bcc.11864_bpt.46',
        'Cropped Jeans': 'http://www.yesstyle.com/en/women-cropped-jeans/list.html/bcc.11869_bpt.46',
        'Washed Jeans': 'http://www.yesstyle.com/en/women-washed-jeans/list.html/bcc.11866_bpt.46',
        'Boot-cut Jeans': 'http://www.yesstyle.com/en/women-boot-cut-jeans/list.html/bcc.11868_bpt.46',
        'Denim Shorts': 'http://www.yesstyle.com/en/women-denim-shorts/list.html/bcc.11867_bpt.46'
    },

    'Pants' : {
        'Dress Pants / Trousers': 'http://www.yesstyle.com/en/women-dress-pants-trousers/list.html/bcc.11886_bpt.46',
        'Slim-Fit / Skinny Pants': 'http://www.yesstyle.com/en/women-slim-fit-skinny-pants/list.html/bcc.11891_bpt.46',
        'Drawstring Pants': 'http://www.yesstyle.com/en/women-drawstring-pants/list.html/bcc.11889_bpt.46',
        'Baggy / Harem / Wide-Leg Pants': 'http://www.yesstyle.com/en/women-baggy-harem-wide-leg-pants/list.html/bcc.11890_bpt.46',
        'Cropped / Capri': 'http://www.yesstyle.com/en/women-cropped-capri/list.html/bcc.11888_bpt.46',
        'Cargo Pants': 'http://www.yesstyle.com/en/women-cargo-pants/list.html/bcc.11887_bpt.46',
        'Training Pants / Sweatpants': 'http://www.yesstyle.com/en/women-training-pants-sweatpants/list.html/bcc.11893_bpt.46'
    },

    'Skirts': {
        'Denim Skirts': 'http://www.yesstyle.com/en/women-denim-skirts/list.html/bcc.11870_bpt.46',
        'Mini Skirts': 'http://www.yesstyle.com/en/women-mini-skirts/list.html/bcc.11873_bpt.46',
        'Long Skirts': 'http://www.yesstyle.com/en/women-long-skirts/list.html/bcc.11872_bpt.46',
        'Pencil-Cut': 'http://www.yesstyle.com/en/women-pencil-cut/list.html/bcc.11875_bpt.46',
        'Buttoned Skirts': 'http://www.yesstyle.com/en/women-buttoned-skirts/list.html/bcc.11876_bpt.46',
        'A-Line Skirts': 'http://www.yesstyle.com/en/women-a-line-skirts/list.html/bcc.11877_bpt.46',
        'Layered & Tiered': 'http://www.yesstyle.com/en/women-layered-tiered/list.html/bcc.11879_bpt.46',
        'Pleated Skirts': 'http://www.yesstyle.com/en/women-pleated-skirts/list.html/bcc.11880_bpt.46',
        'Jumper Skirts': 'http://www.yesstyle.com/en/women-jumper-skirts/list.html/bcc.11871_bpt.46',
        'Knit Skirts': 'http://www.yesstyle.com/en/women-knit-skirts/list.html/bcc.11878_bpt.46',
        'Wool Skirts': 'http://www.yesstyle.com/en/women-wool-skirts/list.html/bcc.11881_bpt.46'
    },

    'Shorts': {
        'Denim Shorts': 'http://www.yesstyle.com/en/women-denim-shorts/list.html/bcc.11883_bpt.46',
        'Jumper Shorts & Suspenders': 'http://www.yesstyle.com/en/women-jumper-shorts-suspenders/list.html/bcc.11885_bpt.46',
        'Gym Shorts': 'http://www.yesstyle.com/en/women-gym-shorts/list.html/bcc.11884_bpt.46',
        'Skorts/Culottes': 'http://www.yesstyle.com/en/women-skorts-culottes/list.html/bcc.11874_bpt.46'
    },
    'Playsuits & Jumpsuits': ['http://www.yesstyle.com/en/women-playsuits-jumpsuits/list.html/bcc.11953_bpt.46'],
    'Active & Loungewear' : ['http://www.yesstyle.com/en/women-active-loungewear/list.html/bcc.11314_bpt.46'],
    'Sets': ['http://www.yesstyle.com/en/women-sets/list.html/bcc.11159_bpt.46'],
    'Swimwear': ['http://www.yesstyle.com/en/women-swimwear/list.html/bcc.11275_bpt.46'],
    'Hoodies': ['http://www.yesstyle.com/en/women-hoodies/list.html/bcc.11916_bpt.46'],
    'Sweaters': {
        'Pullovers / Sweatshirts': 'http://www.yesstyle.com/en/women-pullovers-sweatshirts/list.html/bcc.11911_bpt.46',
        'Hoodies': 'http://www.yesstyle.com/en/women-hoodies/list.html/bcc.11912_bpt.46',
        'Capes': 'http://www.yesstyle.com/en/women-capes/list.html/bcc.11913_bpt.46',
        'Turtlenecks': 'http://www.yesstyle.com/en/women-turtlenecks/list.html/bcc.11914_bpt.46',
        'Cardigans': 'http://www.yesstyle.com/en/women-cardigans/list.html/bcc.11915_bpt.46'
    },
    'Jackets': ['http://www.yesstyle.com/en/women-all-jackets/list.html/bcc.11844_bpt.46'],
    'Blazers': ['http://www.yesstyle.com/en/women-all-blazers/list.html/bcc.11845_bpt.46'],
    'Outerwear': {
        'Trench Coats': 'http://www.yesstyle.com/en/women-trench-coats/list.html/bcc.11858_bpt.46',
        'Hooded Coats': 'http://www.yesstyle.com/en/women-hooded-coats/list.html/bcc.11859_bpt.46',
        'Down / Padded Jackets': 'http://www.yesstyle.com/en/women-down-padded-jackets/list.html/bcc.11853_bpt.46',
        'Fur Coats & Jackets': 'http://www.yesstyle.com/en/women-fur-coats-jackets/list.html/bcc.11857_bpt.46',
        'Wrap Coats & Jackets': 'http://www.yesstyle.com/en/women-wrap-coats-jackets/list.html/bcc.11862_bpt.46',
        'Tweed': 'http://www.yesstyle.com/en/women-tweed/list.html/bcc.11861_bpt.46',
        'Wool & Cashmere': 'http://www.yesstyle.com/en/women-wool-cashmere/list.html/bcc.11860_bpt.46'
    },
    'Belts': ['http://www.yesstyle.com/en/women-belts/list.html/bcc.11262_bpt.46'],
    'Hats & Scarves': ['http://www.yesstyle.com/en/women-hats-scarves/list.html/bcc.11263_bpt.46'],
    'Hosiery': {
        'Leg Warmers': 'http://www.yesstyle.com/en/women-leg-warmers/list.html/bcc.11942_bpt.46',
        'Socks & Stockings': 'http://www.yesstyle.com/en/women-socks-stockings/list.html/bcc.11943_bpt.46',
        'Leggings & Tights': 'http://www.yesstyle.com/en/women-leggings-tights/list.html/bcc.11892_bpt.46'
    },

    'Innerwear': {
        'Bras & Sets': 'http://www.yesstyle.com/en/women-bras-sets/list.html/bcc.11303_bpt.46',
        'Panties / Thongs / Briefs': 'http://www.yesstyle.com/en/women-panties-thongs-briefs/list.html/bcc.11304_bpt.46',
        'Lingerie': 'http://www.yesstyle.com/en/women-lingerie/list.html/bcc.11305_bpt.46',
        'Slips & Camis': 'http://www.yesstyle.com/en/women-slips-camis/list.html/bcc.11306_bpt.46',
        'Sleepwear': 'http://www.yesstyle.com/en/women-sleepwear/list.html/bcc.11307_bpt.46',
        'Shapewear / Body Support': 'http://www.yesstyle.com/en/women-shapewear-body-support/list.html/bcc.11308_bpt.46'
    },
    'Plus-size': {
        'Tops': 'http://www.yesstyle.com/en/women-tops/list.html/bcc.11917_bpt.46',
        'Bottoms': 'http://www.yesstyle.com/en/women-bottoms/list.html/bcc.11918_bpt.46'
    },
    'Maternity': {
        'innerwear': 'http://www.yesstyle.com/en/women-innerwear/list.html/bcc.11920_bpt.46'
    },
    'Shoes' : {
        'Sandals': 'http://www.yesstyle.com/en/shoes-sandals/list.html/bcc.11533_bpt.46',
        'Pumps': 'http://www.yesstyle.com/en/shoes-pumps/list.html/bcc.11532_bpt.46',
        'Loafers & Flats': 'http://www.yesstyle.com/en/shoes-loafers-flats/list.html/bcc.11531_bpt.46',
        'Boots': 'http://www.yesstyle.com/en/shoes-boots/list.html/bcc.11530_bpt.46',
        'Sneakers': 'http://www.yesstyle.com/en/shoes-sneakers/list.html/bcc.11534_bpt.46',
        'Slip-Ons': 'http://www.yesstyle.com/en/shoes-slip-ons/list.html/bcc.11955_bpt.46',
        'Others': 'http://www.yesstyle.com/en/shoes-others/list.html/bcc.11536_bpt.46'
    },
    'Bags': {
        'Backpacks': 'http://www.yesstyle.com/en/bags-backpacks/list.html/bcc.11944_bpt.46',
        'Satchels': 'http://www.yesstyle.com/en/bags-satchels/list.html/bcc.11545_bpt.46',
        'Totes': 'http://www.yesstyle.com/en/bags-totes/list.html/bcc.11546_bpt.46',
        'Hobo & Shoulder Bags': 'http://www.yesstyle.com/en/bags-hobo-shoulder-bags/list.html/bcc.11547_bpt.46',
        'Messenger Bags': 'http://www.yesstyle.com/en/bags-messenger-bags/list.html/bcc.11548_bpt.46',
        'Clutches': 'http://www.yesstyle.com/en/bags-clutches/list.html/bcc.11549_bpt.46',
        'Wallets & Coin Purses': 'http://www.yesstyle.com/en/bags-wallets-coin-purses/list.html/bcc.11732_bpt.46',
        'Carryalls': 'http://www.yesstyle.com/en/bags-carryalls/list.html/bcc.11550_bpt.46',
        'Business Bags': 'http://www.yesstyle.com/en/bags-business-bags/list.html/bcc.11551_bpt.46',
        'Others': 'http://www.yesstyle.com/en/bags-others/list.html/bcc.11552_bpt.46'

    },
    'Accessories': {
        'Necklaces & Pendants': 'http://www.yesstyle.com/en/accessories-necklaces-pendants/list.html/bcc.11174_bpt.46',
        'Bracelets & Bangles': 'http://www.yesstyle.com/en/accessories-bracelets-bangles/list.html/bcc.11175_bpt.46',
        'Earrings': 'http://www.yesstyle.com/en/accessories-earrings/list.html/bcc.11173_bpt.46',
        'Rings': 'http://www.yesstyle.com/en/accessories-rings/list.html/bcc.11176_bpt.46',
        'Anklets': 'http://www.yesstyle.com/en/accessories-anklets/list.html/bcc.11734_bpt.46',
        'Sets': 'http://www.yesstyle.com/en/accessories-sets/list.html/bcc.11193_bpt.46',
        'Brooches & Pins': 'http://www.yesstyle.com/en/accessories-brooches-pins/list.html/bcc.11177_bpt.46',
        'Charms': 'http://www.yesstyle.com/en/accessories-charms/list.html/bcc.11567_bpt.46',
        'Hair Accessories': 'http://www.yesstyle.com/en/accessories-hair-accessories/list.html/bcc.11327_bpt.46'
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
    item_page = read_page(link)
    soup = BeautifulSoup(item_page)

    images = []
    try:
        imgs = soup.find('div', {'class': 'detailgallery'}).findAll('img')
        for img in imgs:
            images.append( img['src'])
    except:
        pass
    views = []
    if images:
        index = 1
        while index <= len(images):
            views.append({ 'viewId': index, 'viewUrl': images[index-1]})
            index += 1
    
    colors = []
    table = soup.find('table', {'class': 'actable attrTable'})
    if table:
        trs = table.findAll('tr')
        for tr in trs[1:]:
            tds = tr.findAll('td')
            price = tds[0].contents[0].strip('US$')
            color_name = tds[1].contents[0].split('-')[0].strip()
            size = tds[1].contents[0].split(' - ')[-1].strip()

            size_dict = { 'price': price, 'size': size, 'regPrice': ''}
            c = None
            for color in colors:
                if color['colorName'] == color_name:
                    c = color
                    break
            if not c:
                c = { 'colorName': color_name, 'colorUrl': '', 'colorId': '', \
                    'colorValue': {'blue': '', 'green': '', 'red': ''}, \
                    'views': views, 'sizes': [ size_dict ]
                }
                colors.append(c)
            else:
                c['sizes'].append( size_dict )
    else:
        price = soup.find('b', {'class': 'finalprice'}).contents[0].strip('US$')
        trs = soup.find('table', {'class': 'infotable'}).findAll('tr')
        tr = trs[0]
        td = tr.findAll('td')[-1]
        text = td.contents[0]
        color_name = text.split('-')[0].strip()
        size = text.split('-')[-1].strip()
        size_dict = { 'price': price, 'size': size, 'regPrice': ''}
        c = { 'colorName': color_name, 'colorUrl': '', 'colorId': '', \
            'colorValue': {'blue': '', 'green': '', 'red': ''}, \
            'views': views, 'sizes': [ size_dict ]
        }
        colors.append(c)
    
    title_info = soup.find('div', {'class': 'titleInfo'})
    title = title_info.find('b', {'class': 'ptitle'}).contents[0]
    brand = ''
    try:
        title_info.find('h3', {'class': 'brand'}).find('a').contents[0]
    except:
        pass

    description_table = soup.find('table', {'class': 'actable virtable'})
    description = ''
    productId = ''
    try:
        trs = description_table.contents[2:]
        for tr in trs:
            description += str(tr)
        description = '<table><tr><td>Brand</td><td>' + brand + '</td></tr>' + description + '</table>'
    except:
        pass
    
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
    try:
        all_items = soup.find('ul', {'class': 'itemlist'}).findAll('a', {'class': 'coverlink'})
        for item in all_items:
            url = site_url + item['href']
            try:
                scrape_item(category, subcategory, gender, url)
            except Exception, e:
                log_file.write(str(e) + ' : ' + url)
    except Exception, e:
        log_file.write(str(e) + ' : ' + link)
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
        log_file.write(key)
        if type(cats[key]) == type({}):
            for sub_key in cats[key]:
                log_file.write( sub_key )
                scrape_page(key, sub_key, gender, cats[key][sub_key])
        else:
            for link in cats[key]:
                scrape_page(key, '', gender, link)

if __name__ == '__main__':
    scrape(mens_categories, 'men')
    scrape(womens_categories, 'women')
    log_file.close()


