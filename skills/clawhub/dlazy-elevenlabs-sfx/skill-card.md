## Description:

Generates 1–22 second sound effects from text descriptions using the ElevenLabs text-to-sound model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate short sound effects from text prompts for foley, ambience, alerts, and game audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy for generation, and submitted content may be processed by its hosted service.

Mitigation: Send only prompts and media you intend to share with the service.

Risk: Generation can consume paid credits.

Mitigation: Use --dry-run to review the request and cost estimate before generation, and check available credits.

Risk: The dLazy API key may be stored in the CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when preferred, and rotate or revoke keys from the dLazy dashboard.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [JSON result with generated audio URLs; audio can also be saved to a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated sound effects are 1–22 seconds long; asynchronous jobs and local saving are supported.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
