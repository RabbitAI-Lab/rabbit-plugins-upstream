## Description:

A structured workflow skill dedicated to social-media carousel design, using a single-confirmation and cover-first flow to plan carousel slides and generate matching visuals through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, marketers, and content teams use this skill to plan social-media carousel narratives, confirm slide direction once, generate a cover first, and then produce remaining slides with a consistent visual system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow installs or runs a third-party npm-distributed CLI and depends on dLazy hosted services.

Mitigation: Review the linked CLI source or npm package before use, and use the npx option when a persistent global install is not desired.

Risk: Prompts and local media paths supplied to generation commands may be uploaded to dLazy services.

Mitigation: Avoid submitting sensitive prompts or media unless they are intended for dLazy processing.

Risk: The CLI stores a dLazy API key in local configuration or reads it from the DLAZY_API_KEY environment variable.

Mitigation: Use normal local credential protections and rotate or revoke the API key from the dLazy dashboard when access is no longer needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with planning tables, status updates, command snippets, and generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a stepwise confirmation flow; image generation depends on dLazy API credentials and hosted services.]

## Skill Version(s):

1.3.14 (source: ClawHub release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
