## Description:

The ElevenLabs music_v1 model generates 10–300-second original music from natural-language prompts for background music, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators can generate 10–300-second music tracks from natural-language prompts for background music, ads, and short-video soundtracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied media are sent to dLazy, and generation spends service credits.

Mitigation: Only send content you are comfortable sharing, and use --dry-run to preview the payload and estimated cost.

Risk: The pinned CLI implementation and its credential-file protections were outside the bundled artifact review.

Mitigation: Review the pinned CLI before installation and use a revocable API key.

## Reference(s):

- [dLazy CLI project (release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [JSON result with a generated audio asset URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio is returned by URL; asynchronous mode can return a task ID.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
