## Description:

Moonshot AI thinking model with text, image, and video understanding. Suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call dLazy's Kimi K3 model through the dLazy CLI for complex analysis, coding, writing, and multimodal prompt tasks involving text, images, and video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the third-party @dlazy/cli package.

Mitigation: Review the package or source when needed and prefer npx or a local install over a global install.

Risk: Prompts and selected media files may be sent to dLazy hosted services.

Mitigation: Pass only prompts and files intended for upload to dLazy.

Risk: The skill depends on a dLazy API key stored locally or supplied through the environment.

Mitigation: Rotate or revoke the dLazy API key if compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, JSON, Guidance]

**Output Format:** [JSON response containing generated outputs; content may be text, markdown, code, or guidance depending on the prompt.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation IDs and optional local saving through the dLazy CLI.]

## Skill Version(s):

1.2.9 (source: server release metadata; artifact frontmatter and CLI install spec reference 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
