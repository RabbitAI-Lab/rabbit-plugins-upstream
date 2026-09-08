## Description:

Validates whether a QA testing request includes clear requirements and enough context before starting the test design workflow, returning missing information and clarification questions when input is insufficient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and test-design agents use this skill as the first workflow step to evaluate input quality, identify missing requirement context, and ask focused clarification questions before generating test cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may provide real customer, payment, identity, phone, financial, or production data while asking for QA validation.

Mitigation: Mask or redact sensitive data before using the skill, and avoid supplying real production records unless properly de-identified.

Risk: Incomplete or vague requirements can lead to limited or misleading downstream test-case guidance.

Mitigation: Review generated validation results and require clarification for missing business goals, user roles, constraints, boundaries, or context before relying on test cases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-input-validation)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or JSON-like validation results with missing-information lists, clarification questions, recommendations, and optional test-case guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include validation_result, input_quality_score, missing_info, clarification_questions, and recommendation fields.]

## Skill Version(s):

1.7.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
