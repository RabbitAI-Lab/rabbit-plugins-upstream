## Description:

Guides an agent to turn a clothing photo into a clean, white-background product flat-lay image while preserving visible garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and content creators use this skill to make isolated, front-facing garment flat-lays from model photos, street photos, or customer photos for product listings and downstream imagery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source or model photos and prompts are sent to an external image provider.

Mitigation: Use an approved provider and avoid sensitive personal photos unless authorized for that service.

Risk: Stored image-provider credentials may be selected during generation.

Mitigation: Check which provider and credentials are configured before submitting photos.

Risk: Obscured garment details may be reconstructed inaccurately.

Mitigation: Inspect generated garments against the source, especially details hidden by people or accessories.

## Reference(s):

- [Clothing Extraction release](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with prompt templates and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Following the guidance produces saved garment image files, typically JPEG or PNG; review reconstructed or obscured details before use.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
