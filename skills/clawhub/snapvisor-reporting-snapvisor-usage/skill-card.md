## Description:

Reports SnapVisor account build and screenshot usage, project trends, team members, and pending invites without changing account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

SnapVisor account users and administrators use this skill to review build and screenshot activity, identify busy projects, and check team membership or pending invitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting SnapVisor grants access to account analytics and, for team reporting, admin-scoped member and invite details.

Mitigation: Confirm the requested reporting access before connecting; grant the admin scope only if team reporting is needed.

Risk: Usage or access reports may be misleading if the wrong account, date range, or permissions are used.

Mitigation: Confirm the account and reporting window, report only returned values, and disclose missing permissions instead of filling gaps.

## Reference(s):

- [SnapVisor reporting skill on ClawHub](https://clawhub.ai/bsalaeddin/skills/snapvisor-reporting-snapvisor-usage)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Short report with totals, trend table, project breakdown, and optional team and invite lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports returned values only; does not estimate costs or change account settings.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
