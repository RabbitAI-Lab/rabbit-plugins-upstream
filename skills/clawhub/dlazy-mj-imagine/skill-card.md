## Description:

Midjourney style image generation through the dLazy CLI, supporting aspect ratio, bot type, and output selection for artistic and highly stylized creative generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to invoke dLazy's Midjourney-style image generation command with prompts, aspect ratios, bot selection, and output choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media files are sent to dLazy's hosted API and media storage.

Mitigation: Avoid submitting confidential prompts or sensitive media unless the dLazy service terms and data handling are acceptable for the use case.

Risk: Authentication may save a dLazy API key in the local CLI configuration.

Mitigation: Protect the local config file, prefer scoped keys, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Execution depends on the pinned third-party @dlazy/cli package.

Mitigation: Review the pinned package and provider before installation, and use the declared pinned version rather than an unpinned latest install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI results containing generated image URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can save generated image assets to a local path when the --save option is used.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
