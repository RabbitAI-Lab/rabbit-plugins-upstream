## Description: <br>
Slack工作区管家LITE helps agents use a ClawLink OAuth Slack connection to send basic channel messages and list workspace channels and users. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, workspace operators, and team agents use this skill to post simple Slack channel notifications, discover channel IDs, and query workspace members through a ClawLink-managed Slack OAuth connection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send messages to Slack channels when connected with sufficient OAuth scopes. <br>
Mitigation: Review Slack OAuth scopes, confirm channel IDs and message text before posting, and use the skill only in workspaces where the agent is authorized to post. <br>
Risk: The skill can list workspace users and channels through the connected Slack workspace. <br>
Mitigation: Install only where the agent is allowed to inspect workspace membership and channel metadata, and confirm trust in the ClawLink Slack connection. <br>
Risk: Callback URLs can expose results if they are untrusted or misdirected. <br>
Mitigation: Avoid untrusted callback URLs and verify callback destinations before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/slack-workspace-free) <br>
- [Slack Web API](https://slack.com/api/*) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-shaped Slack API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces ClawLink command guidance for Slack channel messages, channel lists, and user lists.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
