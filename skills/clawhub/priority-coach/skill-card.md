## Description:

Priority Coach is a Chinese-language personal coaching skill that helps users reduce overwhelm, choose the top 1-3 priorities, and turn the first priority into a small action they can start today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for low-pressure priority coaching: clarifying what matters now, making a lightweight plan, starting a first step, wrapping up the day, or resuming a longer-term focus. The skill can optionally save local priority and session records only after explicit user consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved or exported local records may contain personal priorities, energy patterns, or raw answers.

Mitigation: Save records only after explicit consent, avoid saving raw answers unless needed and consented to, and do not share terminal output or logs that include exports.

Risk: The skill provides priority coaching, not crisis, medical, legal, or final life-decision support.

Mitigation: For high-risk crisis expressions, pause normal coaching and direct the user toward trusted people, local emergency support, or qualified professional help.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [README](README.md)
- [Router](references/router.md)
- [State scripts](references/states.md)
- [Cold start](references/cold-start.md)
- [Daily flows](references/daily-flows.md)
- [Mainline review](references/review.md)
- [Memory schema](references/memory-schema.md)
- [Copy tone](references/copy-tone.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown coaching cards with optional local record-management shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured priority, daily action, evening wrap, low-burden, habit, and review cards; optional local JSON records are created only with explicit user consent.]

## Skill Version(s):

0.3.1 (source: server release metadata, skill frontmatter, README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
