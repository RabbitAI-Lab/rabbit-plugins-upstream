## Description:

Fetches a company's public ATS-hosted job openings through the Crawlora API across Greenhouse, Lever, Workday, Ashby, SmartRecruiters, Workable, Personio, Recruitee, iCIMS, Oracle Recruiting, Rippling, Pinpoint, Eightfold, Gem, UKG, and Teamtailor, returning normalized JSON for boards, job details, and hiring-velocity snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external researchers, recruiters, and developers use this skill to retrieve public ATS job boards, individual posting details, and hiring-velocity snapshots when they know or can resolve the company's ATS platform and board slug.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call Crawlora API endpoints beyond the documented ATS job-board use case, including arbitrary methods and request bodies.

Mitigation: Review or constrain scripts/crawlora.sh to the documented /jobs endpoints and read-only GET requests before installing in a restricted environment.

Risk: The skill relies on a Crawlora API key stored in the CRAWLORA_API_KEY environment variable.

Mitigation: Keep the key in environment or secret storage only, avoid query-string or committed secrets, and scope agent access to the key where possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/ats-job-boards-research)
- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; most board and list results are paginated and should be walked for complete pulls.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
