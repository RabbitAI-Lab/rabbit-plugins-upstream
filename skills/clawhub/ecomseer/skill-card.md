## Description:

EcomSeer is an AI-powered overseas customer acquisition platform by Beijing Miaozhisheng Technology, built for foreign trade and manufacturing companies. It streamlines the entire international customer development workflow—market intelligence, brand building, overseas promotion, inquiry qualification, and CRM—leveraging commercial databases, multilingual content, and smart outreach to help Chinese manufacturers connect with qualified global buyers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fly0pants](https://clawhub.ai/user/fly0pants)

### License/Terms of Use:

MIT-0

## Use Case:

External trade and manufacturing teams use EcomSeer to research TikTok Shop products, categories, shops, creators, videos, and advertising across supported markets. They can also request deeper market and competitor analyses for overseas promotion planning.

### Deployment Geography for Use:

Global; supported TikTok Shop markets include the US, UK, Indonesia, Thailand, Vietnam, Malaysia, the Philippines, and Singapore.

## Known Risks and Mitigations:

Risk: Routine requests can trigger remote research that forwards credentials and requires polling indefinitely without interruption.

Mitigation: Use a version that supports research cancellation and polling timeouts; review credential and context sharing plus report access and retention before submitting confidential business information.

## Reference(s):

- [EcomSeer website](https://www.ecomseer.com)
- [EcomSeer ClawHub release](https://clawhub.ai/fly0pants/skills/ecomseer)
- [Product search and rankings API reference](artifact/references/api-goods.md)
- [Product detail API reference](artifact/references/api-product-detail.md)
- [Influencer API reference](artifact/references/api-influencer.md)
- [Video API reference](artifact/references/api-video.md)
- [Shop API reference](artifact/references/api-shop.md)
- [Advertising and creative API reference](artifact/references/api-ad.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown summaries and tables, with links to hosted HTML research reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual English and Chinese responses; content varies by query and selected market.]

## Skill Version(s):

2.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
