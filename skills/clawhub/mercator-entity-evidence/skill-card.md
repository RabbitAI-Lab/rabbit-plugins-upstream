## Description:

MERCATOR Entity Evidence enriches a company domain or name with evidenced company facts, returning source URLs, verbatim excerpts, retrieval timestamps, confidence, and source agreement while surfacing conflicts and UNKNOWN fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arzuo](https://clawhub.ai/user/arzuo)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to verify or enrich company identity facts for a domain or name while retaining source evidence for review. It is suited to workflows that need sourced legal names, headquarters, founding year, employee counts, executives, funding, industry, or primary-domain information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid calls spend the user's own wallet funds through an x402 payment header.

Mitigation: Use the free validation route first and only send X_PAYMENT for intentional paid requests.

Risk: Payment headers could be exposed or sent to an untrusted endpoint if environment values are logged or redirected.

Mitigation: Do not log X_PAYMENT values, and keep MERCATOR_BASE_URL on the documented service endpoint unless another endpoint is intentionally trusted.

Risk: Open-web evidence can be incomplete, conflicting, or wrong even when an excerpt is present on the cited page.

Mitigation: Review returned source URLs and treat UNKNOWN or conflicting fields as unresolved rather than final facts.

## Reference(s):

- [MERCATOR Entity Evidence service homepage](https://mercator-entity-evidence.fly.dev)
- [ClawHub skill page](https://clawhub.ai/arzuo/skills/mercator-entity-evidence)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with bash examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and jq; the paid route requires an externally supplied X_PAYMENT x402 header.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
