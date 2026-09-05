## Description:

Convenes a multi-expert panel to review a Product Requirements Document (PRD) and return a GO, NO-GO, or CONDITIONAL GO verdict with preserved dissent and failure signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cpsean](https://clawhub.ai/user/cpsean)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers and product teams use this skill to stress-test written PRDs before committing engineering resources. It is suited for feature, pricing, UX, and product-proposal reviews where the desired output is a structured second opinion with a clear verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process confidential PRDs or linked product documents through the agent's existing workspace and connector access.

Mitigation: Use it only in approved workspaces and with documents the agent is permitted to read.

Risk: The panel verdict may be over-weighted as an authoritative business decision.

Mitigation: Treat the output as decision support and validate recommendations with responsible product, research, business, and engineering owners.

Risk: Named expert perspectives may be mistaken for real statements or endorsements.

Mitigation: Keep the required disclaimer in every run and preserve the distinction between public-framework interpretation and actual individual opinion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cpsean/skills/product-review-panel-skill)
- [Server-Resolved Source Repository](https://github.com/CPsean/Product-Review-Panel-skill)
- [README](README.md)
- [Skill Definition](SKILL.md)
- [Disclaimer Template](references/templates/disclaimer.md)
- [Output Structure Template](references/templates/output-structure.md)
- [Information Gap Check Workflow](references/workflows/information-gap-check.md)
- [PRD Classification Workflow](references/workflows/prd-classification.md)
- [Verdict Logic Workflow](references/workflows/verdict-logic.md)
- [Chinese Panel Personas](references/personas/experts-cn.md)
- [International Panel Personas](references/personas/experts-intl.md)
- [The Closer Persona](references/personas/closer.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review transcript with structured intake, panel tendencies, final verdict, dissent, next steps, and failure signals.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill should always include its expert-perspective disclaimer and should treat verdicts as decision support rather than authoritative business decisions.]

## Skill Version(s):

1.0.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
