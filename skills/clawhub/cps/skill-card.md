## Description:

外卖红包 helps users request food-delivery coupon links in natural language and returns clickable offers for platforms such as 美团, 饿了么, and 京东外卖.

This skill is ready for commercial/non-commercial use.

## Publisher:

[onsoul](https://clawhub.ai/user/onsoul)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent for food-delivery coupon links, including broad requests for meal deals or platform-specific requests for 美团, 饿了么, or 京东外卖. The agent fetches available campaigns and returns a concise Markdown list of clickable coupon links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad food-related phrases may trigger this skill when a user wanted neutral restaurant recommendations or browsing.

Mitigation: Use the skill for explicit coupon-link requests; users who want neutral recommendations should say so clearly.

Risk: The skill depends on external promotional endpoints that may be rate-limited or temporarily unavailable.

Mitigation: Retry transient failures briefly, skip failed individual link conversions, and tell the user to try again later if no links are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/onsoul/skills/cps)
- [Fore.vip service](https://fore.vip)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Guidance]

**Output Format:** [Markdown list of clickable coupon links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns up to 20 coupon links and may skip individual campaign links when conversion requests fail.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
