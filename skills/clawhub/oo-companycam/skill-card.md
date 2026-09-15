## Description:

CompanyCam (companycam.com). Use this skill for CompanyCam requests to read, create, update, and delete data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers managing CompanyCam accounts use this skill to inspect live action schemas and run account, project, tag, company, and user workflows through an OOMOL-connected CompanyCam account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI that require review before execution.

Mitigation: Review the oo CLI installation path carefully, prefer verified package-manager or manually downloaded installer steps from OOMOL, and avoid running curl-to-bash or invoke-expression commands without verification.

Risk: The skill can create, update, archive, restore, or delete CompanyCam records.

Mitigation: Require explicit confirmation before any CompanyCam write, archive, restore, update, or delete action, including confirmation of the target and payload.

## Reference(s):

- [CompanyCam Skill Page](https://clawhub.ai/oomol/skills/oo-companycam)
- [CompanyCam Homepage](https://companycam.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action execution; CompanyCam action responses include data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
