import slackweb
import os
import arxiv

text = "test"
slack_id = os.getenv("SLACK_WEBHOOK_URL")
#author = "Saikat Guha"

slack = slackweb.Slack(url=str(slack_id))

search = arxiv.Search(
  query = "quantum",
  max_results = 5,
  sort_by = arxiv.SortCriterion.SubmittedDate
)


for result in search.results():
  attachments = [
        {
        "mrkdwn_in": ["text"],
            "color": "#36a64f",
            "text": result.summary,
            "thumb_url": "http://placekitten.com/g/200/200",
            "footer": "footer",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
            "ts": 123456789
        }
    ]
  slack.notify(text=result.title, attachments=attachments)


