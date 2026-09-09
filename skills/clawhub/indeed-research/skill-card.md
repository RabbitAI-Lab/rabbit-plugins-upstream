## Description:

Searches Indeed job postings, resolves Indeed location suggestions, and retrieves single job listings through the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search public Indeed postings by role and location, resolve valid Indeed location strings, page through recent results, and fetch full details for a known job key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call broader Crawlora API endpoints than the Indeed-specific workflow describes.

Mitigation: Review endpoint paths and arguments before execution, and restrict use to the documented Indeed endpoints unless broader Crawlora access is intended.

Risk: The skill requires a Crawlora API key and sends job-search queries to Crawlora.

Mitigation: Provide the key only through CRAWLORA_API_KEY, avoid committing credentials, and use the skill only where sending those queries to Crawlora is acceptable.

Risk: CRAWLORA_API_BASE or command arguments influenced by untrusted input could redirect or alter API requests.

Mitigation: Run the helper in a trusted shell environment and do not pass untrusted API base values, endpoint paths, or request bodies.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/indeed-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests are sent to Crawlora and responses are returned as normalized JSON.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
