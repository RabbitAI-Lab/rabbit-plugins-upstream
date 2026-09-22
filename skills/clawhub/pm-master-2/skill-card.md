## Description:

Project and program management skill for technology teams that produces planning, governance, reporting, scheduling, risk, RAID, EVM, stage-gate, SOW parsing, DOCX export, and controlled outbound communication artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[slearnai](https://clawhub.ai/user/slearnai)

### License/Terms of Use:

MIT-0

## Use Case:

Project managers, program managers, delivery leads, and engineering teams use this skill to create and maintain project artifacts for waterfall, agile, iteration, hybrid, and program governance workflows. It is intended for artifact-producing project execution rather than casual project-management advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate core project records such as project.yaml and generated project artifacts.

Mitigation: Install it only in workspaces where project.yaml changes are expected, use backups or dry-run modes for high-impact workflows, and review generated changes before relying on them.

Risk: The outbound email workflow can send external communications when email is enabled and a backend is configured.

Mitigation: Keep email.enabled false unless an administrator has configured a trusted backend and approval process; use dry-run review before any send.

Risk: Approval flags for email and gates are audit labels rather than cryptographic proof of human consent.

Mitigation: Require a reliable approval workflow outside the agent and treat --approve values as recorded attestations to be checked by that workflow.

Risk: SOW parsing can replace existing WBS subtrees.

Mitigation: Use dry-run modes and backups before parsing SOWs or applying generated WBS updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/slearnai/skills/pm-master-2)
- [Publisher profile](https://clawhub.ai/user/slearnai)
- [README](artifact/README.md)
- [Usage guide](artifact/references/usage.md)
- [Lifecycle reference](artifact/references/lifecycle.md)
- [Project schema](artifact/references/project-schema.md)
- [Template index](artifact/references/templates-index.md)
- [Configuration guardrails](artifact/config.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown, YAML, JSON, DOCX exports, Mermaid diagrams, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces and updates project files such as project.yaml, charters, WBS, schedules, risk registers, RAID logs, status reports, dashboards, and audit records.]

## Skill Version(s):

2.2.16 (source: server release evidence, artifact frontmatter, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
