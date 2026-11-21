## Description:

Audit any agent skill (SKILL.md) for quality, structure and prompt-injection / security risks before installing or publishing it. Use when the user wants to vet, review, score or compare skills, or before installing any third-party skill from ClawHub, skills.sh or GitHub. Produces a scored report card and a badge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hugororo2003](https://clawhub.ai/user/hugororo2003)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill publishers use this skill to assess an agent skill or skill repository before installing, publishing, comparing, or using it as a quality gate. It produces a static scored report card and badge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented GitHub command can run unpinned third-party code locally.

Mitigation: Review the source and run a pinned, reviewed revision or a reviewed local copy.

Risk: The scanner reports a report-path overwrite risk.

Mitigation: Use a dedicated output directory and confirm report file paths before running the CLI.

Risk: Security inspection was partial, with 57.1% coverage and three files only partially inspected.

Mitigation: Inspect the remaining code before relying on the audit or installing the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/hugororo2003/skills/skill-audit)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, JSON]

**Output Format:** [Scored report card in Markdown, HTML, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes findings, a grade, and a shareable badge; critical findings produce a non-zero exit code.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
