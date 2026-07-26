## Description: <br>
Manage Clawdbot agents: discover, profile, track capabilities, define routing hierarchy, and assign tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentandbot-design](https://clawhub.ai/user/agentandbot-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to maintain a Clawdbot agent registry, profile agent capabilities, validate routing rules, and coordinate task delegation with approval and escalation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent delegation and escalation paths can route work broadly or notify external human channels if the registry is accepted unchanged. <br>
Mitigation: Review and edit the registry before installation, remove personal notification identifiers, and restrict external notifications to channels the operator explicitly approves. <br>
Risk: Sensitive tasks may be assigned without the intended human review if approval settings are too permissive. <br>
Mitigation: Keep approval required for sensitive workflows and review auto-accept lists before enabling delegation. <br>
Risk: The permission checker is a lightweight helper and should not be treated as an enforcement boundary. <br>
Mitigation: Use the checker as advisory output only, and enforce assignment policy in the deployment environment or agent runtime. <br>


## Reference(s): <br>
- [Agent manager ClawHub release page](https://clawhub.ai/agentandbot-design/skills/agents-manager) <br>
- [Agent Profile Schema](references/agent-profile-schema.md) <br>
- [Agent Registry](references/agent-registry.md) <br>
- [Health Check Template](references/health-check-template.md) <br>
- [Task Routing Rules](references/task-routing-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON reports or agent cards, shell command examples, configuration edits, and Mermaid graph text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js for bundled scripts.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
