## Description:

FDE PRD Writer turns an approved problem-discovery package and POC engagement charter into an English PRD specification handoff for engineering, QA, deployment, Agent Skill design, and POC execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukun0821](https://clawhub.ai/user/xukun0821)

### License/Terms of Use:

MIT-0

## Use Case:

Field delivery, product, engineering, and QA teams use this skill to turn an approved POC charter and problem-discovery package into a traceable PRD handoff with functional requirements, acceptance criteria, test scenarios, scope boundaries, and downstream handoff notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated PRDs may contain unvalidated assumptions if upstream discovery or POC charter evidence is missing.

Mitigation: Confirm the required upstream problem-discovery package and POC engagement charter before drafting, and mark unresolved information as to be confirmed.

Risk: The local traceability checker only verifies structural identifier relationships and can miss incorrect business logic or acceptance criteria.

Mitigation: Review requirements, acceptance criteria, priorities, scope changes, tool boundaries, and handoffs manually before engineering or QA handoff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xukun0821/skills/fde-prd-writer)
- [PRD quality gate](references/prd-quality.md)
- [PRD writing standards](references/prd-style.md)
- [Method selection](references/method-selection.md)
- [FDE Delivery Loop handover contract](references/upstream-downstream-contracts.md)
- [Test scenario design](references/test-scenarios.md)
- [User story guidance](references/user-stories.md)
- [PRD skeleton template](templates/prd-skeleton.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown PRD handoff package with optional local traceability-check command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to English unless another language is explicitly requested; the traceability checker detects identifier and relationship gaps but does not judge business correctness.]

## Skill Version(s):

1.0.0 (source: server release metadata and TRUST-CARD.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
