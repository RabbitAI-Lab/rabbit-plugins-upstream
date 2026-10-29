## Description:

Chat with the dLazy sandbox agent, a project-scoped assistant for running skills across multiple turns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to discover dLazy projects or templates and hold multi-turn conversations with a project-scoped sandbox agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat triggers could send unrelated requests to dLazy without clear user intent.

Mitigation: Use the skill only for explicitly requested dLazy work and restrict generic chat activation where possible.

Risk: Prompts and attached files leave the device, and project sessions retain context.

Mitigation: Review prompts and files before sending, and avoid including sensitive information unless authorized.

Risk: Requests may consume credits, and the saved API key grants access to the dLazy organization.

Mitigation: Protect the saved key, rotate or revoke it when needed, and monitor credit usage.

## Reference(s):

- [CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [Streamed conversational text and task-dependent files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the selected dLazy skill or project; attached files are uploaded to the hosted service.]

## Skill Version(s):

1.2.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
