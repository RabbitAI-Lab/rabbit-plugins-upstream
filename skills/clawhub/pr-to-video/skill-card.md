## Description:

Turns a GitHub pull request into a narrated code-change explainer video using its diff, commits, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to explain a pull request's changes in a storyboarded video, from code review through a rendered MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HyperFrames commands can fetch unpinned components and update globally installed skills.

Mitigation: Use a sandboxed workspace and pin or review HyperFrames versions before running installation or updates.

Risk: Private pull-request content may be exposed to external media providers during video production.

Mitigation: Use a minimally scoped GitHub token and avoid sensitive private PRs unless the provider workflow is approved.

## Reference(s):

- [ClawHub pr-to-video release](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design](references/story-design.md)
- [Code vocabulary](references/code-vocabulary.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Video]

**Output Format:** [Markdown storyboard and script, HTML frames, and MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a GitHub pull request as the source of the explanation.]

## Skill Version(s):

1.0.47 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
