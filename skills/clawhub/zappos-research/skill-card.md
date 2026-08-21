## Description:

Researches Zappos's footwear and apparel catalog, including the brand directory, product search, product detail, pricing, images, ratings, fit feedback, and color variants, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Zappos products, browse brand catalogs, inspect product detail, and compare public catalog data through Crawlora's normalized JSON API instead of scraping zappos.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can make broader Crawlora requests than the Zappos-only skill description implies.

Mitigation: Review before installation, grant only an appropriate Crawlora API key, and prefer or enforce usage limited to the documented /zappos/* GET endpoints.

Risk: Public catalog data may be incomplete, paginated, unavailable, or limited to featured review excerpts.

Mitigation: Use pagination, handle empty or 404 responses, and present product or fit findings as API-returned catalog data rather than complete Zappos review coverage.

## Reference(s):

- [zappos-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/zappos-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that call Crawlora and return JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and paginated Zappos endpoints; product detail includes selected public catalog fields and up to two featured reviews.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
