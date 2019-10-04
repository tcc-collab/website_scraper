"""
News: main.py module
"""

from requests_html import HTML

# from src.scrapers import fetch_html
# from src.scrapers import TRINITY_LINK as url
url = "http://trinitycollege.edu.np"


def news_page_link(html_soup):
    """
    Returns -> [str] link of news page.
    Params -> [requests.HTML object] HTML of web page.
    """
    # Container div with all top news and p tag(at last) with more link
    news_div = html_soup.find("div#news_event", first=True)

    more_news_div_tag = news_div.find("div")[-1]
    more_news_a_tag = more_news_div_tag.find("a", first=True)
    more_news_link = url + more_news_a_tag.attrs["href"]
    return more_news_link


def get_top_news(html_soup):
    """
    Returns -> [list] list of latest news[type dict]
      News -> [Dict] attrs:
        'title' -> [str] title of news
        'link' -> [str] full link for the news

    Params -> [requests.HTML object] HTML of web page.
    """
    # Container div with all top news
    print(html_soup)
    # news_div = html_soup.find("div.title", first=True)

    # list of divs containing news title and link
    test = """
    news_items = news_div.find("div.event_text")
    top_news = []

    for news in news_items:
        news_a_tag = news.find("a", first=True)
        title = news_a_tag.text
        link = news_a_tag.attrs.get("href")
        full_link = url + link
        news_dict = {"title": title, "full_link": full_link}
        top_news.append(news_dict)

    return top_news
    """


def get_all_news(html_soup):
    """
    Returns -> [list] list of all news[type dict]
      News -> [Dict] attrs:
        'title' -> [str] title of news
        'link' -> [str] full link for the news
        'date' -> [str] Date of news eg:
        'content' -> [str] short summary of news
        [Note: content = 'News' or 5/6 words string most of time]

    Params -> [requests.HTML object] HTML of web page.
    """
    print(html_soup)


#    all_news_div = news_page_soup.find("div#content_text", first=True)
#    news = all_news_div.find("div#news")
#
#    more_news = []
#    for news in news:
#        date = news.find("div.date", first=True).text
#        content = news.find("div.content", first=True).text
#        title_div = news.find("div.title1", first=True)
#        title = title_div.find("a", first=True).text
#        link_div = news.find("div.more", first=True)
#        link = url + link_div.find("a", first=True).attrs.get("href")
#
#        news_dict = {"date": date, "title": title, "content": content, "link": link}
#        more_news.append(news_dict)
#
#    return more_news


if __name__ == "__main__":
    with open("../cache/index.html", "r") as rf:
        data = rf.read()
        html = HTML(html=data, url=url)

    get_top_news(html)

    all_news = """
    from requests_html import HTMLSession
    url = "http://trinitycollege.edu.np?page=news&type=news"
    session = HTMLSession()
    result = session.get(url)

    with open("../cache/news/all_news.html", "w") as rf:
        data = rf.write(result.html.html)
        # html = HTML(html=data, url=url)

    get_all_news(html)
    """