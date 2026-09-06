## Description:

stellar-trails provides a six-phase workflow wrapper for agent tasks, adding activation checks, traceability IDs, phase gates, scope commitment, and task-tier adaptation across coding, documentation, planning, and data work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to apply structured planning, implementation, verification, and delivery discipline to general-purpose agent work. It is suited to coding, document, visualization, data-processing, and multi-step planning tasks where traceability and phase gates matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Startup actions may update the skill, start persistent services, kill port listeners, and write cross-session state.

Mitigation: Review before installation and make startup actions explicit, opt-in, and bounded before using the skill in shared or sensitive environments.

Risk: The startup workflow can touch credentials or interfere with important Python services on port 3000.

Mitigation: Avoid running it around valuable GitHub tokens, sensitive task history, shared networks, or important services on port 3000 unless those behaviors are removed or constrained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [Publisher profile](https://clawhub.ai/user/hoshiyomix)
- [Workflow phases](artifact/procedure/phases.md)
- [Architecture](artifact/knowledge/architecture.md)
- [Code standards](artifact/constraints/code-standards.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown workflow reports, phase markers, checklists, plans, verification notes, shell command blocks, and task-specific code or configuration when required.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow depth adapts by task complexity; higher-complexity tasks may include explicit approval gates before implementation.]

## Skill Version(s):

9.15.1 (source: evidence release, SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
