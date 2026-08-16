## Description:

Teable (teable.cn) lets an agent read, create, update, and delete Teable data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Teable data through an OOMOL-connected account, including reading spaces, bases, tables, and records and performing confirmed create, update, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change Teable data available to the connected OOMOL account.

Mitigation: Let read actions run normally, but review exact table IDs, record IDs, and payloads before approving create, update, or delete actions.

Risk: Delete actions permanently remove Teable records.

Mitigation: Require explicit approval of the target table and record before running destructive actions.

Risk: First-time CLI installation and account connection steps rely on OOMOL tooling and account access.

Mitigation: Run installer or connection steps only when setup is needed and the user trusts OOMOL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-teable)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Teable homepage](https://teable.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Teable metadata icon](https://static.oomol.com/logo/third-party/teable.svg)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides read actions directly and requires confirmation before write or destructive Teable actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
