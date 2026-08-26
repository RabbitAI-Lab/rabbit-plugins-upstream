## Description:

Researches Pinterest profiles, boards, pins, ideas categories, and search results via the Crawlora API, returning clean JSON for public Pinterest research instead of direct Pinterest scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and marketing teams use this skill to retrieve normalized JSON for public Pinterest profiles, boards, pins, category feeds, and keyword search results through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can be used as a general Crawlora API client beyond the documented Pinterest endpoints.

Mitigation: Use the skill only when that broader API-client behavior is acceptable, and review command paths or POST bodies before execution.

Risk: The Crawlora API key could be exposed or overused if it is passed through unsafe commands or stored in files.

Mitigation: Keep CRAWLORA_API_KEY scoped to the session, do not hardcode or commit it, and avoid sending sensitive prompt or local data in arbitrary requests.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Pinterest data from Crawlora endpoints.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
