## Description:

Fetches any company's job openings straight from its Applicant Tracking System (ATS) via the Crawlora API, returning clean JSON for board listings, single job details, and hiring-velocity snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and recruiting researchers use this skill to retrieve public ATS-hosted job postings, inspect single postings, resolve supported ATS board slugs, and summarize hiring signals for a company.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public job-board lookup parameters and the Crawlora API key to Crawlora.

Mitigation: Keep CRAWLORA_API_KEY private and scoped, and install only when that data sharing is acceptable.

Risk: Implicit curl configuration loading can alter request behavior in some environments.

Mitigation: Prefer a helper version that disables implicit curl configuration loading with curl -q or --disable before other curl arguments.

Risk: Incomplete pagination or incorrect ATS slug parameters can produce partial or empty job-board results.

Mitigation: Use the documented endpoint parameters, resolve slugs with company-search when supported, and walk pagination for complete board pulls.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/ats-job-boards-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, API Calls]

**Output Format:** [Markdown guidance with shell commands that return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and supported ATS provider slug parameters.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
