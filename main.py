import instaloader
import psycopg2
from datetime import datetime
import time
import logging
import requests

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Database connection information
DB_HOST = 'ep-tight-limit-a6uyk8mk.us-west-2.retooldb.com'
DB_USER = 'retool'
DB_PASSWORD = 'jr1cAFW3ZIwH'
DB_NAME = 'retool'

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    dbname=DB_NAME
)

# Initialize Instaloader
L = instaloader.Instaloader()

# List of Instagram usernames
usernames = [ "helenebjorklund" , "manhammar" , "larsisak10" , "sanna_backeskog" , "linneawickman" ,
              "riksdagsmattias", "dzenan.cisija", "landsbygdsministern", "adnandibrani_",
             "aidahadzialic", "annacarensatherberg", "carinaodebrink", "niklassigvardsson", "muranovicazra","lena_hallengren",
"tomaskronstahl",
"lailanaraghi",
"tomas_eneroth",
"monicahaider",
"jockesandell1",
"ida.karkiainen",
"fredriklundhsammeli",
"walleanna",
"perarne_h",
"johanssonmorgan70",
"adrian.magnusson",
"yasminebladelius",
"socdemola1",
"anders_y",
"annikastrandhall",
"kadir.kasirga",
"lawenredar",
"mattiasvepsa",
"jytteguteland",
"mkallifatides",
"mirjar",
"danielvencu",
"magdalenanderssons",
"mikaeldamberg",
"asawestlund",
"leif_nysmed",
"alexandravolker",
"serohe",
"mathias.tegner",
"annavikstrom2",
"selinmarkus",
"azadeh_rojhan",
"fredrik_olovsson_",
"shekarabiardalan",
"gustaf_lantz",
"mejern",
"gunsvan",
"norsjoisak",
"strombergannabelle",
"pederbjork",
"asa.ericsson",
"othorell",
"louisethunstrom",
"jessicaroden",
"kgfdirekt",
"jarrebring",
"idaekerothclausson",
"matilda_ernkrans",
"karin_sundin",
"t3resacarvalh0",
"johanlofstrand7",
"lindh_eva",
"pontusandersson92",
"sdtobbe",
"angelika.bengtssonsd",
"mattiasbj85",
"dennisdioukarev",
"staffansigvardeklof",
"sd.aron.emilsson",
"mattias.eriksson.falk",
"yasmineswe",
"mikael_eskilandersson",
"runarfilper",
"nima.gholam.ali.pour",
"rasmusgiertz",
"scraphonan",
"rogerhedlund",
"erikhellsborn",
"richard_jomshof",
"sdkarlsson",
"martin.kinnunen",
"lindaappelgrenlindberg",
"angelica_lundbergsd",
"patrickreslow",
"jessicastegrud",
"stahlherrstedt",
"johnnysvedin",
"svennesd",
"beatrice_timgren",
"henrik.vinge",
"westmontmartin",
"markuswiechel",
"lars_wistedt_riksdagsledamot",
"akesson.jimmie",
"fredrikahlstedt",
"emmaahlstromkoster",
"annsofiealm",
"beckmansasikter",
"helenabouveng",
"camillabrunsberg",
"idadrougge",
"lars_engsund_moderaterna",
"karin_enstrom",
"mats.green",
"gustafgothberg",
"anncharlotte.hammar",
"johanna.hornberger",
"hultbergjohan",
"misa133",
"ledamothogstrom",
"davidjosefsson_moderat",
"moderatkarlsson",
"fredrikkarrholm",
"skaracharlotte",
"erikottoson",
"lassepuess",
"edwardriedl",
"jessicarosencrantz",
"oliverrosengren",
"anna.afsillen",
"jesperskalberg",
"helena.storckenfeldt",
"magdalenathuresson",
"ledamotweinerhall",
"ledamotwarnick",
"borianaaberg",
"andrea.andersson_tay",
"nadjaawad",
"nooshidadgostar",
"lorena_dv",
"kajsafredholm",
"xami_gw",
"gunnarssonhanna",
"tony.haddou",
"malcolmjallow",
"lottajohnssonfornarve",
"isabellmixter",
"danielriazat",
"karin.ragsjo",
"lindasnecker",
"hakan.svenneling",
"ilonaszw",
"ciczie",
"jessicawetterling_",
"christofer_bergenblock",
"catojonny",
"muharremd",
"catarinaderemar",
"annalasses",
"ulrika_liljeberg",
"helenalindahl.c",
"rickardnordin_",
"emelie_nyman_c",
"anneli_sjolund",
"centermona",
"elisabethtr",
"centerhelena",
"andersadahl",
"martin_adahl",
"lili.andre_kd",
"yusuf.aydin82",
"mathias.bengtssson",
"berntssonmagnus",
"camilla_brodin",
"gudrunbrunegard",
"christianckd",
"bandyprasten",
"torsten_elofsson",
"danhovskar",
"ingemarkihlstrom",
"magnus.oscarsson",
"mikaeloscarsson",
"camillarinaldo69",
"larrysoder",
"rolandutbult",
"leilaelmi",
"almericson",
"emmaberginger",
"helldendaniel",
"annika_hirvonen",
"linuslaksomp",
"rebeckalemoine",
"katarina_luhr",
"janneriise_mp",
"jacobrisberg",
"marta_stenevi",
"uwesterlund",
"louise_eklund",
"joarforssell",
"robert.g.hannah",
"fredmalm",
"elinnilssonliberal",
"lina.nordquist",
"jakobolofsgard",
"ceciliaronnliberal",
"anna_starbrink",]

