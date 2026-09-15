## Description:

Researches homes and used cars through the Crawlora API, covering property search, estimates, market trends, vehicle search, and listing or dealer details while returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public real-estate and vehicle listings, compare properties or cars, and retrieve normalized listing, estimate, trend, or dealer details through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search parameters and a Crawlora API key to Crawlora's API.

Mitigation: Use it only for intended public listing research and keep CRAWLORA_API_KEY in the environment, not in prompts, files, or command-line arguments.

Risk: The endpoint reference includes Rightmove property and agent searches even though the main description names Zillow, Redfin, CarMax, Autotrader, and Cars.com.

Mitigation: Review the endpoint reference before use and confirm whether Rightmove endpoints are intended for the release.

Risk: Returned listing, estimate, trend, and vehicle data may be incomplete, paginated, platform-specific, or unsuitable as professional advice.

Mitigation: Walk paginated results where coverage matters, cross-check important decisions against primary sources, and avoid treating outputs as real-estate, financial, or automotive advice.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/real-estate-autos-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment and uses public listing data only.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
