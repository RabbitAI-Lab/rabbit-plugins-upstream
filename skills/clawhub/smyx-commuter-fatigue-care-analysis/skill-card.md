## Description:

The skill analyzes living-room media from the first 30 minutes after an office worker arrives home for fatigue-related cues and returns a structured report with supportive care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Smart-home users or household administrators use it to review fatigue-related cues in after-work living-room media and receive non-diagnostic care suggestions or a history report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload household video for analysis, and the documented setup-only option may still allow network activity.

Mitigation: Require explicit fatigue-analysis and upload consent, confirm provider retention and deletion terms, and do not rely on --export-env-only to prevent network activity.

Risk: The skill may silently register or reuse an account, and its API secret identity-field reuse is unresolved.

Mitigation: Protect account tokens and do not configure an API secret until its identity-field reuse is fixed.

Risk: The bundle does not verify the advertised smart-home controls or server privacy safeguards.

Mitigation: Confirm these behaviors and privacy safeguards with the provider before enabling the service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)
- [Skill API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured fatigue analysis or history report in JSON or Markdown, with care suggestions and report links when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue-related observations, a non-diagnostic fatigue score, suggested supportive actions, or historical report links.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
