## Description:

Turns a GitHub pull request into a code-change explainer video built from the diff, commits, and changed files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn an existing GitHub pull request into a narrated HyperFrames code-change explainer, including PR ingestion, storyboard and script planning, frame generation, captions, transitions, and final MP4 rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run GitHub CLI/API reads against the target pull request, which can expose private repository metadata to the local workflow and any configured credentials.

Mitigation: Run it only in an environment where the target PR and GitHub credential scope are appropriate, and avoid sensitive private PRs unless that exposure is acceptable.

Risk: The workflow relies on npx HyperFrames execution, registry block installation, and possible global skill/tool updates.

Mitigation: Use a sandboxed environment, review requested updates and registry blocks before approval, and keep the generated project separate from the caller repository.

## Reference(s):

- [Skill workflow](artifact/SKILL.md)
- [Code vocabulary](artifact/references/code-vocabulary.md)
- [Story design](artifact/references/story-design.md)
- [Visual design](artifact/references/visual-design.md)
- [Motion language](artifact/references/motion-language.md)
- [Cut catalog](artifact/references/cut-catalog.md)
- [Frame worker role](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated HyperFrames project files, ending in an MP4 render.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project artifacts such as BRIEF.md, STORYBOARD.md, SCRIPT.md, frame HTML, captions, an assembled index, and renders/video.mp4.]

## Skill Version(s):

1.0.38 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
