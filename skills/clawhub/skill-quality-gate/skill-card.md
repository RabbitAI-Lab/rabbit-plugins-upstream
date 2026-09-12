## Description:

Skill Quality Gate helps agents and developers evaluate a skill directory before release with a nine-part quality checklist and a local CLI that reports pass/fail results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent maintainers use this skill before publishing or submitting a skill to check required metadata, script compilability, documentation, bilingual coverage, trigger guidance, gatekeeping content, desensitization, and basic secret patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the quality gate as a complete security or release approval.

Mitigation: Use it as a lightweight checklist and require human review plus separate security scanning before publishing.

Risk: The installation guidance includes an unpinned global npx path.

Mitigation: Install only from a pinned, reviewed commit or signed release.

Risk: Security evidence says the gate implementation can give users false confidence.

Mitigation: Do not rely on the script as an automated publish blocker until exit-code behavior and secret scanning are reviewed and fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/skill-quality-gate)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance and human-readable CLI pass/fail output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Artifact claims a local zero-dependency Python script; results require human review before release decisions.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and README mention 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
