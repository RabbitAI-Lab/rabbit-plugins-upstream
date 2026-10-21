## Description:

Analyzes a reference image's composition, colors, lighting, and style and generates a new image in a similar style with Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to produce new images based on the visual style of a reference image through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images passed as local files are uploaded to dLazy's service.

Mitigation: Only provide images or media that you are comfortable uploading to dLazy.

Risk: The skill depends on an external npm package and a dLazy API key.

Mitigation: Confirm you trust the pinned dLazy package before installing; rotate or revoke your API key in the dLazy dashboard if needed.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (linked in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)

## Skill Output:

**Output Type(s):** [JSON text, Image URLs, Image files (optional)]

**Output Format:** [JSON response with generated image URLs; optionally a downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID for later polling.]

## Skill Version(s):

1.3.33 (source: server-resolved ClawHub release; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
