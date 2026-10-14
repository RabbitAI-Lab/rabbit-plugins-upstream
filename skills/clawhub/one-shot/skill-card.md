## Description:

Creates e-commerce image variants by replacing the model, background, or both while aiming to preserve the original garment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creative operators use this skill to make multiple audience- and scene-specific versions of an existing garment photo without a new photo shoot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts may be sent to an external image-generation provider.

Mitigation: Send only images and prompts you are comfortable sharing with the selected provider; use trusted local files or image URLs and explicit provider credentials.

Risk: Synthetic demographic variants or model likenesses could mislead viewers or imply an unauthorized endorsement.

Mitigation: Confirm rights and consent for source images and likenesses, and review variants before publication; avoid fabricated endorsements.

Risk: Image edits can alter garment details despite instructions to preserve them.

Mitigation: Compare generated images against the source garment and reject variants with changed logos, colors, cuts, or other product details.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated JPEG image variants to local files.]

## Skill Version(s):

1.0.20 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
