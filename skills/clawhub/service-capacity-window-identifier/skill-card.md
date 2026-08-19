## Description:

Select a service capacity window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations planners and service teams use this skill to select a concise service capacity reservation window from a supplied date, time, and timezone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on user-provided date, time, and timezone and has no independent scheduling validation logic.

Mitigation: Provide only the reservation details needed for the request and review the returned date-time against the operational calendar before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/service-capacity-window-identifier)
- [Publisher Profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Concise date-time value in Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the capacity_window field from the supplied capacity_request date, time, and timezone.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
