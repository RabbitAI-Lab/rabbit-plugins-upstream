## Description:

Insites helps agents operate Insites through an OOMOL-connected account to read audit data, search audits, and start website audits using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Insites SEO and AEO audit workflows through an OOMOL-connected account, including retrieving audit results, listing audits, and starting new website audits after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions recommend running an unverified remote installer directly in a shell.

Mitigation: Review the installer path before use and prefer installing the oo CLI from verified official release documentation or a signed package.

Risk: The start_audit action changes Insites account state.

Mitigation: Confirm the exact start_audit payload and expected effect with the user before allowing the action to run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-insites)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Insites Homepage](https://insites.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
