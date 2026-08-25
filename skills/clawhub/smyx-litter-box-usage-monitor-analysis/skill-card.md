## Description:

Analyzes litter-box area videos or video URLs to estimate each cat's litter-box visit frequency and duration, compare behavior with historical baselines, and produce behavior-based urinary health alerts that are not medical diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as multi-cat households, catteries, boarding centers, and veterinary inpatient teams use this skill to submit litter-box area videos and receive structured usage-frequency, per-visit-duration, historical-baseline, and alert outputs. The skill is intended for behavior monitoring and early warning only, not diagnosis or replacement of veterinary care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private in-home pet videos or video URLs can be sent to external services for remote processing.

Mitigation: Use only videos the user is authorized to share, avoid footage containing people or sensitive household details when possible, and confirm consent for remote processing before running the skill.

Risk: The skill can create or reuse an internal user identity and query account-linked historical reports.

Mitigation: Run the skill in a workspace with an intended identity context, disclose that history may be account-linked, and review returned historical data before sharing it onward.

Risk: Authentication tokens may be persisted locally in SQLite storage.

Mitigation: Install only in trusted environments, restrict workspace access, and remove local skill data when the skill is no longer needed.

Risk: Current configuration includes dev or private endpoint settings in addition to public service endpoints.

Mitigation: Review configuration before use and allow network access only to expected production endpoints.

Risk: Behavior alerts may be mistaken for veterinary diagnosis.

Mitigation: Present results as behavior-based monitoring signals and direct users to veterinary evaluation for medical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Structured text or JSON analysis report, with optional Markdown table output for historical report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and cloud-returned historical report data; local video inputs are limited to mp4, avi, and mov files up to 10 MB according to the artifact documentation.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
