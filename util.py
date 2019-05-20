
from sqlalchemy import create_engine, and_, text
from sqlalchemy.orm import sessionmaker


def create_session(config):
    engine = create_engine(config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session


def formatAuthors(authors):
    if(authors[0] == "none"):
        return "none"
    authorsFormatted = ""
    for author in authors:
        authorsFormatted += author["name"] + ' '
    return authorsFormatted

# Check if certain props exisit: authors, publish date, isbn, # pages if not will state not Avail.


def checkBookProperties(book):

    props = {}
    if ("author_name" in book):
        props['author_name'] = book['author_name']
    else:
        props['author_name'] = 'N/A'
    if("publish_date" in book):
        props["publish_date"] = book["publish_date"]
    else:
        props["publish_date"] = "Not Available"
    if("isbn" in book):
        props["isbn"] = book["isbn"]
    else:
        props["isbn"] = "not available"

    return props


def checkWishListBookProps(book):
    props = {}
    if("authors" in book):
        props["authors"] = formatAuthors(book["authors"])
    else:
        props["authors"] = "Not available"
    if("number_of_pages" in book):
        props["number_of_pages"] = book["number_of_pages"]
    else:
        props["number_of_pages"] = -1  # not available
    if("publish_date" in book):
        props["publish_date"] = book["publish_date"]
    else:
        props["publish_date"] = "Not Available÷"
    return props


def prepareResponseListOfBooks(jsonResponseObj):
    bookList = []
    for book in jsonResponseObj["docs"]:
        title = book["title"]
        props = checkBookProperties(book)
        bookList.append(
            {"title": title, "author_name": props['author_name'], "publish_date": props["publish_date"], "ISBN": props["isbn"]})

    return bookList


def prepareWishList(jsonResponseObj, id):
    bookList = []
    title = jsonResponseObj[id]["title"]
    isbn = id.split(':')
    props = checkWishListBookProps(jsonResponseObj[id])
    bookList.append({"title": title, "authors": props['authors'],
                     "publish_date": props["publish_date"], "ISBN": isbn[1], "number_of_pages": props["number_of_pages"]})
    return bookList
