## Description:

Main entry point for the LJH product-launch toolkit, routing ecommerce product-launch questions before a task, recommending next steps after a task, and guiding users through the full launch chain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and product-launch teams use this skill to route product, content, creator, paid-media, and unit-economics questions to the appropriate LJH workflow. In guided mode, it helps move through the full product-launch chain from product selection to profitability review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route directly into linked LJH workflows, which may continue a business process beyond the initial router response.

Mitigation: Install only when this routing behavior is desired, and review the selected workflow before acting on its recommendations.

Risk: Guided mode can save product, pricing, campaign, creator, and launch conclusions in local dossier files.

Mitigation: Before guided mode, decide whether the dossier is acceptable; if the information is sensitive, explicitly decline dossier creation and review or delete any generated notes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomeng/skills/ljh)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Markdown or plain text routing guidance with next-step recommendations; guided mode may create local Markdown dossier files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to linked LJH workflows and may persist onboarding or product-launch dossier notes when the user permits local files.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
