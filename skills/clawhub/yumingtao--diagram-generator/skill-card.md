## Description:

Generate professional standalone HTML/SVG technical diagrams for architecture, infrastructure, topology, deployment, data-flow, sequence, process, trust-boundary, cloud, and draw.io use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yumingtao](https://clawhub.ai/user/yumingtao)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use the skill to turn architecture briefs, system descriptions, deployment topologies, data flows, and process narratives into standalone technical diagrams, or to make targeted edits to existing diagrams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial: scripts/check-diagram.mjs was only partly inspected and five PNG files were not analyzed.

Mitigation: Consider the incomplete scan coverage when deciding whether to install; inspect the partially reviewed script and unscanned images if needed.

Risk: Draw.io XML output is experimental and may not import correctly.

Mitigation: Import-test generated XML in draw.io before relying on it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yumingtao/skills/diagram-generator)
- [Generation rules](resources/generation-rules.md)
- [Diagram planning model](resources/diagram-ir.md)
- [HTML/SVG template](resources/template.html)

## Skill Output:

**Output Type(s):** [Files, HTML, SVG]

**Output Format:** [Standalone HTML with inline SVG and embedded CSS]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports SVG and PNG export and print/PDF output. Draw.io XML is experimental and opt-in.]

## Skill Version(s):

1.4.0 (source: release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
