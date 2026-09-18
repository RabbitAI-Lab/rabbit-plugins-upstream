## Description:

Generate a daily digest summarizing workspace activity, memory entries, and completed tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and workspace maintainers use this skill for end-of-day reviews, retrospectives, handover summaries, and productivity logs based on workspace memory artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Daily digests can include sensitive content from workspace memory logs and MEMORY.md.

Mitigation: Review and redact generated digests before sharing them outside the workspace or automating delivery to any channel.

Risk: Automated delivery to shared channels can expose workspace context to unintended audiences.

Mitigation: Use only approved destinations for scheduled or chained delivery.

## Reference(s):

- [Daily Digest Reference](references/guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured digest with key events, decisions, files touched, open items, and memory updates.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
