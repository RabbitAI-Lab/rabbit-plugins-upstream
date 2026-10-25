## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate multilingual speech from prompts with Gemini 2.5 text-to-speech, choosing a voice language and voice. The agent receives a result envelope with generated-media links or asynchronous task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent through dLazy's hosted API, so sensitive text may leave the local environment.

Mitigation: Review dLazy's privacy and pricing terms, and avoid sending confidential text unless approved.

Risk: Authentication may store the dLazy API key in the local CLI configuration.

Mitigation: Use the documented DLAZY_API_KEY environment-variable option to avoid saving the key locally; rotate or revoke keys through the account dashboard when needed.

## Reference(s):

- [dLazy CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [JSON result envelope with generated-media links or asynchronous task status]

**Output Parameters:** [1D (prompt-driven; optional voice language and voice selection)]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; asynchronous requests may initially return a task ID.]

## Skill Version(s):

1.3.32 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
