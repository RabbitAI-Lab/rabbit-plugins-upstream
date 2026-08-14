## Description:

A distilled meta-skill that augments native autonomous discovery with self-verification, reflection, super-agent orchestration, and continuous learning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to run autonomous discovery workflows that propose, test, rank, and report hypotheses with evidence traces. It also adds post-run reflection and preference/error memory for repeated use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep local cross-session memory about usage, errors, notes, and preferences.

Mitigation: Use an opt-in memory workflow, keep saved notes non-sensitive, and provide a way to inspect and delete learned_patterns.json.

Risk: The skill encourages future behavior changes and may write learned experience back into its own instructions.

Mitigation: Require user approval before edits to SKILL.md and review any proposed instruction changes before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-native-autonomous-discovery)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with structured findings and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update a local learned_patterns.json memory file when the learner script is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
