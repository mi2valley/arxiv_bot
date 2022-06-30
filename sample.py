import slackweb
import os
import arxiv
import datetime
from dataclasses import dataclass

#slack_id = os.getenv("SLACK_WEBHOOK_URL")
#slack = slackweb.Slack(url=str(slack_id))

@dataclass
class Result:
    url: str
    title: str
    abstract: str
    words: list
    score: float = 0.0

def main():
    subject = 'cat:physics.* OR cat:quant-ph'
    keywords = {'quantum memory': 3, 'atomic frequency comb': 3, 'quantum internet': 2, 'quantum repeater': 2, 'quantum walk': 2, 'entanglement distribution': 2, 'photon': 1}
    score_threshold = 2

    day_before_yesterday = datetime.datetime.today() - datetime.timedelta(days=2)
    day_before_yesterday_str = day_before_yesterday.strftime('%Y%m%d')
    # datetime format YYYYMMDDHHMMSS
    arxiv_search = f'({subject}) AND ' \
                  f'submittedDate:' \
                  f'[{day_before_yesterday_str}000000 TO {day_before_yesterday_str}235959]'
    papers = arxiv.Search(query=arxiv_search,
                           max_results=100,
                           sort_by='submittedDate')
    results = search_keyword(list(papers), keywords, score_threshold)

    slack_id = os.getenv("SLACK_WEBHOOK_URL")
    notify(results, slack_id)


def search_keyword(
        papers: list, keywords: dict, score_threshold: float
        ) -> list:
    results = []

    for paper in papers:
        url = paper['arxiv_url']
        title = paper['title']
        abstract = paper['summary']
        score, hit_keywords = calc_score(abstract, keywords)
        if (score != 0) and (score >= score_threshold):
            result = Result(
                    url=url, title=title, abstract=abstract,
                    score=score, words=hit_keywords)
            results.append(result)
    return results


def calc_score(abst: str, keywords: dict) -> (float, list):
    sum_score = 0.0
    hit_kwd_list = []

    for word in keywords.keys():
        score = keywords[word]
        if word.lower() in abst.lower():
            sum_score += score
            hit_kwd_list.append(word)
    return sum_score, hit_kwd_list

def notify(results: list, slack_id: str) -> None:
    star = '*'*80
    today = datetime.date.today()
    n_papers = len(results)
    text = f'{star}\n \t \t {today}\tnum of papers = {n_papers}\n{star}'
    send2app(text, slack_id)
    # descending
    for result in sorted(results, reverse=True, key=lambda x: x.score):
        url = result.url
        title = result.title
        abstract = result.abstract
        word = result.words
        score = result.score

        text = f'\n score: `{score}`'\
               f'\n hit keywords: `{word}`'\
               f'\n url: {url}'\
               f'\n title:    {title}'\
               f'\n abstract:'\
               f'\n \t {abstract}'\
               f'\n {star}'

        send2app(text, slack_id)

def send2slack(text: str, slack_id: str) -> None:
    # slack
    if slack_id is not None:
        slack = slackweb.Slack(url=slack_id)
        slack.notify(text=text)

  #slack.notify(text=result.title, attachments=attachments)


if __name__ == "__main__":
    main()