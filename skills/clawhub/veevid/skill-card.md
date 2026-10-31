## Description:

Provides Veevid API workflows for generating and editing video, images, and audio, transcribing speech, running video tools, and checking prices and credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meigesir](https://clawhub.ai/user/meigesir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to choose a media model, quote credit costs, prepare approved inputs, and submit Veevid requests for media generation or editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media inputs are sent to Veevid and the chosen model.

Mitigation: Review the selected files and approve the upload; ask before uploading private or sensitive material.

Risk: Some models may adjust charges based on actual media lengths, and failed jobs may have refund exceptions.

Mitigation: Quote the exact request, provide real input lengths, and get confirmation of the required credits before generating.

Risk: Deleting a creation is permanent and may also remove uploaded source audio.

Mitigation: Confirm the exact creation to delete before sending the deletion request.

## Reference(s):

- [Veevid API reference](references/api-reference.md)
- [Video model reference](references/models-video.md)
- [Image model reference](references/models-image.md)
- [Audio model reference](references/models-audio.md)
- [Video tools reference](references/models-tools.md)
- [Veevid API key settings](https://veevid.ai/settings/api-keys)
- [Veevid pricing](https://veevid.ai/pricing)
- [Veevid Skill on ClawHub](https://clawhub.ai/meigesir/skills/veevid)

## Skill Output:

**Output Type(s):** [API Calls, Files, Guidance, Shell commands, Configuration instructions, JSON, Markdown]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be video, image, or audio files; available output fields vary by model.]

## Skill Version(s):

1.3.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
