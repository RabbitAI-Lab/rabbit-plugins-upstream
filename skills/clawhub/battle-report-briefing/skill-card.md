## Description:

Creates mobile-friendly, single-screen tactical battle briefings with PNG visuals, flags, tactical summaries, and multi-source checks for historical or military conflicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superchangme](https://clawhub.ai/user/superchangme)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn public-source battle or military-conflict research into compact visual briefings, including side-by-side force comparison, key performance indicators, command structure, and cited source summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to create files under /tmp/openclaw/sent and send image attachments to a user.

Mitigation: Confirm the intended recipient before sending attachments and ensure generated files contain only intended public-source briefing content.

Risk: Battle briefings can include uncertain historical casualty, commander, or unit details.

Mitigation: Use public sources, cross-check key figures across multiple independent references, and mark lower-confidence details when the underlying records are incomplete.

Risk: Prompts or generated artifacts could include sensitive personal information if supplied by a user.

Mitigation: Avoid putting sensitive personal information into prompts or briefing assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/superchangme/skills/battle-report-briefing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with HTML/CSS snippets and PNG image output instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces mobile 390px briefing imagery and emphasizes public-source research, cross-checking, and citation quality.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter: v1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
