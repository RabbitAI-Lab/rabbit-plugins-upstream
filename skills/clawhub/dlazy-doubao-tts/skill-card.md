## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn text prompts into speech with Doubao TTS, choosing a language and voice and optionally saving the generated asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI's login behavior and requested account access were not fully inspected; security inspection was partial with medium confidence.

Mitigation: Before installing or authenticating, review the CLI and confirm that its login flow and requested organization access are expected.

## Reference(s):

- [dLazy CLI source link listed by the skill](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated speech asset, with a JSON result envelope containing its URL; the asset can optionally be saved as a file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice and language are selectable; the skill documents synchronous and asynchronous generation.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
