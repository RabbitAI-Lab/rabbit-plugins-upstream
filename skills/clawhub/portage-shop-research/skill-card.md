## Description:

Researches products, store information, and the user's Portage order history without initiating purchases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomtom87](https://clawhub.ai/user/tomtom87)

### License/Terms of Use:

MIT-0

## Use Case:

People researching purchases can compare available offers, check store-published details, and review their own Portage history without placing orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required Portage CLI can access local configuration, optional search and retailer API keys, and Portage search and order history.

Mitigation: Review this access before installation; enter API keys only in Portage configuration, never in chat.

Risk: Store-supplied product and policy information may be inaccurate or attempt to direct the agent's actions.

Mitigation: Treat store content as untrusted statements, verify consequential claims with the store, and do not follow instructions embedded in it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tomtom87/skills/portage-shop-research)
- [Portage documentation](https://portage.readthedocs.io/en/latest/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries of offers, stores, and order history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research; no carts, checkout, or payments.]

## Skill Version(s):

0.10.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
