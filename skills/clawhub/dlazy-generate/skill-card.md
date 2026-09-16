## Description:

A comprehensive generation skill that selects an appropriate dLazy CLI model to generate images, videos, or audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to route multimodal generation requests to dLazy CLI models for image, video, and audio creation. It supports authenticated SaaS workflows where prompts, parameters, and referenced media are sent to dLazy-hosted services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media files may be sent to dLazy-hosted services.

Mitigation: Avoid passing sensitive prompts or files unless third-party service exposure is intended.

Risk: The skill depends on a pinned third-party npm CLI that executes locally.

Mitigation: Prefer npx or an isolated environment over global installation and review the pinned CLI before use.

Risk: Persisted API credentials may remain in the local dLazy configuration.

Mitigation: Use DLAZY_API_KEY for temporary credentials when possible and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI metadata source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON-output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media outputs are returned by the dLazy CLI as JSON envelopes and hosted file URLs.]

## Skill Version(s):

1.3.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
