## Description:

Chat with the dLazy sandbox agent for project-scoped, multi-turn skill workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to start or continue project-scoped conversations with the dLazy sandbox agent, discover available skills and projects, and optionally attach files for hosted agent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a hosted dLazy chat service that requires an API key.

Mitigation: Install only if you intend to use dLazy, avoid running the CLI with elevated privileges, and use revocable organization-scoped API keys.

Risk: Attached local files are uploaded to dLazy storage before being referenced by the chat session.

Mitigation: Attach files only when you are comfortable uploading them to dLazy storage.

Risk: Global npm installation persists a CLI binary on the user system.

Mitigation: Prefer per-invocation npx usage when you do not want a global install, and review the linked CLI source or package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and conversational text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream hosted agent responses and may reference uploaded files when the user attaches local files.]

## Skill Version(s):

1.2.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
