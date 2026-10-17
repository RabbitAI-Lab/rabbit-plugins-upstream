## Description:

Turns a GitHub pull request into a code-change explainer video using its diff, commits, and changed files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to explain a GitHub pull request as a narrated changelog, feature reveal, fix, or refactor walkthrough.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HyperFrames tooling and live registry blocks can change between runs.

Mitigation: Use a pinned, reviewed HyperFrames version and review blocks before installing them.

Risk: PR ingestion and audio generation can access local GitHub and media-provider credentials.

Mitigation: Use scoped GitHub credentials and approve media-provider access only when needed.

Risk: The workflow may update global HyperFrames skills and start a local preview server.

Mitigation: Review updates before running them and stop the preview server after use.

## Reference(s):

- [pr-to-video release on ClawHub](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design guide](references/story-design.md)
- [Visual design guide](references/visual-design.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Video files]

**Output Format:** [Markdown brief, storyboard and script; HTML frames; rendered MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional narration, captions, and contributor credits.]

## Skill Version(s):

1.0.51 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
