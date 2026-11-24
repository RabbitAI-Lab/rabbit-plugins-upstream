## Description:

Generates original 10–300 second music tracks from natural-language prompts using the ElevenLabs music_v1 model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and developers can generate original music for background audio, advertisements, and short-video soundtracks by supplying a natural-language prompt and duration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial: it found no clear harmful behavior but reported a mismatch between the demonstrated CLI authentication behavior and the stated music-generation purpose, with package, configuration, and API details unresolved.

Mitigation: Before installation, review the pinned @dlazy/cli 1.2.3 package and confirm that its authentication flow and requested actions match the intended music-generation use.

Risk: The skill sends prompts to dLazy's hosted API and stores the API key in the local CLI configuration when using the documented login flow.

Mitigation: Avoid submitting sensitive prompt content, protect the local configuration file, and rotate or revoke the organization key if it may have been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI repository (referenced by skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Hosted music asset with JSON result metadata and asset URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Music duration is 10–300 seconds (default 30 seconds); asynchronous jobs may return a task identifier before the asset is ready.]

## Skill Version(s):

1.3.44 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
