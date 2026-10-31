## Description:

Find real restaurants, cafes, bars, shops and cultural places in Mexican towns (menus, promotions, WhatsApp, live map) on BETAP (betap.world); propose new businesses and publish promotions with the owner's key. Use when your human asks where to eat, drink, shop or go in Mexico (Jalisco and beyond), wants their business on a live map, or wants their promotions published. No key needed to search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xavierabraham](https://clawhub.ai/user/xavierabraham)

### License/Terms of Use:

MIT-0

## Use Case:

People planning where to eat, drink, shop, or visit in Mexico can find local businesses and cultural places through BETAP and get concise options with public pages. With the appropriate key and authorization, an agent can propose a real business for review or publish and manage promotions requested by that business's owner.

### Deployment Geography for Use:

Mexico

## Known Risks and Mitigations:

Risk: BETAP logs search terms and the agent name, and business proposals may include operator contact details or an owner's email.

Mitigation: Avoid personal details in search terms; share operator contact details and owner email only when the user chooses to provide them.

Risk: Agent and business keys grant access to proposals or owner-authorized promotion changes.

Mitigation: Keep keys secret, use a business key only for promotions the owner requested, and confirm the live promotion details with the user.

Risk: Unverified business details or offers could mislead people.

Mitigation: Propose only real businesses with a public source, do not invent businesses or offers, and report when no nearby results are found.

## Reference(s):

- [BETAP homepage](https://betap.world/en)
- [BETAP English agent documentation](https://betap.world/llms-en.txt)
- [BETAP businesses by city](https://betap.world/negocios)
- [BETAP ClawHub release](https://clawhub.ai/xavierabraham/skills/betap)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language recommendations and explanations based on BETAP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include business names, categories, public page links, current promotions, and instructions for proposing businesses or managing owner-authorized promotions.]

## Skill Version(s):

1.1.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
