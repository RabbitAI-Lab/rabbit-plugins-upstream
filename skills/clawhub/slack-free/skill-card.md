## Description: <br>
slack-free helps agents send plain-text Slack messages to channels or users and read recent channel history through a configured Slack tool and bot token. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to automate basic Slack communication tasks, including posting notifications and reading recent channel messages from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post to Slack and read channel history using a live Bot Token. <br>
Mitigation: Limit the bot to the minimum required Slack scopes and channels, keep the token managed by the agent platform, and verify every target channel, user, and message before execution. <br>
Risk: The release evidence flags unrelated file, API, and command-execution instructions that broaden authority beyond the Slack LITE purpose. <br>
Mitigation: Treat non-Slack file, API, and command-execution guidance as out of scope unless the publisher narrows or removes it, and review the skill before deployment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON Slack action payloads and plain-text Slack message content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Slack Bot Token, appropriate Slack scopes, and known channel or user identifiers.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
