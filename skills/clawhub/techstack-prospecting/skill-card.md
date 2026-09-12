## Description:

Find and qualify company websites by their detected technologies using Crawlora's tech-stack dataset and live website checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, growth teams, and sales operations teams use this skill to build or qualify technology-based account lists from Crawlora dataset searches and live website checks. It supports prospect shortlisting, integration targeting, and domain-list qualification while preserving uncertainty about company fit and outreach permission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prospecting queries, selected domains or URLs, live-check request bodies, and the Crawlora API key are sent to Crawlora.

Mitigation: Install only when that data sharing is acceptable, keep the API key in the environment, and scope live checks to user-approved shortlists.

Risk: Detected technologies and absence filters can be incomplete or stale, especially when tools are private, backend-only, or missed by a homepage-only live check.

Mitigation: Label dataset-only and live observations separately, preserve unknowns, include freshness fields when available, and avoid treating absence as proof.

Risk: A generated prospect list could be mistaken for permission to contact companies or write to a CRM.

Mitigation: Treat exports as research outputs only until the user confirms outreach policy, consent requirements, and any CRM write criteria.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/techstack-prospecting)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Text]

**Output Format:** [Markdown tables or CSV with supporting shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes domains, verified company identity when available, matching technologies, detection confidence and evidence, dataset freshness, live-check status, fit rationale, and source URLs.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
