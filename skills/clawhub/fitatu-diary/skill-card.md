## Description:

Helps an agent manage a user's Fitatu food diary, nutrition goals, measurements, workouts, and reports through Fitatu tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jezue](https://clawhub.ai/user/jezue)

### License/Terms of Use:

MIT-0

## Use Case:

Fitatu users and their agents use this skill to review meals and nutrition progress, log food and body data, manage goals, and prepare diary reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an agent to Fitatu may disclose or change sensitive nutrition, weight, body, goal, recipe, and workout data.

Mitigation: Use a trusted agent and prefer local or read-only access when changes are unnecessary.

Risk: Remote HTTP access can expose sensitive Fitatu data if the endpoint is insufficiently protected.

Mitigation: Avoid binding to 0.0.0.0; before remote access, use a trusted tunnel, VPN, or TLS with firewall restrictions.

## Reference(s):

- [Fitatu API project (skill metadata homepage)](https://github.com/Jezue/fitatu_library)
- [Fitatu agent documentation](https://github.com/Jezue/fitatu_library/blob/main/docs/AGENTS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Conversational text or Markdown with setup commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize account data and confirm requested diary changes.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata; skill metadata lists fitatu-api 0.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
