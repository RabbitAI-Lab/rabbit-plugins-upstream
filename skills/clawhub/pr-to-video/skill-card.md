## Description:

Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video - changelog, feature reveal, fix, or refactor walkthrough built from the diff, commits, and files: the input is a code change, not a website.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to convert GitHub pull requests into code-change explainer videos that summarize what changed, why it matters, and how the implementation works.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs GitHub CLI commands and may access private pull request data available to the active gh session.

Mitigation: Use it only on repositories whose PR data may be processed by the workflow, and prefer a disposable workspace or account for sensitive repositories.

Risk: The skill can use HeyGen or local audio tooling and may send narration, music lookup, or related audio workflow data through external providers.

Mitigation: Confirm the selected audio provider and offline fallback before running, and avoid sensitive repository content when those external flows are not acceptable.

Risk: The workflow asks agents to run unpinned HyperFrames commands that can install registry blocks and update global HyperFrames skills.

Mitigation: Review the HyperFrames version, requested block names, and update commands before installation or execution.

## Reference(s):

- [ClawHub pr-to-video skill page](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Code vocabulary](references/code-vocabulary.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Code, Configuration, Files]

**Output Format:** [Markdown workflow instructions with shell commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces HyperFrames project artifacts including brief, PR capture data, storyboard, script, audio metadata, HTML frame compositions, captions, preview index, snapshots, and rendered MP4.]

## Skill Version(s):

1.0.37 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
