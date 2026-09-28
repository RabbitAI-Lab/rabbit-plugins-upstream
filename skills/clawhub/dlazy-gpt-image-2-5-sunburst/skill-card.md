## Description:

Helps agents generate and edit images with GPT Image 2.5 Sunburst using text prompts and optional reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit detailed images from prompts and reference images, including work requiring in-image text or specific aspect ratios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media are sent to the third-party dLazy service.

Mitigation: Avoid submitting sensitive prompts or media unless approved for sharing with dLazy.

Risk: The dLazy CLI may store an API key locally during login.

Mitigation: Protect the local credential and rotate or revoke it if exposed.

Risk: Image generation may consume dLazy credits or incur charges.

Mitigation: Check available credits and use the cost-estimate option before submitting requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Image URLs, Guidance]

**Output Format:** [CLI JSON response with image URLs or asynchronous task status; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to five reference images, selectable aspect ratio and quality, and optional asynchronous generation.]

## Skill Version(s):

1.2.11 (source: ClawHub release metadata; bundled CLI instructions specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
