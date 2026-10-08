## Description:

Extracts the first frame and audio from a source video, generates a video-understanding prompt, and returns a Seedance 2.0 replication bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a source video into a prompt and first-frame, audio, and video assets for a Seedance 2.0 replication workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a dLazy API key, which the CLI may save locally.

Mitigation: Confirm you trust the dLazy CLI and service before authenticating, and protect the local key.

Risk: Local media passed to the skill is uploaded to the hosted dLazy service.

Mitigation: Only submit media you are comfortable uploading to dLazy.

Risk: A global CLI installation persists on the machine.

Mitigation: Prefer the pinned-version npx invocation if you do not want a persistent global install.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may be returned as hosted links; asynchronous requests may first return a task ID.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
