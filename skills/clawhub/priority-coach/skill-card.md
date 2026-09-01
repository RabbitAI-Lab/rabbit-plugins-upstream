## Description:

Priority Coach is a gentle personal-growth coaching skill that helps users reduce overwhelm, choose the 1-3 priorities that matter now, and turn the first priority into a small action they can start today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for personal priority coaching, daily planning, evening wrap-up, habit check-ins, low-burden recovery mode, and longer-term priority review. It is designed to produce concise coaching guidance and structured cards rather than full schedules or final life decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save priority and session summaries locally when the user agrees, which may include personal goals, routines, or sensitive context.

Mitigation: Ask for explicit consent before any write, keep saved records minimal, avoid raw answers or sensitive emotional details by default, and remind users that local records can be deleted or exported.

Risk: Delete and export commands operate on local coaching records and can expose or remove the user's saved priority history.

Mitigation: Use delete and export commands only after the user clearly requests them, and confirm broad deletion actions before proceeding.

Risk: Users in self-harm, violence, medical, or severe mental-health crisis contexts may need support beyond priority coaching.

Mitigation: Do not continue ordinary priority coaching in crisis scenarios; direct the user toward trusted people, local emergency support, or professional help.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [Router Reference](references/router.md)
- [State Scripts](references/states.md)
- [Daily Flows](references/daily-flows.md)
- [Mainline Review](references/review.md)
- [Memory Schema](references/memory-schema.md)
- [Copy Tone](references/copy-tone.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown coaching responses with structured cards and optional inline shell commands for local record management]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce priority cards, action cards, wrap-up cards, low-burden mode cards, review cards, and user-approved local record commands.]

## Skill Version(s):

0.3.0 (source: ClawHub release evidence, SKILL.md frontmatter, README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
