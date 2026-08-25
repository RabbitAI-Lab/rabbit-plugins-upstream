## Description:

This skill invokes dLazy's Claude Sonnet 5 CLI wrapper for text generation, reasoning, code generation, and complex agentic work with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to call dLazy's hosted Claude Sonnet 5 service from an agent workflow for text, coding, reasoning, and multimodal prompt tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-specified local media may be sent to dLazy's hosted service.

Mitigation: Use the skill only with data approved for third-party SaaS processing, and avoid passing sensitive local files unless the environment allows that transfer.

Risk: The dLazy API key is stored locally when using CLI login or auth setup.

Mitigation: Keep the local config restricted to the OS user, use per-invocation environment variables where appropriate, and rotate or revoke the key if the machine is shared or compromised.

Risk: Installing the third-party CLI adds supply-chain dependency on the @dlazy/cli package.

Mitigation: Use the pinned npx invocation or pinned global install from the metadata, and review the package or source before use in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON response containing generated outputs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional image and video inputs, dry-run cost estimates, asynchronous execution, and saving returned assets.]

## Skill Version(s):

1.2.11 (source: server release metadata; artifact frontmatter lists 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
