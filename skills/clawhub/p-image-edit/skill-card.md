## Description:

Use when someone wants to edit an existing photo -- change outfits or backgrounds, compose from reference images, or apply prompt-driven edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to guide prompt-driven edits of existing photos through Pruna's image-editing API while preserving specified identity, pose, lighting, background, or product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send user-provided photos to Pruna's API.

Mitigation: Use only images the user has permission to share, and avoid sensitive personal, biometric, confidential, or proprietary images unless sharing with Pruna is approved.

Risk: The skill asks the agent to install Pruna companion skills from external package references.

Mitigation: Review the companion skills and install only the components needed for the task from trusted package references.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pruna-ai/skills/p-image-edit)
- [Pruna Files API](https://api.pruna.ai/v1/files)
- [Pruna Predictions API](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with curl command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user-provided image references before calling Pruna's API.]

## Skill Version(s):

1.0.11 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
