## Description:

Build a requirements-based software shortlist using Crawlora product discovery, public vendor pages, and review samples. Use to compare vendors against must-haves, pricing assumptions, integration needs, and demo questions before a buying decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external consultants, and buying teams use this skill to compare software vendors against business requirements, pricing assumptions, integrations, and demo questions before a buying decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vendor research may disclose confidential internal requirements, private URLs, or sensitive business details to a third-party service.

Mitigation: Use only requirements and URLs approved for external disclosure, and avoid sending sensitive business details unless that disclosure is acceptable.

Risk: Crawlora API calls use account credentials and can consume the user's credit budget.

Mitigation: Set CRAWLORA_API_KEY only in trusted environments, keep searches within the intended scope and credit budget, and stop or back off on authentication and rate-limit errors.

Risk: Public vendor pages and review samples can be incomplete, stale, or non-representative.

Mitigation: Preserve source URLs and collection dates, distinguish claims from observations and inferences, and treat unresolved requirements as conditional until verified in a demo or trial.

## Reference(s):

- [Skill page](https://clawhub.ai/crawlora-org/skills/software-vendor-shortlisting)
- [Crawlora profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with requirements matrices, shortlist rationale, price scenarios, and demo checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source URLs, collection dates, unresolved questions, and separated claims, observations, and inferences.]

## Skill Version(s):

1.0.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
