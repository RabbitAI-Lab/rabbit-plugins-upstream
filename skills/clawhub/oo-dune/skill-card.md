## Description:

Dune (dune.com). Use this skill for Dune requests such as searching, reading data, executing saved queries, and retrieving query results through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to operate Dune through an OOMOL-connected account, inspect live connector schemas, execute saved Dune queries, and retrieve query status, metadata, and JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Prefer an official package manager or downloaded installer with version and checksum verification, and run setup only after explicit user approval.

Risk: Dune work is routed through OOMOL and the oo CLI connected account.

Mitigation: Use the skill only when that routing is acceptable, and inspect the live action schema before constructing request payloads.

## Reference(s):

- [Dune homepage](https://dune.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Dune skill page](https://clawhub.ai/oomol/skills/oo-dune)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect connector schemas before running Dune actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
