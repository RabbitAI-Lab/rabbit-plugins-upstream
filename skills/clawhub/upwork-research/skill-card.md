## Description:

Researches Upwork job postings and freelancer profiles via the Crawlora API, including public job search, job-detail lookup, freelancer-profile lookup, and clean JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and hiring teams use this skill to search public Upwork job listings, inspect a specific job posting, research freelancer profiles, estimate market rates, and support freelancer due diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to an environment-overridden API base.

Mitigation: Run it only with a trusted CRAWLORA_API_BASE value or leave CRAWLORA_API_BASE unset so the default Crawlora API endpoint is used.

Risk: Search terms and request arguments may expose sensitive research intent to the API provider.

Mitigation: Use non-sensitive Upwork research terms and keep the Crawlora API key scoped and revocable.

Risk: Untrusted command arguments could change the API path or request body sent by the helper script.

Mitigation: Avoid running the helper in environments where command arguments can be influenced by untrusted input.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; returns normalized JSON for public Upwork job and freelancer data.]

## Skill Version(s):

1.0.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
