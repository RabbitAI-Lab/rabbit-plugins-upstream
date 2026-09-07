## Description:

stellar-trails applies a six-phase agent workflow to coding, document, data, planning, and analysis tasks with traceability gates, approval pauses, verification steps, and delivery reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add structured task discipline around software changes, document generation, data processing, planning, and analysis. It is intended to guide agents through specification, planning, implementation, verification, and delivery with explicit traceability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives itself broad automatic control over agent behavior, shell and network commands, updates, local services, credential handling, and persistent logs.

Mitigation: Install only in isolated environments where those behaviors are acceptable, and review or gate the automation before use with valuable tokens or unrelated local services.

Risk: The skill can write cross-session logs and profiles that may retain task or user context.

Mitigation: Avoid sensitive information in managed workspaces and review or clear stored logs and profiles before sharing or reusing environments.

Risk: The skill can start local web servers and terminate local Python processes.

Mitigation: Use it in disposable development environments and confirm that local services on the expected ports are not needed for unrelated work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [Publisher profile](https://clawhub.ai/user/hoshiyomix)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with checklists, phase markers, shell command blocks, and generated artifacts when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes traceability IDs, approval gates, verification notes, and delivery reports.]

## Skill Version(s):

9.15.2 (source: SKILL.md metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
