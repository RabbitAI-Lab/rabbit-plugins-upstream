## Description:

Helps agents rewrite prose naturally, edit fiction, audit long-form continuity, and check revisions against original text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT

## Use Case:

Writers, editors, and developers use this skill to humanize drafts, edit and continue fiction, and review multilingual rewrites and long manuscripts for fidelity, style, and continuity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation and local draft access may expose more project material than intended.

Mitigation: Use only the needed writing modules and limit file access to the relevant project and drafts.

Risk: An exposed MCP service may allow unwanted access to project files or coordination tasks.

Mitigation: Set a narrow project root; keep HTTP on loopback unless protected by a strong bearer token behind HTTPS.

Risk: Generated fixes or audits may alter meaning or miss important errors.

Mitigation: Review fixes and audit reports before applying them to important documents.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/whh110112/skills/human-writing-skills)
- [Long-form consistency guide](docs/long-form-consistency.md)
- [Editing and fidelity guide](docs/editing-tools.md)
- [Agent orchestration guide](docs/agent-orchestration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Audit reports]

**Output Format:** [Prose, editorial guidance, and structured review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce revision prompts and local audit files.]

## Skill Version(s):

0.15.3 (source: ClawHub release metadata and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
