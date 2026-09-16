## Description:

GatherUp helps an agent search and read GatherUp business and customer data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they need an agent to retrieve GatherUp business locations or customers from an account connected through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that may execute changing code on a user's machine.

Mitigation: Do not let an agent run installer commands automatically; install the oo CLI only from a trusted, versioned source after reviewing the installer or using a safer package-manager path.

Risk: Authentication and connection setup can affect the user's OOMOL and GatherUp account access.

Mitigation: Let the user confirm sign-in, connection, and billing steps manually before retrying GatherUp actions.

## Reference(s):

- [GatherUp Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-gatherup)
- [GatherUp Homepage](https://gatherup.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal action responses are JSON from the oo CLI with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
