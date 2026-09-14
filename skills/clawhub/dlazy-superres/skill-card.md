## Description:

This skill uses the dLazy image super-resolution service to upscale images and return enhanced image URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to restore or upscale low-resolution image assets through the dLazy hosted CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and hosted dLazy service.

Mitigation: Prefer an isolated or on-demand npx invocation if a persistent global binary is not needed, and review the package before installation.

Risk: The dLazy API key is required for use and grants access to the user's dLazy organization.

Mitigation: Keep the API key revocable, rotate it when needed, and avoid sharing it in prompts, logs, or saved command output.

Risk: Local images or upstream file references may be uploaded to dLazy cloud storage for processing.

Mitigation: Do not pass private files, sensitive images, or sensitive upstream outputs unless the user has approved using the third-party cloud service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted image URLs from files.dlazy.com; the --save option can download the result asset locally.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
