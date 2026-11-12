## Description:

Use html-shot when a design or page must become image assets through a real browser — an OG/social card in PNG/JPEG/WebP, a one-element or full-page screenshot, an SVG raster, a transparent badge, or a favicon/app-icon set (.ico, .icns, apple-touch, PWA) for a site, Next, Electron or Tauri. Triggers on HTML 转图片, SVG 转 PNG, favicon, 应用图标. Not for editing existing raster images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use HTML Shot to turn existing HTML, SVG, or requested web pages into raster image assets and generate favicon or app icon files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports incomplete file coverage, and the README includes an install example that does not pin a CLI version.

Mitigation: Review the release before installation and pin a reviewed CLI version for reproducible installs.

Risk: Rendering executes page JavaScript, which can request remote resources referenced by the input.

Mitigation: Render only trusted HTML, SVG, or requested URLs; use --offline for local designs when suitable, while recognizing it is not a sandbox.

## Reference(s):

- [CLI and capture modes](references/cli.md)
- [Icon presets and size requirements](references/icons.md)
- [Security and reproducibility](references/security.md)
- [Starter templates](references/templates.md)
- [Project page](https://github.com/rockbenben/aishort-skills/tree/main/skills/html-shot)
- [ClawHub skill page](https://clawhub.ai/rockbenben/skills/html-shot)

## Skill Output:

**Output Type(s):** [Files, Guidance, Shell commands]

**Output Format:** [PNG, JPEG, and WebP images; favicon and app-icon files; Markdown instructions and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image dimensions, format, capture mode, and icon set depend on the requested deliverable.]

## Skill Version(s):

1.2.4 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
