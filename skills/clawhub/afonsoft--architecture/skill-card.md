## Description:

Coordinates architecture documentation under docs/architecture by routing ADRs, design documents, Markdown-native diagrams, editable draw.io artifacts, optional interactive diagrams, and gap audits to the appropriate installed tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to create and maintain repository architecture deliverables, including ADRs, design documents, Markdown-native diagrams, editable draw.io diagrams, and optional interactive architecture artifacts. It routes work to the appropriate installed diagram or audit skill while keeping docs/architecture as the canonical location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional preflight checks may reveal local tool and skill installation paths.

Mitigation: Run the preflight only in repositories where local tool inventory is acceptable, and review its output before sharing logs.

Risk: The workflow relies on delegated diagram and audit skills when they are installed.

Mitigation: Use pinned or preinstalled tooling and review generated architecture files before committing or publishing them.

Risk: User-facing confirmations are expected in Portuguese.

Mitigation: Use this skill in contexts where Portuguese approval prompts are acceptable, especially for gap-analysis gates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/architecture)
- [Publisher Profile](https://clawhub.ai/user/afonsoft)
- [Source Metadata URL](https://github.com/afonsoft/skills)
- [Architecture Inventory Contract](references/architecture-inventory.md)
- [Gap-Analysis Handoff](references/gap-audit-handoff.md)
- [Archify](https://github.com/tt-a1i/archify)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, architecture document templates, diagram source instructions, and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update files under docs/architecture and route work to installed diagram or audit skills.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
