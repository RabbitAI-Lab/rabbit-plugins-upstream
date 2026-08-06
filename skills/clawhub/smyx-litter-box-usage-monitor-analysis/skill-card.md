## Description:

Analyzes litter-box area video or URL inputs to track cat entry and exit events, summarize usage frequency and visit duration against history, and produce behavior-based urinary-health alerts without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as pet owners, catteries, veterinary inpatient wards, and boarding centers use this skill to review litter-box videos, monitor per-cat usage patterns, and surface behavior-based urinary-health alerts for follow-up with veterinary care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that the skill sends supplied videos or URLs to a cloud service for analysis.

Mitigation: Use only with videos and URLs that are appropriate to share with the third-party cloud service, and avoid submitting sensitive household, clinic, or boarding-center footage without consent.

Risk: The security scan reports that the skill silently creates or reuses an account identity and can query account-scoped history.

Mitigation: Review the workspace identity and history behavior before deployment, and isolate workspace data when multiple users or sensitive reports are involved.

Risk: The security scan reports that service tokens may be stored in a local workspace SQLite database.

Mitigation: Restrict access to the workspace data directory, rotate credentials after testing, and avoid running the skill in shared or untrusted workspaces.

Risk: The skill produces behavior-based health alerts that are not medical diagnoses.

Mitigation: Present alerts as screening signals and direct users to veterinary evaluation for diagnosis or treatment decisions.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Structured text or JSON analysis reports, with Markdown table output for report history listings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report export link returned by the remote service.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter declares 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
