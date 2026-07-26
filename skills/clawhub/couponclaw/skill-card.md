## Description: <br>
CouponClaw finds coupon codes, compares cashback stacking options, and calculates final checkout prices across China, the United States, the United Kingdom, Australia, Southeast Asia, and DTC brands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiajiaoy](https://clawhub.ai/user/jiajiaoy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping assistants use this skill to find current coupon codes, compare cashback portals, identify stackable savings, and prepare daily deal briefings before checkout. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Coupon and cashback recommendations depend on public shopping, coupon, and cashback pages that can be unavailable, expired, or changed by merchant terms. <br>
Mitigation: Browse the cited pages at run time, mark unavailable pages clearly, record expiry or stacking restrictions when available, and avoid fabricating coupon codes. <br>
Risk: Daily deal notifications create a recurring push subscription when the user explicitly enables them. <br>
Mitigation: Enable push only on explicit request, review subscription state with status or cron listing commands, and remove it with the off command when no longer needed. <br>


## Reference(s): <br>
- [CouponClaw ClawHub listing](https://clawhub.ai/jiajiaoy/skills/couponclaw) <br>
- [CouponClaw README](artifact/README.md) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown-style text with browser-navigation instructions, structured coupon and cashback summaries, and optional cron subscription messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No API keys are required; optional daily deal notifications use the OpenClaw cron runtime.] <br>

## Skill Version(s): <br>
1.1.8 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
