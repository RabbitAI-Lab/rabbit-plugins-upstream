## Description:

Architect Diagram Pro is a local-first agent skill for generating architecture and structural diagrams as self-contained HTML, inline SVG, or Mermaid code with built-in layout, readability, and retry guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chesaram](https://clawhub.ai/user/chesaram)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, architects, and technical writers use this skill to turn system descriptions or user-specified project files into readable architecture, flow, sequence, topology, ER, state, Gantt, or related structural diagrams. It is intended for local diagram drafting and documentation workflows where generated diagrams are reviewed before sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad diagram-related phrases.

Mitigation: Install it only when a broad local diagramming assistant is desired, and rely on its clarification workflow when the requested diagram type or output format is ambiguous.

Risk: Generated diagrams may summarize user-specified local architecture files or project details.

Mitigation: Review diagrams before sharing them and avoid including sensitive architecture details in public outputs.

Risk: Unsupported requests such as statistical charts, 3D or map views, direct PNG/PDF export, and reverse engineering may be out of scope.

Mitigation: Use the documented capability matrix and require user confirmation before substituting a supported diagram format.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chesaram/skills/architect-diagram-pro)
- [README](README.md)
- [Architecture Layout](references/architecture-layout.md)
- [Arrow Text Clearance](references/arrow-text-clearance.md)
- [Capability Matrix](references/capability-matrix.md)
- [Clarification Gate](references/clarification-gate.md)
- [Diagram Types](references/diagram-types.md)
- [HTML Template Guide](references/html-template-guide.md)
- [Self Check and Errors](references/self-check-and-errors.md)
- [SVG Efficient Template](references/svg-efficient-template.md)
- [Three Invariants](references/three-invariants.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Guidance]

**Output Format:** [Markdown containing self-contained HTML, inline SVG, Mermaid code blocks, or file-generation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated diagrams are local-first and should be reviewed before sharing, especially when based on project architecture files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
