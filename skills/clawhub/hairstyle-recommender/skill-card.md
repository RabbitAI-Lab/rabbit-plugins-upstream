## Description:

Analyze portrait photos to recommend the most flattering hairstyle based on face shape, facial features, hair texture, and personal style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nellyxiaolong-cmyk](https://clawhub.ai/user/nellyxiaolong-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

External users can upload portrait or headshot photos to receive hairstyle recommendations, barber or stylist talking points, and optional AI-generated preview images. The skill is intended for haircut planning and style exploration, not professional cosmetology, medical, or identity assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional preview feature sends portrait photos and prompts to RunComfy.

Mitigation: Use the text recommendation workflow for sensitive images, or obtain clear user consent before using the preview script.

Risk: The preview script downloads a service-provided result URL.

Mitigation: Treat downloaded outputs as untrusted and harden the script with HTTPS enforcement, host allowlisting, image validation, and response-size limits before operational use.

Risk: AI-generated hairstyle previews can alter unintended image details or misrepresent real haircut results.

Mitigation: Present generated previews as directional references and rely on the written haircut guidance when discussing feasibility with a stylist.

## Reference(s):

- [Hairstyle Knowledge Reference](artifact/references/hairstyles.md)
- [RunComfy](https://www.runcomfy.com)
- [ClawHub Skill Page](https://clawhub.ai/nellyxiaolong-cmyk/skills/hairstyle-recommender)

## Skill Output:

**Output Type(s):** [analysis, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown recommendations with optional shell commands for image preview generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May optionally create an AI-generated hairstyle preview image when configured with a RunComfy API token.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
