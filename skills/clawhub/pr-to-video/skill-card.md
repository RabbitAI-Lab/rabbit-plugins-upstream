## Description:

PR to Video turns a GitHub pull request into a code-change explainer video by building a changelog, feature reveal, fix explainer, or refactor walkthrough from the PR diff, commits, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to convert a GitHub pull request into a source-traceable explainer video with a storyboard, script, rendered frames, captions, audio metadata, and final MP4 output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may update installed HyperFrames skills and dependencies automatically before use.

Mitigation: Require explicit approval or use a pinned/manual update process before running the skill, especially in workspaces with GitHub or media-provider credentials.

Risk: Running the workflow in a credentialed workspace can expose the task to actions that depend on GitHub and media-provider access.

Mitigation: Review the skill before install and run it only in a workspace where the available credentials and provider access are appropriate for the PR being processed.

## Reference(s):

- [Story Design](artifact/references/story-design.md)
- [Visual Design](artifact/references/visual-design.md)
- [Code Vocabulary](artifact/references/code-vocabulary.md)
- [Motion Language](artifact/references/motion-language.md)
- [Cut Catalog](artifact/references/cut-catalog.md)
- [Frame Worker](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and generated project files, including storyboard and script markdown, HTML frame compositions, captions metadata, audio metadata, an assembled index, and an MP4 render.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses gated workflow checkpoints and bounded frame-worker packets; final video output depends on GitHub PR access, HyperFrames tooling, and available audio/media providers.]

## Skill Version(s):

1.0.26 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
