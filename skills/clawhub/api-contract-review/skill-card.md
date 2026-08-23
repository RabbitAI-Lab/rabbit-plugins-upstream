## Description:

Reviews consumer-visible API contracts for breaking changes and local design consistency across HTTP APIs, webhooks, event schemas, and API specs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API reviewers use this skill to evaluate API changes before release, checking compatibility against a before/after contract diff and design consistency against in-repo precedent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad API-review phrasing when the user intended implementation, security, or architecture review.

Mitigation: Use explicit requests to select API contract review and route implementation, security, or architecture concerns to the corresponding review workflow.

Risk: Compatibility conclusions can be misleading if the previous contract is not inspected.

Mitigation: Require a before/after diff for breaking-change findings and label unresolved semantics as questions.

Risk: Design consistency findings can become opinionated without local precedent.

Mitigation: Cite sibling endpoints or specs for conventions; otherwise drop the item or keep it as an open question.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/api-contract-review)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with ranked findings, migration guidance, and open questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Breaking-change findings require before/after citations; consistency findings require citations to in-repo precedent.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
