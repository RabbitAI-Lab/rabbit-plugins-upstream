## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to generate images from text prompts with Jimeng, optionally adding reference images and choosing output dimensions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy, and generation uses service credits.

Mitigation: Send only intended content, confirm acceptance of the service and credit use, and use --dry-run to review the payload and estimated cost first.

Risk: The CLI saves an API key in local user configuration.

Mitigation: Restrict access to the local configuration file and rotate or revoke the key if it may have been exposed.

Risk: The skill depends on an installed or on-demand CLI package.

Mitigation: Review the pinned CLI package before installation.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Files]

**Output Format:** [Generated image files (PNG) and image URLs in JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports selectable image dimensions and up to 10 optional reference images; results can return asynchronously or be saved locally.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
