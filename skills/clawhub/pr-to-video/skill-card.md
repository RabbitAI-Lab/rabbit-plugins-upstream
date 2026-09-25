## Description:

Turns a GitHub pull request into a code-change explainer video, using the PR diff, commits, and files to build changelog, feature reveal, fix, or refactor walkthroughs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn pull requests into explainer videos that summarize the change, highlight important diff hunks, narrate behavior, and render a final MP4 for review or release communication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow runs live HyperFrames commands from npx and can update or install external workflow components.

Mitigation: Run it in a constrained workspace, confirm update and install prompts, and review the selected registry blocks before continuing.

Risk: The workflow uses the local gh session to read pull request data, which may include private repository metadata and diffs.

Mitigation: Use it only on repositories and pull requests the operator is authorized to expose to the workflow, and review generated PR artifacts before sharing outputs.

Risk: Audio and media steps may use configured media-provider credentials for narration, music, sound effects, or catalog assets.

Mitigation: Check HyperFrames authentication status, prefer offline mode when appropriate, and avoid adding provider credentials to per-repository files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design](artifact/references/story-design.md)
- [Visual design](artifact/references/visual-design.md)
- [Code vocabulary](artifact/references/code-vocabulary.md)
- [Motion language](artifact/references/motion-language.md)
- [Cut catalog](artifact/references/cut-catalog.md)
- [Frame worker](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown instructions, shell commands, project configuration, HTML frame compositions, storyboard and script files, and a rendered MP4 file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a HyperFrames project containing BRIEF.md, STORYBOARD.md, SCRIPT.md when narration is used, frame HTML, index.html, audio metadata when available, captions when built, and renders/video.mp4.]

## Skill Version(s):

1.0.42 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
