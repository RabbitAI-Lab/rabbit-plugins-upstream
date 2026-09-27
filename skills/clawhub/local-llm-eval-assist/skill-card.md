## Description:

Helps users calibrate local LLM self-evaluation against predefined criteria and source evidence while reducing unnecessary evaluation calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and evaluators use this guidance to set scoring criteria before assessing their own LLM outputs, cite supporting text, compare rule-based checks with model scores, and sample or cache reviews to reduce evaluation calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Self-evaluation can inflate scores or obscure disagreements between rule checks and model judgments.

Mitigation: Define scoring criteria in advance, cite the evaluated text, report disagreements, and use independent evaluations for external claims.

Risk: Generic trigger words may activate the skill outside the intended evaluation context.

Mitigation: Confirm that the request concerns LLM scoring or evaluation before applying its guidance.

Risk: Primarily Chinese instructions may be less accessible to non-Chinese readers despite multilingual metadata.

Mitigation: Translate or review the instructions in the reader's preferred language before relying on them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/local-llm-eval-assist)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference scores should cite evaluated text and flag conflicts between rule checks and model scores; they are not independent certification.]

## Skill Version(s):

1.0.0 (source: ClawHub release and manifest.json; skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
