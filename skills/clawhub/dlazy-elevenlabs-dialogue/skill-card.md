## Description:

Generates ElevenLabs eleven_v3 dialogue audio with up to ten distinct voices and expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, podcasters, and developers can turn multi-speaker dialogue into generated audio, assigning voices per line and using tags such as whispers or giggling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue prompts and supplied media may be sent to dLazy-hosted services.

Mitigation: Share only text and files you intend to send to that service.

Risk: The CLI can save an API key in the local user configuration file.

Mitigation: Restrict access to the local configuration and rotate or revoke a key if it may have been exposed.

Risk: The pinned CLI executable and its hosted-service handling were not verified in the release review.

Mitigation: Review the pinned @dlazy/cli version before installing or using it with sensitive content.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source (declared by the skill)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service and documentation](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Audio files, JSON result metadata]

**Output Format:** [Generated dialogue audio returned as a result URL or saved to a local path, with structured result metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 20 dialogue lines and up to 10 unique voices per request; audio can be saved with --save.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
