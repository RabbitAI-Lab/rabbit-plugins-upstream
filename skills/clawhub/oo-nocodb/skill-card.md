## Description:

NocoDB (nocodb.com) skill for reading, creating, updating, and deleting NocoDB data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live NocoDB connector schemas and run read, write, and destructive NocoDB actions through OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remote installer directly in a shell.

Mitigation: Review the installer source and prefer a signed, pinned, or package-manager installation path before use.

Risk: Write and destructive actions can change or remove real NocoDB data.

Mitigation: Confirm exact payloads, target bases or tables, and expected effects with the user before running write or destructive actions.

## Reference(s):

- [NocoDB homepage](https://nocodb.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub NocoDB skill page](https://clawhub.ai/oomol/skills/oo-nocodb)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before constructing action payloads; command results are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
