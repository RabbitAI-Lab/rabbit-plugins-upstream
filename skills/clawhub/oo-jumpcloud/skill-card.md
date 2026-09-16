## Description:

JumpCloud (jumpcloud.com). Use this skill for ANY JumpCloud request -- searching and reading data. Whenever a task involves JumpCloud, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect JumpCloud systems and system users through an OOMOL-connected account. It is intended for search and read workflows that fetch connector schemas before running listed JumpCloud actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts in a shell.

Mitigation: Before installing, use a signed package or downloaded installer with a published checksum when available.

Risk: JumpCloud access depends on sensitive account-backed credentials and connector scopes.

Mitigation: Keep usage to the disclosed read-only actions unless a future version clearly discloses and constrains write actions.

## Reference(s):

- [ClawHub JumpCloud skill page](https://clawhub.ai/oomol/skills/oo-jumpcloud)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [JumpCloud homepage](https://jumpcloud.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns read-oriented JumpCloud data with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
