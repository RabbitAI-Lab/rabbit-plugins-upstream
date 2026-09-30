## Description:

Turns a GitHub pull request into a narrated code-change explainer video using its diff, commits, and changed files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn a GitHub pull request into a short, reviewable video explaining what changed and why.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted PR diff text may influence frame-worker instructions.

Mitigation: Review third-party PR content and constrain worker tools and filesystem access before processing it.

Risk: Live, unpinned tool updates and registry installs may change the code that runs.

Mitigation: Review dependency and skill updates before running them in a controlled environment.

Risk: PR content may be sent through GitHub, HyperFrames, or HeyGen-related services.

Mitigation: Check data-sharing permissions and avoid sending confidential PRs without approval.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design](artifact/references/story-design.md)
- [Visual design](artifact/references/visual-design.md)
- [Code vocabulary](artifact/references/code-vocabulary.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Video]

**Output Format:** [Markdown storyboard and script, HTML frames, and MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include narration, captions, and a contact sheet.]

## Skill Version(s):

1.0.43 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
