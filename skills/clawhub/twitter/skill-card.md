## Description: <br>
Searches and reads X/Twitter profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces, and supports posting, likes, unlikes, follows, and unfollows after OAuth authorization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bibaofeng](https://clawhub.ai/user/bibaofeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to gather Twitter/X intelligence, monitor public activity, and perform authorized posting or engagement actions through the AIsa relay. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The AIsa API key may be exposed in normal command output or shared logs. <br>
Mitigation: Use a limited, rotatable AIsa API key and avoid running or sharing status/debug output in shared logs. <br>
Risk: The skill can perform public account actions, including publishing, liking, following, and unfollowing from a connected Twitter/X account. <br>
Mitigation: Require explicit user confirmation before publishing or engagement actions, and verify the target account, tweet, text, and media before execution. <br>
Risk: Text or media submitted for posting can disclose confidential information publicly. <br>
Mitigation: Review post content and attachments before submission and avoid posting confidential media or text. <br>


## Reference(s): <br>
- [ClawHub Twitter Skill](https://clawhub.ai/bibaofeng/skills/twitter) <br>
- [AIsa Homepage](https://aisa.one) <br>
- [AIsa API Reference](https://docs.aisa.one/reference/) <br>
- [AIsa Twitter OAuth](references/post_twitter.md) <br>
- [AIsa Twitter Engagement](references/engage_twitter.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and AISA_API_KEY; TWITTER_RELAY_BASE_URL and TWITTER_RELAY_TIMEOUT are optional.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