# List of proxies with authentication
proxies = [
"185.242.94.162:6247:ddewarhy:aimii5b6lrs4",
"198.12.112.175:5186:ddewarhy:aimii5b6lrs4",
"89.35.80.95:6750:ddewarhy:aimii5b6lrs4",
"216.74.118.229:6384:ddewarhy:aimii5b6lrs4",
"45.61.98.142:5826:ddewarhy:aimii5b6lrs4",
"161.123.154.55:6585:ddewarhy:aimii5b6lrs4",
"171.22.250.232:6351:ddewarhy:aimii5b6lrs4",
"45.131.92.173:6784:ddewarhy:aimii5b6lrs4",
"91.246.193.231:6488:ddewarhy:aimii5b6lrs4",
"154.194.8.162:5693:ddewarhy:aimii5b6lrs4",
"23.247.37.157:6459:ddewarhy:aimii5b6lrs4",
"45.192.136.130:5424:ddewarhy:aimii5b6lrs4",
"84.247.60.231:6201:ddewarhy:aimii5b6lrs4",
"45.146.31.203:5790:ddewarhy:aimii5b6lrs4",
"103.75.229.88:5836:ddewarhy:aimii5b6lrs4",
"91.246.192.87:6088:ddewarhy:aimii5b6lrs4",
"104.239.92.170:6810:ddewarhy:aimii5b6lrs4",
"45.192.138.155:6797:ddewarhy:aimii5b6lrs4",
"154.92.125.64:5365:ddewarhy:aimii5b6lrs4",
"45.114.15.225:6206:ddewarhy:aimii5b6lrs4",
"103.99.34.125:6740:ddewarhy:aimii5b6lrs4",
"45.56.174.150:6403:ddewarhy:aimii5b6lrs4",
"206.206.64.232:6193:ddewarhy:aimii5b6lrs4",
"89.40.223.173:6209:ddewarhy:aimii5b6lrs4",
"154.95.38.141:5799:ddewarhy:aimii5b6lrs4",
"77.83.233.158:6776:ddewarhy:aimii5b6lrs4",
"104.143.229.93:6021:ddewarhy:aimii5b6lrs4",
"104.223.157.244:6483:ddewarhy:aimii5b6lrs4",
"198.23.128.89:5717:ddewarhy:aimii5b6lrs4",
"104.238.8.94:5952:ddewarhy:aimii5b6lrs4",
"107.179.114.104:5877:ddewarhy:aimii5b6lrs4",
"216.173.80.90:6347:ddewarhy:aimii5b6lrs4",
"38.153.140.107:8985:ddewarhy:aimii5b6lrs4",
"45.43.65.181:6695:ddewarhy:aimii5b6lrs4",
"64.137.62.171:5816:ddewarhy:aimii5b6lrs4",
"157.52.253.52:6012:ddewarhy:aimii5b6lrs4",
"173.214.177.3:5694:ddewarhy:aimii5b6lrs4",
"207.244.217.192:6739:ddewarhy:aimii5b6lrs4",
"161.123.33.8:6031:ddewarhy:aimii5b6lrs4",
"37.35.40.203:8293:ddewarhy:aimii5b6lrs4",
"104.239.106.67:5712:ddewarhy:aimii5b6lrs4",
"104.239.107.244:5896:ddewarhy:aimii5b6lrs4",
"134.73.104.219:6853:ddewarhy:aimii5b6lrs4",
"45.43.70.36:6323:ddewarhy:aimii5b6lrs4",
"134.73.65.138:6690:ddewarhy:aimii5b6lrs4",
"157.52.174.232:6441:ddewarhy:aimii5b6lrs4",
"45.67.3.240:6403:ddewarhy:aimii5b6lrs4",
"103.47.53.60:8358:ddewarhy:aimii5b6lrs4",
"104.250.207.107:6505:ddewarhy:aimii5b6lrs4",
"185.242.94.133:6218:ddewarhy:aimii5b6lrs4",
"5.154.253.19:8277:ddewarhy:aimii5b6lrs4",
"136.0.109.239:6525:ddewarhy:aimii5b6lrs4",
"104.239.5.164:6818:ddewarhy:aimii5b6lrs4",
"206.206.118.67:6305:ddewarhy:aimii5b6lrs4",
"38.153.152.249:9599:ddewarhy:aimii5b6lrs4",
"45.131.94.190:6177:ddewarhy:aimii5b6lrs4",
"103.76.117.245:6510:ddewarhy:aimii5b6lrs4",
"157.52.174.67:6276:ddewarhy:aimii5b6lrs4",
"104.222.185.144:5707:ddewarhy:aimii5b6lrs4",
"107.181.141.146:6543:ddewarhy:aimii5b6lrs4",
"104.148.5.89:6100:ddewarhy:aimii5b6lrs4",
"157.52.253.122:6082:ddewarhy:aimii5b6lrs4",
"161.123.152.247:6492:ddewarhy:aimii5b6lrs4",
"161.123.154.157:6687:ddewarhy:aimii5b6lrs4",
"154.92.121.199:5218:ddewarhy:aimii5b6lrs4",
"166.88.58.248:5973:ddewarhy:aimii5b6lrs4",
"194.31.162.113:7629:ddewarhy:aimii5b6lrs4",
"194.39.32.85:6382:ddewarhy:aimii5b6lrs4",
"5.157.131.154:8414:ddewarhy:aimii5b6lrs4",
"64.137.121.247:6502:ddewarhy:aimii5b6lrs4",
"206.206.69.130:6394:ddewarhy:aimii5b6lrs4",
"107.181.128.190:5202:ddewarhy:aimii5b6lrs4",
"38.153.137.241:5549:ddewarhy:aimii5b6lrs4",
"103.3.227.157:6710:ddewarhy:aimii5b6lrs4",
"64.137.31.169:6783:ddewarhy:aimii5b6lrs4",
"84.46.204.248:6551:ddewarhy:aimii5b6lrs4",
"134.73.2.27:6368:ddewarhy:aimii5b6lrs4",
"166.88.195.153:5785:ddewarhy:aimii5b6lrs4",
"5.157.131.8:8268:ddewarhy:aimii5b6lrs4",
"5.157.131.249:8509:ddewarhy:aimii5b6lrs4",
"104.239.88.192:5812:ddewarhy:aimii5b6lrs4",
"216.173.75.3:6304:ddewarhy:aimii5b6lrs4",
"104.239.5.80:6734:ddewarhy:aimii5b6lrs4",
"64.137.57.113:6122:ddewarhy:aimii5b6lrs4",
"216.19.205.164:6485:ddewarhy:aimii5b6lrs4",
"150.107.202.4:6621:ddewarhy:aimii5b6lrs4",
"23.247.7.112:5785:ddewarhy:aimii5b6lrs4",
"162.245.188.7:5966:ddewarhy:aimii5b6lrs4",
"172.245.7.86:5139:ddewarhy:aimii5b6lrs4",
"216.173.79.205:6611:ddewarhy:aimii5b6lrs4",
"104.250.204.67:6158:ddewarhy:aimii5b6lrs4",
"45.127.250.128:5737:ddewarhy:aimii5b6lrs4",
"37.35.40.159:8249:ddewarhy:aimii5b6lrs4",
"216.173.111.191:6901:ddewarhy:aimii5b6lrs4",
"45.146.31.170:5757:ddewarhy:aimii5b6lrs4",
"161.123.130.150:5821:ddewarhy:aimii5b6lrs4",
"134.73.98.192:6771:ddewarhy:aimii5b6lrs4",
"166.88.3.111:6582:ddewarhy:aimii5b6lrs4",
"194.39.33.29:5738:ddewarhy:aimii5b6lrs4",
"216.173.122.196:5923:ddewarhy:aimii5b6lrs4",
]

