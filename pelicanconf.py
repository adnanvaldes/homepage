# Main settings file
AUTHOR = 'Adnan Valdes'
SITENAME = 'Adnan Valdes'
SITEURL = "https://adnanvaldes.pages.dev"
HOMEPAGE = SITEURL



# PATH = ""
THEME = "theme"
TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'
DEFAULT_DATE = "fs"
USE_FOLDER_AS_CATEGORY = False
FEED_ALL_ATOM = "feeds/atom.xml"
FEED_ALL_RSS = "feeds/feed.rss"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = 'blog'
DELETE_OUTPUT_DIRECTORY = False

# _relative to PATH, above_
# /home/einhard/Desktop/blog/extra
ARTICLE_EXCLUDES = ["extra"]
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    "extra/styles.css" : {"path" : "css/styles.css"},
    "extra/resume.html" : {"path" : "resume.html"},
    "extra/main.js" : {"path" : "js/main.js"}
}

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARCHIVES_SAVE_AS = "archives.html"
POST_SAVE_AS = ""
SERVER_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
AUTHOR_URL = ""
BLOG_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
RESUME = "resume.html"
MENUITEMS = [
        ('Home', HOMEPAGE),
        ('RSS', FEED_ALL_ATOM),
        ('Resume', RESUME),
        ('Archive', ARCHIVES_SAVE_AS)
]
