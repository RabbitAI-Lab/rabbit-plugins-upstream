## Description: <br>
Manage AgentMail inboxes and messages by creating disposable inboxes, sending and receiving email, and listing messages through the AgentMail CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stepandel](https://clawhub.ai/user/stepandel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agents use this skill to configure the AgentMail CLI, create disposable inboxes, send messages, and read or delete AgentMail messages during email-enabled workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an AgentMail API key, which could expose account capabilities if stored or shared carelessly. <br>
Mitigation: Use task-scoped AGENTMAIL_API_KEY values on shared machines and protect or remove ~/.agentmail/config.json when persistent setup is not needed. <br>
Risk: The agent can send and read AgentMail messages once configured. <br>
Mitigation: Install only when the workflow requires email access and review recipients, message contents, and inbox identifiers before sending or reading sensitive mail. <br>
Risk: Inbox deletion and message deletion can remove inboxes or entire message threads. <br>
Mitigation: Require explicit approval before deleting inboxes or messages, especially in shared or persistent AgentMail accounts. <br>


## Reference(s): <br>
- [agentmail-cli ClawHub listing](https://clawhub.ai/stepandel/skills/agentmail-cli) <br>
- [AgentMail](https://agentmail.to) <br>
- [agentmail-cli homepage](https://github.com/stepandel/agentmail-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recommends --json for machine-readable AgentMail CLI output and requires AGENTMAIL_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
