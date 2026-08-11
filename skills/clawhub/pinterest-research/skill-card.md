## Description:

Researches Pinterest profiles, boards, pins, ideas categories, and search results through the Crawlora API and returns clean JSON for agent use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, marketers, and developers use this skill to inspect public Pinterest profiles, boards, pins, idea categories, and keyword search results for trend research, content planning, competitor audits, or brand-monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper accepts arbitrary paths and can be used outside the documented Pinterest endpoints.

Mitigation: Use only the documented /pinterest endpoints unless the script is reviewed and intentionally approved for broader Crawlora API use.

Risk: An overridden CRAWLORA_API_BASE could send the Crawlora API key to an untrusted destination.

Mitigation: Leave CRAWLORA_API_BASE unset or pin it to https://api.crawlora.net/api/v1 before running the helper.

Risk: The skill requires a Crawlora API key for remote API calls.

Mitigation: Store the key only in CRAWLORA_API_KEY and avoid hardcoding, committing, logging, or passing it in query parameters.

## Reference(s):

- [Pinterest endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/pinterest-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public Pinterest data returned by Crawlora endpoints; list endpoints may require paging through cursor or offset fields.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
