## Description:

Record, render, optimize, and embed a demo GIF in a repo's README.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to add reproducible demo GIFs to repositories by choosing a suitable recording method, generating a script, rendering and optimizing the asset, and embedding it in README documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated recording, rendering, package-installation, Docker, sudo, npm, ffmpeg, or README-editing commands may affect the target repository or host environment.

Mitigation: Review generated commands and scripts before execution, and run them in an appropriate development environment.

Risk: Recorded demos can accidentally capture secrets, private data, or live production account state.

Mitigation: Use sanitized fixtures or local test accounts and inspect GIFs or videos before committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/demo-gif-skill)
- [Tape Cookbook](references/tape-cookbook.md)
- [Web App Capture: Playwright + ffmpeg](references/web-capture.md)
- [VHS](https://github.com/charmbracelet/vhs)
- [Playwright](https://playwright.dev/)
- [asciinema](https://asciinema.org/)
- [agg](https://github.com/asciinema/agg)
- [gifski](https://gif.ski/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and generated recording or README snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce .tape files, Playwright scripts, GIF/video conversion commands, optimized GIF assets, and README image embeds.]

## Skill Version(s):

1.0.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
