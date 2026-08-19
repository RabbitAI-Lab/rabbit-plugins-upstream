## Description:

Expands a seed keyword into related Amazon keywords with search volume, trend, PPC bid, ranking difficulty, and competition metrics across 10 supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and marketplace analysts use this skill to expand Amazon seed keywords into related keyword sets with search demand, trend, PPC bid, and competition metrics. It supports keyword discovery, long-tail research, PPC planning, and competition screening for supported Amazon marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes account setup, payment, API-key, and automatic feedback flows in addition to keyword research.

Mitigation: Install only when comfortable with LinkFox handling keyword queries, credentials, SMS onboarding data, optional billing actions, and feedback content; review sensitive prompt, business, or customer data before feedback submission.

Risk: Keyword requests consume LinkFox credits and the skill describes dynamic billing behavior.

Mitigation: Confirm user intent before calls that may consume credits, and avoid automatic retries, broader searches, or pagination after failures or empty results.

Risk: The skill saves complete API responses and cache files under the working directory.

Mitigation: Review saved JSON files for sensitive marketplace or business data and manage workspace retention and access accordingly.

## Reference(s):

- [Jungle Scout Keyword API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-by-keyword)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown tables and summaries, JSON API responses, and saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes complete responses under ./linkfox/<date>/<session>/data and uses a 24-hour local cache; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
