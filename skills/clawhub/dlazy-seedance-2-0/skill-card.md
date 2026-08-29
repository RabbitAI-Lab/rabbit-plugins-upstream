## Description:

ByteDance's latest video generation model supports multi-modal reference inputs, including images, video, and audio, for video generation plus first/last-frame and text-to-video modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy's Seedance 2.0 CLI workflow for generating videos from prompts, reference media, or first/last-frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media may be sent to dLazy cloud services for generation.

Mitigation: Review prompts and media before use, avoid submitting sensitive content unless approved, and confirm the service terms fit the deployment.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Use operating-system account protections, rotate or revoke keys from the dLazy dashboard when needed, or provide DLAZY_API_KEY per invocation to reduce local persistence.

Risk: The skill depends on a pinned third-party npm CLI package.

Mitigation: Review the pinned package or source before installation, and use npx when avoiding a persistent global binary is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs, async task identifiers, or saved local result files through the dLazy CLI.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
