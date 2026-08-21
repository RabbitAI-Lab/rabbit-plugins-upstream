## Description:

批判性思维·学会提问 is a Chinese-language skill that helps agents analyze arguments by identifying issues, conclusions, reasons, assumptions, fallacies, evidence quality, omitted information, alternative causes, and appropriately qualified conclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaxinmmhh](https://clawhub.ai/user/jiaxinmmhh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to evaluate articles, advertisements, social posts, expert claims, reports, policy arguments, and their own drafts for reasoning quality. It provides a reusable critique workflow for argument structure, evidence reliability, fallacies, cognitive bias, data framing, missing information, and conditional conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad analysis requests or in conversations where the user does not expect Chinese-language critical-thinking guidance.

Mitigation: Use it when Chinese-language argument analysis is desired, or narrow activation wording and locale metadata before deployment.

Risk: The skill can produce confident critique guidance even when the source argument or evidence is incomplete.

Mitigation: Ask for missing context, cite uncertainty, and present qualified conclusions rather than definitive judgments when evidence is limited.

## Reference(s):

- [Critical-thinking reference knowledge pack](artifact/references/critical-thinking.md)
- [ClawHub skill page](https://clawhub.ai/jiaxinmmhh/skills/critical-thinking)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown critique with structured argument-analysis sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code, environment access, credential handling, or persistence is present in the artifact.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
