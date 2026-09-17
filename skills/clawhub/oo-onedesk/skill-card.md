## Description:

OneDesk helps agents search and read OneDesk work items, projects, and organization profile data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with connected OneDesk accounts use this skill to inspect live connector schemas, filter OneDesk items and projects, and retrieve work item, project, and organization records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that can execute local code.

Mitigation: Install only when OOMOL is trusted, verify installer source and integrity before execution, and avoid piping remote scripts directly into a shell unless verified.

Risk: The connected OneDesk account is mediated by OOMOL.

Mitigation: Use this skill only when OOMOL is trusted with the connected OneDesk account and review account connection, scope, and billing errors before retrying.

Risk: Future write or destructive connector actions could change or remove OneDesk data.

Mitigation: Inspect live schemas and confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [OneDesk homepage](https://www.onedesk.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub OneDesk skill page](https://clawhub.ai/oomol/skills/oo-onedesk)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions return JSON data from the OneDesk connector; the skill instructs agents to inspect live schemas before constructing requests.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
