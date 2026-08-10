## Description:

ElevenLabs text-to-sound model that generates 1-22 second sound effects from a prompt for foley, ambience, alerts, and game audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and audio teams use this skill to generate short sound effects from text prompts through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any explicitly supplied local media files are sent to the dLazy hosted service for generation.

Mitigation: Review prompts and file inputs before use, and avoid submitting sensitive content unless the user accepts the service handling.

Risk: The skill requires a dLazy API key for hosted API access.

Mitigation: Use a revocable API key, store it through the documented CLI configuration or per-invocation environment variable, and rotate it if exposure is suspected.

Risk: Global CLI installation persists a binary on the user's system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses with generated file URLs and Markdown guidance containing shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation with a generateId and status polling.]

## Skill Version(s):

1.3.6 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
