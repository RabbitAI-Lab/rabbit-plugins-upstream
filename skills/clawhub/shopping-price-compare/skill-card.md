## Description:

省柴柴·全平台商品比价助手 helps users compare prices across Taobao, JD, Pinduoduo, Douyin, Kuaishou, Vipshop, and other shopping platforms, find purchase links, set recurring reminders for consumables, and use saved shopping preferences when judging whether products are worth buying.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marywbrown](https://clawhub.ai/user/marywbrown)

### License/Terms of Use:

MIT-0

## Use Case:

External shoppers use this skill to compare product prices and purchase links across major Chinese shopping platforms, summarize options in a recommendation-friendly format, and maintain recurring purchase reminders for consumable goods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the skill sends shopping searches to remote services and creates or reuses a proxy token.

Mitigation: Review the skill before installation, remove bundled token files, and only run it in an environment where outbound shopping-service requests are acceptable.

Risk: Returned purchase links may be affiliate or tracked links.

Mitigation: Disclose link-tracking behavior to users and verify destination URLs before using recommendations for purchasing decisions.

Risk: The skill stores shopping preferences, reminders, and learning history locally.

Mitigation: Inspect and clear local preference, log, reminder, and token files before sharing, packaging, or installing the skill for another user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/marywbrown/skills/shopping-price-compare)
- [Node.js runtime](https://nodejs.org/)
- [README](artifact/README.md)
- [User preference and persistence notes](artifact/references/user-profile.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown recommendations with product links, prices, comparison tables, and brief purchase guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices and availability are time-sensitive; output may include tracked or affiliate purchase links.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
