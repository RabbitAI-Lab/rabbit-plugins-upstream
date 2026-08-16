## Description:

Generate Mindmap helps an agent turn Markdown outlines or JSON into interactive mind maps and exportable diagram files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to structure content into a mind map, generate command-line steps, and produce shareable or editable diagram outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to write exported mind-map files to user-selected paths.

Mitigation: Review output paths before running generated commands and confirm the requested export location.

Risk: The skill may attempt optional Pillow installation for image export when the dependency is missing.

Mitigation: Use --no-auto-install in shared, locked-down, or policy-managed environments and install dependencies through approved channels.

Risk: Broad trigger wording may cause the skill to activate for requests that are not explicit mind-map tasks.

Mitigation: Use the skill only for explicit mind-map generation requests and confirm the intended output formats before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/generate-mindmap)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and generated file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to create HTML, PNG, JPG, SVG, PDF, or XMind mind-map outputs; optional image exports may require Pillow or Playwright.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
