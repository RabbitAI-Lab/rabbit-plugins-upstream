## Description:

Fetches any company's job openings straight from its Applicant Tracking System (ATS) via the Crawlora API, returning clean JSON for board listings, job details, and hiring-velocity snapshots when the ATS platform and company or board slug are known.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to fetch public ATS-hosted job-board data, individual posting details, and hiring-signal snapshots through the Crawlora API for a specified employer and ATS slug.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send CRAWLORA_API_KEY to a host selected through CRAWLORA_API_BASE.

Mitigation: Avoid setting CRAWLORA_API_BASE and review the target URL before running helper commands.

Risk: The helper is broader than the stated ATS job-board purpose and is not technically restricted to ATS endpoints.

Mitigation: Review proposed paths and commands before execution, and use a limited Crawlora key if available.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ats-job-boards-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; board/list endpoints may be paginated and should be walked for complete results.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
