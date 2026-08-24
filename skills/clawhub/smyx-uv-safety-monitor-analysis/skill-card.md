## Description:

Analyzes pet-area UV disinfection images or videos through a cloud service to produce structured UV exposure risk reports, alerts, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit camera media or media URLs from pet UV disinfection areas and receive structured risk analysis, recommendations, and historical report listings. The skill is best treated as a cloud report generator rather than a guaranteed real-time UV shutoff system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads local media or submits media URLs to a cloud analysis backend, so pet-area images, videos, URLs, and account-linked report data may leave the local workspace.

Mitigation: Use only media and URLs that are acceptable to send to the backend, and review generated report links before sharing them.

Risk: The release evidence says the skill overstates real-time protection and should not be treated as a guaranteed UV shutoff system.

Mitigation: Use the output as advisory risk reporting and keep independent physical or smart-home controls for confirming that UV lamps are off before pets can enter.

Risk: The release evidence says the skill silently creates or reuses account identity state.

Mitigation: Review or clear workspace data files and generated account tokens when persistent identity linkage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON-style analysis and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export links and historical report-list output.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
