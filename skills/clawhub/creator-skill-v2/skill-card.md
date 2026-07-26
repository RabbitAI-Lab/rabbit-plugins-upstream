## Description: <br>
Creator Skill V2 supports standalone influencer search on TikTok, Instagram, and YouTube through skill.deinai.ai, including account onboarding, Stripe subscription, sk_live_ token setup, and MCP search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deinai](https://clawhub.ai/user/deinai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to onboard a skill.deinai.ai account, configure OpenClaw MCP with an API token, and search TikTok, Instagram, or YouTube influencers by query and filters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help start a real Stripe subscription flow. <br>
Mitigation: Require explicit user confirmation before checkout or payment, use only Stripe-hosted checkout, and do not let the agent handle raw card data. <br>
Risk: The skill can create and configure a long-lived sk_live_ API token for MCP use. <br>
Mitigation: Store tokens only as revocable secrets; never place real tokens in skill files, logs, screenshots, or shared prompts. <br>
Risk: Account onboarding, token creation, order polling, and MCP configuration may proceed without clear consent boundaries. <br>
Mitigation: Require explicit confirmation before each account, payment, token, polling, or MCP configuration action, and stop if payment is pending or canSearch is false. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deinai/skills/creator-skill-v2) <br>
- [SkillHub SKILL.md](https://skill.deinai.ai/portal/docs/creator-skill-v2/SKILL.md) <br>
- [Online file index](https://clawhub.ai/api/v1/skills/creator-skill-v2/file?path=references/online-read.md) <br>
- [Installation and authentication](https://clawhub.ai/api/v1/skills/creator-skill-v2/file?path=references/install.md) <br>
- [OpenClaw onboarding](https://clawhub.ai/api/v1/skills/creator-skill-v2/file?path=references/onboarding.md) <br>
- [Stripe payment automation](https://clawhub.ai/api/v1/skills/creator-skill-v2/file?path=references/stripe-payment-automation.md) <br>
- [MCP tools](https://clawhub.ai/api/v1/skills/creator-skill-v2/file?path=references/tools.md) <br>
- [Error handling](https://clawhub.ai/api/v1/skills/creator-skill-v2/file?path=references/errors.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with inline shell, HTTP, YAML, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes MCP setup guidance, account onboarding steps, token handling notes, and influencer search parameters.] <br>

## Skill Version(s): <br>
2.0.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
