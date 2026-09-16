## Description:

Enables agents to search and read Kintone user, department, group, and service metadata through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Kintone connector schemas and run supported read actions for users, departments, groups, and services without handling raw Kintone credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill tells agents to run remote installer scripts directly if the oo CLI is missing.

Mitigation: Review installation before use and install the oo CLI through an inspectable, trusted method instead of letting an agent run remote installer commands automatically.

Risk: The skill can read Kintone user, group, department, and service metadata available to the connected account.

Mitigation: Connect a least-privilege Kintone account and limit use to the listed read actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kintone)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Kintone homepage](https://www.kintone.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
