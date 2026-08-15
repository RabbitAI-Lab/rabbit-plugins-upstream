## Description:

Meta Interpretable Attribution is a distilled attribution-analysis skill that adds self-verification, reflection logging, orchestration hooks, and continuous learning around an interpretable-attribution workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to explain model predictions with global feature importance, local ablation, counterfactual suggestions, and concise natural-language attribution. The skill also supports iterative improvement by recording usage outcomes and failure notes locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local learner notes can retain prompts, filenames, or other sensitive context if that information is recorded as free-form notes.

Mitigation: Do not include secrets, private prompts, customer data, or sensitive filenames in learner notes, and delete learned_patterns.json when retained history is not desired.

Risk: Attribution and counterfactual outputs may be unstable for small samples, greedy counterfactual searches, or nested feature structures.

Mitigation: Use adequate sample sizes and permutation runs, flatten nested inputs before analysis, and validate important explanations against the original attribution workflow before relying on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qq435912743/skills/meta-interpretable-attribution)
- [Distillation Report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown text with optional code and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist local usage and failure notes in learned_patterns.json when the learner script is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
