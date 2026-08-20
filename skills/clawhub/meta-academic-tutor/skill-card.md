## Description:

Meta Academic Tutor is a distilled academic tutoring skill that adds self-verification, self-reflection, super-agent orchestration, and continuous learning to Socratic academic guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users and students use this skill for Socratic academic tutoring, study guidance, and thesis or coursework coaching that avoids providing direct answers or ghostwritten text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs persistent learning, preference tracking, and possible write-back of learned patterns without clear user control or a consistent storage boundary.

Mitigation: Review before installing, confine the data directory, inspect or delete saved profile and learned_patterns.json data, and disable or supervise self-evolution or write-back behavior.

Risk: Academic tutoring can be misused for direct answers, assignment completion, or ghostwritten thesis text.

Mitigation: Preserve the Socratic hint-only response posture, require the user's own attempt or draft, and refuse requests for direct answers, assignment completion, or ghostwriting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-academic-tutor)
- [Publisher profile](https://clawhub.ai/user/qq435912743)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with a three-segment Socratic reply structure and optional inline bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are intended to remain hint-based and end with a concrete next step rather than a completed answer.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
