## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate images from text prompts with Jimeng, optionally providing reference images and selecting an output size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence, and the scan was partial; it noted a purpose/login mismatch and unusual whitespace.

Mitigation: Before installing, review the CLI package and its documented authentication flow; the scan does not establish the image-generation capability.

Risk: Prompts and any supplied local media are sent to dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive prompts or files unless sharing them with the service is appropriate.

## Reference(s):

- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets returned as URLs in a JSON response; asynchronous jobs may return a task identifier.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt, optional reference images, and output size; image URLs are hosted by dLazy.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
