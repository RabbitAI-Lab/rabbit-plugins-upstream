## Description:

Zoom (zoom.com). Use this skill for Zoom requests that read, create, or update Zoom data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect Zoom connector schemas and operate Zoom through OOMOL-backed actions for user lookup and meeting creation, listing, or updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports setup instructions that tell an agent to run unverified remote installer scripts.

Mitigation: Install the oo CLI through a verified, user-reviewed process before using the skill, and avoid allowing an agent to run remote installer commands automatically.

Risk: Using the skill relies on OOMOL as the Zoom connector provider.

Mitigation: Install and use the skill only when the organization is comfortable with OOMOL providing the Zoom connector.

Risk: Write actions can create or update Zoom meetings.

Mitigation: Confirm the exact payload and expected meeting changes with the user before running create_meeting or update_meeting.

## Reference(s):

- [ClawHub Zoom skill page](https://clawhub.ai/oomol/skills/oo-zoom)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Zoom homepage](https://www.zoom.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown instructions with shell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI; action responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
