## Description:

Chat with the dLazy hosted sandbox agent across multiple turns in a project-scoped conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users use the dLazy CLI to discover skills and projects, start a hosted agent conversation, and continue multi-turn work within a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected options are sent to the dLazy hosted service.

Mitigation: Invoke the external agent deliberately, preferably with an explicit request to use dLazy chat; avoid sending sensitive prompts unless appropriate.

Risk: Files attached with --files are uploaded to dLazy storage.

Mitigation: Review attachments and obtain authorization before uploading local files.

Risk: Login or auth set saves a dLazy API key locally.

Mitigation: Protect local credentials and use an API key only when intending to use the hosted service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Streaming conversational text in the terminal]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn responses]

## Skill Version(s):

1.2.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
