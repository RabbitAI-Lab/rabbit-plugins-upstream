## Description:

Connects an agent to dLazy's project-scoped sandbox chat for multi-turn tasks and skill execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can discover available skills and projects, start a sandbox-agent chat, and continue work across turns in a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat prompts are sent to the hosted dLazy service.

Mitigation: Use the service only for information approved for external processing.

Risk: Files attached to a chat are uploaded to dLazy storage.

Mitigation: Review attached files before upload and omit sensitive material unless authorized.

Risk: Login can save an API key locally, and the skill's trigger wording is broad.

Mitigation: Protect or revoke the saved key as needed, and invoke the skill for explicit dLazy-related requests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI repository (artifact metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Conversational text, potentially including Markdown or code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn replies]

## Skill Version(s):

1.2.28 (source: ClawHub release; artifact frontmatter lists 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
