## Description:

Searches Indeed job postings and pulls single job listings via the Crawlora API - keyword and location search, location autocomplete, and job detail by job key - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, recruiters, job seekers, and agents use this skill to search public Indeed postings, resolve valid Indeed locations, page through recent results, and fetch full job details by job key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indeed search terms, locations, job keys, and the Crawlora API key are sent to Crawlora when the helper is used.

Mitigation: Use the skill only when sharing those request details with Crawlora is acceptable, keep CRAWLORA_API_KEY in the environment, and do not commit the key.

Risk: Requests outside the documented Indeed route set could expose unrelated account surfaces or send unintended data.

Mitigation: Use scripts/crawlora.sh with only /indeed/search, /indeed/locations/suggest, and /indeed/job as documented by the artifact.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/indeed-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment and uses the documented Indeed endpoints only.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
