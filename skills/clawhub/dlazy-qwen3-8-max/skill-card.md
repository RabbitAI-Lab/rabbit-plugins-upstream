## Description:

This skill sends text prompts and optional images to dLazy's hosted Alibaba Qwen reasoning model for complex reasoning, code engineering, and long-context analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use the skill to generate text or code and analyze long-context prompts with optional image input through dLazy's hosted Qwen service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and noted a mismatch between the advertised model capability and the CLI login or authentication setup.

Mitigation: Before installing, review the CLI login and authentication flow, the padded section, and the referenced package; use the CLI only if you trust it with your credentials.

Risk: Prompts and local image, video, or audio files supplied to the CLI are sent to dLazy's hosted API or media storage.

Mitigation: Avoid sending sensitive prompts or files unless sharing them with the service is permitted.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, JSON]

**Output Format:** [JSON response envelope containing generated results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content varies with the prompt; some results may be returned as hosted URLs.]

## Skill Version(s):

1.2.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
