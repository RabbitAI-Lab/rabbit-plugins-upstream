## Description:

Generates short video spoken scripts with high contrast hooks, strong audience resonance, story structure, and personal IP positioning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to draft short-form spoken scripts for videos, character stories, and personal IP viewpoint content. It structures the script around a seven-step pattern from contrast hook through punchline ending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to install and run a third-party CLI and use dLazy cloud services.

Mitigation: Install and run the CLI only when that behavior is intended, and review the linked source and npm package before deployment.

Risk: Prompts and referenced media files may be sent to dLazy API and storage endpoints.

Mitigation: Avoid sending sensitive content, and treat CLI generation as a cloud service interaction.

Risk: The CLI supports storing a long-lived dLazy API key in local configuration.

Mitigation: Prefer per-run environment variables where practical, and rotate or revoke API keys from the dLazy dashboard when access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source and homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text script paragraphs, with optional inline bash command blocks when using the dLazy CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated result URLs from files.dlazy.com when CLI generation is explicitly used.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
