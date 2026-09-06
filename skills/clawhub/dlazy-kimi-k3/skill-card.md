## Description:

Provides agent access to Moonshot AI's Kimi K3 model for text generation and image or video understanding in complex analysis, coding, and writing tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to invoke dLazy's hosted Kimi K3 model for long-form reasoning, coding assistance, writing, and multimodal analysis from prompts plus optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists a dLazy API key in local CLI configuration, and the security summary notes that file-permission protection may not be enforced by the referenced CLI.

Mitigation: Prefer per-run DLAZY_API_KEY use or verify permissions on ~/.dlazy/config.json after login; rotate or revoke the key from the dLazy dashboard if the machine is shared or the key may have been exposed.

Risk: Prompts and selected media files are sent to dLazy API and storage endpoints.

Mitigation: Review inputs before use and avoid submitting sensitive text or media unless that is acceptable under the user's organization policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON result envelope from the dLazy CLI, with generated content in result.outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts prompts plus optional image and video inputs; asynchronous runs may return a task identifier for later polling.]

## Skill Version(s):

1.2.7 (source: server release evidence; artifact frontmatter and install spec list 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
