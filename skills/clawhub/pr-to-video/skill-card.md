## Description:

Turns a GitHub pull request into a code-change explainer video, using the PR diff, commits, files, and contributors to build a narrated HyperFrames walkthrough.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn a GitHub pull request into a concise video explanation for changelogs, feature reveals, bug-fix walkthroughs, or refactor summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs the agent to silently update installed skills and shared tooling before use.

Mitigation: Require explicit approval for updates, show the versions being used, and pin or separately manage tooling before running the workflow on sensitive repositories.

Risk: The workflow reads GitHub PR details through the user's GitHub authentication and may use HyperFrames media credentials for audio when enabled.

Mitigation: Run it only on repositories and media accounts the user is authorized to access, and review generated project files before rendering or sharing the video.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [SKILL.md](artifact/SKILL.md)
- [Story design](artifact/references/story-design.md)
- [Visual design](artifact/references/visual-design.md)
- [Code vocabulary](artifact/references/code-vocabulary.md)
- [Motion language](artifact/references/motion-language.md)
- [Cut catalog](artifact/references/cut-catalog.md)
- [Frame worker](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with shell commands, generated project files, HTML frame compositions, captions, audio metadata, and an MP4 render]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitHub PR data, optional contributor avatars, optional narration and background music, and HyperFrames validation before final rendering.]

## Skill Version(s):

1.0.24 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
