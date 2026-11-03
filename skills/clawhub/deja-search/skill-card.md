## Description:

Search the user's past AI coding sessions with the deja CLI to recover earlier decisions, fixes, preferences, and project context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to find decisions and lessons from earlier coding sessions before editing, recommending tools, or revisiting solved issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches may surface text from earlier coding conversations across projects in the current agent context.

Mitigation: Narrow searches when working with sensitive material.

Risk: Recalled instructions may propose changes to global agent rules.

Mitigation: Review proposed global-rule changes before confirming them.

Risk: The supplied artifact review does not establish the external CLI's retention or redaction behavior.

Mitigation: Consult the publisher's privacy documentation before use where retention or redaction matters.

## Reference(s):

- [Deja-vu guide for OpenClaw memory](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)
- [Deja-vu privacy documentation](https://vshulcz.github.io/deja-vu/guide/privacy.html)
- [ClawHub skill release](https://clawhub.ai/vshulcz/skills/deja-search)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Concise Markdown guidance and deja CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface recalled excerpts from prior coding sessions.]

## Skill Version(s):

0.23.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
