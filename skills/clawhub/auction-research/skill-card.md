## Description:

Researches Bonhams auctions and lots via the Crawlora API for upcoming and past sales, lot search, estimates, realized prices, departments, and auction detail, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to search Bonhams auction calendars, comparable lots, estimates, realized prices, departments, and auction or lot details through Crawlora's normalized API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, path parameters, and request data are sent to Crawlora with the user's CRAWLORA_API_KEY.

Mitigation: Use a scoped API key and avoid confidential client, collection, or acquisition data in queries.

Risk: The helper performs outbound API calls to Crawlora and returns data from public auction sources.

Mitigation: Confirm outbound API use is allowed in the deployment environment and review important auction facts against primary sources before relying on them.

Risk: Manual helper use could broaden exposure if undocumented routes or unsafe query values are attempted.

Mitigation: Use the documented Bonhams routes and keep the helper's route, method, path, and query validation in place.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/auction-research)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends documented requests to https://api.crawlora.net/api/v1.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
