## Description:

Provides a six-dimension framework for reviewing monthly WorkBuddy conversations, while the shipped utility exports conversations rather than generating the advertised diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users can use the six-dimension framework to reflect on their monthly conversations and priorities. The included utility lists or exports individual conversations; it does not produce or schedule the claimed monthly report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive conversation history may be exported into persistent plaintext files.

Mitigation: Review what will be exported, restrict access to the output files, and delete them when no longer needed.

Risk: Documentation promises scheduled six-dimension analysis, but the shipped utility only lists and exports conversations.

Mitigation: Do not rely on automatic diagnosis or scheduling without independently confirming those capabilities.

Risk: The utility appends promotional text and a link to its terminal output.

Mitigation: Inspect the output before sharing it, and remove unwanted promotional content.

## Reference(s):

- [WorkBuddy Monthly Checkup on ClawHub](https://clawhub.ai/guipi888/skills/ch-build-7ky6p0bu)
- [WorkBuddy](https://www.workbuddy.cn)

## Skill Output:

**Output Type(s):** [Markdown, Text, JSON]

**Output Format:** [Markdown diagnostic report described in documentation; shipped utility exports conversations as Markdown, plain text, or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports may include full message text and are written as local plaintext files.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
