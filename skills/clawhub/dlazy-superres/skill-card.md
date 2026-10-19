## Description:

Enhances low-resolution images and returns a URL for the upscaled result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to improve the clarity and detail of low-resolution images and obtain an enhanced image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party CLI package runs when the skill is used.

Mitigation: Review and trust the @dlazy/cli package before installing; use the pinned npx invocation if a persistent global installation is unwanted.

Risk: Local input images may be uploaded to dLazy's hosted service.

Mitigation: Only submit images you are comfortable sending to the service.

Risk: An API key may be stored in local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation if preferred, and rotate or revoke the key through the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Image URLs, Shell commands]

**Output Format:** [Markdown with image URLs and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON containing a hosted image URL; an optional save command downloads the result.]

## Skill Version(s):

1.3.32 (source: server release; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
