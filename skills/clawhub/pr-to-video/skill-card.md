## Description: <br>
Turn a GitHub pull request into a code-change explainer video for a changelog, feature reveal, fix, or refactor walkthrough built from the diff, commits, and files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to convert GitHub pull requests into concise explanatory videos that summarize code changes, show selected diff evidence, generate narration and captions, and render a final MP4. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to run a silent HyperFrames skill updater through npx, which can change globally installed skills before user approval. <br>
Mitigation: Review or remove the silent updater step before installation, ask for approval before any global skill or CLI update, and pin or review the update source. <br>
Risk: The workflow uses the local GitHub CLI session to read PR contents, including private PRs the user can access. <br>
Mitigation: Run it only against intended repositories, confirm the active gh account and scopes before use, and avoid using it in workspaces where private PR data should not be processed. <br>
Risk: Audio and media steps can use HeyGen or media credentials when narration, music, or sound effects are enabled. <br>
Mitigation: Confirm the active media provider and credentials before enabling audio, and choose offline or silent modes when credential use is not appropriate. <br>


## Reference(s): <br>
- [Story design](references/story-design.md) <br>
- [Visual design](references/visual-design.md) <br>
- [Motion language](references/motion-language.md) <br>
- [Code vocabulary](references/code-vocabulary.md) <br>
- [Cut catalog](references/cut-catalog.md) <br>
- [Frame worker](sub-agents/frame-worker.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown plans and scripts, JSON sidecars, HTML frame files, shell commands, and an MP4 video file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a HyperFrames project from a GitHub PR, including storyboard, script, audio metadata, captions, frame compositions, index.html, contact sheet, and renders/video.mp4.] <br>

## Skill Version(s): <br>
1.0.23 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
