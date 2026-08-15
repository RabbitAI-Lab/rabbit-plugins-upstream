## Description:

Generates HTML investment and招商 strategy reports for science and industrial parks, including industry inventory, benchmark analysis, chain-strengthening recommendations, and target-company lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External business-development, government affairs, and investment-promotion users can use this skill to generate a decision-oriented HTML report for a target park. The report combines public and PatSnap-style enterprise data signals to summarize industry structure, compare benchmark parks, and identify招商 targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated business data or recommendations may be incomplete or uncertain, especially where the skill marks items as medium or low confidence.

Mitigation: Review the generated report and verify key enterprise, policy, financing, and target-company claims before using it for investment or招商 decisions.

Risk: The skill may perform web searches and call PatSnap-style enterprise data tools when available.

Mitigation: Confirm that the agent environment is permitted to access the relevant web and enterprise data sources before running the skill.

Risk: The generated HTML report may load Chart.js from a CDN.

Mitigation: Use an approved local copy or approved network allowlist if external CDN loading is not permitted in the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/park-investment-report)
- [Publisher profile](https://clawhub.ai/user/yuanzhian-patsnap)

## Skill Output:

**Output Type(s):** [Analysis, Files, Code, Guidance]

**Output Format:** [HTML report file with charts, tables, and narrative analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a standalone report under @session/reports and may include Chart.js loaded from a CDN.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
