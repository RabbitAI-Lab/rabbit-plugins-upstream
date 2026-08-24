## Description:

Turns a GitHub pull request into a code-change explainer video using the PR diff, commits, files, and contributor context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn GitHub pull requests into source-grounded explainer videos for changelogs, feature reveals, bug fixes, and refactor walkthroughs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can read pull request content available to the user's GitHub CLI login, including private repository PRs.

Mitigation: Run it only for PRs the user is authorized to process and review the generated storyboard, script, and video before sharing outside the repository's intended audience.

Risk: The workflow may update HyperFrames-related skills before use.

Mitigation: Confirm the update step with the user and apply normal change-control review when the runtime environment requires pinned or preapproved tooling.

Risk: The workflow can use configured media credentials for narration, music, or related media assets.

Mitigation: Check the reported auth/provider status before generation and use the documented offline path when external media services should not be used.

Risk: Generated explanations may misstate the intent or impact of a code change if the PR evidence is interpreted incorrectly.

Mitigation: Use the built-in review gates for the plan, storyboard, contact sheet, and final render before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story Design](artifact/references/story-design.md)
- [Visual Design](artifact/references/visual-design.md)
- [Code Vocabulary](artifact/references/code-vocabulary.md)
- [Motion Language](artifact/references/motion-language.md)
- [Cut Catalog](artifact/references/cut-catalog.md)
- [Frame Worker Delta](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown workflow guidance with generated HyperFrames project files, HTML frame compositions, captions, audio metadata, and an MP4 render output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses PR-derived evidence, storyboard and script artifacts, frame HTML, contributor avatars when available, and optional voice or music assets.]

## Skill Version(s):

1.0.29 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
