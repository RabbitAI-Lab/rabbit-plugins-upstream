## Description:

This skill lets agents call dLazy's hosted Claude Sonnet 5 text generation tool for reasoning, coding, tool orchestration, and multimodal prompt inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to send prompts, and optionally image or video inputs, to dLazy's hosted Claude Sonnet 5 tool and receive generation results through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted API and media storage.

Mitigation: Do not submit sensitive data unless that use is approved for dLazy; review prompts and media paths before invoking the CLI.

Risk: Login can store a dLazy API key in the local user configuration.

Mitigation: Use npx or the DLAZY_API_KEY environment variable for less persistent setup, and rotate or revoke keys if exposure is suspected.

Risk: The skill depends on a third-party hosted provider and pinned CLI package.

Mitigation: Install the declared pinned CLI version and use the skill only in environments approved for third-party hosted model providers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON from the dLazy CLI, with generated model content returned in the result payload.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async runs may return a task identifier for later polling; generated asset URLs may be hosted on files.dlazy.com.]

## Skill Version(s):

1.2.10 (source: server release evidence; artifact frontmatter reports 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
