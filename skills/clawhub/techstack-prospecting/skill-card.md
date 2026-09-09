## Description:

Find and qualify company websites by their detected technologies using Crawlora's tech-stack dataset and live website checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, partnerships, and developer-relations teams use this skill to build or qualify account lists by matching public websites against detected technology profiles and live website checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can expose the Crawlora API key if an untrusted API base override is used.

Mitigation: Keep CRAWLORA_API_BASE unset unless the endpoint is fully controlled and trusted; use a limited Crawlora key and rotate it if the helper was run with an unexpected API base.

Risk: Prospecting results may overstate certainty because detected software does not prove business fit, purchase intent, or current installation status.

Mitigation: Use public, non-sensitive domains or URLs, verify shortlisted candidates with live checks, preserve unknowns, and clearly label discrepancies between stored and live observations.

## Reference(s):

- [Techstack endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/techstack-prospecting)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables or CSV-style results with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results preserve unknowns and include domains, detected technologies, confidence or evidence, freshness timestamps, live-check status, fit rationale, and source URLs when available.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
