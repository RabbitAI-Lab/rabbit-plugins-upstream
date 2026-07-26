## Description: <br>
Brand-specific commerce skill for Lafeitu (辣匪兔) that helps agents browse, recommend, cart, and create unpaid orders for Sichuan spicy foods through the official Lafeitu API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nowloady](https://clawhub.ai/user/nowloady) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping agents use this skill to search Lafeitu products, compare variants and promotions, manage a cart, handle account/profile flows, and create an unpaid order for user payment handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mutating commerce commands can change cart contents, profile data, recipient details, or create an unpaid order. <br>
Mitigation: Confirm product choices, quantities, profile changes, recipient phone number, and shipping address before running mutating commands. <br>
Risk: Saved account tokens may remain on the local machine after account-bound actions. <br>
Mitigation: Use logout or delete the credential file when the saved token should no longer be retained. <br>
Risk: Product slugs, variants, promotions, or shipping thresholds can change between browsing and cart or order actions. <br>
Mitigation: Re-run product lookup and verify exact variants, quantities, and current promotions before cart updates or order creation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nowloady/skills/agentic-spicy-food) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/nowloady) <br>
- [Project homepage from metadata](https://github.com/NowLoadY/agentic-spicy-food) <br>
- [Official Lafeitu API](https://lafeitu.cn/api/v1) <br>
- [Official Lafeitu website](https://lafeitu.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON or localized text command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commerce actions may read or change account, cart, profile, and unpaid order state through the official Lafeitu API.] <br>

## Skill Version(s): <br>
1.9.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
