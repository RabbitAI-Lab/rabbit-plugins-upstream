## Description:

Alibaba's flagship Qwen reasoning model is exposed through the dLazy CLI for complex reasoning, code engineering, long-context analysis, and text or image input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users invoke this skill to send prompts and selected image inputs to the dLazy-hosted Qwen model and receive generated responses for reasoning, coding, and analysis tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy cloud endpoints for processing.

Mitigation: Avoid submitting sensitive prompts or local files unless cloud upload to dLazy is intended.

Risk: The skill depends on a third-party CLI package and API-key based account access.

Mitigation: Review the dLazy CLI package before installation, prefer npx or a local sandboxed install when possible, and rotate or revoke the API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON envelope containing generated output values; user-facing content may be text, Markdown, code, shell commands, configuration, or guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task polling and optional result download through the dLazy CLI.]

## Skill Version(s):

1.2.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
