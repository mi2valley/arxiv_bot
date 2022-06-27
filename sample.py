import slackweb
import os

slack_id = os.getenv("SLACK_INCOMING_WEBHOOK_URL")
if slack_id is not None:
  slack = slackweb.Slack(url=slack_id)
  slack.notify(text="hello world")