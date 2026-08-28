## Description:

Audits the DSA problem bank for coverage gaps and proposes new YAML entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to audit a DSA problem bank, identify categories below expected NeetCode coverage, and prepare a markdown proposal report for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Gauntlet scripts and writes a temporary markdown report.

Mitigation: Confirm the expected Gauntlet workspace and review the generated report path before invoking the skill.

Risk: Proposed YAML problem entries could be incorrect or unsuitable if merged without review.

Mitigation: Review the proposal report and validate entries before applying any changes to the problem bank.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-gauntlet-curate)
- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with YAML proposal snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a temporary report and requires human review before any problem-bank changes.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
