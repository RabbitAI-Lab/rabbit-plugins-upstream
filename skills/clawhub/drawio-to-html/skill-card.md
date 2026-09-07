## Description:

Convert drawio/diagrams.net XML files into standalone HTML pages with embedded SVG rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nellyxiaolong-cmyk](https://clawhub.ai/user/nellyxiaolong-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when they need an agent to convert a drawio/diagrams.net file into a browser-viewable standalone HTML page and report the generated file details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted .drawio content can be copied into generated HTML or SVG without escaping, which could allow browser-side script execution when the output is opened.

Mitigation: Use the converter only with trusted .drawio files, or escape HTML/SVG text and validate attributes before opening generated output from untrusted sources.

Risk: The converter supports only a subset of diagrams.net features and may omit swimlanes, images, custom shapes, complex gradients, or additional diagrams after the first one.

Mitigation: Review the generated HTML visually against the source diagram before sharing or relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nellyxiaolong-cmyk/skills/drawio-to-html)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance, Files]

**Output Format:** [Markdown guidance with shell command examples and a generated standalone HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated HTML embeds SVG and has no external runtime dependencies.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
