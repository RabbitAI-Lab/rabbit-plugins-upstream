## Description:

Statamic connector skill for reading, creating, updating, and deleting Statamic account data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to manage Statamic sites and licenses through an OOMOL-connected account, including listing sites and performing confirmed create, update, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote shell installer commands for the oo CLI.

Mitigation: Review OOMOL's official install instructions and verify the installer where possible before executing it.

Risk: Write and destructive actions can create, overwrite, or delete Statamic site and license data.

Mitigation: Confirm the exact action, site, domains, payload, and intended effect with the user before allowing create_site, update_site, or delete_site.

Risk: Connector action schemas may differ from assumptions in a prompt or prior run.

Mitigation: Fetch the live action schema with oo connector schema before constructing payloads.

## Reference(s):

- [ClawHub Skill: Statamic](https://clawhub.ai/oomol/skills/oo-statamic)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Statamic](https://statamic.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with command snippets and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may call the oo CLI and can return JSON responses from the Statamic connector.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
