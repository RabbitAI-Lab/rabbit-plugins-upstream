## Description:

FDE Skill helps frontline deployment engineers structure enterprise AI rollouts by guiding discovery, quantification, delivery, audit, and continuous improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Frontline deployment engineers and enterprise AI teams use this skill to diagnose business workflows, identify AI-ready nodes, build knowledge and ontology artifacts, guide deployment, and maintain audit-backed continuous improvement. It is intended for agent-assisted enterprise AI governance rather than general application coding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local, persistent, and remote operational authority.

Mitigation: Install and test it first in an isolated environment or dedicated enterprise profile with least-privilege access.

Risk: Activation can involve persistent configuration writes, hooks, daemon behavior, workflow activation, model operations, or cloud operations.

Mitigation: Require explicit human confirmation before enabling persistent changes or remote operations, and keep an auditable record of approvals.

Risk: Running activation commands with sensitive credentials available could expose repository, cloud, SSH, browser-session, or production access.

Mitigation: Run commands from a non-privileged shell without production secrets or active high-value sessions in the environment.

Risk: Installer and external package behavior may not be sufficiently reviewed or pinned for safe default installation.

Mitigation: Review, pin, and verify installer dependencies before enterprise deployment.

## Reference(s):

- [FDE Skill on ClawHub](https://clawhub.ai/kongfangxun/skills/sofagent)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)
- [Minimal Change Engineer Template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Code Reviewer Template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, checklists, structured reports, and generated configuration or skill artifacts when the agent invokes supported tools.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation or update of local workflow, audit, ontology, knowledge, and configuration files when explicitly activated by the user and available tooling.]

## Skill Version(s):

1.4.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
