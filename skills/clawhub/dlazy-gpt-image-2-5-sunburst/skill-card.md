## Description:

Generates and edits images from text prompts and optional reference images through the dLazy-hosted GPT Image 2.5 Sunburst service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit detailed images from text prompts and reference images, with controls for aspect ratio and quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image files are sent to dLazy-hosted services.

Mitigation: Share only prompts and reference files approved for upload to the dLazy service.

Risk: The CLI can save a dLazy API key in local configuration.

Mitigation: Confirm the CLI and service are trusted before installing; rotate or revoke keys through the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI source (skill metadata link; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image URLs, Images, JSON]

**Output Format:** [JSON containing generated image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation and optional local saving of results.]

## Skill Version(s):

1.2.15 (source: ClawHub release metadata; skill frontmatter and CLI install specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
