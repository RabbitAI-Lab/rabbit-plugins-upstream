## Description:

Researches products, prices, brands, and categories on Zalando using the Crawlora API, returning clean JSON for product search, category browsing, brand lookup, autocomplete, and storefront resolution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Zalando catalog data, compare prices, resolve country storefronts, and retrieve normalized product or category results through Crawlora instead of scraping Zalando pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the user's Crawlora API key to a host selected through CRAWLORA_API_BASE.

Mitigation: Use a low-privilege Crawlora key and leave CRAWLORA_API_BASE unset unless the target host is fully trusted.

Risk: The helper script can make arbitrary Crawlora requests beyond the five documented Zalando GET endpoints.

Mitigation: Review invocations before use and prefer a version or wrapper that restricts calls to the documented Zalando endpoints.

## Reference(s):

- [Zalando endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/zalando-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API requests that require CRAWLORA_API_KEY.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
