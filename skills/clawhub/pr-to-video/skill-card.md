## Description:

Turns a GitHub pull request into a code-change explainer video built from the PR diff, commits, files, and contributor metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn a GitHub pull request into a narrated HyperFrames explainer video for changelogs, feature reveals, fixes, or refactor walkthroughs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses existing GitHub authentication to read PR content and related metadata.

Mitigation: Confirm the GitHub account and repository access are appropriate before running the PR fetch step.

Risk: PR diffs and contributor identities are stored in a local HyperFrames project directory.

Mitigation: Use an approved local project location and remove generated artifacts when the PR content should no longer be retained.

Risk: The workflow may use HeyGen or other media providers when signed in.

Mitigation: Review provider sign-in status and offline fallback behavior before generating narration, music, or media assets.

Risk: Generated HTML can load GSAP from jsDelivr during preview or rendering.

Mitigation: Run previews and renders only in environments where that CDN dependency is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Publisher profile](https://clawhub.ai/user/heygen-com)
- [Code vocabulary](artifact/references/code-vocabulary.md)
- [Story design](artifact/references/story-design.md)
- [Visual design](artifact/references/visual-design.md)
- [Motion language](artifact/references/motion-language.md)
- [Cut catalog](artifact/references/cut-catalog.md)
- [Frame worker](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown workflow guidance with shell commands and generated HyperFrames project files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces storyboard and script markdown, HTML frame compositions, media metadata, and a final MP4 render in a project directory.]

## Skill Version(s):

1.0.30 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
