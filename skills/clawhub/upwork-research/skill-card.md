## Description:

Researches Upwork job postings and freelancer profiles via the Crawlora API, returning clean JSON for job searches, job details, and freelancer profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Upwork opportunities, inspect job details, compare budgets, and review public freelancer profile signals before outreach or hiring decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call API paths beyond the three Upwork endpoints described by the skill.

Mitigation: Use it only with /upwork/search, /upwork/job/{id}, and /upwork/freelancer/{id}; review calls before execution.

Risk: Crawlora requests require an API key and may consume account credits.

Mitigation: Store the key only in CRAWLORA_API_KEY, use a revocable key, and monitor credit usage.

Risk: Returned results are limited to public Upwork data and may be incomplete for high-stakes hiring decisions.

Mitigation: Treat the JSON as research input and verify important decisions against current Upwork pages and applicable terms.

## Reference(s):

- [upwork-research endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; responses are limited to public Upwork data returned by the Crawlora API.]

## Skill Version(s):

1.0.4 (source: server release metadata, released 2026-08-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
