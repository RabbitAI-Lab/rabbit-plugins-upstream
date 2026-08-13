## Description:

TRIZ Innovation Pro guides engineering teams through TRIZ-based product problem analysis, from component modeling and causal-chain diagnosis to concept solution generation and solution detail drafting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and product innovation teams use this skill to structure TRIZ analysis for product improvement problems, identify root causes, select key problems, and draft concept solutions with implementation detail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product designs, patent context, and modification requests may contain confidential engineering or intellectual-property details that are processed by the named analysis tools.

Mitigation: Sanitize inputs and avoid including confidential details unless that processing is acceptable for the workspace.

Risk: Generated TRIZ problem rankings and solution proposals may be incomplete or unsuitable for direct engineering implementation.

Mitigation: Have qualified engineers review the analysis, assumptions, patent references, feasibility ratings, and implementation details before using the output in product decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/triz-innovation-pro)
- [System Component Analysis](references/01_system_component_analysis.md)
- [Contact Relationship Analysis](references/02_component_touch_analysis.md)
- [Functional Modeling](references/03_functional_modeling.md)
- [Problem Description and Core Problem Selection](references/04_functional_modeling_problem_summary.md)
- [Causal Chain Analysis](references/05_causal_chain_analysis.md)
- [Causal Chain Problem Filtering](references/06_causal_chain_problem_summary.md)
- [Solution Generation](references/07_solution.md)
- [Solution Detail Generation](references/08_solution_detail.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown summaries and tables with JSON-backed intermediate analysis and optional Mermaid flowchart output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports summary and detail display modes; solution detail output can reference patent-derived concept data when available.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter and manifest list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
