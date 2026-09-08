## Description:

This skill analyzes greenhouse plant images or videos with environmental sensor context to produce structured reports and prioritized climate-control actions such as irrigation, shading, ventilation, wet-curtain, and heating commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External greenhouse operators and developers use this skill to analyze plant morphology, environmental sensor context, and historical greenhouse reports so they can generate decision-support recommendations for irrigation, shading, ventilation, wet-curtain, and heating actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Greenhouse media, report-history requests, and automatic account association are sent to the vendor service.

Mitigation: Install only when that vendor-service data flow is acceptable, and review account-association behavior before deployment.

Risk: The security evidence says reusable tokens may be stored locally.

Mitigation: Use a proper secret store and restrict local credential access before treating the release as routine.

Risk: The security evidence says the release ships with risky plaintext development API settings.

Mitigation: Switch released endpoints to HTTPS production settings before operational use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Greenhouse API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with report links and prioritized action guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are decision-support recommendations and report summaries; the skill documentation says not to emit PID values or exact actuator-opening percentages.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
