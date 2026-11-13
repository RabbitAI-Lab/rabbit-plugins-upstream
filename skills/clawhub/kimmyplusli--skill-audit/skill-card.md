## Description:

Skill Audit guides an agent through a ClawHub pre-publish security checklist for OpenClaw skill folders and emits a scored pass/fail report with concrete fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kimmyplusli](https://clawhub.ai/user/kimmyplusli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill publishers, and reviewers use this skill to audit OpenClaw skills before publishing or installing them. It checks code behavior, SKILL.md instructions, release metadata, and discoverability against ClawHub publishing expectations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit commands can be unsafe if a user pastes untrusted paths or text directly into a shell.

Mitigation: Use concrete, quoted, validated paths when adapting the skill's grep and find commands.

Risk: A mechanical checklist can miss semantic prompt-injection instructions written in prose.

Mitigation: Read the audited skill's instructions as agent-facing text and report any instruction to contact external services, read unrelated files, or hide output.

Risk: Audit output is advisory and could introduce incorrect or misleading publication guidance if accepted without review.

Mitigation: Review findings and scan the audited skill before publishing, installing, or deploying it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kimmyplusli/skills/skill-audit)
- [OpenClaw](https://openclaw.ai)
- [checklist.md](artifact/checklist.md)
- [README.md](artifact/README.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown scored audit report with pass, warn, and fail findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file and command evidence, declaration diff results, scoring, and concrete remediation guidance.]

## Skill Version(s):

0.2.1 (source: frontmatter, changelog, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
