## Description:

Chat with the dLazy sandbox agent, a project-scoped assistant for multi-turn, end-to-end skill execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run multi-turn conversations with the dLazy hosted sandbox agent, discover available skills and projects, and continue project-scoped sessions from the terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, command options, and attached files may be sent to dLazy services.

Mitigation: Use the skill only for prompts and files appropriate for dLazy cloud processing, and avoid attaching sensitive local files unless sharing them is intended.

Risk: The dLazy API key can be saved in the local CLI configuration.

Mitigation: Protect the CLI config file, rotate or revoke keys when needed, or provide DLAZY_API_KEY per command instead of persisting a key.

Risk: Generic chat triggers could invoke the dLazy CLI when another local workflow was intended.

Mitigation: Confirm the command is intentionally targeting dLazy before running chat commands or uploading files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and terminal-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy CLI commands; local files attached with --files are uploaded by the dLazy CLI before use.]

## Skill Version(s):

1.2.20 (source: server release evidence; artifact frontmatter lists 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
