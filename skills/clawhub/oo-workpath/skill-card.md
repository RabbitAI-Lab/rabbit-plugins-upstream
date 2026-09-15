## Description:

Workpath (workpath.com). Use this skill for ANY Workpath request — searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to retrieve Workpath goals, key results, teams, and users through an OOMOL-connected Workpath account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote shell installer commands.

Mitigation: Review the oo CLI installation path before installing; prefer official package-manager or signed, version-pinned installation steps with checksum or signature verification, and avoid pipe-to-shell commands from an elevated shell.

Risk: The skill depends on an established oo CLI installation and Workpath connection.

Mitigation: Run connector actions only after the CLI and Workpath connection are already established; the listed actions in the supplied evidence are read-only and aligned with Workpath data lookup.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-workpath)
- [Workpath Homepage](https://www.workpath.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; listed connector actions are read-only in the supplied evidence.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
