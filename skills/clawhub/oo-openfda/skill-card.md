## Description:

openFDA helps an agent search, read, and count records in supported openFDA drug datasets through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query openFDA drug datasets, inspect live connector schemas, search paginated records, and count common field values without calling the openFDA API directly. Results are informational and should not be treated as medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask users to execute remote installer scripts for the oo CLI.

Mitigation: Review the skill before installing, prefer verified or package-manager installation channels when available, and confirm the CLI source before running installer commands.

Risk: openFDA requests are routed through OOMOL's connector service with server-side credential handling.

Mitigation: Use the skill only when third-party routing is acceptable, and avoid sending sensitive patient, proprietary, or investigative query terms through the connector.

## Reference(s):

- [openFDA homepage](https://open.fda.gov/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openfda)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include openFDA connector results, schema inspection commands, pagination guidance, setup guidance, and warnings that results are informational rather than medical advice.]

## Skill Version(s):

1.0.2 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
