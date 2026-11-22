## Description:

Checks whether a report's file:line references point to existing files and in-range line numbers in relation to a selected directory tree, without judging whether the cited content supports the claim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, reviewers, and auditors can check whether file and line references in reports still resolve in a chosen project tree. They can use the results to flag missing files or out-of-range line numbers before relying on those references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A report-supplied file reference may escape the selected folder and still be treated as valid evidence.

Mitigation: Use trusted reports and confirm referenced paths stay within the selected tree before relying on results.

Risk: The security scan was partial because some local references could not be resolved, so its evidence is incomplete.

Mitigation: Review unresolved references and inspect the skill's behavior before installing or relying on it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/evidence-anchor)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Anchor checking rules](artifact/references/rules.md)
- [Usage examples](artifact/references/usage.md)
- [Scope limits](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands]

**Output Format:** [Plain text status report with optional summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports anchor status and file line counts; does not assess whether cited content supports a claim.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
