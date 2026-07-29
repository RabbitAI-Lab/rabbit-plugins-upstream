## Description: <br>
Use when a design has to become image assets through a real browser: an og:image or social preview card, an HTML/CSS or SVG design exported as PNG/JPEG/WebP, a screenshot of a page or one element, or a favicon and app-icon set. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rockbenben](https://clawhub.ai/user/rockbenben) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to render HTML, SVG, local files, or URLs into browser-accurate image assets such as social cards, screenshots, favicons, and app icons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: HTML, SVG, or URL inputs can execute JavaScript in local Chromium, and remote pages can make network requests during capture. <br>
Mitigation: Use the skill only with trusted inputs and avoid capturing untrusted remote pages or files. <br>
Risk: Browser-based rendering requires local Node.js dependencies and a Chromium-capable Playwright setup. <br>
Mitigation: Confirm Node.js and Playwright/Chromium installation before relying on the skill in a release or CI workflow. <br>
Risk: Rendered assets can appear successful while still containing visual issues such as clipped text, missing glyphs, or unexpected transparency. <br>
Mitigation: Inspect generated images and, for transparent outputs, verify alpha behavior with an image tool before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rockbenben/skills/html-shot) <br>
- [Publisher profile](https://clawhub.ai/user/rockbenben) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell commands that generate PNG, JPEG, WebP, ICO, ICNS, SVG, and app-icon files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a local Chromium-capable Playwright workflow; generated image files depend on the supplied HTML, SVG, URL, and command options.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter, package.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
