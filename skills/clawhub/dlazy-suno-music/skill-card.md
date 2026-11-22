## Description:

Suno music generation model that creates music with or without vocals using inspiration mode with auto-generated lyrics or custom mode with manually supplied lyrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can generate music from prompts, choosing automatic or custom lyrics, vocals, or instrumental output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the login operation as unexplained in relation to the music-generation purpose.

Mitigation: Review the login and account setup details before authenticating, and use a dLazy API key only if the hosted service is intended.

Risk: The security analysis is partial because some referenced paths or resources were unavailable.

Mitigation: Review the referenced materials and resolve unavailable paths before relying on the benign verdict.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy homepage](https://dlazy.com)
- [CLI source listed in the skill documentation](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio files, JSON, Shell commands]

**Output Format:** [Generated audio assets and a JSON response containing result URLs or asynchronous task status; optional local audio file when saved.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation accepts a text prompt and optional style, title, vocal, and instrumental settings.]

## Skill Version(s):

1.3.41 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
