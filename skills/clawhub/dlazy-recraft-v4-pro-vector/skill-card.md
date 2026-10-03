## Description:

Generates detailed vector artwork from text prompts using the hosted dLazy Recraft V4 Pro Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to create detailed vector artwork from text prompts for illustrations and production assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly supplied to the CLI may be uploaded to dLazy, and generated assets are hosted there.

Mitigation: Avoid submitting sensitive prompts or files without approval and review the service terms before use.

Risk: Logging in can save an API key locally, and installing a third-party CLI adds software to the environment.

Mitigation: Review the linked CLI source and package; use the pinned npx invocation or DLAZY_API_KEY when a persistent install or saved key is not desired.

## Reference(s):

- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown instructions with shell examples; the CLI returns JSON containing generated asset URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artwork can be saved locally with the CLI's --save option.]

## Skill Version(s):

1.3.23 (source: server-resolved release evidence; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
