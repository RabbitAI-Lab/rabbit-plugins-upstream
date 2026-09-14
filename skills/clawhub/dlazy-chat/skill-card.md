## Description:

Chat with the dLazy sandbox agent, a project-scoped assistant for multi-turn work that can run skills end-to-end.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to start or continue project-scoped, multi-turn conversations with the dLazy hosted sandbox agent, including chats that reference existing projects, selected skills, and attached local files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, options, and attached files to the dLazy hosted service.

Mitigation: Only attach files and share content that are appropriate to upload to dLazy; review organizational data-handling requirements before use.

Risk: The dLazy API key is stored locally or supplied through the environment.

Mitigation: Treat the API key as a credential, use least-persistent authentication where practical, and rotate or revoke it if the machine or package environment is suspected of compromise.

Risk: Installing the CLI globally creates a persistent executable from an npm package.

Mitigation: Review the dLazy CLI source or package before installation and prefer the pinned npx path unless a global binary is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Terminal chat output and Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from the hosted dLazy agent and may reference files uploaded through the dLazy CLI.]

## Skill Version(s):

1.2.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
