## Description:

Analyzes fixed-camera footage at a home entrance or balcony to estimate a child's outdoor time from entry and exit events and produce a daily summary with reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use the skill to review estimated outdoor time from doorway or balcony footage and receive daily activity summaries and reminders. Developers may integrate its reports into family-care applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private footage may be sent to a remote service even when export-only or server-selection options are used, because those options are ignored.

Mitigation: Before using private footage, confirm where videos are sent and the provider's retention and deletion practices, and obtain informed guardian consent.

Risk: Credentials may be unexpectedly reused as account identifiers.

Mitigation: Avoid supplying credentials until account identifiers are separated from secrets and local token storage is appropriately protected.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis)
- [API interface and data fields](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured activity summaries, event counts and durations, and reminder text in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimates time from observed entry and exit events; it does not measure exercise or establish a medical conclusion.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
