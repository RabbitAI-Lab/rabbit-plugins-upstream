## Description:

Searches Indeed job postings and pulls single job listings via the Crawlora API -- keyword and location search, location autocomplete, and job detail by job key -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and research agents use this skill to search public Indeed postings, resolve valid Indeed location strings, page through results, and fetch full details for a specific posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indeed search terms, locations, job keys, and the Crawlora API key are sent to Crawlora.

Mitigation: Use only when this data sharing is acceptable, keep the key in CRAWLORA_API_KEY, and do not hardcode or commit the key.

Risk: Use of public Indeed posting data may be subject to Crawlora and Indeed terms.

Mitigation: Review the relevant service terms before using the skill for job research workflows.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/indeed-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends Indeed search terms, locations, and job keys to Crawlora.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
