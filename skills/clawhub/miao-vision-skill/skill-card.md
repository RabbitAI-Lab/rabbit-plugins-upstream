## Description:

Creates local-first data posters, reports, browser decks, and article infographics, with optional data-story media and version review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

People working with local text or data use this skill to create shareable visual reports, posters, decks, and infographics, or to inspect and revise their versions. Optional image and video generation can illustrate a verified conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional local CLI remains installed after plugin removal.

Mitigation: Approve installation separately and account for the persistent local CLI when uninstalling.

Risk: Optional image and video generation sends approved prompts or reference images to remote providers and may incur fees.

Mitigation: Use only non-sensitive prompts and approved references; confirm upload scope and charges before generation.

## Reference(s):

- [Miao Vision on ClawHub](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)
- [Report workflow](artifact/references/report.md)
- [Browser deck workflow](artifact/references/deck.md)
- [Review Viewer workflow](artifact/references/review-viewer.md)
- [Optional AI media setup](artifact/references/media-setup.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [HTML, PDF, PNG, optional image/video files, and concise Markdown delivery notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first source-data workflows; optional Review Viewer for inspecting and comparing versions.]

## Skill Version(s):

0.10.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
