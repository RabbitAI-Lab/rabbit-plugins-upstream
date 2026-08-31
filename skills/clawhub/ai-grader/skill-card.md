## Description:

ai-grader helps users evaluate and compare AI agents or responses against a 45-item work-awareness rubric, producing scores, red-flag checks, reports, and improvement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and AI operators use this skill to grade AI behavior, compare candidate agents, identify weak or risky dimensions, and generate local reports that support review and improvement planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store evaluation records and generate local reports in the skill directory.

Mitigation: Use anonymized inputs, avoid private transcripts or customer data, and review generated files before sharing them.

Risk: The skill includes owner and personality analysis that may profile people or relationships around an AI system.

Mitigation: Treat these analyses as optional and private, and use them only with appropriate consent and context.

Risk: Rubric and LLM-as-judge scores can be subjective or incomplete for high-stakes decisions.

Mitigation: Use scores as review aids, confirm red-flag findings with human reviewers, and avoid relying on the skill as the sole approval gate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-grader)
- [External probe pack](external_probe_pack.md)
- [AI evaluation protocol](references/ai_eval_protocol.md)
- [External evaluation workflow](references/ai_external_eval.md)
- [Capability bounds](references/ai_capability_bounds.md)
- [Domain fit assessment](references/ai_domain_fit.md)
- [Improvement plan](references/ai_improvement_plan.md)
- [Owner grading](references/ai_owner_grading.md)
- [Persona resonance](references/ai_persona_resonance.md)
- [Growth trend analysis](references/ai_growth_trend.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance, JSON evaluation records, and generated local HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write persistent local evaluation records and generated report files in the skill directory.]

## Skill Version(s):

2.6.0 (source: frontmatter, manifest, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
