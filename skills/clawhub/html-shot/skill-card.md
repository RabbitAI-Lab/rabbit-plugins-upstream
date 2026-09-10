## Description:

Renders HTML, URLs, or SVG files into static image assets such as social cards, screenshots, favicons, and app icon sets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design-focused agents use this skill to turn HTML/CSS, URLs, or SVG sources into local image files for social previews, screenshots, badges, favicons, and platform icon sets. It is useful when browser-grade CSS rendering, CJK text, emoji, transparency, and asset-path handling matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted HTML can execute JavaScript in local Chromium, make outbound requests, and access assets exposed under the input or base directories.

Mitigation: Render only trusted sources, use a narrow working directory and base path, and inspect logs for refused or missing assets before using generated images.

Risk: Setup may involve npm, npx, Playwright browser installation, and optional sudo commands for Linux dependencies.

Mitigation: Review install commands and dependency changes before execution, and run them in a controlled environment appropriate for local browser rendering.

Risk: Rendered output can vary when host fonts, browser channel, platform libraries, or missing CJK and emoji fonts differ across machines.

Mitigation: Pin the intended runtime where repeatability matters, install the documented fonts and Chromium dependencies, and visually verify generated images before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rockbenben/skills/html-shot)
- [Project homepage](https://github.com/rockbenben/aishort-skills/tree/main/skills/html-shot)
- [README](README.md)
- [Skill instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [shell commands, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands; rendered assets are PNG, JPEG, WebP, ICO, ICNS, SVG, and app icon files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local Node.js, Playwright/Chromium, and sharp; outputs are written to caller-selected local paths.]

## Skill Version(s):

1.1.5 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
