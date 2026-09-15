## Description:

Provides read-only access to Breathe account, employee, department, and location data through the OOMOL-connected breathe connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Breathe connector schemas and run read-only Breathe lookups for account, employee, department, and location data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the installer path before installing and prefer a pinned official package or a downloaded script whose checksum or signature has been verified.

Risk: Using the skill can read HR data available to the connected Breathe account.

Mitigation: Use an appropriately scoped Breathe connection and avoid exposing command output beyond the intended requester.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Breathe homepage](https://www.breathehr.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command responses are JSON objects containing data and meta.executionId; action schemas should be inspected before constructing payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
