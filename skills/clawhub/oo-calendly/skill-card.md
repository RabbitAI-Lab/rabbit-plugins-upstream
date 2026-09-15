## Description:

Operate Calendly through an OOMOL-connected account to read, create, update, and delete Calendly data instead of calling the Calendly API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and scheduling teams use this skill to manage Calendly workflows through the oo CLI, including users, event types, invitees, availability, scheduled events, organizations, memberships, routing forms, and webhooks. It supports booking, scheduling-link, invitation, webhook, and availability changes with confirmation safeguards for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code in a shell.

Mitigation: Review and trust OOMOL's installer path before running it; prefer a verifiable package-manager or signed installation method when available.

Risk: Write and destructive Calendly actions can change, remove, or overwrite scheduling data.

Mitigation: Inspect the live action schema, confirm the exact target and payload, and require explicit approval before write or destructive actions.

## Reference(s):

- [Calendly homepage](https://calendly.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Calendly skill page](https://clawhub.ai/oomol/skills/oo-calendly)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live action schema checks before Calendly requests; state-changing and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
