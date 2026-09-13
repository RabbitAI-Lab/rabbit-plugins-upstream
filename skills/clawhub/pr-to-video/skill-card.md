## Description:

Turns a GitHub pull request into a code-change explainer video for changelogs, feature reveals, fixes, or refactor walkthroughs using the PR diff, commits, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn a GitHub pull request into a source-traceable HyperFrames explainer video with a storyboard, narration or captions, animated code frames, and a rendered MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on mutable external HyperFrames and npm-resolved code during execution.

Mitigation: Use a pinned or preinstalled HyperFrames CLI and review any skill or registry updates before accepting them.

Risk: The workflow may update global HyperFrames skills during setup.

Mitigation: Run it in a project-scoped sandbox and review global skill changes before use.

Risk: The workflow uses GitHub CLI access to read the target pull request and can optionally use HeyGen or media credentials.

Mitigation: Limit the runtime environment to the needed repository and credentials, and avoid exposing unnecessary home-directory secrets.

## Reference(s):

- [Story design](artifact/references/story-design.md)
- [Visual design](artifact/references/visual-design.md)
- [Code vocabulary](artifact/references/code-vocabulary.md)
- [Motion language](artifact/references/motion-language.md)
- [Cut catalog](artifact/references/cut-catalog.md)
- [Frame worker PR-to-video delta](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, generated project files, HTML frame code, JSON metadata, and MP4 video output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a project-scoped HyperFrames workflow that may create storyboard, script, captions, frame compositions, contact sheets, and renders/video.mp4.]

## Skill Version(s):

1.0.34 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
