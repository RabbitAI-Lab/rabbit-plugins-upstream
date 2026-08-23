## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from prompts or reference images with Seedream 5.0 Lite through dLazy's hosted cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media files supplied to the skill are sent to dLazy's cloud service.

Mitigation: Use the skill only for intended dLazy image-generation requests and avoid passing private files unless upload to the service is acceptable.

Risk: The skill depends on a third-party CLI and hosted API.

Mitigation: Install the pinned CLI version from the declared package source and review the provider before deployment.

Risk: Authentication may store an API key in the local dLazy CLI configuration.

Mitigation: Protect the local configuration file, rotate or revoke keys from the dLazy dashboard when needed, or use DLAZY_API_KEY for per-session authentication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing generated image output URLs, or asynchronous task identifiers when no-wait mode is used.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
