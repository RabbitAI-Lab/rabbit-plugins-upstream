## Description:

Helps agents create self-contained HTML artwork with SVG, Canvas, and CSS, either by recreating a reference artwork or by painting from a text description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erich1566](https://clawhub.ai/user/erich1566)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to plan, generate, and refine code-based artwork as offline-openable HTML files. It is especially suited for recreating paintings, producing styled illustrations, and comparing code art against a reference image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated artwork may contain inaccurate visual recreations or code that does not match the user's intended reference.

Mitigation: Review the produced HTML visually, compare against the requested reference when available, and iterate before relying on the result.

Risk: The local analyzer may process user-provided reference images.

Mitigation: Run the analyzer only on intended local images and avoid providing sensitive images unless local processing is acceptable.

Risk: Generated HTML files may include script logic for Canvas rendering or comparison tooling.

Mitigation: Inspect generated HTML before sharing or deployment, and keep it self-contained without unexpected network calls.

## Reference(s):

- [HTML Code Painting ClawHub Skill Page](https://clawhub.ai/erich1566/skills/html-code-painting)
- [analysis-workflow.md](references/analysis-workflow.md)
- [canvas-techniques.md](references/canvas-techniques.md)
- [style-playbooks.md](references/style-playbooks.md)
- [svg-techniques.md](references/svg-techniques.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with inline code and self-contained HTML file content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local image-analysis commands for user-provided reference images; generated artwork is intended to be a single offline-openable HTML file.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
