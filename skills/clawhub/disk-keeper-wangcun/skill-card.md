## Description:

净盘师 DiskKeeper is a Windows disk-cleaning agent that inventories disk usage and recycle-bin state, previews cleanup plans, and can remove allowlisted temporary files, caches, ghost recycle receipts, and optionally recycle-bin contents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mingyi-blog](https://clawhub.ai/user/mingyi-blog)

### License/Terms of Use:

MIT-0

## Use Case:

External Windows users and support agents use this skill to inspect low disk space, compare claimed and measured cleanup effects, preview deletion plans, and run local cleanup commands for rebuildable cache and temporary data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deletion behavior may be broader or more irreversible than the safety claims suggest.

Mitigation: Review cleanup plans manually and run plan or clean without --yes before allowing deletion.

Risk: Running with elevated privileges can increase the impact of an incorrect cleanup target.

Mitigation: Avoid running the skill as administrator unless the reviewed task specifically requires it.

Risk: The recycle --purge mode permanently empties the entire recycle bin.

Mitigation: Do not use recycle --purge unless the user explicitly intends to permanently remove all recycle-bin contents.

Risk: Unattended cleanup can repeat unsafe deletion choices if roots are not tightly scoped.

Mitigation: Do not configure unattended cleanup until deletion roots are strictly allowlisted and audit failures are fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mingyi-blog/skills/disk-keeper-wangcun)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local cleanup plans, command sequences, status reports, and configuration guidance for scheduled cleanup.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
