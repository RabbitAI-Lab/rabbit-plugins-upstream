## Description:

Video human segmentation tool that invokes Aliyun's async SegmentVideoBody and returns a same-length black/white mask video for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to submit videos to dLazy's hosted video segmentation service and retrieve mask video output for compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI.

Mitigation: Prefer `npx @dlazy/cli@1.2.3` for one-off use, or review the pinned package and source before a global install.

Risk: The CLI stores or accepts a dLazy API key.

Mitigation: Use OS-user-restricted config permissions, prefer per-invocation `DLAZY_API_KEY` where appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: User-provided video paths are uploaded to dLazy-hosted services for processing.

Mitigation: Only submit videos approved for third-party cloud processing and review dLazy service terms before use.

Risk: The documentation has parameter and output-format inconsistencies around `--prompt` and image/png examples.

Mitigation: Run `dlazy videoseg -h` before execution and rely on live CLI help over stale examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown instructions with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return result URLs, async task metadata, and saved output files; local input videos are uploaded to dLazy-hosted services when provided.]

## Skill Version(s):

1.3.21 (source: server release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
