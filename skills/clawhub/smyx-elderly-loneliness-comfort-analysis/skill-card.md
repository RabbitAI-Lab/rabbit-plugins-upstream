## Description:

Analyzes fixed-camera elder-care video, with optional audio, to identify loneliness-related behaviors and return a loneliness index, structured report, and warm companionship recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams, family caregivers, and developers use this skill to analyze elder-care camera footage for behavioral signs associated with loneliness and to produce structured reports, family-facing summaries, and companionship action suggestions. It is intended for supportive care workflows and does not provide a medical or psychiatric diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private elder-care video or optional audio may be sent to cloud analysis endpoints.

Mitigation: Use only with informed elder and caregiver consent, minimize captured areas and audio where possible, and review the service provider's endpoint, retention, and deletion practices before deployment.

Risk: History and export actions can expose account-linked care reports.

Mitigation: Restrict who can run report listing and export commands, verify identity scoping before use, and avoid sharing generated report links outside the care team.

Risk: The local workspace may contain identity values, API tokens, or account state.

Mitigation: Treat the workspace as sensitive, limit filesystem access, rotate or revoke tokens after testing, and remove local account state when the skill is no longer needed.

Risk: Loneliness scoring and behavioral labels could be mistaken for clinical diagnosis.

Mitigation: Present outputs as behavioral observations and supportive-care suggestions only, and escalate health concerns to qualified elder-care or mental-health professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-comfort-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports with structured JSON analysis payloads, history listings, recommendations, and report/export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud APIs for analysis, history lookup, and report export; local input files are limited to supported video formats.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
