## Description:

Video replicate tool: extracts the first frame and audio from the source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle (first frame + audio + video).

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy's video replication workflow on a reference video and return a first frame, extracted audio, and generated video bundle. It is useful when recreating the structure of a source video through a hosted media generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source videos, prompts, and selected media files may be uploaded to dLazy's hosted API and media storage.

Mitigation: Use the skill only with media and prompts that are appropriate for processing by dLazy's cloud service.

Risk: A dLazy API key may be stored in the local CLI configuration for authentication.

Mitigation: Prefer per-invocation credentials or npx when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated media URLs, optional downloaded files, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return asynchronous task identifiers when invoked with --no-wait and can save generated assets to a local path when --save is provided.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
