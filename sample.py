import slackweb
import os
import arxiv

text = "test"
slack_id = os.getenv("SLACK_WEBHOOK_URL")
author = "Saikat Guha"

slack = slackweb.Slack(url=str(slack_id))

search = arxiv.Search(
  query = "quantum",
  max_results = 10,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

for result in search.results():
  print(result.title)
  slack.notify(text=result.title)


