## Description:

Searches Google's public careers site (careers.google.com) via the Crawlora API and pulls single job postings by id, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, analysts, and agents use this skill to search public Google Careers postings by role and location, retrieve detailed postings by numeric job id, and track public posting changes over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to an overrideable API base.

Mitigation: Use the default api.crawlora.net endpoint, do not accept untrusted CRAWLORA_API_BASE values, and keep the key only in the CRAWLORA_API_KEY environment variable.

Risk: The helper script is broader than the Google Jobs use case and can issue arbitrary methods or paths.

Mitigation: Restrict routine use to GET requests against /google-jobs/search and /google-jobs/job with reviewed parameters.

Risk: Job search queries may reveal sensitive intent or personal information.

Mitigation: Avoid putting confidential or personal data in job queries and use the skill only in a trusted environment.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs public Google Careers posting data; search page size is fixed at 20 results and job detail lookup requires a numeric Google job id.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
