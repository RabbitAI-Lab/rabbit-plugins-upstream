## Description:

Researches Douyin e-commerce products from a user's category, budget, and filters, returning candidate products, selection reasons, and questions to verify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users researching Douyin e-commerce products use the skill to screen candidates by category, budget, and stated filters, then review visible product details and follow-up questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI package is fetched and run without a pinned version, creating a supply-chain risk.

Mitigation: Review the package installation approach before use and prefer an approved pinned version where available.

Risk: Search terms or product identifiers may be sent to SocialDataX.

Mitigation: Avoid confidential search terms and identifiers, and consider whether sending the inputs to SocialDataX is acceptable.

## Reference(s):

- [SocialDataX AI and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-product-research)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown table with candidate products, matching criteria, visible details, selection reasons, and questions to verify]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Starts with one result page, shows up to five candidates, and reviews two to three relevant product details; findings are a preliminary screen, not sales or profit estimates.]

## Skill Version(s):

0.1.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
