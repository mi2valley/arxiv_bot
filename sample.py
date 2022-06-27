import slackweb
import os

text = "test"
slack_id = os.getenv("SLACK_WEBHOOK_URL")
print(type(slack_id))
"""
def main() -> None:
    # slack
    if slack_id is not None:
        slack = slackweb.Slack(url=slack_id)
        slack.notify(text="test")

if __name__ == "__main__":
    main()
"""

slack = slackweb.Slack(url=str(slack_id))
slack.notify(text=text)