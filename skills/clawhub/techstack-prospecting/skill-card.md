## Description:

Find and qualify company websites by their detected technologies using Crawlora's tech-stack dataset and live website checks. Use for technology-based account lists, integration targeting, or qualifying an existing domain list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, sales engineers, and go-to-market teams use this skill to find or qualify company websites by detected web technologies, then verify shortlisted candidates with Crawlora dataset and live website checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the Crawlora API key and requested domains, URLs, filters, and request bodies to Crawlora.

Mitigation: Keep CRAWLORA_API_KEY in the environment, use the skill only for intended Crawlora workflows, and avoid private or sensitive URLs unless appropriate.

Risk: Live checks can submit more targets than needed and consume external API capacity.

Mitigation: Bound live checks to a shortlist, back off on 429 responses, retry transient 5xx responses once, and stop on 401 or 403 responses.

Risk: Stored technology detections and corpus counts can be incomplete or stale and do not prove buying intent, company geography, or absence of a technology.

Mitigation: Preserve unknowns, include detection freshness and live-check status, label dataset versus live discrepancies, and avoid inferring geography from TLD alone.

## Reference(s):

- [techstack-prospecting endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown table or CSV with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes domain, verified company identity when available, matching technologies, detection confidence and evidence, freshness or live-check status, fit rationale, and source URLs.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
