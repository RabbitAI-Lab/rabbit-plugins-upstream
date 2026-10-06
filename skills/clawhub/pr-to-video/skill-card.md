## Description:

Turns a GitHub pull request into a code-change explainer video using its diff, commits, and changed files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn a GitHub pull request into a narrated visual walkthrough of a feature, fix, or refactor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to private pull requests may expose sensitive code through GitHub authentication and an external video project.

Mitigation: Use only approved repositories and a sandboxed project environment; review the PR content before sharing the video or project.

Risk: Unpinned HyperFrames commands and registry blocks can change between runs.

Mitigation: Review and pin HyperFrames tooling and registry blocks before installation or execution.

Risk: Skill setup may update globally installed HyperFrames skills.

Mitigation: Review updates before approval and run the workflow in an isolated environment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Code vocabulary](references/code-vocabulary.md)
- [Cut catalog](references/cut-catalog.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Video]

**Output Format:** [Markdown planning documents, HTML frames, and an MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video content is derived from the selected pull request.]

## Skill Version(s):

1.0.46 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
