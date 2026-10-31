## Description:

Analyzes a pet image or video to match a registered pet with vaccination records and report whether a reminder is due.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet hospital staff, boarding teams, and pet insurance staff can use the skill to match a pet image or video to a registered pet and review its linked vaccination history for due reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configuration-only option can still upload pet media.

Mitigation: Wait for that option to be fixed before relying on it, and confirm the provider's media retention and account terms before submitting images or videos.

Risk: The skill automatically registers accounts and stores reusable login tokens.

Mitigation: Protect access to the shared token database and use separate identities for separate users.

Risk: A reminder may not reflect the pet's linked vaccination history.

Mitigation: Verify that each report uses the correct linked vaccination records before relying on its reminder.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, JSON, Markdown]

**Output Format:** [Structured vaccination reminder report or Markdown report list, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports depend on matching a registered pet and accessing its linked vaccination records.]

## Skill Version(s):

1.0.14 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
