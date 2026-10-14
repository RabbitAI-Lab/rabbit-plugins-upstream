## Description:

Generates Suno music with automatic or custom lyrics, with vocals or as an instrumental track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request original music from the dLazy Suno service, choosing automatic or supplied lyrics and vocal or instrumental output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI can store an API key locally and send prompts to a hosted service.

Mitigation: Use a trusted dLazy account and review what prompts and credentials you provide.

Risk: Media file paths supplied to the CLI may be uploaded, and generation may consume paid credits.

Mitigation: Share only intended files and check the cost estimate with --dry-run before generation.

Risk: A global CLI installation persists on the device.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 command if a persistent installation is not wanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance and shell commands; the CLI returns JSON with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of immediate media URLs.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
