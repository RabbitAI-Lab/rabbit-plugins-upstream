## Description:

Image generation skill that automatically selects an appropriate dLazy CLI image model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to select and run dLazy image-generation, editing, upscaling, matting, and vectorization models from natural-language prompts and optional reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and referenced local media files are sent to dLazy's hosted service.

Mitigation: Avoid confidential prompts and sensitive files unless that data handling is acceptable for the deployment.

Risk: The skill depends on a third-party npm CLI.

Mitigation: Review the pinned dLazy CLI package and source before installation, and use npx for on-demand execution when persistent global installation is not desired.

Risk: A dLazy API key may be stored in local CLI configuration.

Mitigation: Use OS user-restricted config permissions or per-invocation environment variables, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands; executed dLazy commands return JSON envelopes and hosted media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key.]

## Skill Version(s):

1.3.11 (source: ClawHub release metadata; artifact frontmatter declares 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
