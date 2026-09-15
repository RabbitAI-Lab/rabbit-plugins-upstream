## Description:

Dup Finder helps an agent find duplicate files with a three-stage hash check and report findings before optional deletion with --apply.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and file-system users use this skill to identify duplicate files in local directories, inspect the space that could be reclaimed, and optionally remove duplicate copies after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The --apply mode can permanently delete duplicate files.

Mitigation: Run dry-run first, review the reported groups, avoid broad directories such as an entire home folder, and keep independent backups before applying deletion.

Risk: The documented one-line installation uses an unpinned external CLI command.

Mitigation: Prefer a pinned or manually reviewed install source before using the skill in a managed environment.

Risk: The primary instructions are Chinese-language documentation.

Mitigation: Install only where reviewers can understand the instructions or can obtain a trusted translation before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/dup-finder)
- [Publisher Profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Publisher Homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Analysis, JSON, Text]

**Output Format:** [Markdown guidance with shell commands and optional text or JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script exits with rc=0 for success, rc=1 when duplicates are found during dry-run, and rc=2 for usage or environment errors.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
