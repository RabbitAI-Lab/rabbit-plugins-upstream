## Description:

A gentle personal coaching skill that helps people clarify their current priorities, choose a small next action, and reflect on progress over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users can use this skill for personal prioritization, lightweight daily planning, habit reflection, and resuming longer-term goals. It helps turn a small set of priorities into a manageable next action without making decisions for the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved priorities may appear after an ambiguous greeting, or a record may be deleted accidentally.

Mitigation: Check that a retrieved record matches the user's intent and confirm the record index before deleting it.

Risk: The security scan was partial, and its guidance calls out maintainer scripts that may snapshot project files or fetch URLs.

Mitigation: Review developer scripts before running them and avoid exposing sensitive project files or data.

Risk: Personal priorities and reflections can be sensitive when saved locally.

Mitigation: Review the content before consenting to save it, keep records minimal, and inspect saved data before sharing.

## Reference(s):

- [Priority Coach on ClawHub](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [Routing guide](artifact/references/router.md)
- [Daily planning and reflection flows](artifact/references/daily-flows.md)
- [Local memory schema and consent rules](artifact/references/memory-schema.md)
- [Thinking habits guide](artifact/references/thinking-habits.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational guidance and structured Markdown coaching cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized from user input; local records are written only with explicit consent.]

## Skill Version(s):

0.4.0 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
