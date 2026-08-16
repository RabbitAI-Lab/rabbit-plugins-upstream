## Description:

Helps agent users, skill authors, maintainers, and teams create practical workflows, checklists, analysis, code changes, and decision support for Nano Banana Pro-style productivity needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External agent users, skill authors, maintainers, and teams use this skill to turn Nano Banana Pro-style workflow demand into actionable plans, templates, checklists, analysis, code changes, or implementation guidance. It is intended for local-hardware-friendly productivity support rather than cloud-only training or deployment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms may activate the skill on generic image, edit, generate, pro, nano, or banana requests.

Mitigation: Prefer explicit invocation or narrow trigger terms in agent environments that support trigger control.

Risk: Workflow or implementation guidance could be incorrect or mismatched to the user's environment.

Mitigation: Review generated plans, code, shell commands, and configuration before applying them, and validate results against the stated success criteria.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub release page](https://clawhub.ai/kyro-ma/skills/work-productivity-nano-banana-workflow-helper)
- [Popular ClawHub skill demand: Nano Banana Pro](https://clawhub.ai/skills/nano-banana-pro)
- [Popular ClawHub skill demand: Nano Pdf](https://clawhub.ai/skills/nano-pdf)
- [Skill Quality Report - 2026-08-01](https://github.com/weiflycc-cmd/awesome-copilot/issues/62)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, validation notes, and remaining risks when relevant.]

## Skill Version(s):

0.20260815.40440 (source: evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
