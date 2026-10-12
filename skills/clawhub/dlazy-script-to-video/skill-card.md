## Description:

Turns scripts into storyboarded, shot-by-shot videos using dLazy's hosted generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video production teams use this skill to turn scripts or scene breakdowns into multi-shot storyboarded videos with consistent characters, audio, and subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy's hosted service.

Mitigation: Attach only files intended for dLazy and avoid sharing sensitive prompts.

Risk: Signing in can store a dLazy API key locally.

Mitigation: Protect the local configuration or use a per-invocation API key; rotate the key if exposed.

Risk: A global CLI installation persists on the user's machine.

Mitigation: Use the pinned npx invocation when a persistent installation is not wanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Video]

**Output Format:** [Streaming text responses and hosted video-generation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped conversations support follow-up requests.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
