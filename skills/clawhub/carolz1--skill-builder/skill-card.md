## Description:

Build, modify, optimize, or review AI agent skills across platforms with a low-friction workflow for intent capture, drafting, self-testing, review, and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carolz1](https://clawhub.ai/user/carolz1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to turn repeatable workflows into skill packages, improve existing skills, or review drafts with structured quality checks and minimal back-and-forth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can draft, edit, evaluate, and optionally install other skills, so generated skill content may affect future agent behavior.

Mitigation: Review generated or modified skills before confirming installation, and keep installation as a separate user-confirmed step.

Risk: The skill uses broad activation language and silent capability checks, which can make it active in loosely described workflow-capture requests.

Mitigation: Confirm the intended task, output format, and testing path before making file changes or installation changes.

Risk: Full evaluation workflows may save user-provided prompts to local evaluation files.

Mitigation: Avoid including sensitive business or personal wording in evaluation prompts unless local storage is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/carolz1/skills/skill-builder)
- [Server-resolved GitHub provenance](https://github.com/CarolZ1/skill-builder)
- [README](README.md)
- [Skill Structure Guide](references/skill-structure-guide.md)
- [Trigger Writing Guide](references/trigger-writing-guide.md)
- [Quality Checklist](references/quality-checklist.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional code blocks, file edits, shell commands, and structured review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or revise skill package files and evaluation prompts when the host environment supports filesystem access.]

## Skill Version(s):

1.0.0 (source: frontmatter); release metadata version 0.1.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
