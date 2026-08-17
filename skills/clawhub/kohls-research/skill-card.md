## Description:

Researches Kohl's catalog data by browsing category taxonomy, retrieving product reviews by web_id, finding nearby stores, and returning typeahead suggestions as JSON through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research public Kohl's catalog categories, product reviews, store locations, and search suggestions without scraping Kohls.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call arbitrary Crawlora API paths and send arbitrary POST data beyond the Kohl's research workflow.

Mitigation: Review before installing, restrict use to the listed Kohl's endpoints, and avoid sending private or unrelated data through the script.

Risk: The skill requires giving the agent a Crawlora API key.

Mitigation: Provide the key only through CRAWLORA_API_KEY and do not hardcode, commit, or pass it in query parameters.

## Reference(s):

- [Kohl's endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/kohls-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses cover public Kohl's catalog, reviews, store, and suggestion data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
