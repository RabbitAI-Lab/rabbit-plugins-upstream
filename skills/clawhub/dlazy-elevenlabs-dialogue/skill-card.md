## Description:

Generates ElevenLabs eleven_v3 dialogue audio with up to 10 distinct voices assigned across a conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can turn dialogue lines into a single multi-voice ElevenLabs eleven_v3 audio track for character scenes, podcasts, or short skits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found unexplained dLazy authentication steps and did not fully inspect the CLI; dialogue is sent to the hosted service for generation.

Mitigation: Review the CLI authentication flow and dLazy service terms, and send only dialogue content you are comfortable processing through that service.

## Reference(s):

- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio asset with JSON result or task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result can be returned as a hosted URL or saved locally; asynchronous runs can return a task identifier.]

## Skill Version(s):

1.3.42 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
