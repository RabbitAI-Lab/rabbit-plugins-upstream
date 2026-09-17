## Description:

Terraform helps agents inspect Terraform account, organization, workspace, and run data through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to retrieve HCP Terraform account, organization, workspace, and run details from an OOMOL-connected Terraform account. It is intended for read-oriented Terraform inspection workflows where the agent first checks live action schemas and then runs supported oo CLI connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users or agents to run remote installer commands that have not been independently verified.

Mitigation: Prefer pinned, signed, or checksum-verified oo CLI releases and review installer sources before execution.

Risk: Terraform requests and account metadata are routed through OOMOL as a third-party processor.

Mitigation: Install only when OOMOL processing is acceptable for the organization, and use the skill for the listed read-only Terraform actions unless broader connector use is separately approved.

Risk: Connector responses may be incomplete or misleading for operational decisions.

Mitigation: Inspect live action schemas before submitting payloads and independently verify important Terraform state or run information before relying on it.

## Reference(s):

- [ClawHub Terraform Skill](https://clawhub.ai/oomol/skills/oo-terraform)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Terraform](https://www.hashicorp.com/products/terraform)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include oo CLI connector schema commands, connector run commands, setup guidance, and read-only Terraform resource summaries.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
