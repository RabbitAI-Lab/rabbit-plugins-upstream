## Description:

Kustomer lets an agent read, search, create, and update Kustomer customer records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support, operations, and developer agents use this skill to retrieve, search, create, and update Kustomer customer records after the user has connected Kustomer through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kustomer customer data may be processed through OOMOL and the connected account.

Mitigation: Review OOMOL connector permissions and data-routing expectations before install or use.

Risk: Curl-or-PowerShell pipe install commands can execute remote installer content.

Mitigation: Prefer a verified installer or approved package source and confirm the installer payload before running it.

Risk: Create and update actions can change Kustomer customer records.

Mitigation: Inspect the connector schema and confirm the exact payload and effect with the user before write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kustomer)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Kustomer homepage](https://www.kustomer.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires inspecting the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
