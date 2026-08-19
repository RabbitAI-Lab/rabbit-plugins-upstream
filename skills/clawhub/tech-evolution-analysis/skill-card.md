## Description:

A seven-step technology evolution analysis workflow that uses TRIZ evolution paths, SVOP functional abstraction, and PatSnap patent and paper retrieval to identify product evolution directions, opportunity gaps, cross-domain analogies, 3/5/10 year forecasts, gray-rhino signals, and black-swan signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product strategy teams, and technology analysts use this skill to decompose a product, retrieve and score patent and paper evidence, map findings onto TRIZ evolution paths, and produce future-form predictions with gray-rhino and black-swan monitoring signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML reports may include active content from loosely controlled analysis inputs.

Mitigation: Use trusted inputs, sanitize or escape JSON and report content, and review generated HTML before opening it in a browser or sharing it.

Risk: The skill writes persistent local analysis folders and report artifacts.

Mitigation: Run it in a workspace where local file creation is expected and review generated files before reuse.

Risk: Live data conclusions depend on the required PatSnap MCP service being configured and authorized.

Mitigation: Confirm MCP account authorization and tool availability before relying on database-backed analysis; label outputs as framework-only when the service is unavailable.

## Reference(s):

- [Tech Evolution Analysis on ClawHub](https://clawhub.ai/yuanzhian-patsnap/skills/tech-evolution-analysis)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [Step 1-2 Components and SVOP](references/step1-2-components-svop.md)
- [Step 3 Double-Track Search](references/step3-double-track-search.md)
- [Step 4 Multi-Dimensional Scoring](references/step4-multi-dim-scoring.md)
- [Step 5 TRIZ Labeling](references/step5-triz-labeling.md)
- [Step 6 Evolution Tree](references/step6-evolution-tree.md)
- [Step 7 Prediction Report](references/step7-prediction-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON, HTML visualization, and HTML report artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces step-by-step analysis files, rendered mind maps, TRIZ evolution-forest HTML, prediction JSON, and a final HTML report when configured with the required PatSnap MCP service.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
