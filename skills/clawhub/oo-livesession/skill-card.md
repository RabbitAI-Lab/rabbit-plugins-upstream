## Description:

LiveSession helps agents search and read LiveSession session replay data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and support teams use this skill to inspect the LiveSession action schema and list session replays with pagination and common filters from a connected LiveSession account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute arbitrary code if followed automatically.

Mitigation: Review setup before installing, do not let an agent run the remote installer automatically, and install the oo CLI through a verified, user-controlled method where possible.

Risk: Authentication, connection, and billing recovery steps can change local authentication state or account configuration.

Mitigation: Run setup and recovery steps only after the matching command failure, and keep sign-in, connection, and billing actions user-directed.

## Reference(s):

- [ClawHub LiveSession Skill](https://clawhub.ai/oomol/skills/oo-livesession)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [LiveSession Homepage](https://livesession.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live action schema before constructing request payloads; normal listed use is read-only.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
