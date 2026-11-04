## Description:

Uses fal.ai sync-lipsync v3 to generate a video whose speaker lip movements match supplied audio, for dubbing, localization, or virtual presenters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media creators use this skill to dub or localize video and sync virtual presenters' lip movements to audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input video and audio are uploaded to dLazy's hosted media storage for processing.

Mitigation: Use media you are comfortable uploading to dLazy.

Risk: The CLI saves an API key locally, and generation may incur costs.

Mitigation: Review the pinned CLI before installation, protect the saved API key, and check command help and cost estimates before generating.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated lip-synced video URL or saved video file, with JSON task status from the CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return a task status before the output is ready.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata; bundled artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
