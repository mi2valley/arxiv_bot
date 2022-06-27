import slackweb
import os
import arxiv

text = "test"
slack_id = os.getenv("SLACK_WEBHOOK_URL")
author = "Saikat Guha"

def au_search(author: str):
  search = arxiv.Search(query ='au:"'+author+'"',max_results = 1,sort_by = arxiv.SortCriterion.SubmittedDate)
  return search
"""
def main() -> None:
    # slack
    if slack_id is not None:
        slack = slackweb.Slack(url=slack_id)
        slack.notify(text="test")

if __name__ == "__main__":
    main()
"""
search = au_search(au)
attachments = search.results()[0].as_dict()
slack = slackweb.Slack(url=str(slack_id))
slack.notify(text=text, attachments=attachments)