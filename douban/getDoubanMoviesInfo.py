import time
import requests
import json

url = 'https://movie.douban.com/j/new_search_subjects'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
}
params = {
    'sort': 'U',
    'range': '0,10',
    'tags': '',
    'start': '',
    'genres': '',
}


def get_movie_info(pages, movie_type):
    """
    暂时只放了爬取多少页与电影类型两个参数
    :param pages: 爬取页数
    :param movie_type: 电影类型(豆瓣搜索中支持的类型即可)
    :return:
    """
    res_data = []
    for num in range(pages):
        time.sleep(0.1)
        start_num = num * 20
        params['start'] = start_num
        params['genres'] = movie_type
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()['data']
            res_data.append(data)

            print('爬取第', num + 1, '页成功！')
        else:
            print('爬取第', num + 1, '页失败！')
            break
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(res_data, fp=fp, ensure_ascii=False)


if __name__ == '__main__':
    get_movie_info(pages=10, movie_type='喜剧')
