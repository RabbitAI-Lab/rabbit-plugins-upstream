## Description: <br>
Publish tweets to X (Twitter) using the official Tweepy library. Supports text-only tweets, tweets with images or videos, and returns detailed publish results including tweet ID and URL. Requires X API credentials (API Key, API Secret, Access Token, Access Token Secret). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiangsier-xyz](https://clawhub.ai/user/jiangsier-xyz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to publish text, media tweets, replies, and threads to X from an agent workflow or command line using their own X API credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish tweets, media, replies, and threads using X credentials with write access. <br>
Mitigation: Use a dedicated or test X app/account where possible and install only if granting write-capable X API credentials is acceptable. <br>
Risk: Credentials are required for publishing and could be exposed if copied into source files or logs. <br>
Mitigation: Provide credentials through environment variables, keep them out of source control, and rotate them if exposure is suspected. <br>
Risk: Generated text or selected media may be posted publicly or violate platform/content expectations. <br>
Mitigation: Review tweet text and media before invoking publish commands and follow X platform rules. <br>
Risk: The runtime installs Tweepy from a version range when provisioning its virtual environment. <br>
Mitigation: For production use, pin Tweepy or run in a locked environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jiangsier-xyz/skills/x-publisher) <br>
- [Tweepy Documentation](https://docs.tweepy.org/) <br>
- [X API Documentation](https://developer.twitter.com/en/docs/twitter-api) <br>
- [X Developer Portal](https://developer.twitter.com/en/portal/dashboard) <br>
- [X API Reference](references/x_api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, JSON, Guidance] <br>
**Output Format:** [Command-line text with a JSON result block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include tweet IDs, URLs, creation timestamps, preview text, and thread details when posting succeeds.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
