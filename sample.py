import slackweb
import os
import argparse
import sys


text = "test"
parser = argparse.ArgumentParser(description='slack env')
parser.add_argument('env', type=str)
#slack_id = os.getenv("SLACK_INCOMING_WEBHOOK_URL")
args = parser.parse_args()
if sys.argv:
  del sys.argv[1:]
#print(type(slack_id))
"""
def main() -> None:
    # slack
    if slack_id is not None:
        slack = slackweb.Slack(url=slack_id)
        slack.notify(text="test")

if __name__ == "__main__":
    main()
"""

slack = slackweb.Slack(url=args.env)
slack.notify(text=text)