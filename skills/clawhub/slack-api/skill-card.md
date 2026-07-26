## Description: <br>
Slack provides Maton-managed OAuth access to Slack APIs for sending messages, managing channels, searching conversations, and automating workspace workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access Slack workspaces through Maton for messaging, channel management, user lookup, search, reactions, files, and workflow automation. Because the skill can read and modify Slack data, users should review requested actions before approval, especially destructive or private-channel operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub Slack Skill](https://clawhub.ai/byungkyu/skills/slack-api) <br>
- [Maton](https://maton.ai) <br>
- [Maton CLI Manual](https://cli.maton.ai/manual) <br>
- [Slack API Methods](https://api.slack.com/methods) <br>
- [Slack Web API Reference](https://api.slack.com/web) <br>
- [Slack Block Kit Reference](https://api.slack.com/reference/block-kit) <br>
- [Slack Rate Limits](https://api.slack.com/docs/rate-limits) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown guidance with CLI, HTTP, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a Slack OAuth connection managed through Maton.] <br>

## Skill Version(s): <br>
1.0.11 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
