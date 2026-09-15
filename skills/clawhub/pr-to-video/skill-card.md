## Description:

Turns a GitHub pull request into a code-change explainer video built from the PR diff, commits, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn a GitHub PR into a HyperFrames explainer video that highlights what changed, why it matters, and who contributed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable package execution and global skill updates can change behavior between runs.

Mitigation: Prefer a pinned HyperFrames version and review any global skill update before running.

Risk: The skill uses a GitHub CLI session to read PR data, which may include private or confidential code.

Mitigation: Run only on trusted PRs, use a sandbox for untrusted public PRs, and get explicit approval before processing confidential private PR content.

Risk: Narration or media requests may be sent to HeyGen or external media services.

Mitigation: Confirm provider use and approvals before sending private PR content to external media providers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Code vocabulary](references/code-vocabulary.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown workflow guidance with shell commands plus generated HyperFrames project files and MP4 video output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitHub PR data, optional contributor avatars, optional narration and music metadata, and HyperFrames frame compositions.]

## Skill Version(s):

1.0.35 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
