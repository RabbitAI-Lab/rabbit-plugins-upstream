## Description: <br>
Publish tweets to X (Twitter) using the official Tweepy library, including text-only tweets, media tweets, replies, and reply-chained threads, with detailed publish results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiangsier-xyz](https://clawhub.ai/user/jiangsier-xyz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to verify X API credentials and publish tweets, media posts, replies, or multi-tweet threads from a configured X account. It is suited for workflows where an agent needs to prepare and execute X publishing commands with user-provided credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish to a real X account using the user's credentials. <br>
Mitigation: Use a test account or review each post and thread before running the publish commands. <br>
Risk: X API credentials grant account access and could be misused if exposed. <br>
Mitigation: Keep X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, and X_ACCESS_TOKEN_SECRET private, scoped, and out of committed files. <br>
Risk: Public posts may be copied, archived, or redistributed even if later deleted. <br>
Mitigation: Treat all generated tweets, media, replies, and threads as public records before publishing. <br>
Risk: Published content or uploaded media may violate platform rules or third-party rights. <br>
Mitigation: Check X platform rules and confirm uploaded media is licensed or authorized before posting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jiangsier-xyz/skills/x-publisher) <br>
- [Publisher Profile](https://clawhub.ai/user/jiangsier-xyz) <br>
- [Tweepy Documentation](https://docs.tweepy.org/) <br>
- [X API Documentation](https://developer.twitter.com/en/docs/twitter-api) <br>
- [X Developer Portal](https://developer.twitter.com/en/portal/dashboard) <br>
- [X API Reference](references/x_api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; runtime scripts print human-readable status text and JSON objects.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, and X_ACCESS_TOKEN_SECRET environment variables; X_HTTP_PROXY is optional.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