proxy_index = 0


def rotate_proxy():
    global proxy_index
    proxy_index = (proxy_index + 1) % len(proxies)
    proxy = proxies[proxy_index]
    logging.info(f"Using proxy: {proxy}")
    ip, port, user, password = proxy.split(':')
    proxy_url = f"http://{user}:{password}@{ip}:{port}"
    return {"http": proxy_url, "https": proxy_url}


def insert_post_into_db(caption, timestamp, post_type, owner_username, display_url, video_url):
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO igposts (caption, timestamp, type, ownerusername, displayurl, videourl)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (caption, timestamp, post_type, owner_username, display_url, video_url))
        connection.commit()
    except Exception as e:
        logging.error(f"An error occurred while inserting into the database: {e}")


def get_last_5_posts(username, proxy):
    try:
        session = requests.Session()
        session.proxies.update(proxy)
        L.context._session = session
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()

        count = 0
        for post in posts:
            caption = post.caption
            timestamp = post.date_utc
            post_type = 'video' if post.is_video else 'image'
            display_url = post.url
            video_url = post.video_url if post.is_video else None

            insert_post_into_db(caption, timestamp, post_type, username, display_url, video_url)

            logging.info(f"Inserted post from {username} into the database.")

            count += 1
            if count >= 2:
                break
    except instaloader.exceptions.ProfileNotExistsException:
        logging.warning(f"Profile {username} does not exist.")
    except instaloader.exceptions.ConnectionException:
        logging.error("Connection error. Try again later.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


# Main loop to run the script
try:
    while True:
        proxy = rotate_proxy()
        for i, username in enumerate(usernames):
            logging.info(f"Fetching posts for {username}")
            get_last_5_posts(username, proxy)
            logging.info("\n" + "-" * 30 + "\n")

            time.sleep(15)  # Wait 15 seconds between each fetch

            if (i + 1) % 10 == 0:  # Rotate proxy after every 10 users
                proxy = rotate_proxy()

        # Sleep for 10 minutes (600 seconds) after processing all usernames
        logging.info("Sleeping for 1 minutes...")
        time.sleep(60)
except KeyboardInterrupt:
    logging.info("Script terminated by user.")
finally:
    # Close the database connection
    connection.close()
    logging.info("Database connection closed.")
