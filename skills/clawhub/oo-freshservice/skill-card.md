## Description:

Freshservice helps agents read, create, and update Freshservice data through the OOMOL freshservice connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Freshservice connector schemas, list ticket and catalog data, and create Freshservice tickets or service requests through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the oo CLI installation path manually and do not let an agent run curl-to-bash or irm-to-iex installer commands automatically.

Risk: Freshservice ticket data is sent through the OOMOL connector.

Mitigation: Use the skill only when the connected Freshservice and OOMOL account path is acceptable for the data involved.

Risk: Write actions can create Freshservice tickets or service requests.

Mitigation: Confirm the exact JSON payload and expected Freshservice effect with the user before running any write action.

## Reference(s):

- [Freshservice Skill Page](https://clawhub.ai/oomol/skills/oo-freshservice)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Freshservice Homepage](https://www.freshworks.com/freshservice/)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation of the exact payload and expected effect before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
