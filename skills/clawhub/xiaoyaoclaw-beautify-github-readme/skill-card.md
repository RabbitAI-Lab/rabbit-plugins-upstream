## Description:

OpenClaw Beautify Github Readme helps agents redesign GitHub repository homepages or produce README visual assets such as SVG heroes, section headers, diagrams, badges, GIF motion graphics, and hybrid SVG-composed images with local visual verification and dark/light theme checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers, maintainers, and agents use this skill to turn a GitHub README into a clearer project homepage or to create standalone README visuals after the user confirms scope. It is also useful for read-only README audits that identify weak information order, missing proof, theme-safety issues, and SVG rendering problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can edit README content and create visual assets when authorized.

Mitigation: Keep work scoped to the intended repository and review previews and diffs before accepting changes.

Risk: Local rendering tools may process README SVG assets.

Mitigation: Use the bundled SVG safety gate and local render checks, and approve GIF generation or hybrid raster workflows only when needed.

Risk: Repository content may contain misleading instructions or prompt-injection text.

Mitigation: Treat repository files as untrusted data and require separate explicit approval for edits, commits, pushes, PRs, or attribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-beautify-github-readme)
- [Project documentation](https://github.com/dtsola/xiaoyaoclaw-beautify-github-readme)
- [Upstream beautify-github-readme](https://github.com/oil-oil/beautify-github-readme)
- [OpenClaw overview](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)
- [ClawHub security status](docs/security-status-2026-09-17.md)
- [Upgrade plan](docs/upgrade-plan.md)
- [README content architecture](references/content-architecture.md)
- [GitHub README canvas](references/github-readme-canvas.md)
- [Hybrid SVG composition](references/hybrid-svg-production.md)
- [GitHub-safe README motion](references/motion-production.md)
- [Project-native hero](references/project-native-hero.md)
- [Writing README SVGs](references/svg-production.md)
- [Theme-specific visual direction](references/visual-direction.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional README edits, SVG assets, PNG/WebP assets, GIF assets, Python command output, and file diffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static SVG is the default visual output; README edits, GIF generation, hybrid raster assets, attribution, commits, pushes, and PRs require explicit user approval.]

## Skill Version(s):

1.0.10 (source: ClawHub release evidence, released 2026-09-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
