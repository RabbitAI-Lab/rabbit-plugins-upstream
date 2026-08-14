## Description:

A resume optimization and interview coaching assistant for Chinese and English resumes, mock interviews, job search strategy, salary negotiation, and offer comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers, career coaches, and recruiting support teams use this skill to improve resumes, prepare for behavioral, technical, and HR interviews, compare offers, and plan salary negotiation. It supports bilingual Chinese and English coaching workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional learning behavior can write local memory files containing user preferences, usage patterns, errors, and notes.

Mitigation: Make persistence explicit and opt-in, keep the stored data reviewable and deletable, and avoid storing sensitive resume, employer, compensation, or interview details.

Risk: The skill describes self-modifying behavior that may update SKILL.md after repeated errors or usage thresholds.

Mitigation: Require review before applying generated changes, then scan and revalidate the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/resume-interview-coach)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Markdown with structured reports, before/after resume edits, mock interview dialogue, scored feedback, and inline shell commands for the optional learning script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sourced job-search research when web search is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
