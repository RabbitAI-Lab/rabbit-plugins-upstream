## Description:

Alibaba's flagship Qwen reasoning model, strong at complex reasoning, code engineering, and long-context analysis, accepts text and image input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call dLazy's hosted Qwen 3.8 Max model for text generation, reasoning, code engineering, long-context analysis, and image-grounded prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media files are sent to dLazy's hosted API and media storage.

Mitigation: Confirm the user trusts dLazy as a cloud provider and avoid sending sensitive inputs unless that use is approved.

Risk: The dLazy CLI stores an API key in local user configuration when authenticated.

Mitigation: Protect the local config file and rotate or revoke the API key from the dLazy dashboard when access should change.

Risk: A global CLI install persists a local executable beyond a single invocation.

Mitigation: Use npx @dlazy/cli@1.2.3 for one-off use when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON result envelope containing generated output values, with agent-facing responses commonly rendered as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs when --no-wait is used; local media paths supplied by the user may be uploaded to dLazy media storage.]

## Skill Version(s):

1.2.8 (source: server release metadata; artifact frontmatter is 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
