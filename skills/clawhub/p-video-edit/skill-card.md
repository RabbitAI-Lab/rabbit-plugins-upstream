## Description:

Use when someone wants to edit an existing video with a text instruction - recolor, restyle, remove or add objects, change environment or lighting, update on-screen text, or apply optional reference-guided product and accessory edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through prompt-driven edits to an existing short video using Pruna's p-video-edit model, including attribute, environment, lighting, text, object, and optional reference-guided edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected videos and optional images to a third-party API and requires a paid Pruna API key.

Mitigation: Use it only with media that is acceptable to send to Pruna, confirm PRUNA_API_KEY handling before use, and check Pruna's data handling terms for sensitive media.

Risk: The skill asks the agent to install mutable companion skills before generation.

Mitigation: Review or pin companion skills before allowing installation in a production or sensitive workflow.

## Reference(s):

- [ClawHub skill page for p-video-edit](https://clawhub.ai/pruna-ai/skills/p-video-edit)
- [Pruna file upload endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides prompt drafting, media upload, prediction creation, polling, and follow-on video workflows; the edited video is produced by the Pruna API rather than by the skill itself.]

## Skill Version(s):

1.0.11 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
