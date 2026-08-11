## Description:

Cross-cultural product scouting skill for e-commerce teams that generates culturally grounded consumer product ideas, expands sourcing and shopping keywords, and guides demand and competition validation with Amazon, Google Trends, Alexa, and 1688-oriented workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External product developers, cross-border sellers, brand founders, and research teams use this skill to identify culturally distinctive products for a target market, generate sourcing and voice-search prompts, and decide which ideas deserve further validation. The workflow is designed for guided product ideation followed by step-by-step demand, seasonality, and competition checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real LinkFox credentials, login flows, billing access, or private product-research prompts may be used during validation workflows.

Mitigation: Review credential handling before installation, use least-privilege access, and keep sensitive prompts or customer data out of validation runs unless sharing is approved.

Risk: Custom LINKFOX_* gateway or API URL settings can send requests to an untrusted destination.

Mitigation: Use trusted default endpoints unless the alternate destination has been reviewed and approved.

Risk: Feedback reporting and public file uploads can share research artifacts outside the local workspace.

Mitigation: Remove credentials, private customer data, and sensitive product strategy details before reporting feedback or creating public upload links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-cross-cultural-product-scout)
- [Cross-cultural product selection skill definition](artifact/skills/cross-cultural-product-selection/SKILL.md)
- [Chart templates for Amazon competition reports](artifact/skills/cross-cultural-product-selection/references/chart-templates.md)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML reports, guidance, shell commands]

**Output Format:** [Markdown-style product research guidance with optional JSON data files and HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs match the user's language when possible and pause for user confirmation before running validation steps.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
