## Description: <br>
Customer support via Crisp API for checking, reading, searching, and responding to Crisp inbox messages using configured Crisp credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paul-phan](https://clawhub.ai/user/paul-phan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Customer support operators and developers use this skill to let an agent inspect Crisp inbox conversations, search conversation history, send customer replies, and update conversation status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify live Crisp customer support conversations using a plugin token. <br>
Mitigation: Install only when agent access to the Crisp inbox is intended, and grant the narrowest Crisp scopes possible. <br>
Risk: Customer replies and conversation status changes can affect real support interactions. <br>
Mitigation: Require explicit human approval before sending replies, marking conversations read, or resolving conversations. <br>
Risk: Crisp credentials can expose customer support data if shared through shell profiles or repositories. <br>
Mitigation: Keep CRISP_WEBSITE_ID, CRISP_TOKEN_ID, and CRISP_TOKEN_KEY out of shared files and rotate tokens if exposure is suspected. <br>


## Reference(s): <br>
- [Crisp REST API Reference](artifact/references/api.md) <br>
- [Crisp Marketplace](https://marketplace.crisp.chat/) <br>
- [Crisp API Base URL](https://api.crisp.chat) <br>
- [Crisp Skill on ClawHub](https://clawhub.ai/paul-phan/skills/crisp) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CRISP_WEBSITE_ID, CRISP_TOKEN_ID, and CRISP_TOKEN_KEY environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
