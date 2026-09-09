## Description:

Researches homes and used cars through the Crawlora API, including Zillow and Redfin property search, estimates, and market trends, plus CarMax, Autotrader, and Cars.com vehicle and dealer lookups that return JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research public real-estate and vehicle listings, compare home or car search results, check property estimates and market trends, and inspect specific listings or dealers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses a real Crawlora API key and can send authenticated requests.

Mitigation: Use it only in trusted environments, keep CRAWLORA_API_KEY out of prompts, logs, and committed files, and rotate the key if it may have been exposed.

Risk: CRAWLORA_API_BASE can redirect authenticated requests to a non-default endpoint.

Mitigation: Leave CRAWLORA_API_BASE unset unless the destination is fully trusted.

Risk: The helper can call broader Crawlora endpoints than the skill description names.

Mitigation: Review requested paths before execution and restrict use to the intended real-estate and vehicle research endpoints.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/real-estate-autos-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; the helper prints raw JSON from Crawlora API endpoints.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
