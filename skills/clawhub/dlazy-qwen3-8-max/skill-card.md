## Description:

Alibaba's flagship Qwen reasoning model (2.4T-parameter MoE) supports complex reasoning, code engineering, long-context analysis, and text or image input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Qwen 3.8 Max model for prompt-based text generation, code engineering help, long-context reasoning, and optional image-grounded requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs the @dlazy/cli package to call a hosted model API.

Mitigation: Review the CLI source or npm package provenance when supply-chain risk matters, and prefer npx or a sandbox instead of a global install where appropriate.

Risk: Prompts, parameters, and selected local media files may be sent to dLazy endpoints for processing.

Mitigation: Only pass prompts and files you are comfortable uploading to dLazy, and follow your organization's data-handling requirements.

Risk: The skill depends on a dLazy API key stored locally or supplied through DLAZY_API_KEY.

Mitigation: Protect the key, restrict local config access, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON response from the dLazy CLI, with generated content typically surfaced as text, markdown, code, or guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; image inputs may be uploaded to dLazy media storage when provided.]

## Skill Version(s):

1.2.10 (source: server release evidence; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
