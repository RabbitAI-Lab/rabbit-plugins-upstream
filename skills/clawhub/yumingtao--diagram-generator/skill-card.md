## Description:

Generate polished, standalone HTML/SVG technical diagrams from natural-language briefs, structured component lists, or existing diagram models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yumingtao](https://clawhub.ai/user/yumingtao)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to turn system descriptions or existing diagram models into architecture, infrastructure, data-flow, deployment, trust-boundary, and process diagrams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial: one script was partly interpreted and five PNG files were outside the analyzer's supported scope.

Mitigation: Review the uncovered script and image assets or use a scan that covers them before installation.

Risk: A diagram can present assumed or inferred system details as fact.

Mitigation: Confirm assumptions with the user and review the rendered diagram and checker warnings before sharing it.

## Reference(s):

- [Generation rules](resources/generation-rules.md)
- [Diagram IR model](resources/diagram-ir.md)
- [HTML/SVG template](resources/template.html)
- [Diagram checker](scripts/check-diagram.mjs)
- [ClawHub skill page](https://clawhub.ai/yumingtao/skills/diagram-generator)

## Skill Output:

**Output Type(s):** [Files, HTML, SVG]

**Output Format:** [Standalone HTML with inline SVG]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Self-contained; supports SVG download, PNG export, and print/PDF.]

## Skill Version(s):

1.4.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
