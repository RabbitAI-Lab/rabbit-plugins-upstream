## Description:

Routes image, video, and audio requests to a suitable dLazy model and runs generation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can request image, video, or audio generation in natural language and use the skill to select and run a suitable dLazy model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media are sent to dLazy services for generation.

Mitigation: Submit only prompts and media intended for the service, and review dLazy's privacy terms before use.

Risk: The API key is stored in local CLI configuration, and the external CLI executable was not fully audited in this review.

Mitigation: Protect the local API key, rotate or revoke it if exposed, and review the CLI source and pinned package before installing.

Risk: Generation requests may incur charges.

Mitigation: Check the applicable pricing or account balance before running generation requests.

## Reference(s):

- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Generated images, Generated videos, Generated audio, Hosted media URLs, Shell commands]

**Output Format:** [Media files or hosted URLs, with JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The selected model and media output depend on the request.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
