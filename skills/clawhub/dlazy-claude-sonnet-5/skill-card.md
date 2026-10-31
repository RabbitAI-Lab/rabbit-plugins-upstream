## Description:

Provides access to Claude Sonnet 5 through dLazy for reasoning, coding, complex tool orchestration, and text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other prompt-driven users use this skill to generate text, code, and other content through dLazy, with optional image and video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy for inference and processing.

Mitigation: Share only material appropriate for the service and review dLazy's data policies before sending sensitive content.

Risk: Authentication stores a dLazy API key in local CLI configuration, and requests consume service credits.

Mitigation: Protect the local key, use it only in a trusted environment, and monitor usage; rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, JSON, Generated media links]

**Output Format:** [Model-generated content, returned in a JSON response envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include output asset URLs; image and video inputs are supported.]

## Skill Version(s):

1.2.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
