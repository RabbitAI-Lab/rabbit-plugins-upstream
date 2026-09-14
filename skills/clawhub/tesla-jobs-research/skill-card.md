## Description:

Researches Tesla job postings via the Crawlora API by searching Tesla's careers site by title, department, or location and retrieving full posting details by id as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search public Tesla job openings, page through filtered listing results, and fetch full posting descriptions, responsibilities, and requirements by job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends Tesla job search terms or job ids to Crawlora.

Mitigation: Use the CRAWLORA_API_KEY environment variable, do not hardcode or commit the key, and avoid sending secrets or personal data in search parameters.

Risk: The skill uses public Tesla job posting data and may be subject to Tesla's terms and availability.

Mitigation: Use the results for public job research only, respect Tesla's terms, and recheck important postings before relying on them.

Risk: Listing searches use substring filters and return metadata-only results.

Mitigation: Try broader query or location substrings when results are missing, page through results, and call the job detail endpoint for full descriptions and requirements.

## Reference(s):

- [Tesla Jobs endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/tesla-jobs-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and returns paginated listing metadata or full job posting JSON.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
