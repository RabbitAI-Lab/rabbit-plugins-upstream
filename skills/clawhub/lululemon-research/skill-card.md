## Description:

Researches Lululemon's catalog, including category navigation, listings, product details, outfit recommendations, and store directory results, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping research agents use this skill to retrieve public Lululemon catalog, product, review, outfit, and store information through Crawlora instead of scraping storefront HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Lululemon lookup parameters, and possibly location coordinates for store searches, to Crawlora's API.

Mitigation: Use it only for public storefront research and avoid submitting private account data or sensitive location details.

Risk: The helper requires a Crawlora API key.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode, place it in query parameters, or commit it.

## Reference(s):

- [lululemon-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/lululemon-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and is limited to documented Lululemon GET endpoints.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
