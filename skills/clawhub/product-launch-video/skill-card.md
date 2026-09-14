## Description:

Turn a product or marketing URL, pasted script, or brief into a product launch or promo video for SaaS promos, feature reveals, product demos, app launches, company launches, site tours, and product showcases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing teams use this skill to turn a product URL, script, or brief into a launch video workflow with captured brand assets, storyboard and script planning, generated frame compositions, captions, audio metadata, and an MP4 render.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs HyperFrames shell commands and can update related skills or use mutable remote tooling.

Mitigation: Use a pinned, locally reviewed HyperFrames CLI and run the workflow in a project-limited sandbox before deployment.

Risk: The workflow may access product URLs and media-provider credentials while capturing assets and generating audio or media metadata.

Mitigation: Use trusted source URLs and scoped media-provider credentials, and avoid running the workflow on confidential assets without an approved sandbox.

Risk: Server security evidence reports a project-boundary file write flaw involving untrusted storyboard frame source paths.

Mitigation: Do not use untrusted STORYBOARD.md files until frame source paths are constrained to the project directory.

## Reference(s):

- [Product Launch Video ClawHub Listing](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story Design](artifact/references/story-design.md)
- [Visual Design](artifact/references/visual-design.md)
- [Motion Language](artifact/references/motion-language.md)
- [Cut Catalog](artifact/references/cut-catalog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus generated project files, HTML frame compositions, JSON metadata, and MP4 video output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a project-scoped video workspace with brief, storyboard, script, frame HTML, captions or audio metadata when enabled, assembled index, snapshots, and renders/video.mp4.]

## Skill Version(s):

1.0.37 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
