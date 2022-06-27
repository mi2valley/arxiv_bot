import slackweb
import os
import arxiv

text = "test"
slack_id = os.getenv("SLACK_WEBHOOK_URL")
l = arxiv.query(query='au:"Saikat Guha"')
"""
def main() -> None:
    # slack
    if slack_id is not None:
        slack = slackweb.Slack(url=slack_id)
        slack.notify(text="test")

if __name__ == "__main__":
    main()
"""
attachments = l[0].as_dict()
slack = slackweb.Slack(url=str(slack_id))
slack.notify(text=text, attachments=attachments)