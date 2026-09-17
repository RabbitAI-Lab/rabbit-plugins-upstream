## Description:

Fern helps agents inspect live Fern connector schemas and retrieve customer, payment-account, transaction, and exchange-rate data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support staff, and operations users can use this skill to answer explicit Fern data requests from a connected OOMOL account, including customer, payment account, transaction, and exchange-rate lookups. The skill is suited to read-only investigation and reporting workflows where the agent should inspect the connector schema before running a request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct remote shell installers for the oo CLI.

Mitigation: Prefer verified package-manager installation or checksum-validated installer steps before using the CLI.

Risk: Read-only Fern lookups can expose sensitive customer, payment account, transaction, and business data from the connected account.

Mitigation: Run the skill only for explicit Fern data requests and limit outputs to the information needed for the user task.

## Reference(s):

- [ClawHub Fern skill page](https://clawhub.ai/oomol/skills/oo-fern)
- [Fern homepage](https://fernhq.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Fern requests; responses include connector data and an execution ID when actions run successfully.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
