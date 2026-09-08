## Description:

Chat with the dLazy sandbox agent to start or continue project-scoped, multi-turn agent work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to start or continue dLazy sandbox-agent chats, discover available skills and projects, attach files when needed, and manage project sessions through the pinned dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, session context, selected project identifiers, and attached files may be sent to dLazy services.

Mitigation: Avoid attaching sensitive files unless that is intended, and review organization data-sharing requirements before use.

Risk: Installing the npm CLI globally leaves a persistent local command available on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution, or install globally only after trusting dLazy and the pinned package.

Risk: The skill requires a dLazy API key that may be saved locally or supplied through the environment.

Mitigation: Protect the local CLI config and environment, and rotate or revoke the organization-scoped key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source link from skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Terminal text or Markdown streamed by the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and dLazy service access; attached files may be uploaded to dLazy storage.]

## Skill Version(s):

1.2.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
