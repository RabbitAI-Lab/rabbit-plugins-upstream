## Description:

Generate polished standalone HTML/SVG technical diagrams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yumingtao](https://clawhub.ai/user/yumingtao)

### License/Terms of Use:

MIT

## Use Case:

Developers, architects, and engineers use the skill to turn system briefs, codebase notes, or deployment descriptions into technical maps, or to revise existing diagrams. It supports system, implementation, infrastructure, trust, data movement, deployment, and process views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence, but inspection was incomplete: the checker script was only partially inspected and five binary images were outside its analysis scope.

Mitigation: Review the checker script and excluded assets when making an installation decision, and inspect generated diagrams for accuracy before sharing them.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/yumingtao/skills/diagram-generator)
- [Diagram Generation Rules](resources/generation-rules.md)
- [Diagram IR](resources/diagram-ir.md)
- [HTML/SVG Template](resources/template.html)
- [Diagram Output Checker](scripts/check-diagram.mjs)

## Skill Output:

**Output Type(s):** [HTML files, SVG diagrams, Draw.io XML (experimental and opt-in)]

**Output Format:** [Standalone HTML with inline SVG; optional embedded Draw.io XML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [HTML output is self-contained and supports SVG and PNG export and print/PDF. Generated diagrams are intended to pass the included geometry and placeholder checker.]

## Skill Version(s):

1.4.2 (source: server-resolved release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
