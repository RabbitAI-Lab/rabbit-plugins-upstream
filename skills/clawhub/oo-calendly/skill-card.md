## Description:

Calendly (calendly.com). Use this skill for ANY Calendly request: reading, creating, updating, and deleting data through the OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Calendly through the oo CLI, including reading Calendly records and creating or managing bookings, scheduling links, webhooks, memberships, invitations, and availability schedules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run unverified remote installer scripts.

Mitigation: Review installation steps before use and prefer a verifiable package or installer with checksum or signature validation.

Risk: The skill can modify or delete Calendly data.

Mitigation: Confirm the exact payload and effect before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Calendly homepage](https://calendly.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-calendly)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Calendly connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
