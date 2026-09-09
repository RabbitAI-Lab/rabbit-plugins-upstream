## Description:

List today's football fixtures and live scores using the futbol-libre-hoy CLI/package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nazzal5448](https://clawhub.ai/user/nazzal5448)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve today's football fixtures, live scores, dated fixture lists, JSON output, and match URLs for more detail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external npm or PyPI package and contacts verfutbollibre.net for match data.

Mitigation: Confirm the package and network dependency are acceptable before installation; pin or inspect the package when stronger supply-chain control is required.

Risk: Running the disclosed CLI commands may execute external package code in the local environment.

Mitigation: Run commands in a normal user environment and review the package before use in sensitive contexts.

## Reference(s):

- [futbol-libre-hoy homepage](https://verfutbollibre.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and match URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON output when the --json command option is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
