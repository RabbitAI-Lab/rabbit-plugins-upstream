## Description:

Build a requirements-based software shortlist using Crawlora product discovery, public vendor pages, and review samples to compare vendors against must-haves, pricing assumptions, integration needs, and demo questions before a buying decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Business buyers, procurement teams, and software evaluators use this skill to turn requirements into an evidence-backed vendor matrix, shortlist, pricing comparison, and demo or trial checklist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, scrape URLs, and the Crawlora API key are sent to Crawlora during vendor research.

Mitigation: Avoid confidential budgets, internal architecture, credentials, and non-public procurement details in queries or scrape targets unless sharing them with Crawlora is acceptable.

Risk: Vendor pages, search results, and review samples can be incomplete, stale, or weakly matched to the buyer's requirements.

Mitigation: Preserve sources and collection dates, distinguish claims from inferences, treat unknown requirements as conditional, and validate decisive items in a demo or trial.

## Reference(s):

- [software-vendor-shortlisting endpoint reference](artifact/reference/endpoints.md)
- [Crawlora service](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/software-vendor-shortlisting)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with requirement matrices, shortlist rationale, pricing scenarios, source notes, and demo or trial checklist items.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source URLs, collection dates when available, evidence type labels, unresolved questions, and conditional or rejected candidate reasons.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
