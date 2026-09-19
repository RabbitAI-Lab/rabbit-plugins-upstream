## Description:

Researches Tesla job postings via the Crawlora API by searching Tesla's careers site by title, department, or location and retrieving full posting details by id as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search public Tesla job openings, filter listings by role or location, and retrieve full posting descriptions, responsibilities, and requirements from a documented third-party API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search parameters and the Crawlora API key are sent to Crawlora as a third-party API provider.

Mitigation: Install only if that provider relationship is acceptable, keep CRAWLORA_API_KEY in the environment, and avoid sensitive personal data in search parameters.

Risk: API credentials could be exposed if they are hardcoded, committed, or passed on the command line.

Mitigation: Use the provided helper's environment-variable flow and keep the API key out of source files, query parameters, and shared logs.

Risk: List responses contain posting metadata only and may not be enough for detailed job analysis.

Mitigation: Fetch the specific job detail endpoint before summarizing requirements, responsibilities, or full descriptions.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/tesla-jobs-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; list results are paginated and metadata-only until a detail request is made.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
