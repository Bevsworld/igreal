import instaloader
import psycopg2
from datetime import datetime
import time

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
usernames = ["helenebjorklund",
"manhammar",
"larsisak10",
"sanna_backeskog",
"linneawickman",
"riksdagsmattias",
"dzenan.cisija",
"landsbygdsministern",
"adnandibrani_",
"aidahadzialic",
"annacarensatherberg",
"carinaodebrink",
"niklassigvardsson",
"muranovicazra",
"lena_hallengren",
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
"anna_starbrink",]  # Replace with actual usernames


def insert_post_into_db(caption, timestamp, post_type, owner_username, display_url, video_url):
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO igposts (caption, timestamp, type, ownerusername, displayurl, videourl)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (caption, timestamp, post_type, owner_username, display_url, video_url))
        connection.commit()
    except Exception as e:
        print(f"An error occurred while inserting into the database: {e}")


def get_last_5_posts(username):
    try:
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

            print(f"Inserted post from {username} into the database.")

            count += 1
            if count >= 5:
                break
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile {username} does not exist.")
    except instaloader.exceptions.ConnectionException:
        print("Connection error. Try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main loop to run the script every 15 minutes
try:
    while True:
        for username in usernames:
            print(f"Fetching posts for {username}")
            get_last_5_posts(username)
            print("\n" + "-" * 30 + "\n")

        # Sleep for 15 minutes (900 seconds)
        print("Sleeping for 15 minutes...")
        time.sleep(900)
except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    # Close the database connection
    connection.close()
    print("Database connection closed.")
