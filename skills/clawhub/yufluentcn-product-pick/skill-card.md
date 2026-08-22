## Description:

选品分析 helps agents analyze Amazon, TikTok Shop, and AliExpress product candidates using BSR, sales signals, pricing, reviews, margin, competition, and IP-risk signals through Yufluent's cloud product-pick service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[metahuan](https://clawhub.ai/user/metahuan)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, sourcing teams, and agents use this skill to turn browser-extracted, pasted, or authorized API product data into go, watch, or no-go product-selection guidance. It is intended for product research, inventory planning, blue-ocean screening, and competition or IP-risk review before procurement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product candidate data, search terms, and browser-extracted market data are sent to Yufluent's cloud service.

Mitigation: Use the skill only when that data sharing is acceptable for the workflow and account.

Risk: Browser-based discovery depends on the configured Browser Service and the pages it can access.

Mitigation: Keep BROWSER_SERVICE_URL pointed at a trusted local or managed Browser Service and use authorized pages or approved data exports.

Risk: The skill depends on the requests package for network calls.

Mitigation: Pin or constrain the requests dependency before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/metahuan/skills/yufluentcn-product-pick)
- [Yufluent Product Pick homepage](https://www.changzhiai.com/skills/product-pick)
- [Yufluent API console](https://claw.changzhiai.com)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Formatted text or JSON product research report with CLI metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include blue_ocean_score, competition_score, ip_risk, capital_impact, and verdict fields from the Yufluent product-pick API.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
