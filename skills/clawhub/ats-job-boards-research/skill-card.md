## Description:

Fetches a company's public ATS-hosted job openings and job-detail data through the Crawlora API, returning normalized JSON for supported platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, analysts, and agents use this skill to retrieve public ATS job board listings, single posting details, and hiring-velocity snapshots for companies when the ATS platform and board slug are known or resolvable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to Crawlora as an external API provider.

Mitigation: Install and use it only if Crawlora is an acceptable external provider for the intended workflow.

Risk: The Crawlora API key could be exposed if users place it in command-line arguments, source files, or logs.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode, commit, or pass it as a query parameter.

Risk: Queries may include sensitive or internal-only company research details.

Mitigation: Avoid placing sensitive or internal-only company information in request parameters.

Risk: Returned job data remains subject to the source job board's terms and may require pagination for a complete pull.

Mitigation: Respect source terms and walk paginated board endpoints when completeness matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/ats-job-boards-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET endpoints for public ATS job board data.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
