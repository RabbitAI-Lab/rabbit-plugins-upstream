## Description:

Uses the dLazy CLI to generate fast lip-synced video from supplied video and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to synchronize a video's lip movements with supplied audio, with optional captions and audio enhancement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI runs external package code.

Mitigation: Review @dlazy/cli before installing; use the pinned npx @dlazy/cli@1.2.3 invocation to avoid a persistent global binary.

Risk: Local media supplied to the CLI is uploaded to dLazy.

Mitigation: Only supply video and audio files you intend to upload to the hosted service.

Risk: CLI login stores the API key in a local configuration file.

Mitigation: Use DLAZY_API_KEY per invocation if you do not want the key saved locally.

Risk: The documented example and output format may not match actual CLI behavior.

Mitigation: Check dlazy heygen-lipsync-speed -h and confirm the response before relying on the documented example.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI repository (artifact metadata link; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [CLI JSON response with a hosted result URL or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local download via --save; documented example command and output format may be inaccurate.]

## Skill Version(s):

1.3.29 (source: ClawHub release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
