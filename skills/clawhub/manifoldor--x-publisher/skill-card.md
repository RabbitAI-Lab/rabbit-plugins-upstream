## Description: <br>
Publish tweets to X (Twitter) using the official Tweepy library. Supports text-only tweets, tweets with images or videos, and returns detailed publish results including tweet ID and URL. Requires X API credentials (API Key, API Secret, Access Token, Access Token Secret). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to publish text, image, or video tweets from an agent workflow through configured X API credentials. It can also verify that the configured credentials can access the target X account before posting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured X credentials can post from the associated account. <br>
Mitigation: Use the narrowest practical account tokens, store credentials according to the machine's trust model, and review the exact text and media paths before running tweet commands. <br>
Risk: Posts and uploaded media may create platform, policy, or rights issues once published. <br>
Mitigation: Review content for X policy compliance and confirm media usage rights before publishing. <br>


## Reference(s): <br>
- [X API Reference](artifact/references/x_api.md) <br>
- [Tweepy Documentation](https://docs.tweepy.org/) <br>
- [X API Documentation](https://developer.twitter.com/en/docs/twitter-api) <br>
- [X Developer Portal](https://developer.twitter.com/en/portal/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Text] <br>
**Output Format:** [Markdown guidance with shell commands and JSON publish results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires X API credentials and optional media file paths; successful posts include tweet ID, URL, timestamp, and text preview.] <br>

## Skill Version(s): <br>
1.0.6 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
