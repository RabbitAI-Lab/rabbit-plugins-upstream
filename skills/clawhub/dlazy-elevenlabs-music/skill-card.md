## Description:

Generates original 10–300 second music tracks from natural-language prompts using ElevenLabs music_v1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, advertisers, and video producers use this skill to generate original background music, ad music, and short-video soundtracks from natural-language prompts. A dLazy API key is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media supplied to the skill are sent to dLazy's hosted service, and generation uses service credits.

Mitigation: Avoid sending sensitive material, review dLazy's service terms, and use --dry-run to preview the request and estimated cost.

Risk: The dLazy API key is stored in local CLI configuration; protections in the external CLI build were not verified.

Mitigation: Protect the local configuration file and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON result metadata]

**Output Format:** [Generated audio track returned as a URL or saved file, with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One track per request; duration is 10–300 seconds. Asynchronous runs may return task status before the audio is ready.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
