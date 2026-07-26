## Description: <br>
Read and send messages via Beeper CLI across WhatsApp, Telegram, Signal, Instagram, Twitter/X, LinkedIn, Facebook Messenger, and other connected networks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nerveband](https://clawhub.ai/user/nerveband) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to query Beeper chats, read recent messages, search conversations, and send messages across connected networks after explicit user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access private chats and message history through the Beeper API. <br>
Mitigation: Install only when the operator is comfortable granting chat access, keep the Beeper API on localhost where possible, and limit exposure of the bearer token. <br>
Risk: Send commands can post messages across connected networks. <br>
Mitigation: Show the exact recipient, network, and complete message draft, then wait for explicit user approval before any send operation. <br>
Risk: The wrapper passes the bearer token to a hard-coded Beeper CLI binary that is not included in the reviewed artifact. <br>
Mitigation: Verify the CLI binary at the configured path before installation or execution. <br>
Risk: The wrapper may auto-launch Beeper Desktop. <br>
Mitigation: Expect Beeper Desktop to start during use and confirm this behavior is acceptable for the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nerveband/skills/beeper-api-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; CLI responses may be JSON, text, or markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Beeper Desktop API access and BEEPER_TOKEN; send operations require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
