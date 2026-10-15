## Description:

Find and qualify company websites by their detected technologies using Crawlora's tech-stack dataset and live website checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business development teams use this skill to find or qualify public company websites by detected technologies and verify promising prospects before compiling an account list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public domains, URLs, and search filters are sent to Crawlora in API-key-authenticated requests.

Mitigation: Confirm third-party sharing is acceptable; do not submit confidential internal hosts or sensitive proprietary lists.

Risk: A missing or stale technology detection can lead to incorrect prospect qualification.

Mitigation: Check detection evidence and freshness, refresh shortlisted sites when appropriate, and label uncertainty or discrepancies between stored and live results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/techstack-prospecting)
- [Crawlora](https://crawlora.net)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Table or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes domains, technology evidence, freshness and live-check status, fit rationale, and source URLs; unknowns remain explicit.]

## Skill Version(s):

1.0.11 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
