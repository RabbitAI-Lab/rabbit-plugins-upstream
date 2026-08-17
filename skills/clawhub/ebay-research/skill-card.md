## Description:

Researches eBay listings, items, and sellers using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public eBay listings, item details, seller reputation, seller feedback, and seller shop inventory through normalized Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora API paths even though the skill is framed as eBay-only research.

Mitigation: Review requested paths before execution and prefer a version that restricts calls to documented /ebay endpoints.

Risk: The skill requires an API key for Crawlora requests.

Mitigation: Store the key only in CRAWLORA_API_KEY and avoid hardcoding, logging, or committing credentials.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ebay-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API requests.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
