## Description:

Linkfox OS routes cross-border e-commerce prompts to LinkFox agents for marketplace data queries, market analysis, product selection, listing optimization, media generation, compliance checks, sourcing, and related workflow automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and their agents use this skill to submit one-shot LinkFox tasks for product research, market analysis, listing work, product media generation, compliance checks, sourcing, and cross-platform analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task prompts, uploaded files, and generated outputs are sent to LinkFox.

Mitigation: Avoid secrets and sensitive personal data in prompts or uploads, and use the skill only when this data sharing is acceptable.

Risk: The skill can guide phone/SMS login and API key handling.

Mitigation: Prefer creating the API key directly on LinkFox, do not share SMS codes in chat, and store API keys only in the expected environment variable.

Risk: The onboarding flow can list plans, create billing orders, and generate payment QR codes.

Mitigation: Review plan, price, account, and order details before any payment or purchase action.

Risk: Result files and share links can expose generated outputs or uploaded-resource links.

Mitigation: Protect or clean .linkfox-os output folders on shared machines and share public task links only with intended recipients.

## Reference(s):

- [LinkFox OS homepage](https://os.linkfox.com/)
- [ClawHub listing](https://clawhub.ai/linkfox-ai/skills/linkfox-os)
- [Agent capabilities reference](references/capabilities.md)
- [Linkfox OS API reference](references/api.md)
- [LinkFox account and environment onboarding](references/onboarding.md)
- [Onboarding API contract](references/onboarding-api.md)
- [Amazon ecosystem skills](references/skills-amazon.md)
- [Market analysis skills](references/skills-market-analysis.md)
- [Product selection skills](references/skills-selection.md)
- [Listing skills](references/skills-listing.md)
- [Media generation skills](references/skills-media.md)
- [IP and compliance skills](references/skills-ip-compliance.md)
- [Third-party platform skills](references/skills-third-platforms.md)
- [General tool skills](references/skills-tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown progress and result text, JSON status objects, shell commands, and local or downloaded result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tasks are asynchronous, require LINKFOXAGENT_API_KEY, and can save results under .linkfox-os in the current workspace.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
