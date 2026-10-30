## Description:

Analyzes camera images or videos for pets in UV disinfection areas and returns a structured safety report with recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding facilities, and smart-home operators can submit camera footage for analysis of pet presence and possible UV exposure, then review the resulting report and recommendations. Treat lamp-state estimates and alerts as advisory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The analysis does not reliably protect pets or confirm that a UV lamp is off.

Mitigation: Keep physical safeguards and direct supervision in place; verify lamp status independently before treating an area as safe.

Risk: The export-only option still runs analysis, and configured API secrets may be transmitted as account identifiers.

Mitigation: Do not assume export-only avoids execution, and avoid supplying secrets until their handling is clarified.

Risk: Cloud footage retention and local token storage are unclear.

Mitigation: Review the service's footage retention and token storage practices before uploading footage or configuring credentials.

## Reference(s):

- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)
- [API reference](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk observations, recommendations, and report links.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
