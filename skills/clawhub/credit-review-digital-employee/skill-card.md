## Description:

Provides reference workflows for credit eligibility checks, risk planning, case intake, collateral and related-party review, pre-lending analysis, and draft review memoranda.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Credit review staff use the skill to structure preliminary reviews, organize evidence and follow-up tasks, and prepare draft review notes. Its outputs are reference material for qualified human review and do not make credit decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credit review guidance or draft assessments could be inaccurate or become outdated, affecting high-impact lending decisions.

Mitigation: Use outputs as drafts only; check current official and institutional criteria and source records, and have an authorized qualified reviewer make every final decision.

Risk: Customer, identity, credit, or account data may be sensitive.

Mitigation: Minimize and de-identify inputs, use authorized minimum-privilege institutional systems for checks, and obtain human confirmation before queries or sharing.

Risk: Security inspection was incomplete, including a degraded tool-misuse check and unresolved local references.

Mitigation: Treat the benign scanner result as limited assurance and manually review the skill and referenced materials before installation or use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/gechengling/skills/credit-review-digital-employee)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON]

**Output Format:** [Reference guidance with Markdown checklists and tables, plus illustrative JSON structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts and illustrative examples require qualified human review; the skill does not execute institutional checks or make approval decisions.]

## Skill Version(s):

2.0.10 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
