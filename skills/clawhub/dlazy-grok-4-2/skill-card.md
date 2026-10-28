## Description:

Efficient text generation, dialogue QA, and logical reasoning using the Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can invoke the dLazy CLI to request the skill's advertised text generation, question answering, and reasoning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy's hosted API, and applicable usage charges may apply.

Mitigation: Avoid sending secrets or sensitive personal information, and check applicable charges before submitting prompts.

Risk: The CLI can save an API key in the local user configuration, and a key could be exposed if that account or file is compromised.

Mitigation: Use the DLAZY_API_KEY environment variable if you prefer not to save the key locally, and rotate or revoke keys through the dLazy dashboard when needed.

Risk: The text-generation capability needs verification before relying on it for chat or text output.

Mitigation: Check the current command help and response behavior with a non-sensitive prompt before depending on text output.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Generated content or a JSON response envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID when --no-wait is used.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
