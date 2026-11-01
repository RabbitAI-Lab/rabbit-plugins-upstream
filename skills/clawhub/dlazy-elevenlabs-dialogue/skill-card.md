## Description:

Generates ElevenLabs eleven_v3 multi-voice dialogue audio, assigning a voice to each line and supporting expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a scripted conversation into a single multi-voice audio performance for character dialogue, podcasts, and short skits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue and selected media are sent to dLazy cloud services, and generation may incur account costs.

Mitigation: Send only content intended for cloud processing and check expected generation costs before running.

Risk: The dLazy API key is stored locally by the CLI, and its separate CLI dependency was not audited in this artifact review.

Mitigation: Protect the local API key, rotate or revoke it if exposed, and review the CLI before installing or upgrading it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio]

**Output Format:** [Generated dialogue audio asset, returned as a hosted URL or saved to a local file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 20 dialogue lines and 10 distinct voices; asynchronous task status is available when requested.]

## Skill Version(s):

1.3.35 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
