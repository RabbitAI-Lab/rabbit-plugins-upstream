## Description:

Skill Factory helps agents design, scaffold, review, and package new OpenClaw skills from domain descriptions using a seven-phase creation protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw skill authors use this skill to design, scaffold, review, and package new skills from domain descriptions. It guides agents through needs analysis, architecture design, reference creation, template creation, quality checks, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skills may include unsafe trigger conditions, excessive tool permissions, poor credential handling, risky file-write behavior, or persistent unsafe instructions.

Mitigation: Review every generated skill before enabling it, including triggers, permissions, credential handling, file-write behavior, and persistence-sensitive instructions.

Risk: Using the skill for high-impact domains or workflows involving accounts, money, public content, or private data can amplify mistakes in generated skill behavior.

Mitigation: Require additional human review and restrict permissions before using generated skills in high-impact or sensitive workflows.

Risk: Skill creation can overwrite existing skill files or accidentally include secrets if the generated package is accepted without review.

Mitigation: Confirm before overwriting existing skill files and run a secret or security scan before claiming a generated skill is ready.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-factory)
- [README](artifact/README.md)
- [Skill anatomy](artifact/references/skill-anatomy.md)
- [Design patterns](artifact/references/design-patterns.md)
- [Quality framework](artifact/references/quality-framework.md)
- [Common pitfalls](artifact/references/common-pitfalls.md)
- [Skill creation template](artifact/templates/skill-creation-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with code blocks and file-structure guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce complete skill package content, templates, review checklists, and installation guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
