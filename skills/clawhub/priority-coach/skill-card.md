## Description:

A gentle personal coaching skill that helps users narrow messy priorities into the 1-3 things that matter now and a smallest action they can start today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill for low-pressure personal priority coaching: sorting current responsibilities, choosing up to three priorities, and turning one priority into a concrete action for today.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local priority and session records may contain personal context.

Mitigation: Save records only after explicit user consent, avoid saving raw personal answers unless the user asks, and remind the user that records can be reviewed, exported, or deleted.

Risk: Record export, migration, or deletion can expose or remove local notes if invoked unintentionally.

Mitigation: Confirm the requested record action before running it and make sure it matches the user's intent.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [Router](references/router.md)
- [States](references/states.md)
- [Cold Start](references/cold-start.md)
- [Daily Flows](references/daily-flows.md)
- [Review](references/review.md)
- [Memory Schema](references/memory-schema.md)
- [Copy Tone](references/copy-tone.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown coaching responses with structured cards and optional local record-management commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save local JSON priority and session records only after explicit user consent.]

## Skill Version(s):

0.3.3 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
