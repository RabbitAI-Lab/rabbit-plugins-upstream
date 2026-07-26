## Description: <br>
Create and send native Slack Block Kit messages, including tables, code cards, structured layouts, buttons, inputs, and rich Slack blocks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bill492](https://clawhub.ai/user/bill492) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to produce Slack messages that need structure beyond plain mrkdwn, including portable OpenClaw presentation blocks, native Slack Block Kit layouts, tables, charts, containers, inputs, and buttons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live Slack posting examples can expose token values or send externally visible messages to the wrong workspace, channel, or thread. <br>
Mitigation: Scope Slack bot tokens to the intended workspace and channels, avoid printing token values in logs, and verify channel and thread identifiers before posting. <br>
Risk: Buttons, inputs, broadcasts, and other interactive blocks may trigger visible or destructive workflows if wired without review. <br>
Mitigation: Review generated blocks and confirm externally visible or destructive interactive workflows before sending or enabling them. <br>
Risk: Raw Block Kit payloads may omit accessibility fallback text or exceed Slack layout constraints. <br>
Mitigation: Include a text fallback for messages with blocks and run the bundled sample validator before publishing or sharing changed samples. <br>


## Reference(s): <br>
- [Slack Block Kit Reference](https://api.slack.com/block-kit/reference) <br>
- [Slack chat.postMessage API](https://slack.com/api/chat.postMessage) <br>
- [Slack Thinking Steps](https://api.slack.com/partners/thinking-steps) <br>
- [ClawHub Skill Page](https://clawhub.ai/bill492/skills/slack-block-kit) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, JSON, Code, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown guidance with Slack Block Kit JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local sample JSON, table generation guidance, sample validation commands, and Slack posting patterns.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
