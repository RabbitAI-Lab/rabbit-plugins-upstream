## Description:

Chat with the dlazy sandbox agent — a project-scoped assistant that runs skills end-to-end over multiple turns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue project-scoped conversations with the dLazy hosted sandbox agent, including multi-turn work and optional file attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy during normal use.

Mitigation: Avoid sending sensitive prompts unless the user intends to share them with dLazy.

Risk: The skill stores or uses a dLazy API key.

Mitigation: Use `dlazy login`, `dlazy auth set`, or `DLAZY_API_KEY` intentionally, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Files attached with `--files` are uploaded before they are referenced by the agent.

Mitigation: Attach only files intended for upload, and use `npx @dlazy/cli@1.2.3` when avoiding a persistent global CLI install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI GitHub repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream agent responses through the dLazy CLI and may reference uploaded files when the user explicitly attaches them.]

## Skill Version(s):

1.2.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
