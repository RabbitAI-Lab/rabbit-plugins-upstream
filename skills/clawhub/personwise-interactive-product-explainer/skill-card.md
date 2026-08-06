## Description:

Create a source-grounded interactive digital-human SaaS or software product explainer that website visitors can question and embed through PersonWise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Product, marketing, and go-to-market teams use this skill to turn verified product materials into private-by-default, askable PersonWise explainers for product launches, product pages, help centers, and sales follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update the PersonWise CLI.

Mitigation: Install or update only after explicit user approval, and use the bundled bootstrap flow that checks release size and hashes before changing the executable.

Risk: The workflow uses browser OAuth and depends on the PersonWise service.

Mitigation: Use the browser authorization flow and never request or handle passwords, OTPs, tokens, cookies, callback URLs, or other secrets.

Risk: Creating an explainer uploads selected product materials and consumes one existing PersonWise course credit.

Mitigation: Upload only user-selected or explicitly authorized materials, read creation readiness before designing, and stop if the account is blocked.

Risk: Unsupported product claims or invented interface details could make the explainer misleading.

Mitigation: Build a claim ledger from current authoritative sources, audit outline and script content against it, and use supplied screenshots directly or factual editorial visuals.

## Reference(s):

- [Product Grounding](references/product-grounding.md)
- [Workflow](references/workflow.md)
- [ClawHub Skill Listing](https://clawhub.ai/personwiseai/skills/personwise-interactive-product-explainer)
- [PersonWise Publisher Profile](https://clawhub.ai/user/personwiseai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command inputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a claim ledger, run and project IDs, source status, review status, final access URL when playable, and omitted or qualified claims.]

## Skill Version(s):

2.1.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
