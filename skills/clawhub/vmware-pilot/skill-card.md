## Description:

vmware-pilot helps an agent design, approve, execute, and manage multi-step VMware workflows through companion VMware skills, with human approval gates and explicit best-effort rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to coordinate VMware incident response, maintenance, deployment, compliance, and rollback workflows that span multiple companion skills. It is intended for multi-step work that needs checkpoints, approvals, and recorded undo actions rather than single VMware operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external runtime package.

Mitigation: Install only in an environment where the vmware-pilot package source is trusted, prefer the pinned installed entry point over uvx, and verify package provenance separately.

Risk: Broad workflow dispatch can lead an agent toward production-changing actions through companion VMware skills.

Mitigation: Review every workflow step, target, parameter, and approval message before execution, and run companion skills with least-privilege service accounts.

Risk: Rollback is explicit and best-effort, so failed work may require manual follow-up.

Mitigation: Confirm rollback intent with the user, inspect recorded rollback actions before running them, and manually undo any dispatched steps that the workflow engine did not record as successful.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-pilot)
- [VMware Pilot Homepage](https://github.com/vmware-skills/VMware-Pilot)
- [Capabilities](references/capabilities.md)
- [Workflow Design](references/workflow-design.md)
- [Integration Patterns](references/integration-patterns.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Templates](references/templates.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with workflow plans, tool-call guidance, YAML snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workflow identifiers, step parameters, approval messages, and rollback guidance.]

## Skill Version(s):

1.11.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
