## Description:

Retrieves Amazon policy and regulatory update lists for sellers by marketplace and date range, then fetches full Markdown article bodies by record ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and their supporting agents use this skill to monitor official Amazon policy, compliance, fee, FBA, and marketplace rule updates across supported sites and open full source articles when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys and session metadata.

Mitigation: Install only when the user trusts LinkFox, keep API keys in environment variables, and avoid sharing saved outputs or logs that may contain account context.

Risk: Gateway override environment variables can redirect requests away from the default LinkFox endpoints.

Mitigation: Avoid setting gateway override variables unless the endpoint is controlled and intentionally approved.

Risk: The onboarding flow can involve phone-based login plus plan, order, and payment data.

Mitigation: Prefer self-service account and payment setup where practical, and review plan and order details before running onboarding commands.

Risk: The scripts write full API responses and cache files into the current working directory.

Mitigation: Review the generated linkfox data directory, manage file retention, and avoid running the skill from a directory where saved response data is inappropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-policy-feed)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown article bodies, JSON API responses, tabular text summaries, and local JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [List calls return titles, AI-generated Chinese summaries, original URLs, publish times, and token cost metadata; detail calls return full Markdown bodies. Scripts use a 24-hour local cache and write full responses under the current working directory.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
