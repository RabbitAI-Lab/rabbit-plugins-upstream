## Description:

Automatically selects a suitable dLazy CLI model for audio and text-to-speech generation based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can request generated speech, music, dialogue, or sound effects in natural language. The agent selects a suitable dLazy CLI audio model and returns the generated media result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local media supplied to the CLI are sent to dLazy's hosted service; local media is uploaded to its media storage.

Mitigation: Review prompts and files before invocation, and provide only media you intend to send to the hosted service.

Risk: The security scan has partial coverage because several local references could not be resolved.

Mitigation: Review the skill and its referenced materials before installation or use.

## Reference(s):

- [dLazy CLI project repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, Guidance]

**Output Format:** [Generated audio results referenced by hosted URLs, with JSON response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports speech, music, dialogue, and sound effects; voice-search results include playable previews.]

## Skill Version(s):

1.3.44 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
