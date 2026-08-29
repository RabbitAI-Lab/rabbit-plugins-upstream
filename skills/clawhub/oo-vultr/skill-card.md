## Description:

Operates Vultr through an OOMOL-connected account to read, create, update, power-manage, and delete cloud resources with live connector schema checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to administer Vultr resources from an agent session through the OOMOL connector. It supports account, instance, DNS, firewall, image, plan, region, snapshot, power, update, creation, and deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, power-manage, and permanently delete real Vultr cloud resources, which may affect service availability or incur charges.

Mitigation: Review the exact payload and expected effect with the user before write actions, and require explicit approval before destructive actions.

Risk: Setup may require installing or running the oo CLI, which introduces local command execution and installer-source trust considerations.

Mitigation: Use the documented OOMOL CLI source and verify the installer source before setup commands are run.

## Reference(s):

- [ClawHub Vultr Skill](https://clawhub.ai/oomol/skills/oo-vultr)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Vultr Homepage](https://www.vultr.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect the live connector schema before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
