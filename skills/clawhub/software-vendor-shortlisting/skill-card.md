## Description:

Build a requirements-based software shortlist using Crawlora product discovery, public vendor pages, and review samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External buyers, procurement teams, and developers use this skill to compare software vendors against must-have requirements, pricing assumptions, integrations, public evidence, and demo or trial questions before a buying decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product names, URLs, queries, and business requirements used in API calls are shared with Crawlora.

Mitigation: Keep secrets, sensitive procurement details, and private documents out of requests unless sharing them with Crawlora is approved.

Risk: Public vendor pages, marketplace profiles, and small review samples can be incomplete, stale, or insufficient for a final buying decision.

Mitigation: Preserve source URLs and collection dates, separate claims from inferences, flag unknowns, and verify critical requirements during a demo or trial.

Risk: Pricing and integration claims can vary by edition, region, billing interval, or plan restriction.

Mitigation: Compare vendors on the same pricing basis and verify workflow-level integration behavior before ranking a vendor as fully supported.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/software-vendor-shortlisting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with requirements matrices, vendor rankings, price scenarios, source notes, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source URLs, collection dates, evidence types, unresolved questions, and demo or trial checklist items when available.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
