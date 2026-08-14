## Description:

Searches Indeed job postings and pulls single job listings via the Crawlora API — keyword and location search, location autocomplete, and job detail by job key — returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and job-search agents use this skill to search public Indeed postings, resolve location strings, page through recent results, and fetch full posting details by job key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call Crawlora endpoints beyond the three documented Indeed endpoints if invoked with other paths.

Mitigation: Review or wrap the script before use so it allows only /indeed/search, /indeed/job, and /indeed/locations/suggest.

Risk: Authenticated Crawlora calls can use credits or expose the configured API key if handled carelessly.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not hardcode or commit it, and monitor Crawlora usage for unexpected calls.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/indeed-research)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for authenticated Crawlora requests.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
