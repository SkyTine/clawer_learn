import json
import time

import requests

url = "https://leetcode-cn.com/graphql/"
headers = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
}


def get_user_data(userSlugs: list):
    """
    爬取所有user的力扣刷题进度~
    :param userSlugs: 用户id
    :return: null
    """
    user_progress = []
    params = {
        "operationName": "userQuestionProgress",
        "variables": {
            "userSlug": "",
        },
        "query": "query userQuestionProgress($userSlug: String!) {\n  userProfileUserQuestionProgress(userSlug: $userSlug) {\n    numAcceptedQuestions {\n      difficulty\n      count\n      __typename\n    }\n    numFailedQuestions {\n      difficulty\n      count\n      __typename\n    }\n    numUntouchedQuestions {\n      difficulty\n      count\n      __typename\n    }\n    __typename\n  }\n}\n"
    }
    print("\033[1;32m开始爬取用户刷题进度~\033[0m")
    user_num = 0
    for user in userSlugs:
        time.sleep(0.1)
        params["variables"]["userSlug"] = user
        try:
            response = requests.post(url=url, data=json.dumps(params), headers=headers)
        except:
            print("爬取出错！请检查网络和请求参数等...")
            break
        data = response.json()["data"]["userProfileUserQuestionProgress"]["numAcceptedQuestions"]
        if response.status_code != 200 or data == []:
            print("\033[1;30;41mERROR:   用户：", user, "信息获取失败！请检查用户id是否正确！ \033[0m")
            continue
        total = data[0]["count"] + data[1]["count"] + data[2]["count"]
        print("用户：", user, ":")
        print("简单题：", data[0]["count"], "中等题：", data[1]["count"], "困难题：", data[2]["count"])
        print("\033[1;32m总题数：", total, "\033[0m")
        user_data = {
            'user': user,
            'easy': data[0]["count"],
            'medium': data[1]["count"],
            'hard': data[2]["count"],
            'total': total
        }
        user_progress.append(user_data)
    print(json.dumps(user_progress))
    fp = open('userProgress.json', 'w', encoding='utf-8')
    json.dump(user_progress, fp=fp, ensure_ascii=False)
    print("\033[1;32m用户刷题进度爬取完成~ \033[0m")


if __name__ == '__main__':
    # eg:
    userSlugs = ["continue-xyx", "ki-kyo", "fornary4", "Ylarod"]
    get_user_data(userSlugs=userSlugs)
