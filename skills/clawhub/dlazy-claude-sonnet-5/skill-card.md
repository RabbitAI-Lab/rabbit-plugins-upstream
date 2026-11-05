## Description:

Anthropic's latest Sonnet — near-Opus quality on coding and long-horizon agentic work at Sonnet cost, with support for text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can send a prompt, optionally with image or video inputs, to dLazy's hosted Claude Sonnet 5 service and receive generated content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy-hosted services, and use requires a stored organization API key.

Mitigation: Send only prompts and media you are comfortable sharing with dLazy; protect the API key and rotate or revoke it when needed. Review the external CLI and verify its credential handling and hosted model claims before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy service](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, JSON, Files]

**Output Format:** [Prompt-dependent content in a JSON response, with optional downloaded result asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and selected media are sent to the hosted service.]

## Skill Version(s):

1.2.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
