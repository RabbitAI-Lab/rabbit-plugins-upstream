## Description:

新帆线索池运营 helps operations staff view private and public lead pools, inspect lead details and statistics, claim or release leads, update follow-up state, remarks, and priority, and generate private-lead daily reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yiqingqiu23187](https://clawhub.ai/user/yiqingqiu23187)

### License/Terms of Use:

MIT-0

## Use Case:

Employees in lead operations use this skill to manage internal e-commerce merchant leads: review lead pools and details, update lead ownership or follow-up metadata, and prepare concise daily private-lead reports. It is intended for user-scoped workflows through the currently logged-in operator's session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The private daily report can present mock conversion metrics as if they were real operational data.

Mitigation: Disable that report, replace the mock KPI section with real metric sources, or clearly label it as demo data before scheduled use.

Risk: The skill can change real lead records, including claims, releases, follow-up status, remarks, and priority.

Mitigation: Require explicit user confirmation that names the affected lead and intended business change before any write action.

Risk: The skill acts through the current user's logged-in browser session and may access user-scoped lead or contact data.

Mitigation: Run it only in an approved authenticated environment and avoid requesting sensitive contact details unless there is a clear business need.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yiqingqiu23187/skills/xinfan-lead-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and reports, with JSON CLI responses for agent processing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated browser session; write actions affect real lead records and should be confirmed by the user.]

## Skill Version(s):

0.1.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
