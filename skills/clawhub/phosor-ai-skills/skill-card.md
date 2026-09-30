## Description:

Helps agents generate videos, images, speech, and e-commerce photography with Phosor AI, and manage the resulting jobs and custom LoRA models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phosor.ai](https://clawhub.ai/user/phosor.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, e-commerce teams, and developers use this skill to generate and edit media, create product and model photography, work with custom LoRA models, and check generation jobs through Phosor AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected media, LoRA files, and generation metadata may be sent to Phosor AI.

Mitigation: Use only approved content and confirm what will be uploaded before running commands.

Risk: Generation commands and broader Image Studio calls can consume account credits.

Mitigation: Review the requested operation and expected costs before submitting jobs.

Risk: The client may use a PHOSOR_API_KEY from the OpenClaw workspace when one is not provided directly.

Mitigation: Confirm which account key will be used and keep it private.

## Reference(s):

- [Phosor AI API reference](references/api.md)
- [Phosor AI documentation](https://docs.phosor.ai)
- [Phosor AI](https://phosor.ai)
- [Phosor AI skill on ClawHub](https://clawhub.ai/phosor.ai/skills/phosor-ai-skills)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance and shell commands; client responses in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation results may include media URLs and job identifiers.]

## Skill Version(s):

1.3.2 (source: frontmatter, VERSION, CHANGELOG; released 2026-09-25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
