from NaverNewsCrawler import NaverNewsCrawler

user_input = input('키워드를 입력하세요: ')

crawler = NaverNewsCrawler(user_input)

user_interset = input('엑셀 파일명을 입력하세요: ')

crawler.get_news(user_interset)
