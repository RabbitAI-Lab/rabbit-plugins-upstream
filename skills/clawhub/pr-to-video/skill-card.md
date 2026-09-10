## Description:

Turn a GitHub pull request into a code-change explainer video using the diff, commits, files, and contributor metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn a GitHub pull request into a narrative code-change explainer, including setup, PR ingestion, storyboard and script planning, frame generation, captions, audio, and final video rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses authenticated GitHub CLI access and processes pull request content that may be private, regulated, or untrusted.

Mitigation: Run it only on PRs the operator is authorized to process, and review the generated storyboard and PR-derived content before producing or sharing the video.

Risk: The skill contacts GitHub, HeyGen, and HyperFrames services and may download contributor avatars or use remote registry components.

Mitigation: Confirm that external service use is acceptable for the project and review mutable remote components before execution.

Risk: The security evidence reports a suspicious verdict because the skill relies on mutable remote tools and has insufficiently explicit boundaries around untrusted PR content.

Mitigation: Perform local review and scanning before deployment, and avoid using the skill for sensitive PRs unless the generated materials and remote dependencies are reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [code-vocabulary.md](references/code-vocabulary.md)
- [cut-catalog.md](references/cut-catalog.md)
- [motion-language.md](references/motion-language.md)
- [story-design.md](references/story-design.md)
- [visual-design.md](references/visual-design.md)
- [frame-worker.md](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated project files; an executed workflow can produce HTML frames and an MP4 video.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitHub pull request content as input and writes generated HyperFrames project artifacts outside the caller repository by default.]

## Skill Version(s):

1.0.32 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
