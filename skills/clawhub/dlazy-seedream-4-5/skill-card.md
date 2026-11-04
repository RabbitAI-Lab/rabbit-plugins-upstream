## Description:

Generate high-quality images with Doubao Seedream 4.5 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents can use this skill to create images from text prompts or reference images through the dLazy Seedream 4.5 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy, and local media files passed to the CLI are uploaded for processing.

Mitigation: Use prompts and images you are comfortable sending to dLazy, and review the service terms before submitting sensitive material.

Risk: Generation may incur costs, and the external CLI and its claimed API-key storage protections were not audited in this review.

Mitigation: Review generation costs, protect the API key, and rotate or revoke it when needed.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [@dlazy/cli package listing](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON result metadata, Shell commands, Configuration instructions]

**Output Format:** [Generated image files or hosted image URLs, with JSON result metadata; Markdown usage guidance with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation supports text prompts and up to 10 reference images; requested sizes include 1:1, 4:3, 3:4, 16:9, 9:16, 3:2, 2:3, and 21:9, at 2K or 4K resolution.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
