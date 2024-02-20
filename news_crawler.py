from korea_news_crawler.articlecrawler import ArticleCrawler
import urllib3
from datetime import datetime, timedelta
urllib3.disable_warnings()
if __name__ == '__main__':
    Crawler = ArticleCrawler()
    Crawler.set_category("IT과학")
    date = datetime(2024,1,1)
    # 병렬 처리를 진행할 경우 금방 limit에 도달 -> 1일 단위는 잘 수집됨
    # 만약 원격 호스트 연결와의 연결이 끊기는 현상 발생시 articlecrawler.py 167line의 sleep 값 늘리기
    for i in range(50):
        d2s = date.strftime("%Y") +'-' + date.strftime("%m") +'-' +date.strftime("%d")
        Crawler.set_date_range(d2s, d2s)
        Crawler.start()
        date = date + timedelta(days=1)