## Description:

Searches Indeed job postings and pulls single job listings via the Crawlora API, including keyword and location search, location autocomplete, and job detail by job key, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Indeed job postings, resolve valid Indeed location strings, page through job search results, and fetch full details for a specific posting by job key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can use the user's Crawlora API key with arbitrary API paths or an overridden API host.

Mitigation: Constrain use to the three documented Indeed GET endpoints and keep CRAWLORA_API_BASE fixed to the Crawlora HTTPS API base.

Risk: A Crawlora API key used in an untrusted environment may need to be treated as exposed.

Mitigation: Store the key only in CRAWLORA_API_KEY, avoid committing it, and rotate the key if it has already been used in an untrusted environment.

Risk: The skill depends on Crawlora as a third-party service for access to public Indeed job data.

Mitigation: Install only after accepting the third-party service dependency and review usage against applicable Indeed and Crawlora terms.

## Reference(s):

- [Indeed endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/indeed-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Indeed job data through Crawlora.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
