## Description: <br>
Manage content, chats, subscribers, and earnings on the Fanvue creator platform via OAuth 2.0 API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[igorls](https://clawhub.ai/user/igorls) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to authenticate with Fanvue and automate creator-account workflows for chats, posts, media, subscribers, and earnings insights. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents toward personalized or mass subscriber messaging using sensitive audience and spending data. <br>
Mitigation: Require manual approval before sending personalized or mass messages, and keep recipient targeting and message content reviewable. <br>
Risk: Subscriber lists, spender analytics, earnings data, OAuth tokens, and signed media URLs are sensitive account data. <br>
Mitigation: Limit OAuth scopes to the workflow, restrict access to fetched data, protect tokens, and avoid retaining signed media URLs longer than necessary. <br>


## Reference(s): <br>
- [Fanvue API Reference](api-reference.md) <br>
- [Fanvue API Documentation](https://api.fanvue.com/docs) <br>
- [OAuth 2.0 Guide](https://api.fanvue.com/docs/authentication/quick-start) <br>
- [Fanvue Developer Portal](https://fanvue.com/developers/apps) <br>
- [Fanvue App Starter Kit](https://github.com/fanvue/fanvue-app-starter) <br>
- [ClawHub Fanvue Skill](https://clawhub.ai/igorls/skills/fanvue) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with TypeScript, HTTP, JSON, and shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes OAuth setup guidance, Fanvue API request examples, response schemas, and agent workflow guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
