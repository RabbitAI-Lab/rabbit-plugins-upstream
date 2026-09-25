## Description:

Midjourney-style image generation with aspect ratio, bot type, and output-position controls for artistic, strongly stylized creative images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Midjourney-style image generation workflow from an agent, optionally selecting aspect ratio, bot type, grid output, or an upscaled output position.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and intentionally supplied local media paths may be sent to dLazy's hosted service.

Mitigation: Use only prompts and media appropriate for dLazy processing, and review the service before using the skill in sensitive environments.

Risk: The dLazy CLI may store an API key in local user configuration.

Mitigation: Protect the local configuration file, rotate or revoke keys when needed, or pass DLAZY_API_KEY per invocation instead of storing a key.

Risk: The skill depends on an external pinned npm CLI and dLazy cloud endpoints.

Mitigation: Install the pinned @dlazy/cli version specified by the evidence and review the external package/source before global installation in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [JSON response with generated image URLs or asynchronous task status, plus optional local file download when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are hosted by dLazy; asynchronous invocations can return a generateId for polling.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
