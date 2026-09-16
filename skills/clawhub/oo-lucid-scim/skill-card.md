## Description:

Lucid SCIM helps agents search and read Lucid SCIM users, groups, and service provider configuration through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Lucid SCIM users, groups, and service provider configuration through the OOMOL connector without handling raw credentials in the skill workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to run a live remote installer directly in the shell.

Mitigation: Review the oo CLI installation path before installing, and prefer a verified package manager or installer with checksum or signature verification.

Risk: Lucid SCIM requests are routed through the OOMOL connector service.

Mitigation: Confirm that the deployment is allowed to route Lucid SCIM requests through the OOMOL-connected account before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-lucid-scim)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Lucid](https://lucid.co)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns oo CLI JSON responses when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
