## Description:

Build a requirements-based software shortlist using Crawlora product discovery, public vendor pages, and review samples. Use to compare vendors against must-haves, pricing assumptions, integration needs, and demo questions before a buying decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to evaluate software vendors against buyer-specific requirements, compare evidence quality, build pricing scenarios, and prepare demo or trial questions before a purchasing decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can send a Crawlora API key and user-controlled requests more broadly than the skill description clearly scopes.

Mitigation: Run the skill only in a trusted environment, keep CRAWLORA_API_BASE unset or set to the intended Crawlora API URL, and bound requests by the user's scope and credit budget.

Risk: Vendor requirements, internal URLs, credentials, or proprietary evaluation data may be sent to Crawlora if included in requests.

Mitigation: Do not pass confidential requirements, credentials, internal URLs, or proprietary evaluation data unless sharing that information with Crawlora has been approved.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with tables, sourced findings, pricing scenarios, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source URLs, collection dates, unresolved questions, and separated claims, review observations, and inferences.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
