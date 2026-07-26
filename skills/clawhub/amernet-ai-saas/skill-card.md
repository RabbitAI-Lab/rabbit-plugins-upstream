## Description: <br>
Connect your AI SaaS intelligent agent to any messaging channel via OpenClaw, including WhatsApp, Telegram, Slack, Discord, iMessage, and more. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amernet](https://clawhub.ai/user/amernet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to route messages from connected messaging channels to an Amernet AI SaaS agent and return the agent response. It also supports reset, status, and AI Growth Engine AutoPilot command routing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connected channel messages and stable user identifiers are forwarded to an external SaaS. <br>
Mitigation: Enable the skill only for channels where this processing is intended, notify channel users where required, and avoid channels with sensitive or regulated information until vendor data handling terms are reviewed. <br>
Risk: The configured API key is described as broadly privileged. <br>
Mitigation: Use a dedicated, least-privilege API key if supported and protect the local OpenClaw configuration file. <br>
Risk: AI Growth Engine AutoPilot deploy and pause requests can trigger real actions. <br>
Mitigation: Relay the assistant's confirmation prompt and continue only after the user confirms the exact pipeline. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/amernet/skills/amernet-ai-saas) <br>
- [Amernet AI SaaS portal](https://saas.salesbay.ai) <br>
- [OpenClaw documentation](https://docs.openclaw.ai) <br>
- [OpenClaw website](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Text responses and Markdown guidance with JSON and HTTP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Forwards connected-channel messages and stable user identifiers to an external SaaS API using configured credentials.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
