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
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 250
SUMMARY_MAX_PARAGRAPHS = 3

# _relative to PATH, above_
ARTICLE_EXCLUDES = ["extra"]
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    "extra/styles.css" : {"path" : "css/styles.css"},
    "extra/resume.html" : {"path" : "resume.html"},
    "extra/main.js" : {"path" : "js/main.js"},
}




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
        ('home/adnan', HOMEPAGE),
        ('rss', FEED_ALL_ATOM),
        ('resume', RESUME),
        ('archive', ARCHIVES_SAVE_AS)
]
SOCIAL = [
    ("email","mailto:elegant.flame6521@fastmail.com"),
    ("github", "https://github.com/adnanvaldes"),
    ("linkedin", "https://www.linkedin.com/in/adnanvaldes/"),
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
    """
    Find img elements and add :class_name: to them
    """
    return re.sub(r'(<img\s)', f'\\1class="{class_name} " ', content)

def add_first_processed_img(content, class_name="image-process-img"):
    """
    Find first image in the content and remove all others.
    """
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
    """
    Move first image found to top of parent container
    """
    images = re.findall(r'<img[^>]*>', content)

    if images:
        # Get the first image
        first_image = images[0]
        # Add the class to the first image
        first_image_with_class = re.sub(r'(<img\s)', f'\\1class="{class_name} " ', first_image)
        # Remove the first image from its original position
        content_without_first_image = content.replace(first_image, '', 1)
        # Move the first image to the top, outside of any <p> tags
        return f'{first_image_with_class} {content_without_first_image}'
    
    # If no images, return the content as is
    return content

JINJA_FILTERS = {
    'process_imgs': process_imgs,
    "add_first_processed_img" : add_first_processed_img,
    "move_first_image_to_top" : move_first_image_to_top,
}
