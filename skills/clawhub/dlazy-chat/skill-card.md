## Description:

Chat with the dLazy sandbox agent, a project-scoped assistant that can run skills end-to-end over multiple turns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to start or continue project-scoped, multi-turn conversations with the dLazy hosted sandbox agent through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat-like requests can trigger a remote SaaS agent using a saved dLazy API key.

Mitigation: Use the skill only when you intentionally want to send prompts to dLazy, prefer explicit dlazy chat invocations, and keep the API key revocable.

Risk: Attached files may be uploaded to dLazy storage before being referenced by the agent.

Mitigation: Attach files only when you are comfortable uploading them to dLazy storage.

Risk: Saved project chat sessions may reuse prior project context.

Mitigation: Clear sessions when you do not want project context reused.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or terminal text streamed from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may depend on the selected dLazy skill, project, uploaded files, and saved chat session context.]

## Skill Version(s):

1.2.13 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
