## Description:

FDE Skill helps frontline deployment engineers guide enterprise AI rollout by constraining agent behavior, auditing changes, preserving lessons learned, and supporting ongoing optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, deployment engineers, and enterprise AI teams use this skill to structure FDE discovery, quantify AI deployment opportunities, produce delivery artifacts, and apply audit and human-review gates around agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is disclosed as a privileged enterprise automation platform with high-impact shell, installation, persistence, MCP, daemon, and sustain-mode behaviors.

Mitigation: Inspect the installer and package version before use, run first in a test environment, and require administrator control for custom overrides and daemon or sustain-mode features.

Risk: Broad MCP roles or tool access can expand the impact of workflow, audit, rollback, training, PR, and deployment actions.

Mitigation: Restrict MCP roles and tools to the minimum required for the deployment task and keep human review gates enabled for destructive or high-impact actions.

Risk: Unpinned activation through npx or similar package execution can run a package version the reviewer has not inspected.

Mitigation: Use pinned, reviewed package versions and verify the resolved artifact before activating the skill in an enterprise environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Engineering minimal-change template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Engineering code-reviewer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose enterprise workflow, ontology, audit, deployment, and review artifacts for human confirmation.]

## Skill Version(s):

1.4.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
