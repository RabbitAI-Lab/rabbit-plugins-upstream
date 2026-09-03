## Description:

Audits dependency supply chains for bad versions, lockfile drift, and artifact integrity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to audit Python dependency supply chains, check lockfile and artifact integrity, and respond to suspected compromised packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad local scan examples can inspect more files than intended when run against large home or project directories.

Mitigation: Run scan commands against specific project directories whenever possible and review paths before execution.

Risk: Environment snapshot files created during incident response can contain secrets or other sensitive values.

Mitigation: Protect access to snapshot files and delete them when they are no longer needed for investigation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-leyline-supply-chain-advisory)
- [OpenClaw Homepage Metadata](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)
- [Incident Response Module](artifact/modules/incident-response.md)
- [Scanning Patterns Module](artifact/modules/scanning-patterns.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with inline shell commands, checklists, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Manual audit and incident-response guidance; commands should be reviewed and scoped before execution.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
