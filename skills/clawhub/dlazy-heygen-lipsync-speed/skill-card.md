## Description:

HeyGen Lipsync Speed helps agents run a fast lip-sync generation workflow through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate lip-synced media quickly from supplied video and audio inputs through dLazy's HeyGen Lipsync Speed model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files supplied to video or audio parameters may be uploaded to dLazy's hosted service for processing.

Mitigation: Avoid private or sensitive media unless the user accepts dLazy handling the files.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation credentials when appropriate and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: The skill depends on a third-party npm CLI and cloud service.

Mitigation: Prefer the pinned npx invocation or review the pinned CLI package and source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files]

**Output Format:** [Markdown guidance with bash command examples and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or asynchronous task IDs; the CLI can save generated assets locally.]

## Skill Version(s):

1.3.19 (source: server release evidence; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
