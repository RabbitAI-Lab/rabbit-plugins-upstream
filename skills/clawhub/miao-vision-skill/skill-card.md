## Description:

Miao Vision helps agents create self-contained local visual artifacts from user-provided articles, text, and data, including reports, posters, infographics, browser decks, and optional data-story images or videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to turn local files, article text, and structured data into evidence-backed visual deliverables such as HTML/PDF reports, posters, infographics, browser decks, and optional explanatory media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update a shared local CLI on first use.

Mitigation: Prefer the packaged or marketplace install path and treat the first-use CLI download approval as local code installation.

Risk: Optional image or video generation can send prompt and approved reference content to a remote media provider and may incur separate charges.

Mitigation: Approve remote media only after reviewing the displayed prompt, reference upload scope, model tier, and pricing summary.

Risk: Uninstalling the plugin does not remove the shared CLI copy.

Mitigation: Delete ~/.miao-vision when the shared CLI should be removed from the machine.

## Reference(s):

- [Article Infographic Workflow](artifact/references/article.md)
- [Data Report Workflow](artifact/references/report.md)
- [Browser Deck Workflow](artifact/references/deck.md)
- [Outcome Brief Plan-First Workflow](artifact/references/outcome-brief.md)
- [Data Story Image Workflow](artifact/references/media-image.md)
- [Data Story Video Workflow](artifact/references/media-video.md)
- [Optional AI Media Setup](artifact/references/media-setup.md)
- [Local Review Viewer](artifact/references/review-viewer.md)
- [Miao Vision Plugin Installation](artifact/install/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown responses with inline shell commands, JSON/YAML specs, and links to local HTML, PDF, PNG, MP4, or preview artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ordinary artifacts keep source data local; optional image or video generation can send approved prompts and references to a remote media provider.]

## Skill Version(s):

0.9.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
