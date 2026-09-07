## Description:

Chat with the dlazy sandbox agent, a project-scoped assistant that runs skills end-to-end over multiple turns and can continue conversational work across project sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to start or continue multi-turn conversations with the dLazy hosted sandbox agent for project-scoped tasks. It is suited to conversational workflows where the agent may run selected skills and retain session context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and options to the dLazy API and uploads files passed with --files to dLazy media storage.

Mitigation: Review local files before attaching them, avoid sending sensitive data unless the dLazy service terms and organization policy allow it, and use explicit prompts for intended dLazy work.

Risk: Using the npm CLI introduces normal third-party package supply-chain exposure.

Mitigation: Use the pinned @dlazy/cli version from the skill metadata, prefer npx or an isolated environment when a global install is not desired, and review the package/source before installation.

Risk: The hosted CLI requires a dLazy API key stored in local config or supplied through an environment variable.

Mitigation: Protect the API key, use OS user-level file permissions, and rotate or revoke the key from the dLazy dashboard if it may be exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or terminal text streamed from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project, skill, session, and file attachment options passed to dlazy chat.]

## Skill Version(s):

1.2.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
