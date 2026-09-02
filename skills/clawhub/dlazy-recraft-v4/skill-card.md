## Description:

1MP raster image generation with refined design judgment for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and external users can use this skill to ask an agent to generate 1MP raster images through the dLazy Recraft V4 command-line workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and input file paths may be sent to dLazy's cloud image-generation service.

Mitigation: Only pass prompts and files that are appropriate for the dLazy service and the user's organization policy.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-run authentication when persistence is not desired, and rotate or revoke keys from dLazy when needed.

Risk: The skill installs and invokes a pinned third-party CLI package.

Mitigation: Review the dLazy CLI source or package before installation in environments with strict supply-chain controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs, saved local files when requested, or asynchronous task identifiers.]

## Skill Version(s):

1.3.11 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
