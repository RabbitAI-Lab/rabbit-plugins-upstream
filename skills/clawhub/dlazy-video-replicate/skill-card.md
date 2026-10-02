## Description:

Helps replicate a source video by extracting its first frame and audio, deriving a prompt through video understanding, and returning a Seedance 2.0 replication bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prepare a video replication workflow from a reference video, including a first frame, audio, and a generated video prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and a hosted service.

Mitigation: Review the CLI before installing; use the pinned npx invocation if a global installation is not desired.

Risk: Selected prompts and media files are sent to dLazy's cloud service.

Mitigation: Share only content appropriate for upload to that service.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Protect the local key and rotate or revoke it if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance and JSON responses containing media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include first-frame, audio, and video assets; asynchronous requests can return a task ID.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
