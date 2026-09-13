## Description:

Anthropic's latest Sonnet model provides near-Opus quality for coding, reasoning, long-horizon agent work, and text generation from text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call dLazy's hosted Claude Sonnet interface for text generation, coding assistance, reasoning, and multimodal prompt workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files are sent to the hosted dLazy service.

Mitigation: Use the skill only with data approved for that service and avoid sending sensitive prompts or media unless permitted.

Risk: The skill relies on an npm CLI authenticated with a dLazy API key.

Mitigation: Prefer the pinned npx invocation while evaluating, avoid elevated privileges, and rotate or revoke the API key if compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON envelope returned by the dLazy CLI with generated outputs or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt input plus optional image and video inputs; results may be returned synchronously or by generateId for polling.]

## Skill Version(s):

1.2.17 (source: server release metadata; artifact frontmatter lists 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
