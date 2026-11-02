## Description:

Helps users manage Shuning OA timesheets and expenses by submitting, editing, and querying work records and checking reimbursement status and approval progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ithou](https://clawhub.ai/user/ithou)

### License/Terms of Use:

MIT-0

## Use Case:

OA users use the skill to manage work-time records and review reimbursement requests and their approval progress.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Password handling and encryption-key handling need security review before connecting an OA account.

Mitigation: Require HTTPS and have the maintainer address passwords in URLs and encryption keys passed as command arguments.

Risk: Timesheet changes, deletion, approval withdrawal, and scheduled monitoring can affect records or notifications.

Mitigation: Confirm the exact timesheet changes and separately authorize deletion, approval withdrawal, and scheduled monitoring.

Risk: Saved credentials and session tokens are sensitive.

Mitigation: Keep saved credentials and tokens private.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ithou/skills/sn-work-record)
- [Publisher profile](https://clawhub.ai/user/ithou)
- [Personal settings and submission boundaries](references/personal-settings.md)
- [Submission idempotency](references/submission-idempotency.md)
- [Timesheet amendment workflow](references/amendment-workflow.md)
- [Reimbursement monitoring](references/reimbursement-monitoring.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text summaries and JSON records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Status and approval-progress summaries; internal identifiers are omitted by default.]

## Skill Version(s):

1.14.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
