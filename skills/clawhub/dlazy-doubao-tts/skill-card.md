## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can turn user-provided text into spoken audio through dLazy's Doubao TTS service, with options for language, voice, and speaking speed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately installed CLI and hosted service process submitted text and generated audio, and service use may incur costs.

Mitigation: Review the pinned package, consider service costs, and use a revocable API key.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata; provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, Files, JSON]

**Output Format:** [JSON result with generated audio output URLs; audio can also be saved to a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language, voice, and speaking speed are configurable; asynchronous jobs can return a task identifier.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
