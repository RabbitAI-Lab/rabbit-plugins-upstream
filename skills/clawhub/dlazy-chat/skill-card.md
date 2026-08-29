## Description:

Chat with the dLazy sandbox agent as a project-scoped, multi-turn assistant that can run dLazy skills end to end.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to start or continue project-scoped conversations with the hosted dLazy sandbox agent, discover available dLazy skills and projects, and attach files deliberately when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a remote hosted agent workflow and sends chat content to dLazy API endpoints.

Mitigation: Use the skill only when dLazy is an intended external service for the task and avoid sending sensitive content unless approved.

Risk: Attached local files are uploaded to dLazy media storage before being referenced by the chat.

Mitigation: Attach files only deliberately and review filenames and contents before using the --files option.

Risk: The dLazy API key can be persisted in a local CLI configuration file.

Mitigation: Prefer environment-scoped credentials when appropriate, rotate or revoke keys from the dLazy dashboard, and verify local config-file permissions.

Risk: Broad chat triggers may invoke a remote SaaS workflow when a narrower local action was intended.

Mitigation: Use explicit dLazy-specific prompts and confirm the selected project or skill id before continuing a session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the dLazy API and upload explicitly attached local files through the dLazy CLI.]

## Skill Version(s):

1.2.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
