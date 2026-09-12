## Description:

CSV Slice helps agents inspect, select columns, deduplicate, filter, and count rows in CSV files using Python's standard csv module.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agent users use this skill for lightweight CSV inspection without spreadsheet tooling or pandas. It supports quick previews, column selection, row filtering, de-duplication, row counts, and optional machine-readable JSON summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary states the packaged tool is local and read-only, while documentation includes inaccurate --apply/write behavior.

Mitigation: Review installed files and rely on the packaged artifact behavior, or updated publisher documentation, before using any write/apply guidance.

Risk: The security guidance flags unpinned global installation advice.

Mitigation: Install the reviewed artifact or a pinned version before enabling the skill globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/csv-slice)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text, JSON, and Markdown guidance with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic CLI output with documented rc=0/1/2 exit statuses.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/manifest.json; artifact/SKILL.md frontmatter and changelog text mention 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
