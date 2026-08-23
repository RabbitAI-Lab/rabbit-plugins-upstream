## Description:

Adds word-timed captions to an Open Recut program by mapping the canonical transcript through timeline.json, reviewing maintained styles on source-backed pixels, rendering a local transparent HyperFrames PNG sequence, and registering it as an overlay contribution for shared delivery render.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-production agents use this skill to add reviewed, word-timed caption overlays to Open Recut projects after a validated transcript and timeline are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media tooling and npx/HyperFrames execution can run project-specific tooling and downloads.

Mitigation: Install only in projects where local media tooling is acceptable and review required dependencies before processing media.

Risk: Generated preview, review, cache, and overlay files can affect unrelated folders if output paths are pointed outside the intended project.

Mitigation: Keep output and review directories inside the intended Open Recut project and avoid Force-style overwrites on important folders.

Risk: Caption style and preview approval depends on generated HTML evidence and structured approval prompts.

Mitigation: Review the source-backed HTML pages and copied approval summaries before rendering final overlay contributions.

## Reference(s):

- [Caption Rules and Data Shape](reference/caption-rules.md)
- [Caption Style Themes](reference/caption-style-themes.md)
- [Caption Feedback Mapping](reference/caption-feedback-mapping.md)
- [ClawHub skill page](https://clawhub.ai/whitetowerai/skills/video-add-captions)

## Skill Output:

**Output Type(s):** [Files, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON, SRT, HTML review pages, PNG overlay frames, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local project artifacts including caption plans, review evidence, style receipts, and transparent overlay frame sequences.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
