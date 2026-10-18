## Description:

Turns a GitHub pull request into a narrated code-change explainer video grounded in its diff, commits, and changed files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to explain a pull request as a changelog, feature reveal, fix, or refactor walkthrough video for reviewers or stakeholders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live, unpinned npm and registry tooling may introduce unexpected changes.

Mitigation: Prefer a locked or preinstalled HyperFrames CLI and approve storyboard-named blocks before installation.

Risk: Private pull requests and GitHub or media-provider credentials may be exposed during processing.

Mitigation: Review the skill before use and run it in a sandbox when access to private PRs or credentials is sensitive.

Risk: Local preview servers may be accessible beyond the intended review session.

Mitigation: Keep previews in a controlled environment and stop the project preview server after review.

## Reference(s):

- [PR to Video release](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design reference](artifact/references/story-design.md)
- [Visual design reference](artifact/references/visual-design.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Files]

**Output Format:** [Markdown storyboard and script, project assets, and rendered MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a contact sheet and frame identifiers for review and revisions.]

## Skill Version(s):

1.0.52 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
