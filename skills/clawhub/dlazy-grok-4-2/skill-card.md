## Description:

Uses the dLazy Grok 4.2 CLI wrapper for text generation, dialogue question answering, and logical reasoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users invoke this skill through the dLazy CLI to send prompts to the hosted Grok 4.2 text model for generated text, chat-style answers, and reasoning assistance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat and question-answering triggers could route prompts to an external dLazy service when the user did not clearly request it.

Mitigation: Prefer explicit invocation of `dlazy grok-4.2` and confirm user intent before sending sensitive prompts or selected files.

Risk: Authentication stores a dLazy API key in the local CLI configuration or uses `DLAZY_API_KEY` per invocation.

Mitigation: Authenticate only when local key storage is acceptable, rotate or revoke keys from the dLazy dashboard as needed, and avoid exposing API keys in prompts, logs, or shared shells.

Risk: Global CLI installation persists third-party executable code on the system.

Mitigation: Use the pinned `npx @dlazy/cli@1.2.3` path when a temporary invocation is preferred, and review the linked CLI source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [CLI JSON response containing generated model outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous calls may return a task identifier for later polling.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
