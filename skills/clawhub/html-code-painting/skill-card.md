## Description:

HTML Code Painting helps agents create self-contained browser artwork with HTML, SVG, Canvas, and CSS from reference images or text descriptions, including analysis and verification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erich1566](https://clawhub.ai/user/erich1566)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when they want an agent to plan, code, and validate offline-openable HTML artwork or faithful painting recreations without relying on AI image-generation APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML may contain active browser code, especially when prompts or source material are untrusted.

Mitigation: Review generated HTML before opening it and keep outputs self-contained without external resource loading.

Risk: The comparison workbench accepts embedded artwork HTML, which could be unsafe if copied from arbitrary third-party sources.

Mitigation: Use the workbench with locally generated or reviewed HTML and avoid inserting untrusted third-party HTML.

## Reference(s):

- [Analysis Workflow](references/analysis-workflow.md)
- [Canvas Techniques](references/canvas-techniques.md)
- [Python Preview](references/python-preview.md)
- [Style Playbooks](references/style-playbooks.md)
- [SVG Techniques](references/svg-techniques.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline code and self-contained HTML output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local HTML artwork files plus optional local analysis or preview artifacts.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
