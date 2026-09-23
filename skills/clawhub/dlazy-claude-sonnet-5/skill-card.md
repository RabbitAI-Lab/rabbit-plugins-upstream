## Description:

Anthropic's latest Sonnet offers near-Opus quality for coding, long-horizon agentic work, reasoning, code generation, and complex tool orchestration, with support for text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Claude Sonnet 5 text generation workflow from an agent, including prompts with optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and explicitly referenced media files to dLazy hosted services.

Mitigation: Use it only with data appropriate for a third-party hosted API, and review the referenced files before invocation.

Risk: Authentication depends on a dLazy API key that may be stored in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when less local persistence is desired, and rotate or revoke the API key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the dLazy CLI and a dLazy API key; async runs may return a generation ID for polling.]

## Skill Version(s):

1.2.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
