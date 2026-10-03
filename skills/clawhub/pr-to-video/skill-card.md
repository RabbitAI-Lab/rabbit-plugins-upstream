## Description:

Turns a GitHub pull request into a code-change explainer video using its diff, commits, and changed files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to explain a pull request as a narrated or captioned video showing the change and its impact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable HyperFrames and npm tooling or registry blocks may change between runs.

Mitigation: Review dependencies before installation and prefer a pinned or locally locked HyperFrames CLI.

Risk: Setup can update globally installed skills.

Mitigation: Review and confirm skill updates before running setup; check automatic update behavior.

Risk: The workflow reads pull-request data through GitHub CLI and may use media credentials and run a local preview server.

Mitigation: Use only approved PRs and credentials, and review project output and local preview access.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Code vocabulary](references/code-vocabulary.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Video]

**Output Format:** [Markdown storyboard and script, HTML frames, and MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project files are written to a cache or user-selected project directory.]

## Skill Version(s):

1.0.45 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
