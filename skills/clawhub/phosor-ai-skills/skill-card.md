## Description:

Phosor AI helps agents generate and manage AI video, image, speech, LoRA, and e-commerce product/model photography jobs through the Phosor AI platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phosor.ai](https://clawhub.ai/user/phosor.ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to submit, poll, and manage media-generation jobs, upload required source assets or LoRA files, synthesize speech, and generate product or model photography through Phosor AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends an API key and user-selected media, prompts, audio, videos, or LoRA files to Phosor AI.

Mitigation: Install and use it only when you trust Phosor with those inputs, and send only assets intended for that service.

Risk: Media generation and analysis can consume paid credits.

Mitigation: Review current pricing or credit estimates before submitting jobs, especially for batch or Image Studio workflows.

Risk: Base URL and HTTP overrides can redirect traffic away from the default production service.

Mitigation: Use overrides only for deployments you control, and keep the default HTTPS production endpoint for normal use.

## Reference(s):

- [Phosor AI homepage](https://phosor.ai)
- [ClawHub skill page](https://clawhub.ai/phosor.ai/skills/phosor-ai-skills)
- [Phosor AI API documentation](https://docs.phosor.ai)
- [Phosor AI API Reference](references/api.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Phosor API key and network access; generated media jobs may require uploaded images, audio, videos, or LoRA files.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter, README.md, CHANGELOG.md, VERSION, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
