## Description:

This skill helps an agent generate high-contrast, story-driven spoken scripts for short videos, character stories, and personal-IP viewpoint content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content agents use this skill to draft colloquial short-video spoken scripts with a hook, story arc, point of view, and punchline. It is also relevant when the user intentionally wants dLazy CLI-assisted media generation alongside script writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is advertised as a spoken-script writer but also asks the agent to use a terminal-based dLazy image-generation CLI with API credentials.

Mitigation: Review the skill before installation and use it only when CLI-based dLazy generation is intended.

Risk: Using the skill may require installing or running an npm package and authenticating with a dLazy API key.

Mitigation: Review the package source and version, protect the API key, and rotate or revoke credentials when they are no longer needed.

Risk: Prompts and media file paths may be sent to dLazy services during CLI-assisted generation.

Mitigation: Avoid submitting sensitive prompts, confidential media, or private local paths unless that data sharing is approved.

Risk: The artifact instructs the agent to execute generation commands after user confirmation.

Mitigation: Require explicit user confirmation before each command and run only one synchronous generation command at a time.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text script content with optional CLI commands and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated scripts follow a seven-step short-video spoken-script structure; CLI-assisted generation should run one command at a time after user confirmation.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
