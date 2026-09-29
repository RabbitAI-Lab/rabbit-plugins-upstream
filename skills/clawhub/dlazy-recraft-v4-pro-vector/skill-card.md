## Description:

Generates detailed vector-oriented illustrations from text prompts using dLazy's hosted Recraft V4 Pro Vector model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other users can create detailed vector-oriented artwork from text prompts and save the generated asset locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI introduces local execution and persistence considerations.

Mitigation: Review the CLI before installation and consider the pinned on-demand npx invocation instead of a global install.

Risk: API credentials can persist locally, and prompts or referenced media files are sent to dLazy's hosted service.

Mitigation: Use a per-invocation API key when preferred, protect stored credentials, and avoid submitting sensitive prompts or files unless intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI repository (publisher-provided link; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image asset links]

**Output Format:** [Markdown guidance and shell commands; CLI responses contain JSON image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets can be saved locally; asynchronous runs return a task ID for polling.]

## Skill Version(s):

1.3.21 (source: server release; bundled skill frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
