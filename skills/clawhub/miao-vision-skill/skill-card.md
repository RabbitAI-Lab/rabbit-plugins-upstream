## Description:

Creates shareable, self-contained data posters, reports, browser decks, and article infographics from supplied local content and data, with optional evidence-grounded media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing presentations and analyses use this skill to turn supplied articles, text, and local datasets into grounded visual artifacts and exportable reports. It can also validate report or deck specifications and support review of generated versions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Export setup may load browser automation code from local locations, including an untrusted workspace.

Mitigation: Run export setup only in trusted workspaces and approve Playwright and browser setup only when exports are needed.

Risk: Some installation paths are not fully version-pinned.

Mitigation: Prefer a trusted, versioned bundle; avoid the unpinned npx compatibility path unless its source is trusted.

Risk: Optional media generation may upload prompts or reference material to a remote provider.

Mitigation: Confirm the exact upload scope before using media generation and exclude sensitive raw data.

## Reference(s):

- [Miao Vision skill listing](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)
- [Article infographic workflow](references/article.md)
- [Report and data poster workflow](references/report.md)
- [Browser deck workflow](references/deck.md)
- [Review Viewer workflow](references/review-viewer.md)
- [Optional media setup](references/media-setup.md)

## Skill Output:

**Output Type(s):** [Files, Markdown guidance]

**Output Format:** [Self-contained HTML artifacts, optional PDF/PNG exports or image/video, and Markdown delivery links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ordinary artifacts use local source data; optional media generation sends approved prompt and reference material to a remote provider.]

## Skill Version(s):

0.10.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
