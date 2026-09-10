## Description:

Rewrites weak ClawHub skill summaries into shorter, clearer storefront copy that is easier to understand and evaluate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External skill publishers and developers use this skill to turn vague ClawHub skill summaries into short, focused storefront copy and receive several replaceable summary options with usage guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested storefront copy could overstate a skill's value or imply unsupported adoption outcomes.

Mitigation: Review generated summaries against the actual skill behavior before publishing.

Risk: The metadata asks for git and the clawhub Node package even though the instructions do not explain their role.

Mitigation: Review dependency expectations in the target environment before installing or using the skill.

## Reference(s):

- [Summary rewrite principles](references/summary_patterns.md)
- [Weak vs strong summary examples](examples/weak_vs_strong_summaries.md)
- [Summary rewrite output template](templates/summary_rewrite_output.md)
- [OpenClaw publisher homepage](https://github.com/bonniegeng-max/openclaw-publisher)
- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/skill-summary-rewriter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown critique with rewrite options and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically identifies the current summary problem, rewrite direction, 3 to 5 replacement summaries, one preferred version, and placement guidance.]

## Skill Version(s):

1.0.2 (source: frontmatter, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
