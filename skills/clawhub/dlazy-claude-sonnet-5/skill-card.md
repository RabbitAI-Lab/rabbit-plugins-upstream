## Description:

Anthropic's Claude Sonnet 5 skill provides hosted text generation for reasoning, code generation, complex tool orchestration, and optional image or video inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill through the dLazy CLI to send text prompts, and optional image or video inputs, to the hosted claude-sonnet-5 model for reasoning, code generation, and complex tool-oriented work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and optional local media paths may be sent to dLazy hosted endpoints.

Mitigation: Use the skill only when sharing the submitted content with dLazy is acceptable, and avoid passing sensitive local files unless the user has approved the upload.

Risk: Authentication stores a dLazy API key in local CLI configuration unless the key is supplied per invocation.

Mitigation: Prefer least-privilege API keys, rotate or revoke keys from the dLazy dashboard when needed, and use the DLAZY_API_KEY environment variable for temporary use.

Risk: A global npm install persists the dLazy CLI binary on the host.

Mitigation: Use the pinned npx invocation when a persistent global installation is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON response envelope containing generated outputs, with agent-facing text, markdown, code, commands, or guidance as the generated value]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task polling, dry-run cost estimation, optional local result saving, and optional image or video inputs.]

## Skill Version(s):

1.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
