## Description:

Builds a requirements-based software shortlist using Crawlora discovery, public vendor pages, and review samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Buyers and procurement teams use this skill to compare software vendors against their requirements, pricing assumptions, integrations, and implementation questions before a purchase decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vendor queries, product identifiers, and target URLs are sent to Crawlora along with an API key.

Mitigation: Only send approved public research inputs; exclude secrets, internal-only URLs, confidential requirements, and procurement-sensitive details unless authorized, and keep the API key out of logs and shared output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/software-vendor-shortlisting)
- [Crawlora](https://crawlora.net)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown requirements matrix, shortlist, pricing scenarios, and demo checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, collection dates, evidence gaps, and conditional recommendations.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
