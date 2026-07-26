## Description: <br>
Audit existing Google Analytics implementation. Checks for common issues, missing configurations, and optimization opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeftekhari](https://clawhub.ai/user/jeftekhari) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and site maintainers use this skill to inspect existing analytics implementations, identify Google Analytics and related tracking issues, and produce prioritized recommendations for improving tracking accuracy, privacy posture, and maintainability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository code inspection may expose analytics snippets or measurement identifiers to the agent context. <br>
Mitigation: Use this skill only in projects where analytics code inspection is acceptable, and preserve the report's measurement ID redaction behavior. <br>
Risk: Audit findings can be incomplete if analytics behavior depends on runtime configuration or deployed tag manager state outside the repository. <br>
Mitigation: Review the generated recommendations against the deployed analytics configuration before making production changes. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance] <br>
**Output Format:** [Markdown audit report with severity-ranked findings, an event coverage table, and ordered next steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Redacts the last six characters of discovered measurement IDs.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
