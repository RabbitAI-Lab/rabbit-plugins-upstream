## Description:

Researches Kohl's catalog categories, product reviews, nearby stores, and typeahead suggestions through the Crawlora API as JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research public Kohl's catalog data, customer reviews, store locations, and search suggestions without scraping Kohls.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send CRAWLORA_API_KEY to an unapproved destination if CRAWLORA_API_BASE is overridden.

Mitigation: Keep CRAWLORA_API_BASE unset or verify it points only to https://api.crawlora.net/api/v1 before running the helper.

Risk: Kohl's lookup terms and store searches are sent to Crawlora.

Mitigation: Avoid submitting private or sensitive data through the skill.

## Reference(s):

- [Kohl's endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and the documented Kohl's GET endpoints.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
