# Main settings file
AUTHOR = 'Adnan Valdes'
SITENAME = 'Adnan Valdes'
SITEURL = "https://adnanvaldes.pages.dev"
HOMEPAGE = SITEURL

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
SUMMARY_MAX_LENGTH = 250
SUMMARY_MAX_PARAGRAPHS = 3

# _relative to PATH, above_
ARTICLE_EXCLUDES = ["extra"]
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    "extra/styles.css" : {"path" : "css/styles.css"},
    "extra/resume.html" : {"path" : "resume.html"},
    "extra/main.js" : {"path" : "js/main.js"},
    # "extra/photos/" : {"path" : "static/"}
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
    ("Email","mailto:elegant.flame6521@fastmail.com"),
    ("Github", "https://github.com/adnanvaldes"),
    ("LinkedIn", "https://www.linkedin.com/in/adnanvaldes/"),
)

DEFAULT_PAGINATION = 5

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

# Plugins

## Image-process
IMAGE_PROCESS = {
    "img" : ["scale_in 10% 10% False"]
}
IMAGE_PROCESS_DIR = "derived"
IMAGE_PROCESS_COPY_EXIF_TAG = True

## FILTERS

import re

def process_imgs(content, class_name="image-process-img"):
    # Use regex to find img tags and add the class attribute
    return re.sub(r'(<img\s)', f'\\1class="{class_name} " ', content)

def add_first_processed_img(content, class_name="image-process-img"):
    # Find all img tags in the content
    images = re.findall(r'<img[^>]*>', content)

    if images:
        # Keep only the first image
        first_image = images[0]
        # Add the class to the first image
        first_image_with_class = re.sub(r'(<img\s)', f'\\1class="{class_name} " ', first_image)
        # Replace the first image in the content and remove any subsequent ones in the summary
        content = content.replace(first_image, first_image_with_class, 1)
        # Remove all other images
        content = re.sub(r'<img[^>]*>', '', content, count=len(images) - 1)

    return content

def move_first_image_to_top(content, class_name="image-process-img"):
    # Find the first img tag in the content
    images = re.findall(r'<img[^>]*>', content)

    if images:
        # Get the first image
        first_image = images[0]
        # Add the class to the first image
        first_image_with_class = re.sub(r'(<img\s)', f'\\1class="{class_name} " ', first_image)
        # Remove the first image from its original position
        content_without_first_image = content.replace(first_image, '', 1)
        # Move the first image to the top, outside of any <p> tags
        return f'{first_image_with_class}<br>{content_without_first_image}'
    
    # If no images, return the content as is
    return content

# Register the filter with Jinja2
JINJA_FILTERS = {
    'process_imgs': process_imgs,
    "add_first_processed_img" : add_first_processed_img,
    "move_first_image_to_top" : move_first_image_to_top,
}
