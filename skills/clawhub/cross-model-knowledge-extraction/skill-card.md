## Description:

Extracts structured capability signatures from skill documentation, including workflow steps, headings, triggers, limits, scripts, and decision rules for model distillation and adversarial verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn teacher-skill documentation into machine-readable capability signatures for distillation planning, capability probing, and adversarial verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes persistent learner memory that can record usage history, errors, notes, and preferences.

Mitigation: Avoid storing sensitive details in learner notes or preferences, and review learned_patterns.json before sharing or publishing the skill.

Risk: The learning workflow can suggest or apply experience back into SKILL.md, which may change future behavior.

Mitigation: Manually review any proposed or automatic edits to SKILL.md before relying on them.

Risk: Regex-based extraction may miss implicit knowledge or nonstandard decision-rule wording.

Mitigation: Compare extracted signatures against the source skill documentation before using them for distillation or verification decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/cross-model-knowledge-extraction)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON capability signature with concise Markdown guidance and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with standard-library Python; learner commands may update learned_patterns.json.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
