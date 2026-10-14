## Description:

Helps agents search Chinese procurement notices and company records and prepare evidence-based market briefings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement analysts use this skill to find Chinese bid opportunities, review company bidding activity, and summarize purchasing and supplier trends from the ZLBX API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to an external procurement API and handles an API key that may be stored locally.

Mitigation: Provide your own key through the environment if preferred, and review where the key is stored before use.

Risk: Without an existing key, trial account creation uses a hashed MAC-derived device identifier.

Mitigation: Require informed consent before registration; use the manual sign-up option if device-based registration is unwanted.

Risk: Account telemetry and credit-consuming data lookups can accompany use of the service.

Mitigation: Review the service's data-sharing and credit terms, and request only the lookups needed for the task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/authoritative-bid-policy-guide-yuanbowang)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with links to procurement notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries identify search filters and distinguish returned records from unverified inferences.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
