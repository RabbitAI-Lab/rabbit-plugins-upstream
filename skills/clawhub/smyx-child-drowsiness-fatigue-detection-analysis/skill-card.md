## Description:

Analyzes child face videos from classroom or home desk settings to estimate visual drowsiness indicators such as PERCLOS, nodding frequency, eye-region changes, and a 0-100 fatigue score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, parents, and developers use this skill to submit child study-area videos or video URLs for drowsiness and fatigue analysis, receive structured fatigue indicators, and query cloud-hosted historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child face videos or video URLs are sent to the configured Life Emergence cloud service.

Mitigation: Use the skill only with guardian or school authorization, avoid highly sensitive footage, and confirm that the configured cloud service is acceptable for the deployment.

Risk: Analysis history is associated with an automatically managed local or cloud identity.

Mitigation: Review identity and history-report behavior before enabling the skill, and prefer explicit confirmation before running history-report queries.

Risk: Workspace data or tokens may be stored locally while the skill accesses cloud APIs.

Mitigation: Review workspace data and token storage, restrict workspace access, and rotate or remove tokens when the skill is no longer needed.

## Reference(s):

- [Child Drowsiness / Fatigue Detection API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, files]

**Output Format:** [Markdown or JSON structured analysis report, with optional saved text output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue metrics, drowsiness events, voice-prompt text, report links, and history-report tables returned from the configured cloud service.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
