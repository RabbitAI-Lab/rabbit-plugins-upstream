## Description:

Helps users calibrate local LLM self-evaluations and reduce evaluation calls through rule checks, evidence-backed scoring, and sampled review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

All rights reserved (documentation and theory; MIT applies only to .py code)

## Use Case:

Developers and other users evaluating their own LLM outputs use this skill to define scoring criteria, cite evidence for scores, compare rule checks with model judgments, and limit evaluation calls. Scores are for internal guidance, not independent certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MIT label may be mistaken for permission to redistribute the documentation and theory, which reserve all rights.

Mitigation: Review the package's license scope before reuse; do not assume the code license covers the text.

Risk: Broad evaluation or scoring prompts may activate this skill unexpectedly.

Mitigation: Enable it only when that activation scope is acceptable.

Risk: Self-assigned scores may be inflated or mistaken for independent validation.

Mitigation: Require quoted evidence, compare scores with rule checks, and use independent evaluation for externally cited results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/local-llm-eval-assist)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference scores should cite evaluated text and flag disagreements between rule checks and model judgments.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
