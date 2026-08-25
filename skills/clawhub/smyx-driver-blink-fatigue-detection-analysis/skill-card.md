## Description:

Analyzes in-cabin driver face video to detect eye state, blink rate, prolonged eye closure, microsleep indicators, and fatigue-driving alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, fleet operators, and vehicle safety teams can use this skill to analyze DMS camera video or URLs for visual fatigue indicators and retrieve structured fatigue-monitoring reports. Results are intended as driver-assistance safety alerts, not medical diagnosis or a substitute for driver judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver face videos and fatigue reports can contain sensitive biometric, safety, and employment-related data.

Mitigation: Obtain explicit driver or employee consent, confirm retention and deletion rules, and require appropriate storage and transport protections before use.

Risk: The skill uploads videos, URLs, report data, and identity-linked requests to configured API endpoints.

Mitigation: Review and approve the configured endpoints and credentials before installation, and disable unintended development or private endpoints.

Risk: The skill may create or reuse local identity and token state for report association.

Mitigation: Inspect local SQLite data and token handling, restrict access to persisted state, and clear stored state when reports or users should no longer be linked.

Risk: Visual fatigue detection can be unreliable when eyes are obscured, lighting is poor, or video quality is low.

Mitigation: Use the output only as an assistive warning, require clear DMS video that meets documented frame-rate and visibility constraints, and keep human driver judgment primary.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-blink-fatigue-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Driver Fatigue Detection API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON report text with report links and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local videos or submit video URLs to configured APIs; historical report lookup returns structured report records.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
