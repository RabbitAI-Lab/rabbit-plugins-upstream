## Description:

Generates images by authoring SVG and exports SVG artwork to PNG, GIF, APNG, WebP, MP4, or embeddable HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-producing agents use this skill to create precise SVG-based illustrations, charts, posters, diagrams, icons, and animations, then export them as editable SVG, raster PNG, animated files, or HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal rendering can create a local virtual environment and download unpinned Python packages.

Mitigation: Use the skill only where local package installation is acceptable, or pre-review and preinstall dependencies in a controlled environment.

Risk: Rendering hostile or unknown SVG files can expose local renderers or a headless browser to untrusted input.

Mitigation: Prefer SVGs generated or trusted by the operator; use a sandboxed or disposable environment for untrusted files.

Risk: MP4 export depends on ffmpeg being available on PATH.

Mitigation: Install ffmpeg before MP4 export or choose GIF, APNG, or WebP output when ffmpeg is unavailable.

## Reference(s):

- [SVG Studio Skill Page](https://clawhub.ai/dqsjqian/skills/svg-studio)
- [SVG Techniques Reference](artifact/references/svg-techniques.md)
- [Hand-Drawn Infographic Style Guide](artifact/references/handdrawn-infographic.md)
- [SVG Animation Reference](artifact/references/animation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with SVG code, Python command snippets, and generated SVG, PNG, HTML, GIF, APNG, WebP, or MP4 files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output format and dimensions depend on the requested artwork, viewBox, render scale, and available local render tools.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
