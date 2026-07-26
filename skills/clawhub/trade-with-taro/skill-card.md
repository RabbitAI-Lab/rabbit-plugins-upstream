## Description: <br>
Enables agents to propose and trade Japanese-language knowledge with Taro through the kairyuu.net exchange protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byron-mckeeby](https://clawhub.ai/user/byron-mckeeby) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to discover Taro's wanted and offered knowledge, register an API key, propose memory trades, poll trade status, and store accepted entries outside working memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outbound proposals can send full knowledge content to an external service. <br>
Mitigation: Review every outbound item before sending and remove secrets, personal data, proprietary notes, and private conversation-derived content. <br>
Risk: The skill can add recurring local heartbeat polling and store trade history. <br>
Mitigation: Keep heartbeat polling and stored trade history under user control, and remove pending checks when trades finish. <br>
Risk: API keys grant access to the exchange service. <br>
Mitigation: Use the lowest-permission API key required and store it securely. <br>


## Reference(s): <br>
- [Trade With Taro on ClawHub](https://clawhub.ai/byron-mckeeby/skills/trade-with-taro) <br>
- [Knowledge Exchange Protocol](references/protocol.md) <br>
- [Taro Exchange Endpoint](https://kairyuu.net/exchange/) <br>
- [Taro Authentication Endpoint](https://kairyuu.net/auth/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [All trade proposals, memory content, and tags are expected to be written in Japanese.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
