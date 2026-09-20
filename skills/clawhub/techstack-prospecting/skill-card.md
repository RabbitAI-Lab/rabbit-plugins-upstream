## Description:

Find and qualify company websites by their detected technologies using Crawlora's tech-stack dataset and live website checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sales operations teams, and developers use this skill to build or qualify account lists by matching public websites against required, alternative, and excluded web technologies. It supports technology-fit research and shortlisting, while preserving unknowns and treating detections as research signals rather than proof of budget, buying intent, or current deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prospecting inputs such as domains, URLs, filters, and live scrape or tech-stack checks are sent to Crawlora under the user's API key.

Mitigation: Install only when that data sharing is acceptable, keep the API key in the environment, and avoid submitting sensitive private URLs or confidential prospect notes.

Risk: Technology, brand, and website-fit data can be incomplete, stale, or directional, especially for private or backend-only tools and homepage-only live scans.

Mitigation: Treat results as research signals, preserve unknowns, compare dataset and live observations, and verify important qualification decisions with source evidence.

Risk: A generated prospect list does not itself authorize outreach or CRM writes.

Mitigation: Review exported lists against the user's outreach policy, consent requirements, and CRM governance before operational use.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/techstack-prospecting)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown table or CSV with supporting shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include domains, verified company identity when available, matching technologies, detection confidence and evidence, dataset or live-check freshness, fit rationale, source URLs, and preserved unknowns.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
