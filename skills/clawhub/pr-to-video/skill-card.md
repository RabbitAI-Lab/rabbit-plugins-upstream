## Description:

Turns a GitHub pull request into a narrated code-change explainer video using its diff, commits, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to explain a pull request as a changelog, feature reveal, fix, or refactor walkthrough video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned HyperFrames commands may update global skills or install registry blocks.

Mitigation: Review updates and registry blocks before execution; prefer a pinned local HyperFrames CLI.

Risk: Private PR contents and contributor details may be read through GitHub authentication and shared with media services.

Mitigation: Use only approved repositories and media services, and review access before processing sensitive code.

Risk: PR content is retained in project files and a local preview server may remain running.

Mitigation: Store the project securely and stop the preview server when review is complete.

## Reference(s):

- [pr-to-video on ClawHub](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Code vocabulary](references/code-vocabulary.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Video]

**Output Format:** [Markdown storyboard and script, HTML frames, and MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a persistent project with a preview and final rendered video.]

## Skill Version(s):

1.0.50 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
