## Description:

Regex Sandbox helps agents test regular expressions against text or files, preview matches, capture groups, replacements, and flags, and return deterministic exit codes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to test regular expressions quickly, inspect match groups, preview replacements, and obtain machine-readable results without adding runtime dependencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable install commands may fetch code that differs from the reviewed artifact.

Mitigation: Install the exact reviewed artifact or pin a commit or version before enabling the skill.

Risk: Regex input, file input, matches, and replacement previews can expose sensitive text in console or JSON output.

Mitigation: Avoid using secrets or sensitive records as input, and review outputs before sharing logs or artifacts.

Risk: Large inputs or expensive regular expressions can consume excessive runtime because the regex engine is not resource-isolated.

Mitigation: Use bounded inputs and review patterns before running the tool on large files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/regex-sandbox)
- [Project Homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with command-line examples; script output is plain text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic exit codes: rc=0 for matches, rc=1 for no matches, and rc=2 for usage or regex compile errors.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and manifest.json; SKILL.md frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
