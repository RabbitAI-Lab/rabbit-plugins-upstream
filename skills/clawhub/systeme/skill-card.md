## Description:

Helps agents manage Systeme.io contacts, tags, course access, community memberships, and subscriptions through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to look up and manage Systeme.io contacts, tags, enrolments, memberships, and subscriptions, with optional approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account access can expose or change sensitive contact, enrolment, and subscription data.

Mitigation: Use only the intended authorized connection; review the target and obtain explicit approval before writes.

Risk: Webhooks, triggers, and destinations can forward matching events continuously to an external URL.

Mitigation: Confirm the exact URL, data sent, and ongoing delivery separately before enabling forwarding.

Risk: Credentials or personal data could be exposed through destination settings or verbose responses.

Mitigation: Do not place credentials in destination headers or bodies; share only the response fields needed.

## Reference(s):

- [Systeme.io skill release](https://clawhub.ai/byungkyu/skills/systeme)
- [Systeme.io API reference](https://developer.systeme.io/reference)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton connection.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence; skill metadata lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
