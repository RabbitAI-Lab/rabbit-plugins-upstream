## Description:

Generates 10–300 seconds of original music from natural-language prompts using ElevenLabs music_v1, for background music, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and developers use this skill to generate original background music, ad music, and short-video soundtracks from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied local media are sent to dLazy hosted services; generated assets are hosted there as well.

Mitigation: Avoid sending sensitive prompts or media unless their use with the hosted service is approved.

Risk: The security scan was partial, with some referenced paths and the CLI package unavailable for inspection.

Mitigation: Review the CLI package and its installation instructions before installing it.

Risk: The CLI uses a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Protect the key, and rotate or revoke it through the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy website](https://dlazy.com)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated music audio asset, returned with a JSON response containing its URL; optionally saved as a local audio file.]

**Output Parameters:** [One music track, 10–300 seconds.]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier for later status checks.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
