## Description:

Helps developers redesign or audit GitHub READMEs and create project-specific visual assets, with local previews and visual checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers and repository maintainers use this skill to improve a GitHub README's visual story, audit its presentation, or create standalone SVG and animated or raster assets without changing the README unless authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: README or asset changes could affect repository content beyond the requested scope.

Mitigation: Confirm the working mode and specific edits first; review previews and diffs before approving commits, pushes, pull requests or publication.

Risk: Local visual checks process repository-provided files using browser or rendering tools.

Mitigation: Use only repositories the user is comfortable granting access to; keep rendering local and review generated previews before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-beautify-github-readme)
- [README canvas guidance](artifact/references/github-readme-canvas.md)
- [SVG production guidance](artifact/references/svg-production.md)
- [Content architecture guidance](artifact/references/content-architecture.md)

## Skill Output:

**Output Type(s):** [Markdown, Visual asset files, Guidance]

**Output Format:** [README Markdown, SVG and optional PNG, WebP or GIF assets, with preview and audit feedback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [README edits and publication require separate user approval; asset-only work leaves the README unchanged.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
