## Description:

Cal.com connector for reading, creating, updating, and deleting Cal.com data through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Cal.com through an OOMOL-connected account, including booking, attendee, event type, schedule, availability, calendar, and profile workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run unverified remote installer scripts on the user's machine.

Mitigation: Review or replace the pipe-to-shell setup with a pinned, verified OOMOL installer before installation.

Risk: The skill can create, update, cancel, delete, or otherwise change Cal.com data.

Mitigation: Confirm the exact payload and expected effect with the user before any write or destructive action.

Risk: OOMOL mediates the Cal.com connection and credential handling.

Mitigation: Use the skill only with a trusted OOMOL account and connected Cal.com app, and account for OOMOL mediation in review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cal)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Cal.com](https://cal.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON; write and destructive Cal.com actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
