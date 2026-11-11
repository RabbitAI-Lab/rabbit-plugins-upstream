## Description:

Generate ElevenLabs eleven_v3 dialogue with up to 10 distinct voices, assigning a voice to each line and supporting expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to produce character dialogue, podcast segments, and short skits with ElevenLabs eleven_v3, assigning voices to individual lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had medium confidence and could not determine the downstream behavior of the reported dLazy login and authentication steps.

Mitigation: Confirm dLazy authentication is expected for your use and review the requested access before signing in.

Risk: Dialogue text is sent to dLazy's hosted API for generation.

Mitigation: Avoid sending confidential or personal dialogue unless your data-handling requirements permit processing by that service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy](https://dlazy.com)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated dialogue audio with JSON result metadata and asset URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 20 dialogue lines and 10 unique voices; generation can return asynchronously.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
