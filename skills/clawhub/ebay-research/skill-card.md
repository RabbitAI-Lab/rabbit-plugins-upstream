## Description:

Researches eBay listings, items, and sellers using the Crawlora API, returning clean JSON for listing searches, item details, and seller vetting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public eBay listings, inspect item details, and evaluate seller reputation through normalized Crawlora API responses instead of scraping eBay pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can expose the Crawlora API key if redirected by environment settings.

Mitigation: Use a trusted execution environment, review commands before running them, and prefer an allowlisted official Crawlora API base.

Risk: The bundled API script is broader than the eBay-only purpose described by the skill.

Mitigation: Restrict use to documented eBay endpoints and review any command that targets other Crawlora paths.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ebay-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live Crawlora API calls.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
