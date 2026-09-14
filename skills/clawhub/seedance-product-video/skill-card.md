## Description:

Generates clean catalog-style e-commerce product videos from product photos or text descriptions using the Ofox video API, guiding the agent through brief collection, prompt drafting, cost estimation, submission, polling, download, and cost reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketplace sellers, and developers use this skill to turn product photos or product descriptions into listing-oriented showcase clips with simple studio backgrounds and camera motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are provided to Ofox through the skill workflow.

Mitigation: Use the skill only when the user trusts Ofox with those inputs and avoid sensitive product imagery or confidential prompt content.

Risk: Fallback dependency guidance may encourage broad or unpinned skill installation.

Mitigation: Install only the specific ofox-video-core dependency from a trusted or pinned source for the agent that needs it.

Risk: The artifact blurs its own boundary around people, presenters, and dialogue.

Mitigation: Route people, presenter, or dialogue requests to a more appropriate skill instead of using this product-video workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ofoxai/skills/seedance-product-video)
- [Ofox Publisher Profile](https://clawhub.ai/user/ofoxai)
- [Ofox Skill Homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-product-video)
- [Ofox API Keys](https://app.ofox.ai)
- [Ofox Models Catalog](https://api.ofox.ai/v1/models/catalog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, files]

**Output Format:** [Markdown guidance with brief recap, generated prompt, cost table, shell commands, and downloaded video path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, jq, and the ofox-video-core dependency.]

## Skill Version(s):

1.14.1 (source: frontmatter, release metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
