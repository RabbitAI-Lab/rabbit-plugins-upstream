## Description:

ElevenLabs text-to-sound model — generates 1–22s short sound effects from a description, suitable for foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators can generate short sound effects from text descriptions for foley, ambience, alerts, and games.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any selected local media files are sent to dLazy services for generation.

Mitigation: Send only prompts and files you intend to share with that service.

Risk: Generation can consume dLazy service credits.

Mitigation: Use the dry-run option to review the payload and cost estimate before making an API request.

Risk: The pinned CLI executable implementation was outside the inspected release bundle.

Mitigation: Review the pinned CLI package before installing or running it.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [Generated sound-effect audio, returned with JSON output metadata and a hosted URL; optionally saved to a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sound effects are 1–22 seconds long; the default duration is 5 seconds.]

## Skill Version(s):

1.3.38 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
