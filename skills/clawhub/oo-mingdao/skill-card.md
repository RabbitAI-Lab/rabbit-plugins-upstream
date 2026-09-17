## Description:

Enables agents to inspect Mingdao connector schemas and run Mingdao read, write, and destructive actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business users use this skill to let an agent work with Mingdao applications, worksheets, records, roles, workflows, approvals, discussions, logs, and knowledge search through a connected OOMOL account. It supports both read-only lookups and state-changing Mingdao operations when the user approves the exact payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes curl-to-bash and irm-to-iex remote installer commands.

Mitigation: Prefer a verified package, pinned release, checksum or signature check, and explicit user approval before any installer runs.

Risk: The connector can modify or delete Mingdao data through write and destructive actions.

Mitigation: Review the live action schema and confirm the exact payload, target, and expected effect before approving state-changing actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mingdao)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Mingdao Homepage](https://www.mingdao.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Mingdao through oo connector commands; write and destructive actions require confirmation before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
