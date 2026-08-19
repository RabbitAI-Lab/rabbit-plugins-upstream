## Description:

Turns a GitHub pull request into a code-change explainer video, using the PR diff, commits, and files to plan and build a changelog, feature reveal, fix explanation, or refactor walkthrough.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn GitHub pull requests into narrative HyperFrames explainer videos for changelogs, feature walkthroughs, fix explanations, and refactor summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may update HyperFrames skills globally before use without an explicit prompt.

Mitigation: Review or disable the silent update behavior before deployment, and prefer pinned or reviewed skill versions in controlled environments.

Risk: The skill uses GitHub CLI access to read PR metadata, diffs, files, and related contributor information.

Mitigation: Run with least-privileged GitHub credentials and process only repositories and pull requests approved for this workflow.

Risk: Narration, music, and sound effects may use configured audio providers such as HeyGen.

Mitigation: Confirm provider terms and data-handling expectations before use, or choose available offline/local audio paths when appropriate.

Risk: Generated video pages load third-party runtime code at render time.

Mitigation: Vendor or clearly disclose the runtime dependency and review generated HTML before publishing rendered outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Code vocabulary](references/code-vocabulary.md)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown plans and scripts, JSON metadata, HTML frame compositions, and MP4 render outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a HyperFrames project with PR capture artifacts, storyboard/script files, frame HTML, captions, audio metadata, contact sheets, and a final video render.]

## Skill Version(s):

1.0.25 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
