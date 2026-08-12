## Description:

Humor Up helps agents punch up toasts, bios, greetings, Slack posts, presentation openers, captions, daily briefs, and jokes in English and Chinese while avoiding humor in sensitive contexts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kimmyplusli](https://clawhub.ai/user/kimmyplusli)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill when they want an assistant to make everyday writing funnier, write original occasion messages or one-liners, caption images, or score and repair jokes. It is designed for bilingual English and Chinese humor workflows with explicit guidance to avoid humor in sensitive, stressful, legal, medical, grief, financial-loss, incident, death, illness, violence, or disaster contexts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Humor may be inappropriate in professional, sensitive, legal, medical, grief, financial-loss, incident-related, death, illness, violence, or disaster contexts.

Mitigation: Keep humor mode off and avoid invoking the skill for those contexts; the skill also instructs the agent to answer plainly and skip jokes when the user is stressed or the topic is sensitive.

Risk: Generated jokes or punch-ups could unintentionally target a person or protected trait.

Mitigation: Review humorous output before sending, and keep jokes aimed at systems, situations, or the assistant rather than individual identity, illness, victimization, or hardship.

Risk: Humor quality and cultural fit can vary across audiences and languages.

Mitigation: Use the safe variant for higher-stakes communication, ask for audience-specific details, and verify bilingual output with a fluent reviewer when tone matters.

## Reference(s):

- [ClawHub humor-up skill page](https://clawhub.ai/kimmyplusli/skills/humor-up)
- [OpenClaw](https://openclaw.ai)
- [README](artifact/README.md)
- [Pattern construction detail](artifact/patterns.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text responses with optional scoring rationale and revised wording]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce two variants for punch-up tasks and a numeric rubric score when asked to assess a joke.]

## Skill Version(s):

0.2.5 (source: frontmatter and changelog, released 2026-08-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
