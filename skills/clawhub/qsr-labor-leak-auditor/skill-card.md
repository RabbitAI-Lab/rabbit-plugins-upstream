## Description: <br>
Real-time labor decision support for restaurant and franchise operators with summary-first mobile-optimized output, surfaced events, state control, goal tracking, recovery planning, forward planning, event-aware comparisons, hidden-by-default math, standardized output structure, and concise correction handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mcphersonai](https://clawhub.ai/user/mcphersonai) <br>

### License/Terms of Use: <br>
CC-BY-NC-4.0 <br>


## Use Case: <br>
Restaurant and franchise operators, general managers, assistant managers, district managers, and multi-unit leaders use this skill to track labor against sales, detect mid-week labor drift, review context-aware labor leaks, and choose corrective actions before payroll closes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store store-level sales, labor cost assumptions, weekly goals, and audit history in the companion store memory system. <br>
Mitigation: Confirm the deployment is allowed to retain this business data, keep records store-scoped, and use the memory engine's deletion controls when hard deletion is required. <br>
Risk: Operators could enter employee PII or named wage details while discussing labor issues. <br>
Mitigation: Prefer roles over names, avoid entering employee PII or named wage details unless operationally necessary, and omit identifying details from retained records when possible. <br>
Risk: Labor recommendations can influence staffing, payroll, and operational decisions. <br>
Mitigation: Treat recommendations as decision support for a responsible manager, review context before reducing labor, and use operator corrections or overrides when local conditions change the result. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mcphersonai/skills/qsr-labor-leak-auditor) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Mobile-oriented Markdown summaries with optional detailed worksheets and scoped export records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Executive-summary-first responses; detailed math is shown on request or when ambiguity, overrides, corrections, or unexpected results require it.] <br>

## Skill Version(s): <br>
3.1.2 (source: frontmatter, release evidence, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
