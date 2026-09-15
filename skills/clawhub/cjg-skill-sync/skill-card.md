## Description:

cjg-skill-sync helps an agent check installed local skills against a version service, summarize available updates, and guide or run guarded update, rollback, baseline, and auto-update commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill users use this skill to inspect whether installed skills are behind the publisher's latest release, review changelog information, and apply selected updates with backup and rollback workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The updater can modify installed skill directories and security evidence warns that safeguards may not fully match the documented safety promises.

Mitigation: Run checks first, inspect proposed changes, keep separate backups of customized skills, and avoid update execution until the safeguard issues have been reviewed.

Risk: Local skill changes could be overwritten or lost during update flows.

Mitigation: Use no-baseline or inspection-oriented checks before applying updates, and do not enable automatic execution for skills with unknown or customized local state.

Risk: Autorun and execute modes can turn update guidance into filesystem changes.

Mitigation: Leave automatic updates disabled unless operationally required, and require explicit human review before enabling autorun or --execute.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j-levee/skills/cjg-skill-sync)
- [Publisher profile](https://clawhub.ai/user/j-levee)
- [Configured version lookup endpoint](https://1318491188-05nz50b82l.ap-guangzhou.tencentscf.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown-style status tables, command guidance, and plain text diagnostics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify installed skill directories when update execution is explicitly enabled.]

## Skill Version(s):

0.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
