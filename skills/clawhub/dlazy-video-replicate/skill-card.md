## Description:

Helps replicate a source video by deriving a prompt and producing a Seedance 2.0 bundle with a first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to derive a video-replication prompt and obtain first-frame, audio, and video results from a source video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and prompts are sent to dLazy services.

Mitigation: Review the media and prompts before submission and check dLazy's terms before use.

Risk: The CLI can save an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard if needed.

Risk: Installing the third-party CLI runs external package code.

Mitigation: Review the pinned @dlazy/cli package before installing; use its npx invocation to avoid a persistent global install.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (skill metadata link; not verified release provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON results]

**Output Format:** [Markdown guidance and CLI JSON containing media URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include generated media links; asynchronous requests require a follow-up status check.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
