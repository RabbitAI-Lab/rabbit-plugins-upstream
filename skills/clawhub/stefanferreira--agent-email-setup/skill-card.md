## Description: <br>
Set up dedicated email accounts for AI agents with role separation, approval workflows, sandbox testing, and production deployment checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stefanferreira](https://clawhub.ai/user/stefanferreira) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to set up and govern dedicated email identities for agents that communicate externally. It provides setup, approval, forwarding, testing, monitoring, and migration guidance for agent email workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill hard-codes broad forwarding and CC behavior to a personal Gmail address. <br>
Mitigation: Replace the domain, agent names, and forwarding or CC addresses with accounts you control; use a managed mailbox for business communications. <br>
Risk: The skill includes local script and knowledge-transfer steps beyond email setup. <br>
Mitigation: Review any referenced scripts and copied files before running provisioning or knowledge-transfer commands. <br>
Risk: Agent email workflows can send external messages if approval steps are skipped. <br>
Mitigation: Keep the explicit approval requirement for every outbound email and preserve sent-message logging for audit review. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/stefanferreira/agent-email-setup) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with checklists, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes approval, forwarding, credential-management, monitoring, testing, and migration guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
