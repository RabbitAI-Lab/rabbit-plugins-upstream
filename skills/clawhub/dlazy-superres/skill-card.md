## Description:

Image super-resolution tool that enhances image clarity and details, returning an enhanced image URL for low-resolution asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and other external users use this skill to upscale selected images through the dLazy hosted API and receive enhanced image URLs or saved result files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts provided to the skill are sent to the dLazy cloud API for processing.

Mitigation: Use only content approved for dLazy cloud processing and review dLazy service terms before use.

Risk: The dLazy CLI may store an API key in the local user configuration.

Mitigation: Use scoped dLazy organization keys where possible and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Local image files selected by the user may be uploaded, and generated assets may be saved to a chosen local path.

Mitigation: Confirm source file paths and save destinations before running the CLI, especially in shared workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI returns hosted image output URLs and can optionally save generated files to a user-specified path.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
