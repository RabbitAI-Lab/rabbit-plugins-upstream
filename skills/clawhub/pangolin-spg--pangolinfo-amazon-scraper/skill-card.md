## Description:

Programmatic Amazon scraping via Pangolinfo APIs for products, keywords, categories, best sellers, and related results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pangolin-spg](https://clawhub.ai/user/pangolin-spg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use the skill to retrieve Amazon product, keyword, category, seller, and ranking data for structured workflows.

### Deployment Geography for Use:

United States, United Kingdom, Canada, Germany, France, Japan, Italy, Spain, Australia, Mexico, Saudi Arabia, United Arab Emirates, and Brazil.

## Known Risks and Mitigations:

Risk: Requested URLs, search terms, and ZIP codes are sent to Pangolinfo, and requests consume service credits.

Mitigation: Review submitted inputs and expected request costs before running queries.

Risk: Password-based login can create a long-lived local token cache at ~/.pangolin_token.

Mitigation: Prefer PANGOLIN_TOKEN; if using password login, protect the cached token and remove it when no longer needed.

## Reference(s):

- [Pangolinfo Amazon Scraper skill](https://www.pangolinfo.com/amazon-scraper-skill/)
- [Amazon API reference](references/amazon-api.md)
- [Amazon Scrape API documentation](https://docs.pangolinfo.com/en-api-reference/amazonApi/amazonScrapeAPI)
- [Error codes and troubleshooting](references/error-codes.md)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Text]

**Output Format:** [Amazon scrape results as JSON, raw HTML, or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned fields vary by parser and requested Amazon data.]

## Skill Version(s):

1.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
