## Description:

Operate Dialpad WFM through an OOMOL-connected account to read, create, and update workforce-management data using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to retrieve Dialpad WFM schedules and metrics and to submit schema-validated connector payloads through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute unaudited code during first-time setup.

Mitigation: Review or verify the oo CLI installer before running it; prefer a signed or otherwise verifiable package when available.

Risk: Write-like Dialpad WFM actions operate through the connected OOMOL account.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write-like actions.

## Reference(s):

- [Dialpad WFM skill page](https://clawhub.ai/oomol/skills/oo-dialpad-wfm)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Dialpad WFM homepage](https://www.dialpad.com/features/workforce-management-software/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
