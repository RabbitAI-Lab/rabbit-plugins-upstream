## Description: <br>
X Dm Auto Chat helps an agent scan X/Twitter direct-message inboxes, read conversation history, generate persona-based replies, send messages, search users, and start new conversations from the user's authenticated browser session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to automate X/Twitter DM workflows that they could perform in their own logged-in browser, including processing pending replies and initiating permitted outreach with persona-guided message text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read private-message data from a logged-in X/Twitter browser session. <br>
Mitigation: Install and run it only for accounts and conversations where the user is authorized, and avoid saving or sharing DM contents outside the intended workflow. <br>
Risk: The skill can send DMs and may be used for unsolicited or bulk outreach. <br>
Mitigation: Require explicit user approval for outreach scope and message content, follow the built-in serial execution and rate-control guidance, and stop on send failures instead of retrying blindly. <br>
Risk: Recipient and message logs may contain sensitive personal or conversation data. <br>
Mitigation: Delete or protect any saved logs, keep only the minimum status data needed for resumability, and avoid storing full message bodies unless required by the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/x-dm-auto-chat) <br>
- [Publisher profile](https://clawhub.ai/user/browseract-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON status/results from browser automation helpers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include per-conversation or per-recipient status, failure reasons, and generated command sequences for browser-act execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
