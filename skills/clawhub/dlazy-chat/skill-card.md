## Description:

Chat with the dLazy sandbox agent, a project-scoped assistant for running skills end to end over multiple turns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to start or continue project-scoped, multi-turn conversations with dLazy's hosted agent. It supports discovering available skills and projects, sending prompts, and attaching files for the remote session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the skill suspicious: its broad activation triggers could route ordinary conversations to dLazy, and the scan found a mismatch between the advertised purpose and inspected behavior. Coverage was partial.

Mitigation: Review the activation rules and the prompts and attachments that will be sent; narrow triggers where possible and avoid sending sensitive content unless appropriate.

## Reference(s):

- [GitHub link listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Streamed conversational text, with project results or generated artifacts as provided by the selected remote skill]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn responses; attached local files are uploaded to dLazy storage before use.]

## Skill Version(s):

1.2.41 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
