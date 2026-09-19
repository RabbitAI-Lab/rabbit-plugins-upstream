## Description:

Breeze helps agents search and read Breeze church management data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Breeze people records, profile fields, tag folders, and tags through OOMOL's oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Prefer installing the oo CLI from a verified release or package manager, or review the installer before execution.

Risk: Breeze records are accessed through OOMOL-connected infrastructure.

Mitigation: Confirm organizational approval for routing Breeze data through OOMOL and use the minimum necessary Breeze connection scopes.

## Reference(s):

- [Breeze homepage](https://www.breezechms.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Breeze skill page](https://clawhub.ai/oomol/skills/oo-breeze)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas to shape request payloads before connector execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
