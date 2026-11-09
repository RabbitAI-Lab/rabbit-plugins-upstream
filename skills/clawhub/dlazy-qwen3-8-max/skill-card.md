## Description:

Alibaba's flagship Qwen reasoning model (2.4T-parameter MoE), strong at complex reasoning, code engineering and long-context analysis. Accepts text and image input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to send text prompts and optional images to dLazy's hosted Qwen 3.8 Max service and receive generated responses or assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review could not establish how the CLI login and authentication steps relate to the stated Qwen purpose or determine their downstream effects.

Mitigation: Review the CLI behavior and credential flow before signing in; use a revocable API key and rotate it if needed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Generated files]

**Output Format:** [Generated content in a JSON response envelope; assets may be returned as URLs or saved to a file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts text prompts and optional images; generated assets can be saved to a local path.]

## Skill Version(s):

1.2.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
