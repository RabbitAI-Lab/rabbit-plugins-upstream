## Description:

7shifts helps agents retrieve 7shifts company, location, department, role, user, and identity data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect read-only 7shifts business data, including companies, departments, locations, roles, users, and the connected identity. The skill is intended for accounts where the oo CLI is installed, signed in, and connected to 7shifts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup fallback includes remote installer commands that could create a supply-chain risk if an agent runs them automatically.

Mitigation: Review installer commands before use, install the oo CLI only from a verified source, and avoid letting agents run curl-to-shell or irm-to-iex commands without explicit approval.

Risk: The skill accesses data from the connected 7shifts account through OOMOL-managed credentials.

Mitigation: Confirm the connected 7shifts account and requested data scope before running connector actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-7-shifts)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [7shifts Homepage](https://www.7shifts.com/)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions are read-oriented in the provided artifact; setup guidance may include authentication, connection, or billing remediation steps.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
