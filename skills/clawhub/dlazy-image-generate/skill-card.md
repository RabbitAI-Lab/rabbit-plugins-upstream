## Description:

Image generation skill that automatically selects an appropriate dLazy CLI image model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route image-generation, image-editing, matting, vectorization, and upscaling requests through the dLazy CLI and hosted image APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and supplied local media paths may be sent to dLazy-hosted API and storage endpoints.

Mitigation: Avoid submitting sensitive, regulated, or confidential content unless dLazy's terms and the user's data-handling requirements permit it.

Risk: Authentication can store a dLazy API key in the local user configuration.

Mitigation: Protect the local config file, prefer scoped or rotatable keys, and revoke or rotate keys from the dLazy dashboard when access changes.

Risk: Generated outputs are hosted by dLazy and may be accessed through returned URLs.

Mitigation: Treat generated URLs and media as externally hosted assets and handle them according to the user's sharing and retention policy.

Risk: The hosted provider may enforce account credits, billing, and content-safety policies.

Mitigation: Confirm account status and acceptable-use constraints before batch, paid, or commercial generation workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs returned by dLazy-hosted services.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
