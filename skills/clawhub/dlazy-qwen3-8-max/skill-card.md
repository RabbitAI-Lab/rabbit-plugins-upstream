## Description:

Alibaba's flagship Qwen reasoning model (2.4T-parameter MoE), strong at complex reasoning, code engineering and long-context analysis. Accepts text and image input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to send text prompts and optional images to dLazy's hosted Qwen 3.8 Max model for reasoning, coding, and long-context analysis, then receive generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial; some referenced material was unavailable, and the npm package's internal behavior was not reviewed.

Mitigation: Review the referenced materials and package before installing; a benign scan verdict is not a guarantee of safety.

Risk: Prompts and supplied local image files are sent to dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive prompts or files unless dLazy's data handling is acceptable for them.

Risk: The CLI requires a dLazy API key, which is stored in local CLI configuration when using the login flow.

Mitigation: Protect the CLI configuration, keep keys out of prompts, and rotate or revoke a key if exposed.

## Reference(s):

- [dLazy CLI repository (documented link)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, JSON]

**Output Format:** [Text or JSON returned by the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task status; supports text and image inputs.]

## Skill Version(s):

1.2.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
