## Description:

Namecheap DNS工具 helps agents manage Namecheap DNS records by fetching current records, previewing diffs, merging changes, creating backups, and supporting rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill for explicit Namecheap DNS work, including reviewing planned DNS changes, applying record updates, creating backups, and restoring prior DNS state when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DNS updates can remove existing records because the workflow may replace a domain's hosted DNS record set.

Mitigation: Use dry-run or diff output first, fetch the current DNS state, and keep backups before applying changes.

Risk: Namecheap records that are not visible through the API can be lost during DNS changes.

Mitigation: Run verification for hidden records, review any warnings, and use force-style overrides only after confirming the records are no longer needed.

Risk: The artifact mixes Namecheap DNS guidance with unrelated project-management and security-scanning claims.

Mitigation: Use the skill only for explicit Namecheap DNS work and do not rely on unrelated project-management or scanner claims.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/namecheap-dns)
- [Publisher Profile](https://clawhub.ai/user/thcjp)
- [Artifact Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-style result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DNS diff previews, backup or rollback guidance, and warnings before high-impact DNS changes.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
