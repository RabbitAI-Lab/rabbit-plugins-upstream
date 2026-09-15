## Description:

Terraform (hashicorp.com). Use this skill for Terraform search and read requests through the OOMOL-connected Terraform connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to inspect Terraform account, organization, workspace, and run information through the OOMOL-connected oo CLI. It helps agents fetch live action schemas, build JSON payloads, and recover from authentication, connection, setup, or billing errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review before installing and prefer a verified, documented oo CLI installation method instead of allowing an agent to run remote installer commands automatically.

Risk: The activation scope is broader than necessary for Terraform requests.

Mitigation: Use the skill only for Terraform account, organization, workspace, and run lookup tasks, and avoid routing unrelated infrastructure work through it.

Risk: Terraform account, organization, workspace, and run metadata can be exposed through the OOMOL connector.

Mitigation: Use accounts and connected Terraform organizations whose metadata is appropriate to expose through the OOMOL connector.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-terraform)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Terraform Homepage](https://www.hashicorp.com/products/terraform)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Terraform account, organization, workspace, and run metadata returned through the OOMOL connector.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
