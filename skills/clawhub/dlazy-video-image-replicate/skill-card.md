## Description:

Studies a provided reference image or video and recreates its look and structure using the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy hosted video-image-replicate agent for reference-based image or video recreation. It supports project-based continuation and optional local file attachments through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to the third-party dLazy service.

Mitigation: Use the skill only for content you intend to share with dLazy, and avoid attaching sensitive or restricted files.

Risk: The dLazy API key is stored locally or supplied to the CLI.

Mitigation: Use scoped organization keys where available, protect the local config file, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Installing the CLI globally adds a third-party npm package to the user's environment.

Mitigation: Prefer the pinned npx invocation for on-demand use, or review the linked CLI source before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, dLazy authentication, and optional local file uploads through the dLazy CLI.]

## Skill Version(s):

1.3.16 (source: release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
