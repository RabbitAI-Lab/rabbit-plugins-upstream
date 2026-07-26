## Description: <br>
Give an AI agent real communication channels - Slack, Discord, Telegram, email, X, SMS - behind one on_message handler via caspian-sdk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[trycaspian](https://clawhub.ai/user/trycaspian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add real messaging channels to an AI agent, route inbound messages through one handler, send replies, and verify channel setup across email, Slack, Discord, Telegram, SMS, X, and related provider flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can connect real messaging accounts, read incoming messages, send replies, and in some channels initiate outbound messages. <br>
Mitigation: Use least-privilege or test credentials, confirm each account connection and outbound capability with the developer, and verify message-sending behavior before connecting production channels. <br>
Risk: The skill includes billing autopay and spend-limit setup that could create recurring payment behavior. <br>
Mitigation: Do not configure billing autopay, top-ups, or spend limits unless the developer explicitly requests them and confirms the intended recurring payment behavior. <br>
Risk: The skill handles powerful API keys, bot tokens, OAuth links, and provider credentials. <br>
Mitigation: Store credentials in environment variables or secret storage, avoid placing production tokens in chat, and rotate or revoke test credentials after validation. <br>


## Reference(s): <br>
- [Caspian Website](https://trycaspianai.com) <br>
- [Caspian REST API Reference](https://api.trycaspianai.com/docs) <br>
- [ClawHub Skill Page](https://clawhub.ai/trycaspian/skills/caspian) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/trycaspian) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, API requests, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CASPIAN_API_KEY and may guide OAuth, token, billing, and messaging-provider setup.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
