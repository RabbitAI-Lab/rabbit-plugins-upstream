## Description:

Efficient text generation, dialogue QA, and logical reasoning using the Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Grok 4.2 text model for prompt-based text generation, dialogue question answering, and logical reasoning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger words could cause ordinary chats to be routed through dLazy.

Mitigation: Prefer explicit invocation with `dlazy grok-4.2` and review the prompt and parameters before sending a request.

Risk: Selected prompts, parameters, and explicitly referenced local files may be sent to dLazy services.

Mitigation: Do not pass sensitive prompts or file paths unless sharing them with dLazy is acceptable for the user's use case.

Risk: Persistent CLI login stores a dLazy API key on the local machine.

Mitigation: Use `DLAZY_API_KEY` per invocation on shared machines, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; prompts and explicitly referenced local files may be sent to dLazy endpoints.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
