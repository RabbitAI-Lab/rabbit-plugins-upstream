## Description:

Generates 10–300 seconds of original music from a text prompt for background music, ads, and short videos using ElevenLabs music_v1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short original music for background tracks, advertisements, and videos through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly supplied to the CLI may be sent to dLazy, and generated outputs are hosted by dLazy.

Mitigation: Avoid submitting sensitive prompts or files unless sharing them with dLazy is acceptable.

Risk: The skill uses a third-party npm CLI and stores an API key locally after login.

Mitigation: Prefer the pinned npx command to avoid a global install; rotate or revoke the key in the dLazy dashboard if necessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown instructions with shell commands and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation results include hosted output links; an optional save path downloads the asset locally.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
