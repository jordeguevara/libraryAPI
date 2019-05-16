
from sqlalchemy import create_engine, and_, text
from sqlalchemy.orm import sessionmaker


def create_session(config):
    engine = create_engine(config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session


# Check if there are authors, pageLength(n/a), publisher, publisher date
def checkBookProperties(book):
    props = {}
    if ("author_name" in book):
        props['author_name'] = book['author_name']
    else:
        props['author_name'] = "Not Available"

    if("first_publish_year" in book):
        props["publish_year"] = book["first_publish_year"]
    else:
        props["publish_year"] = "Not Available"

    if("isbn" in book):
        props["isbn"] = book["isbn"]
    else:
        props["isbn"] = "Not Available"

    return props


def prepareResponseListOfBooks(jsonResponseObj):
    bookList = []
    for book in jsonResponseObj["docs"]:
        title = book["title"]
        props = checkBookProperties(book)
        bookList.append(
            {"bookTitle": title, "author": props['author_name'], "publish_year": props["publish_year"], "ISBN": props["isbn"]})
    return bookList
