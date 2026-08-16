## Description:

Searches Indeed job postings, suggests valid Indeed locations, and retrieves individual job details through the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research public Indeed postings by keyword and location, page through results, resolve location suggestions, and fetch full details for a selected job key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora helper accepts arbitrary API paths, so the configured API key could be used for Crawlora endpoints beyond the documented Indeed paths.

Mitigation: Review proposed calls before execution and restrict use to the documented GET endpoints: /indeed/search, /indeed/locations/suggest, and /indeed/job.

Risk: The skill requires a Crawlora API key for authenticated requests.

Mitigation: Provide the key only through CRAWLORA_API_KEY and do not hardcode, commit, or pass it in query parameters.

## Reference(s):

- [Indeed endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/indeed-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with shell command examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests use public Indeed data through Crawlora.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
