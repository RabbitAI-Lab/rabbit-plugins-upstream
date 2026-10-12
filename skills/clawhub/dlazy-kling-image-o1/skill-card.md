## Description:

Generates images from text prompts or reference images using Kling Image O1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from text prompts and optional reference images through dLazy's Kling Image O1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation requests may spend dLazy credits.

Mitigation: Check the cost estimate with the dry-run option before submitting a request.

Risk: Authentication stores a dLazy API key in local CLI configuration.

Mitigation: Protect the local credential or pass it per invocation; rotate or revoke it if exposed.

Risk: Prompts and referenced local media are sent to dLazy-hosted services.

Mitigation: Avoid submitting private prompts or images unless you intend to share them with the service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Markdown guidance and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted image URLs or an asynchronous task ID; can optionally save an image locally.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
