## Description:

Fetches any company's job openings straight from its Applicant Tracking System (ATS) via the Crawlora API, covering Greenhouse, Lever, Workday, Ashby, SmartRecruiters, Workable, Personio, Recruitee, iCIMS, Oracle Recruiting, Rippling, Pinpoint, Eightfold, Gem, UKG, and Teamtailor, and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, analysts, and agents use this skill to pull public ATS-hosted job boards, individual posting details, and hiring-velocity snapshots when they know or can resolve a company's ATS platform and board slug.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ATS slugs, company domains, job IDs, filters, and the Crawlora API key to Crawlora.

Mitigation: Use it only for public job-board research and avoid confidential target lists, internal identifiers, secrets, or private context in requests.

Risk: The helper has POST-capable behavior that can carry user-supplied JSON bodies.

Mitigation: Keep requests within the documented job-board endpoints and review POST bodies before execution.

Risk: API keys could be exposed if copied into prompts, command arguments, committed files, or request payloads.

Mitigation: Set CRAWLORA_API_KEY in the environment and keep it out of prompts, source files, query parameters, and JSON bodies.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/ats-job-boards-research)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and public ATS platform identifiers such as company slugs, job IDs, tenant details, or domains.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
